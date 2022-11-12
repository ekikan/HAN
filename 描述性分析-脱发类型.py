#准备
import pandas as pd
import matplotlib.pyplot as plt


#读取数据
data = pd.read_csv(r"C:\Users\ekish\Desktop\data\hairloss\2019年国内各类脱发人群的抽样数据.csv")
#男女脱发人数
loss_count = data["性别"].value_counts()
man_loss = loss_count["男"]
woman_loss = loss_count["女"]
# 脱发人数最多的脱发类型
type_count = data["脱发类型"].value_counts()
typeMax = type_count.idxmax()

print(f"男性的脱发人数为{man_loss}，女性的脱发人数为{woman_loss}，脱发人数最多的脱发类型为{typeMax}")
#绘制脱发人群职业柱状图
plt.rcParams["font.sans-serif"] = ["SimHei"]

career_count = data["职业"].value_counts()
plt.subplot(2,2,1)
career_count.plot.bar(ax=plt.gca())
plt.xlabel("职业")
plt.ylabel("人数")
plt.xticks(rotation=45)
#绘制脱发人群所在城市柱状图
city_count = data["所在城市"].value_counts()
plt.subplot(2,2,2)
city_count.plot.bar(ax=plt.gca())
plt.xlabel("城市")
plt.ylabel("人数")
plt.xticks(rotation = 45)
#绘制脱发人群脱发类型柱状图
type_count =data["脱发类型"].value_counts()
plt.subplot(2,2,3)
type_count.plot.bar(ax=plt.gca())
plt.xlabel("脱发类型")
plt.ylabel("人数")
plt.xticks(rotation=45)
#绘制脱发人群年龄分布图
plt.subplot(2,2,4)
plt.hist(data["年龄"],bins=10)
plt.xlabel("年龄")
plt.ylabel("人数")
#调整子图位置并展示
plt.tight_layout()
plt.show()