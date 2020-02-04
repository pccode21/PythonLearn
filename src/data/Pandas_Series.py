import numpy as np
import pandas as pd


s = pd.Series(np.random.rand(5), index=['a', 'b', 'c', 'd', 'e'])
# Series可以简单的理解为一维数据，可以存储整数、浮点数、字符串、Python对象等类型的数据
# 如果index的值未指定，那么将会自动的创建数值类型的索引，从0开始，例如：0，1，2，3……len(data)-1
print(s)
"""
结果：
a    0.596809
b    0.480251
c    0.105080
d    0.300663
e    0.891450
dtype: float64
"""
print(s.index)
"""
结果：
Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
"""
s1 = pd.Series(np.random.randn(5))
print(s1)
"""
结果：
0    1.301689
1    0.527027
2   -1.483021
3    1.479517
4   -0.392570
dtype: float64
"""
d = {'b': 1, 'a': 0, 'c': 2}
s2 = pd.Series(d)  # Series是可以使用字典进行实例化的
print(s2)
"""
结果：
b    1
a    0
c    2
dtype: int64
"""
s3 = pd.Series(d, index=['b', 'c', 'd', 'a'])
print(s3)
"""
结果：
b    1.0
c    2.0
d    NaN
a    0.0
dtype: float64
"""
s4 = pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
print(s4)
"""
结果：
a    5.0
b    5.0
c    5.0
d    5.0
e    5.0
dtype: float64
"""
print(s[0])
print(s[:3])
print(s[s > s.median()])
print(s[[4, 3, 1]])
"""
结果：
0.14904040213310787
a    0.149040
b    0.719744
c    0.191781
dtype: float64
b    0.719744
e    0.721488
dtype: float64
e    0.721488
d    0.421018
b    0.719744
dtype: float64
"""
print(s['a'])
s['e'] = 12.
print(s)
"""
结果：
0.22181200008012658
a     0.221812
b     0.925073
c     0.163313
d     0.453256
e    12.000000
dtype: float64
"""
print('e' in s)
print('f' in s)
"""
结果：
True
False
"""
print(s.get('f'))
print(s.get('f', np.nan))
"""
结果：
None
nan
"""
print(np.exp(s))  # 幂次方
print(np.sqrt(s))  # 开方
print(s.dtype)
print(s.array)
print(s.to_numpy())

s5 = pd.Series(np.random.randn(5), name='my_series')
print(s5)
print(s5.name)
print(id(s5))  # 使用id方法打印s5的内存地址
s6 = s5.rename('my_series_different')
print(s6.name)
print(id(s6))
"""
结果：
0    1.368281
1   -1.582865
2    0.118555
3   -0.347563
4    0.484946
Name: my_series, dtype: float64
my_series
762821269008
my_series_different
762821301728
"""
