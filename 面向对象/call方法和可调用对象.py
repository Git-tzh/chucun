# 测试调用方法__call__


class SalaryAccount:
    '''工资计算类'''
    def __call__(self, salary):
        print("算工资啦......")
        yearSalary = salary*12
        daySalary = salary // 24
        hourSalary = daySalary // 8
        return dict(yearSalary=yearSalary, mouthSalary=salary, daySalary=daySalary, hourSalary=hourSalary)


s = input("请输入月薪："+SalaryAccount)
print("年薪是:"+yearSalary)
