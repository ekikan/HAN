import pandas as pd

data = pd.read_csv(r"C:\Users\ekish\Desktop\feifei\hotpot.csv")

huoguo = data[data["店铺名称"].str.contains("火锅")]
huoguo1 = huoguo.set_index("店铺名称")
huoguo2 =  huoguo1["口味评分"].idxmax()

print(f"成都口味评分最高的火锅店是{huoguo2}")

huoguo3 = huoguo1["人均消费"].idxmin()

print(f"成都人均价格最低的火锅店是{huoguo3}")

huoguo4 = huoguo1.sort_values(by="口味评分",ascending=False)
huoguo5 = huoguo4.head(5)

print(huoguo5)

data["性价比评分"] = (data["口味评分"]/data["人均消费"])*40
data["氛围评分"] = (data["环境评分"]+data["服务评分"])/2
data[["性价比评分","氛围评分"]] = data[["性价比评分","氛围评分"]].round(2)
huoguo1 = data.set_index("店铺名称")
huoguo5 = huoguo1.sort_values(by="性价比评分",ascending=False)
huoguo6 = huoguo1.sort_values(by="氛围评分",ascending=False)
huoguo7 = huoguo5.head(5)
huoguo8 = huoguo6.head(5)
huoguo9 = huoguo1["性价比评分"].idxmax()

print(f"成都性价比最高的餐厅是{huoguo9}")