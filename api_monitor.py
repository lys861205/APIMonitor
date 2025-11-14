#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API监控脚本
功能：
1. 使用POST方式请求指定的API接口
2. 保存返回的内容
3. 下次请求时比较内容是否有变化
4. 记录变更历史
"""

import json
import hashlib
import os
import logging
from datetime import datetime
import requests

class APIMonitor:
    def __init__(self, api_url, storage_file='api_response.json', log_file='api_monitor.log'):
        self.api_url = api_url
        self.storage_file = storage_file
        self.log_file = log_file

        # 设置日志
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def _make_post_request(self, data=None, headers=None):
        """发送POST请求到API"""
        try:
            response = requests.post(
                self.api_url,
                json=data or {},
                headers=headers or {'Content-Type': 'application/json'}
            )
            response.raise_for_status()  # 如果响应状态码不是200会抛出异常
            return response.text
        except requests.exceptions.RequestException as e:
            self.logger.error(f"请求API时出错: {e}")
            raise

    def _save_response(self, response_text):
        """保存响应内容到文件"""
        try:
            # 计算响应内容的哈希值用于比较
            response_hash = hashlib.md5(response_text.encode('utf-8')).hexdigest()

            data = {
                'timestamp': datetime.now().isoformat(),
                'content': response_text,
                'hash': response_hash
            }

            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            self.logger.info("响应内容已保存")
        except Exception as e:
            self.logger.error(f"保存响应内容时出错: {e}")
            raise

    def _load_previous_response(self):
        """从文件加载之前的响应内容"""
        if not os.path.exists(self.storage_file):
            return None

        try:
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            self.logger.warning(f"读取之前响应内容时出错: {e}")
            return None

    def _content_changed(self, new_content, previous_data):
        """比较内容是否有变化"""
        if previous_data is None:
            return True, "首次请求"

        new_hash = hashlib.md5(new_content.encode('utf-8')).hexdigest()
        previous_hash = previous_data.get('hash', '')

        if new_hash != previous_hash:
            return True, f"内容已变更 (上次更新: {previous_data.get('timestamp', '未知')})"
        else:
            return False, f"内容无变化 (上次更新: {previous_data.get('timestamp', '未知')})"

    def check_api(self, post_data=None, headers=None):
        """检查API并比较响应内容"""
        try:
            # 发送POST请求
            self.logger.info(f"正在请求API: {self.api_url}")
            response_text = self._make_post_request(post_data, headers)

            # 加载之前的响应
            previous_data = self._load_previous_response()

            # 比较内容是否有变化
            changed, message = self._content_changed(response_text, previous_data)

            # 保存新的响应
            self._save_response(response_text)

            # 记录变更情况
            if changed:
                self.logger.info(f"检测到变更: {message}")
            else:
                self.logger.info(f"未检测到变更: {message}")

            return {
                'changed': changed,
                'message': message,
                'content': response_text,
                'previous_data': previous_data
            }

        except Exception as e:
            self.logger.error(f"检查API时出错: {e}")
            return {
                'changed': False,
                'message': f"检查API时出错: {e}",
                'content': None,
                'previous_data': None
            }

def main():
    """
    示例用法
    请根据实际情况修改API URL和请求数据
    """
    # 配置API监控器
    API_URL = "https://jsonplaceholder.typicode.com/posts"  # 示例API URL
    STORAGE_FILE = "api_response.json"  # 响应内容保存文件
    LOG_FILE = "api_monitor.log"  # 日志文件

    monitor = APIMonitor(API_URL, STORAGE_FILE, LOG_FILE)

    # 示例POST数据（根据实际API要求修改）
    post_data = {
        "title": "测试标题",
        "body": "测试内容",
        "userId": 1
    }

    # 执行API检查
    result = monitor.check_api(post_data=post_data)

    # 输出结果
    print("=" * 50)
    print("API监控结果")
    print("=" * 50)
    print(f"请求URL: {API_URL}")
    print(f"变更检测: {result['message']}")
    if result['changed']:
        print("状态: 内容已更新 ✓")
    else:
        print("状态: 内容未变更 ○")

    # 显示文件位置
    print(f"\n响应数据文件: {STORAGE_FILE}")
    print(f"详细日志文件: {LOG_FILE}")
    print("=" * 50)

if __name__ == "__main__":
    main()