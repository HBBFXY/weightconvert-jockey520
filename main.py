#WeightConvert.py
WeightStr = input("请输入带符号的重量值:")
if WeightStr[-2:] in ["kg"]:
    pd = (eval(WeightStr[0:-2])) * 2.2046
    print("转换后的重量值是{:.3f}磅".format(pd))
elif WeightStr[-2:] in ["pd"]:
    kg = (eval(WeightStr[0:-2])) / 2.2046
    print("转换后的重量值是{:.3f}公斤".format(kg))
else:
    print("输入格式错误")
