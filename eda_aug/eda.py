#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jieba
import synonyms
import random
from configuration.config import STOPWORDS


class EDA:
    def __init__(self):
        self.stopwords = set()
        self.get_stopwords()

    def get_stopwords(self):
        """
        停用词列表，使用哈工大停用词表
        :return:
        """
        with open(STOPWORDS) as f:
            for line in f.readlines():
                self.stopwords.add(line[:-1])

    @staticmethod
    def get_synonyms(word, size=10):
        """
        近义词获取
        :param size: 获取的近义词数量
        :param word:
        :return:
        """
        return synonyms.nearby(word, size=size)[0]

    def check_synonyms(self, words):
        """
        检查是不是所有词都没法进行近义词替换
        :param words:
        :return:
        """
        for word in words:
            if self.get_synonyms(word, 1):
                return True
        return False

    def synonym_replacement(self, words, n):
        """
        同义词替换
        替换一个语句中的n个单词为其同义词
        :param words:
        :param n:
        :return:
        """
        new_words = words.copy()
        random_word_list = list(set([word for word in words if word not in self.stopwords]))
        random.shuffle(random_word_list)
        num_replaced = 0
        for random_word in random_word_list:
            synonyms4word = self.get_synonyms(random_word)
            if len(synonyms4word) >= 1:
                synonym = random.choice(synonyms4word)
                new_words = [synonym if word == random_word else word for word in new_words]
                num_replaced += 1
            if num_replaced >= n:
                break
        return new_words

    def random_insertion(self, words, n):
        """
        随机插入
        随机在语句中插入n个词
        :param words:
        :param n:
        :return:
        """

        def add_word():
            random_word = random.choice(random_word_list)
            synonyms4word = self.get_synonyms(random_word)
            # 如果当前词没有同义词，那么将它移除，再重新做一次add_word
            if not synonyms4word:
                print(random_word, ' without synonyms')
                random_word_list.remove(random_word)
                add_word()
                return
            random_synonym = random.choice(synonyms4word)
            random_idx = random.randint(0, len(new_words) - 1)
            new_words.insert(random_idx, random_synonym)
            if random_synonym not in self.stopwords:
                random_word_list.append(random_synonym)

        random_word_list = list(set([word for word in words if word not in self.stopwords]))
        new_words = words.copy()
        for _ in range(n):
            add_word()
        return new_words

    @staticmethod
    def random_swap(words, n):
        """
        随即交换
        随机的选择句中两个单词并交换它们的位置。重复n次
        :param words:
        :param n:
        :return:
        """

        def swap_word():
            random_idx_1, random_idx_2 = random.sample(indexes, 2)
            new_words[random_idx_1], new_words[random_idx_2] = new_words[random_idx_2], new_words[random_idx_1]

        new_words = words.copy()
        indexes = [i for i in range(len(words))]
        for _ in range(n):
            swap_word()
        return new_words

    @staticmethod
    def random_deletion(words, p):
        """
        随机删除
        以概率p删除语句中的词
        :param words:
        :param p:
        :return:
        """
        if len(words) == 1:
            return words

        new_words = []
        for word in words:
            r = random.random()
            if r > p:
                new_words.append(word)

        if len(new_words) == 0:
            rand_int = random.randint(0, len(words) - 1)
            return [words[rand_int]]

        return new_words

    @staticmethod
    def random_deletion_v2(words: list, n):
        """
        随机删除n个词
        :param words:
        :param n:
        :return:
        """

        def remove():
            index = random.randint(0, length - 1)
            new_words.pop(index)

        new_words = words.copy()
        length = len(new_words)
        if length <= n:
            rand_int = random.randint(0, length - 1)
            return [words[rand_int]]
        for _ in range(n):
            remove()
            length -= 1
        return new_words

    def eda(self, sentence: str, alpha_sr=0.1, alpha_ri=0.1, alpha_rs=0.1, p_rd=0.1, num_aug=9):
        """
        EDA函数
        :param sentence:
        :param alpha_sr:
        :param alpha_ri:
        :param alpha_rs:
        :param p_rd:
        :param num_aug:
        :return:
        """
        sentence = sentence.replace(' ', '')
        words = list(jieba.cut(sentence))
        num_words = len(words)

        augmented_sentences = set()
        num_new_per_technique = int(num_aug / 4) + 1
        n_sr = max(1, int(alpha_sr * num_words))
        n_ri = max(1, int(alpha_ri * num_words))
        n_rs = max(1, int(alpha_rs * num_words))
        n_rd = max(1, int(p_rd * num_words))

        # 同义词替换sr
        sr_sentences = []
        for _ in range(num_new_per_technique):
            a_words = self.synonym_replacement(words, n_sr)
            augmented_sentences.add(''.join(a_words))
            sr_sentences.append(a_words)
        # 随机插入ri
        for sr_words in sr_sentences:
            a_words = self.random_insertion(sr_words, n_ri)
            augmented_sentences.add(''.join(a_words))

        # 随机交换rs
        for sr_words in sr_sentences:
            a_words = self.random_swap(sr_words, n_rs)
            augmented_sentences.add(''.join(a_words))

        # 随机删除rd
        for sr_words in sr_sentences:
            a_words = self.random_deletion_v2(sr_words, n_rd)
            augmented_sentences.add(''.join(a_words))

        return augmented_sentences
