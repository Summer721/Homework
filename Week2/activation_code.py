#作业要求
# """
# 1、搭建好pyenv环境，理解local、global、shell 3种方式区别，安装部署完成jupyter并运行
# 2、打印出100以内的斐波那契数列，使用2种方法实现
# 3、使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
# 要求：本周日4月1号完成作业
# """
#第三题：
import random
def make_act():
    "make activation code"

    #生成字符列表
    Upper = [chr(i) for i in range(65, 90)]
    Lower = [chr(i) for i in range(97, 123)]
    number_str = [str(i) for i in range(0,10)]

    #10位激活码
    ret_code = ''
    for _ in range(0,10):
        #code_dict = dict(zip(range(3), (random.choice(Upper), random.choice(Lower), random.choice(number_str))))
        code_dict = dict(zip(range(3), map(random.choice,(Upper,Lower,number_str))))
        temp = code_dict[random.choice(list(code_dict.keys()))]
        ret_code += temp
    while True:
        yield ret_code

i = 1
while i <= 200:
    print(next(make_act()))
    i += 1
