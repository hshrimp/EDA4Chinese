#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/10/30 下午2:57
"""
from googletrans import Translator
from googletrans.constants import LANGUAGES
from configuration.config import ips, logging
import random


class GoogleTranslator:
    def __init__(self):
        self.ips = ips
        self.languages = list(LANGUAGES.keys())
        self.service_urls = ['translate.google.cn']
        self.translator = Translator(service_urls=self.service_urls)
        self.get_proxies()

    def translate(self, text, dest='en', src='auto'):
        """
        translate
        :param dest:
        :param src:
        :param text:
        :return:
        """
        try:
            translations = self.translator.translate(text, dest=dest, src=src)
        except Exception as e:
            logging.warning(f'{e},the ip has some mistakes.')
            self.get_proxies()
            translations = self.translator.translate(text, dest=dest)
        return translations

    def get_proxies(self):
        """
        find a ip for proxies
        :return:
        """
        flag = False
        translate_proxies = Translator(service_urls=self.service_urls)
        for ip in self.ips.values():
            try:
                translate_proxies = Translator(service_urls=self.service_urls, proxies={'http': ip})
                translate_proxies.translate('text')
                flag = True
                break
            except Exception as e:
                logging.error(f'{e},there are some mistake with ip: {ip}')
        if flag:
            self.translator = translate_proxies
        else:
            logging.error('the ips are all banned!!!')

    def back_translate(self, text):
        """
        回译
        :param text:string
        :return:
        """
        destination = random.choice(self.languages)
        mid_text = self.translate(text, dest=destination)
        # print(destination, ':', mid_text.text)
        back_text = self.translate(mid_text.text, dest='zh-cn', src=destination)
        return back_text.text


if __name__ == '__main__':
    t = GoogleTranslator()
    print(t.back_translate('张三吃饭了没'))
