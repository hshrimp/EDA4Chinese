# EDA4Chinese

## 中文EDA实现。
    1、本工具的EDA部分是论文[《EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks》](https://arxiv.org/abs/1901.11196)的中文版本实现。  
    2、本文的EDA部分是在https://github.com/zhanlaoban/EDA_NLP_for_Chinese的基础上优化改进，降低了复杂度，感谢作者。
    3、EDA英文，请参考https://github.com/jasonwei20/eda_nlp
    

## EDA Reference

- EDA中文版原仓库：[EDA_NLP_for_Chinese](https://github.com/zhanlaoban/EDA_NLP_for_Chinese)。感谢原作者的付出。
- EDA英文版原仓库：[eda_nlp](https://github.com/jasonwei20/eda_nlp)。感谢原作者的付出。Thanks to the author of the paper.
- [《EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks》](https://arxiv.org/abs/1901.11196)

## Acknowledgments

- [jieba分词](https://github.com/fxsjy/jieba)
- [Synonyms](https://github.com/huyingxi/Synonyms)
- [stopwords](https://github.com/goto456/stopwords)


## EDA创新思路

在本文，作者提出**通用的**NLP数据增强技术，命名为EDA。同时作者表示，他们是第一个给数据增强引入文本编辑技术的人。EDA的提出，也是一定程度上受计算机视觉上增强技术的启发而得到。下面详细介绍EDA的四个方法：

对于训练集中的每个句子，执行下列操作：

- 同义词替换(Synonym Replacement, SR)：从句子中随机选取n个不属于停用词集的单词，并随机选择其同义词替换它们；
- 随机插入(Random Insertion, RI)：随机的找出句中某个不属于停用词集的词，并求出其随机的同义词，将该同义词插入句子的一个随机位置。重复n次；
- 随机交换(Random Swap, RS)：随机的选择句中两个单词并交换它们的位置。重复n次；
- 随机删除(Random Deletion, RD)：以 $p$ 的概率，随机的移除句中的每个单词；

这些方法里，只有SR曾经被人研究过，其他三种方法都是本文作者首次提出。

值得一提的是，长句子相对于短句子，存在一个特性：长句比短句有更多的单词，因此长句在保持原有的类别标签的情况下，能吸收更多的噪声。
为了充分利用这个特性，作者提出一个方法：基于句子长度来变化改变的单词数，换句话说，就是不同的句长，因增强而改变的单词数可能不同。


## Example

    1、安装依赖
    2、example里提供了一个使用模版，直接运行expand_sentence.py
    3、示例输出：
    输入：'中华白海豚浪漫求偶画面'
    输出：
        EDA: {'中华白海豚浪漫求偶镜头', '中华白海豚浪漫画面', '中华白海豚浪漫求偶', '中华白海豚浪漫雄蛙画面', '中华白海豚浪漫求偶底片镜头', '求偶鲇鱼浪漫中华画面', '中华浪漫求偶画面', '中华鲇鱼浪漫求偶画面', '求偶白海豚浪漫中华镜头', '画面白海豚浪漫雄蛙中华', '雌兽中华白海豚浪漫雄蛙画面', '中华鲇鱼浪漫求偶万国画面'}
        