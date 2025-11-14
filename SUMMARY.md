# API监控工具包

这个工具包包含多个Python脚本，用于监控API接口的响应内容变化。

## 文件说明

### 1. api_monitor.py
主程序文件，包含APIMonitor类，提供以下功能：
- 使用POST方式请求指定的API接口
- 保存返回的内容
- 比较内容是否有变化
- 记录变更历史和详细日志

### 2. README.md
使用说明文档，详细介绍了如何使用API监控脚本。

### 3. custom_example.py
自定义配置示例，展示如何使用APIMonitor类创建自定义监控脚本。

### 4. periodic_monitor.py
定时监控脚本，可以定期检查API并记录变化。

## 生成的文件

### 日志文件
- `api_monitor.log` - 主程序日志

### 响应数据文件
- `api_response.json` - 主程序响应数据

## 使用方法

1. 直接运行主程序：
   ```
   python3 api_monitor.py
   ```

2. 运行自定义示例：
   ```
   python3 custom_example.py
   ```

3. 运行定时监控：
   ```
   python3 periodic_monitor.py
   ```

## 功能特点

1. **POST请求支持** - 使用requests库发送POST请求
2. **内容比较** - 使用MD5哈希值比较响应内容变化
3. **数据持久化** - 保存响应内容到JSON文件
4. **日志记录** - 详细记录所有操作和错误信息
5. **错误处理** - 完善的异常处理机制
6. **灵活配置** - 支持自定义API地址、请求数据等参数
7. **定时监控** - 支持定期检查API变化