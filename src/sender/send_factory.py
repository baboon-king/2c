# !/usr/bin/env python
"""
    Created by howie.hu at 2021/4/10.
    Description：分发器工厂，支持分发终端如下：
        - 钉钉
    Changelog: all notable changes to this file will be documented
"""

from importlib import import_module

from src.utils import LOGGER


def send_factory(send_type: str, send_config: dict, send_data: dict) -> bool:
    """
    分发器工厂函数
    :param send_type: 下发终端类型
    :param send_config: 下发终端配置
    :param send_data: 下发内容字典，字段开发者自定义
    :return:
    """
    send_status = False
    try:
        send_module = import_module(f"src.sender.{send_type}_sender")
        send_status = send_module.send(send_config, send_data)
    except ModuleNotFoundError:
        LOGGER.error(f"目标终端类型不存在 {send_type} - {send_config} - {send_data}")
    return send_status
