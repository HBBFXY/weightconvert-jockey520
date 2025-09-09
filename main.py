#WeightConvert.py
WeightStr = input("")
if WeightStr[-2:] in ["kg"]:
    pd = (eval(WeightStr[0:-2])) * 2.2046
    print("对应的英制重量为{:.3f}磅".format(pd))
elif WeightStr[-2:] in ["pd"]:
    kg = (eval(WeightStr[0:-2])) / 2.2046
    print("对应的公制重量为{:.3f}公斤".format(kg))
else:
    print("输入格式错误")
