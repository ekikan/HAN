import pandas as pd

shuju = pd.read_csv(r"C:\Users\ekish\Desktop\HAN\data1.csv",encoding="shift-jis")

print(shuju.iloc[[0,46],[5,6]])
print(shuju[(shuju["０〜14歳割合"]>10)&(shuju["65歳以上割合"]>30)])
print(shuju["総数"].astype(int))

