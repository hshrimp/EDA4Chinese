#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/11/2 下午4:15
文本拓展的一个使用例子。
"""
from eda_aug.eda import EDA

eda = EDA()


def expand(text, num_aug=10):
    # eda的扩展
    print('EDA:', eda.eda(text, num_aug=num_aug))



if __name__ == '__main__':
    expand('中华白海豚浪漫求偶画面', 10)
    """
    EDA: {'中华白海豚浪漫求偶镜头', '中华白海豚浪漫画面', '中华白海豚浪漫求偶', '中华白海豚浪漫雄蛙画面', '中华白海豚浪漫求偶底片镜头', '求偶鲇鱼浪漫中华画面', '中华浪漫求偶画面', '中华鲇鱼浪漫求偶画面', '求偶白海豚浪漫中华镜头', '画面白海豚浪漫雄蛙中华', '雌兽中华白海豚浪漫雄蛙画面', '中华鲇鱼浪漫求偶万国画面'}
    """
