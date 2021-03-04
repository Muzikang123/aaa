from day15.Calc import Calc
import unittest


from ddt import ddt
from ddt import data
from ddt import unpack
'''
DDT:(Data Driven Test)
1、准备数据源
2、进行参数化（就是将数据集中放在某处，让程序自己去取数据）
3、导入ddt的ddt,data,unpack
4.1,、将测试类用@ddt注释
'''
data1=[
    [1,2,3],
    [4,5,9]
]
@ddt
class TestCalc(unittest.TestCase):
    @data(*data1) #引入数据源
    @unpack#不要解包
    def testAdd1(self,a,b,s):
        c=Calc()
        sum=c.Add(a,b)
        #断言
        self.assertEqual(s,sum)
