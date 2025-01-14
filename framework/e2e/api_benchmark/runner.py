#!/bin/env python
# -*- coding: utf-8 -*-
# @author DDDivano
# encoding=utf-8 vi:ts=4:sw=4:expandtab:ft=python
"""
runner
"""

import argparse
import sys

sys.path.append("..")
from utils.yaml_loader import YamlLoader
from utils.logger import logger
from benchtrans import BenchTrans
from jelly import Jelly
from db import DB


def schedule(yaml_path, case_name=None, place=None, card=None):
    """
    例行任务，调试任务二次运行调用。 一定入库，存在数据库操作
    """
    yaml_file = yaml_path
    yaml_loader = YamlLoader(yaml_file)
    if case_name is None:
        cases_name = yaml_loader.get_all_case_name()
        for case_name in cases_name:
            case_info = yaml_loader.get_case_info(case_name)
            try:
                bt = BenchTrans(case_info)
                if not bt.check_torch:
                    logger.get_log().info("{} 缺少Torch配置, Skip...".format(case_name))
                    continue
                jelly = Jelly(bt.get_paddle_api(), bt.get_torch_api(), title=case_name, place=place, card=card)
                jelly.set_paddle_param(bt.get_paddle_inputs(), bt.get_paddle_param())
                jelly.set_torch_param(bt.get_torch_inputs(), bt.get_torch_param())
                jelly.run_schedule()
            except Exception as e:
                print(e)
    else:
        case_info = yaml_loader.get_case_info(case_name)
        bt = BenchTrans(case_info)
        jelly = Jelly(bt.get_paddle_api(), bt.get_torch_api(), title=case_name, place=place, card=card)
        jelly.set_paddle_param(bt.get_paddle_inputs(), bt.get_paddle_param())
        jelly.set_torch_param(bt.get_torch_inputs(), bt.get_torch_param())
        jelly.run_schedule()

        ######  以上是执行逻辑

        ######  以下是入库逻辑


def testing(yaml_path, case_name, place=None, card=None):
    """
    testing mode 本地调试用
    """
    yaml_file = yaml_path
    yaml_loader = YamlLoader(yaml_file)
    case_info = yaml_loader.get_case_info(case_name)
    bt = BenchTrans(case_info)
    jelly = Jelly(bt.get_paddle_api(), bt.get_torch_api(), title=case_name, place=place, card=card)
    jelly.set_paddle_param(bt.get_paddle_inputs(), bt.get_paddle_param())
    jelly.set_torch_param(bt.get_torch_inputs(), bt.get_torch_param())
    jelly.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--yaml", type=str, help="input the yaml path")
    parser.add_argument(
        "--mode",
        type=str,
        default="testing",
        help="""choose mode: [schedule] for ce or [testing] for native test or [rerun] for double check.
              [schedule] and [rerun] will write data into database """,
    )
    parser.add_argument("--case", type=str, default="Tanh", help="case name for [testing] and [rerun] mode")
    parser.add_argument("--place", type=str, default="cpu", help="[cpu] or [gpu]")
    parser.add_argument("--card", type=str, default=None, help="card number , default is 0")
    args = parser.parse_args()
    if args.mode == "schedule":
        db = DB()
        try:
            db.init_mission(mode=args.mode, place=args.place, card=args.card)
            schedule(args.yaml, place=args.place, card=args.card)
            db.save()
        except Exception as e:
            print(e)
            db.error()
    elif args.mode == "testing":
        testing(args.yaml, args.case, place=args.place, card=args.card)
    elif args.mode == "rerun":
        db = DB()
        try:
            db.init_mission(mode=args.mode, place=args.place, card=args.card)
            schedule(args.yaml, args.case, place=args.place, card=args.card)
            db.save()
        except Exception as e:
            print(e)
            db.error()
    else:
        raise AttributeError
