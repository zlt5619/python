"""
预测不同的购买，赎出策略，对基金定投的影响
"""
import random



month_interest=[0.01,0.005,0,-0.005,-0.01]
weight=[10,25,30,25,10]
"""
随机取
random.choices(list)
给定权重取,k推出几个数
random.choices(list,weight,k=1)
"""
real_month_interest=random.choices(month_interest,weight,k=1)[0]
"""
对基金池按50年计算，一共600个月，每个月盈亏按real_month_interest计算，
每个月投资2000，看每一年的收益情况
"""
months=list(range(600))
revenue={}

ji_jin_chi=0
for i in months:
    ji_jin_chi=ji_jin_chi+2000
    ji_jin_chi=ji_jin_chi*real_month_interest+ji_jin_chi
    revenue[i+1]=ji_jin_chi
for i in range(50):
    i=i+1
    i1=str(i)
    income=str(revenue[i*12])
    cost=str(i*12*2000)
    profit=revenue[i*12]-i*12*2000
    profit1=str(profit)
    percent=profit/(i*12*2000)
    percent=str(percent)
    print("第"+i1+"年：总收入为"+income+"  共投入本金"+cost+"  盈利："+profit1+"百分比为："+percent)

