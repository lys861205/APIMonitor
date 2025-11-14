#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys
from api_monitor import APIMonitor

def periodic_monitor(api_url, post_data=None, interval=60, max_runs=None):
    """
    定期监控API的函数

    参数:
    api_url: API地址
    post_data: POST请求数据
    interval: 检查间隔（秒）
    max_runs: 最大运行次数（None表示无限运行）
    """

    # 创建监控器实例
    monitor = APIMonitor(api_url, 'periodic_response.json', 'periodic_monitor.log')

    run_count = 0

    print(f"开始定期监控API: {api_url}")
    print(f"检查间隔: {interval}秒")
    if max_runs:
        print(f"最大运行次数: {max_runs}")
    print("按Ctrl+C停止监控")
    print("-" * 50)

    try:
        while True:
            if max_runs and run_count >= max_runs:
                print("达到最大运行次数，停止监控")
                break

            run_count += 1
            print(f"[{run_count}] {time.strftime('%Y-%m-%d %H:%M:%S')} - 检查API...")

            result = monitor.check_api(post_data=post_data)

            if result['changed']:
                print(f"  → 检测到变更: {result['message']}")
            else:
                print(f"  → 无变更: {result['message']}")

            # 等待下次检查
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\n用户中断，停止监控")

if __name__ == "__main__":
    # 配置参数
    API_URL = "https://jsonplaceholder.typicode.com/posts"

    # POST数据
    POST_DATA = {
        "title": "定时监控测试",
        "body": "这是定时监控的测试内容",
        "userId": 1
    }

    # 检查间隔（秒）
    INTERVAL = 10

    # 最大运行次数（设置为None表示无限运行）
    MAX_RUNS = 3

    # 开始定期监控
    periodic_monitor(API_URL, POST_DATA, INTERVAL, MAX_RUNS)