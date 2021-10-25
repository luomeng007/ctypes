# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/7/19 20:45
software: PyCharm

Description:
"""
import numpy as np

# class theGUID:
#     def __init__(self):
#         self.Data1 = 0xa22b5b8b
#         self.Data2 = 0xc670
#         self.Data3 = 0x4198
#         self.Data4 = np.ones(8, dtype=np.dtype('b'))
#         self.Data4[0] = 0x93
#         self.Data4[1] = 0x85
#         self.Data4[2] = 0xaa
#         self.Data4[3] = 0xba
#         self.Data4[4] = 0x9d
#         self.Data4[5] = 0xfc
#         self.Data4[6] = 0x7d
#         self.Data4[7] = 0x2b

# import ctypes
# import numpy as np
#
# DWORD = ctypes.c_ulong
# WORD = ctypes.c_ushort
# BYTE = ctypes.c_byte
#
#
# class Struct(ctypes.Structure):
#     _fields_ = [("Data1", DWORD),
#                 ("Data2", WORD),
#                 ("Data3", WORD),
#                 ("Data4", BYTE * 8)]
#
#     # data = [b'0x93, 0x85, 0xaa, 0xba, 0x9d, 0xfc, 0x7d, 0x2b']
#
#     def __init__(self, Data1=0xa22b5b8b, Data2=0xc670, Data3=0x4198, Data4=(BYTE * 8)(*list(bytearray([0x93, 0x85, 0xaa, 0xba, 0x9d, 0xfc, 0x7d, 0x2b])))):
#         super(Struct, self).__init__(Data1, Data2, Data3, Data4)
#
#     def print_values(self):
#         print(self.Data1)
#         print(self.Data2)
#         print(self.Data3)
#         print(self.Data4[0])
#         print(self.Data4[1])
#         print(self.Data4[2])
#         print(self.Data4[3])
#         print(self.Data4[4])
#         print(self.Data4[5])
#         print(self.Data4[6])
#         print(self.Data4[7])
#
#
# GUID = Struct()
# GUID.print_values()

# a = [0x93, 0x85, 0xaa, 0xba, 0x9d, 0xfc, 0x7d, 0x2b]
#
# print(a)


# import ctypes
# import numpy as np
#
# DWORD = ctypes.c_ulong
# WORD = ctypes.c_ushort
# BYTE = ctypes.c_ubyte
#
#
# class Struct(ctypes.Structure):
#     _fields_ = [("Data1", DWORD),
#                 ("Data2", WORD),
#                 ("Data3", WORD),
#                 ("Data4", BYTE * 8)]
#
#     data = [0x93, 0x85, 0xaa, 0xba, 0x9d, 0xfc, 0x7d, 0x2b]
#
#     def __init__(self, Data1=0xa22b5b8b, Data2=0xc670, Data3=0x4198, Data4=(BYTE * 8)(*np.array(data, dtype=np.dtype('b')))):
#         super(Struct, self).__init__(Data1, Data2, Data3, Data4)
#
#     def print_values(self):
#         print(self.Data1)
#         print(self.Data2)
#         print(self.Data3)
#         print(self.Data4[0])
#         print(self.Data4[1])
#         print(self.Data4[2])
#         print(self.Data4[3])
#         print(self.Data4[4])
#         print(self.Data4[5])
#         print(self.Data4[6])
#         print(self.Data4[7])
#
#
# GUID = Struct()
# GUID.print_values()

print(np.log(2))
print(-0.577216-0.6931471805599453+1.28)


# def SumSeries(array):
#     whole_result = 0
#     # set how many items series should be calculated
#     num_series = 100
#     n = np.arange(100)
#     result = np.ones(num_series)
#     # set the number of x
#     num_x = len(x)
#     for index_x, x_i in enumerate(x):
#         sum_ = 0
#         for index in n:
#             for num in range(1, index + 1):
#                 result[index - 1] *= num
#
#         series = (-1) ** (n + 1) * x_i ** n / (n * result)
#
#         for element in series:
#             sum_ += element
#
#         whole_result[index] = sum_
#
#
# t_p = -gamma - np.log(x) - SumSeries(r)
