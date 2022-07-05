import os
import jieba
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体 SimHei为黑体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负

'''
说明:
    使用结巴分词,对每一年的新闻进行分词,并完成词频统计,截取词频前十的词语,绘制柱状图
'''
if __name__ == '__main__':
    yearpath = "resultByyear/"
    pic = "pic/"
    for in_ in os.listdir(yearpath):
        timelst = []
        wordlst = []
        # print("年份：",in_[:4])
        fp = open(yearpath + in_, mode="r", encoding='utf-8')
        text = fp.read()

        # 结巴分词
        cut_text = (jieba.lcut(text))

        dic = {}
        for word in cut_text:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1

        # 统计每个词出现次数，从高到第排序
        swd = sorted(list(dic.items()), key=lambda lst: lst[1], reverse=True)

        # 排除那些虚词，连词，标点符号等
        f1 = open('中文虚词列表.txt', encoding="utf-8")
        stop_wds = f1.read()
        f1.close()

        count = 0
        for kword, times in swd:
            if kword not in stop_wds and count <= 10:  # 当前词未包含在排除的那些词里面，就输出现次数
                count += 1
                timelst.append(times)
                wordlst.append(kword)
                # print(kword, times)

        p1 = plt.figure(figsize=(8, 6), dpi=80)  # 确定画布大小
        plt.title(f'{in_[:4]}年份词频统计')  # 设置标题
        plt.bar(range(len(timelst)), timelst, fc='blue')  # 绘制柱状图

        for a, b in zip(list(range(len(timelst))), timelst):
            plt.text(a, b, '%.1f' % b, ha='center', va='bottom', fontsize=10)  # 添加数据标签
        plt.xticks(range(len(timelst)), wordlst)

        plt.savefig(f'{pic + in_[:4]}年份词频统计.png')
        # plt.show()

        fp.close()
        # break
