# API监控脚本

这是一个Python脚本，用于监控API接口的响应内容变化。

## 功能

1. 使用POST方式请求指定的API接口
2. 保存返回的内容
3. 下次请求时比较内容是否有变化
4. 记录变更历史和详细日志

## 使用方法

1. 确保已安装依赖：
   ```
   pip install requests
   ```

2. 修改脚本中的配置参数：
   - `API_URL`: 要监控的API地址
   - `STORAGE_FILE`: 响应内容保存文件名
   - `LOG_FILE`: 日志文件名
   - `post_data`: POST请求的数据

3. 运行脚本：
   ```
   python api_monitor.py
   ```

## 文件说明

- `api_monitor.py`: 主程序文件
- `api_response.json`: 保存最近一次API响应内容
- `api_monitor.log`: 详细日志文件

## 工作原理

1. 脚本发送POST请求到指定API
2. 计算响应内容的MD5哈希值
3. 与之前保存的哈希值比较
4. 如果哈希值不同，则认为内容有变化
5. 保存新的响应内容和哈希值
6. 记录所有操作到日志文件

## 自定义配置

在`main()`函数中可以修改以下参数：

```python
API_URL = "https://jsonplaceholder.typicode.com/posts"  # API地址
STORAGE_FILE = "api_response.json"  # 响应保存文件
LOG_FILE = "api_monitor.log"  # 日志文件
post_data = {  # POST请求数据
    "title": "测试标题",
    "body": "测试内容",
    "userId": 1
}
```
