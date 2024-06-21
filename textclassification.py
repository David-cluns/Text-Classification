#SafeJClass是Hanlp库中用于安全地加载java类的函数
from pyhanlp import SafeJClass
import os

# 设置路径
HANLP_DATA_PATH = "./Dataset"
DATA_FILES_PATH = "THUCNews_TrainSet"
MODEL_PATH = "./model"
MODEL_FILE = f"{DATA_FILES_PATH}.ser"

#获取语料数据，返回两个列表，data(文本内容)，label(对应的主题标签)
def get_corpus_data(corpus_path):
    data = []
    labels = []
    categories = os.listdir(corpus_path)
    for category in categories:
        category_path = os.path.join(corpus_path, category)
        if os.path.isdir(category_path):
            files = [f for f in os.listdir(category_path) if f.endswith('.txt')]
            for file in files:
                file_path = os.path.join(category_path, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    data.append(content)
                    labels.append(category)
    return data, labels

#加载java类
NaiveBayesClassifier = SafeJClass('com.hankcs.hanlp.classification.classifiers.NaiveBayesClassifier')#Hanlp提供的朴素贝叶斯分类器
IOUtil = SafeJClass('com.hankcs.hanlp.corpus.io.IOUtil')#HanLp提供的用于对象读写的实用工具类
MemoryDataSet = SafeJClass('com.hankcs.hanlp.classification.corpus.MemoryDataSet')#HanLP提供的内存数据集类，用于存储训练数据

# 获取语料数据和标签
corpus_path = os.path.join(HANLP_DATA_PATH, DATA_FILES_PATH)
data, labels = get_corpus_data(corpus_path)

#得到根据语料数据训练好的分类器对象
def train_classifier(data, labels):
    dataset = MemoryDataSet()
    for text, label in zip(data, labels):
        dataset.add(label, text)
    classifier = NaiveBayesClassifier()
    classifier.train(dataset)
    return classifier

#将分类器的模型保存到指定路径
def save_classifier(classifier, path):
    if not os.path.exists(path):
        os.makedirs(path)
    model_path = os.path.join(path, MODEL_FILE)
    print(f"将模型存到 {path}")
    IOUtil.saveObjectTo(classifier.getModel(), model_path)

#从指定路径加载分类器模型
def load_classifier(path):
    model_path = os.path.join(path,MODEL_FILE)
    print(f"在 {path}中检查模型")
    if os.path.isfile(model_path):
        print("模型存在, 加载模型...")
        return NaiveBayesClassifier(IOUtil.readObjectFrom(model_path))
    print("模型不存在.")
    return None

#打印文本分类的结果
def predict(classifier, texts):
    results = []
    for text in texts:
        category = classifier.classify(text)
        results.append((text, category))
        print(f"《{text}》\t属于分类\t【{category}】")
    return results


if __name__ == '__main__':
    classifier = load_classifier(MODEL_PATH)
    if classifier is None:
        print("模型文件不存在，开始训练模型...")
        classifier = train_classifier(data, labels)
        save_classifier(classifier, MODEL_PATH)
        print("模型训练完成并已保存。预测结果为：")
    else:
        print("模型加载完成，预测结果为：")

    #要预测的标题列表
    titles_to_predict = [
        "韩国宣布进入人口危机紧急状态",
        "医生称三甲医院很少招中医院校毕业生",
        "陈晓方未回应婚姻破裂传闻",
        "巴黎奥运中国女排25人大名单",
        "美方称乌克兰必须先打败俄罗斯才能加入北约，还表示乌克兰危机对乌人民的安全构成了威胁，如何评价此事？",
        "高考志愿填报该看兴趣还是就业前景",
        "香港顶流姜涛巴黎时装周"
    ]

    #预测并输出结果
    predictions = predict(classifier, titles_to_predict)




