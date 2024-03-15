# CoreProtectDataOptimizer
Optimize and clean up your CoreProtect Minecraft plugin database with ease, significantly reducing disk space usage by removing non-player-generated data from over a month ago.

[简体中文](./README_CN.md) | English

## Requirements

- Python 3.7+
- MySQL 5.7 or higher

## Features

This script cleans non-player data from the co_block table, including data generated by automation devices. It specifically targets data older than a month, effectively reducing the database size from 1.5 billion to 40 million rows in our tests.

## Why Not Use co purge?

In the ``CoreProtect`` database, the `co_block` table occupies the most space, yet the majority of its data is non-essential, with only a small fraction generated by player activities.  
By cleaning up this data, we not only free up disk space but also preserve valuable player-created blocks and other activity data.  
Using `co purge` would indiscriminately remove all data prior to a specified date, including player actions, sign records, chat logs, and more.

## Setting Up

To prepare your environment for running this script, you should create a virtual environment and install the required packages:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt
```

## Usage
To run the script, use the following command in your terminal, making sure to replace path/to/your/config.ini with the actual path to your configuration file:

```bash
python main.py --config path/to/your/config.ini
```
After running the script, consider using the OPTIMIZE TABLE command on your MySQL database to reclaim the freed disk space.

## License

GPL-v3