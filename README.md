# Text-Classification：借助pyhanlp对新闻标题分类

## 背景

利用[HanLP](https://github.com/hankcs/pyhanlp)进行文本分类，对热榜话题按照**标题**分类至财经、彩票、房产、股票、家居、教育、科技、社会、时尚、时政、体育、星座、游戏、娱乐等14类行业中。



## 语料库

本项目的语料库特征文本分类语料库，对应IDataSet接口。文本分类语料库包含两个概念：文档和类目。一个文档只属于一个类目，一个类目可能含有多个文档。本项目所使用的语料库为[THUCNews](http://thuctc.thunlp.org/)以及[搜狗文本分类语料库迷你版.zip](http://file.hankcs.com/corpus/sogou-text-classification-corpus-mini.zip)



### 数据格式

分类语料的根目录。目录必须满足如下结构

```bash
根目录
	├── 分类A
	│   └── 1.txt
	│   └── 2.txt
	│   └── 3.txt
	├── 分类B
	│   └── 1.txt
	│   └── ...
	└── ...

```



## 用法

```bash
#安装pyhanlp库
conda install -c conda-forge openjdk python=3.8 jpype1=0.7.0 -y
pip install pyhanlp

#运行textclassification.py文件
python textclassification.py
```



## 参考资料

- [hankcs/pyhanlp](https://github.com/hankcs/pyhanlp?tab=readme-ov-file)
- [pyhanlp 文本分类与情感分析](https://blog.csdn.net/FontThrone/article/details/82831801)