#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from api_monitor import APIMonitor

# 自定义配置示例
def custom_monitor_example():
    # 配置参数
    API_URL = "https://jsonplaceholder.typicode.com/posts"
    STORAGE_FILE = "my_api_response.json"
    LOG_FILE = "my_api_monitor.log"

    # 创建监控器实例
    monitor = APIMonitor(API_URL, STORAGE_FILE, LOG_FILE)

    # 自定义POST数据
    post_data = {
        "title": "自定义标题",
        "body": "自定义内容",
        "userId": 2
    }

    # 执行检查
    result = monitor.check_api(post_data=post_data)

    # 输出结果
    print("=" * 50)
    print("自定义API监控示例")
    print("=" * 50)
    print(f"请求URL: {API_URL}")
    print(f"变更检测: {result['message']}")
    if result['changed']:
        print("状态: 内容已更新 ✓")
    else:
        print("状态: 内容未变更 ○")

    print(f"\n响应数据文件: {STORAGE_FILE}")
    print(f"详细日志文件: {LOG_FILE}")
    print("=" * 50)

if __name__ == "__main__":
    custom_monitor_example()