import argparse
import configparser
import datetime
import pymysql
import sys


def delete_game_behavior_records(db_config, settings):
    db = pymysql.connect(host=db_config['url'],
                         user=db_config['username'],
                         password=db_config['password'],
                         database=db_config['database'])
    cursor = db.cursor()

    sql = f"DELETE FROM {settings['table_name']} WHERE user IN \
(SELECT rowid FROM {settings['user_table']} WHERE uuid IS NULL AND user!='{settings['excluded_user']}') \
AND time < (UNIX_TIMESTAMP(NOW()) - {settings['time_threshold']}) LIMIT {settings['line_limit']};"

    try:
        start_time = datetime.datetime.now()
        cursor.execute(sql)
        db.commit()
        end_time = datetime.datetime.now()

        total_row = cursor.rowcount
        if total_row > 0:
            print(
                f"{start_time.strftime('%Y-%m-%d %H:%M:%S')} | Rows affected: {total_row} | Execution time: {end_time - start_time}")
        else:
            print(
                f"{start_time.strftime('%Y-%m-%d %H:%M:%S')} | No more rows to delete | Execution time: {end_time - start_time}")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        db.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Delete non-player game behavior records in batches, suited for scheduled tasks.")
    parser.add_argument('--config', type=str, required=True, help='Path to configuration file.')
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config)

    db_config = {
        'url': config['DATABASE']['Url'],
        'username': config['DATABASE']['Username'],
        'password': config['DATABASE']['Password'],
        'database': config['DATABASE']['Database'],
    }

    settings = {key: value for key, value in config['SETTINGS'].items()}

    delete_game_behavior_records(db_config, settings)
