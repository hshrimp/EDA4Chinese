#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/11/2 下午4:15
文本拓展的一个使用例子。
"""
from eda_aug.eda import EDA
from translate.google_translator import GoogleTranslator

eda = EDA()
translator = GoogleTranslator()


def expand(text, num_aug=10):
    # eda的扩展
    print('EDA:', eda.eda(text, num_aug=num_aug))

    # 回译的扩展
    for i in range(num_aug):
        print(i, ' back_translate:', translator.back_translate(text))


if __name__ == '__main__':
    expand('中华白海豚浪漫求偶画面', 10)
    """
    EDA: {'中华白海豚浪漫求偶镜头', '中华白海豚浪漫画面', '中华白海豚浪漫求偶', '中华白海豚浪漫雄蛙画面', '中华白海豚浪漫求偶底片镜头', '求偶鲇鱼浪漫中华画面', '中华浪漫求偶画面', '中华鲇鱼浪漫求偶画面', '求偶白海豚浪漫中华镜头', '画面白海豚浪漫雄蛙中华', '雌兽中华白海豚浪漫雄蛙画面', '中华鲇鱼浪漫求偶万国画面'}
    0  back_translate: 中国白海豚求爱浪漫场景
    1  back_translate: 中国白海豚浪漫宫廷现场
    2  back_translate: 中国白海豚浪漫庭院场景
    3  back_translate: 中国白海豚浪漫求爱场景
    4  back_translate: 中国白海豚，浪漫求爱场景
    5  back_translate: 中国白海豚的浪漫爱情场景
    6  back_translate: 中国白海豚浪漫求爱场景
    7  back_translate: 中国白海豚浪漫之地
    8  back_translate: 中国白海豚的浪漫会合场景
    9  back_translate: 中国白海豚浪漫求爱场景
    """
