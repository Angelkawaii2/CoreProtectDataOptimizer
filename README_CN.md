# CoreProtectDataOptimizer
优化和清理CoreProtect Minecraft插件数据库，通过移除非玩家生成的数据显著减少磁盘空间使用。

## 需求

- Python 3.7+
- MySQL 5.7 或更高版本

## 特点

该脚本清理``co_block``表中的非玩家数据，包括由自动化设备生成的数据。  
在测试中，有效地将数据库大小从15亿行减少到4000万行。

## 为什么不使用co purge？

在 ``Coreprotect`` 数据库中，占空间最大的是 ``co_block`` 表，而此表中大部分包含的是非必要数据，只有一小部分由玩家活动产生。  
通过清理这些数据，不仅节省了磁盘空间，还保留了宝贵的玩家生成的方块和其他操作数据。  
如果使用 `co purge` 会无差别地移除指定日期之前的所有数据，包括玩家记录、告示牌记录、聊天记录等。  

## 设置

为了准备运行这个脚本的环境，你应该创建一个虚拟环境并安装所需的包：

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
# 在Windows上
venv\Scripts\activate
# 在Unix或MacOS上
source venv/bin/activate

# 安装所需的包
pip install -r requirements.txt
```

## 使用方式
要运行脚本，请在终端使用以下命令，确保替换path/to/your/config.ini为您配置文件的实际路径：

```bash
python main.py --config path/to/your/config.ini
```
运行脚本后，考虑在您的MySQL数据库上使用OPTIMIZE TABLE命令来回收释放的磁盘空间。

## 许可证

GPL-v3