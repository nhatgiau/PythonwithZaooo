''' Giới thiệu về đệ quy '''
'''
Đệ quy là một mảng kiến thức nâng cao, ở Python thì nó không thường xuyên được dùng đến, do cách xử lí của Python 
có thể sử dụng những cấu  trúc vòng lặp đơn giản mà không cần dùng tới đệ quy. 
Nhưng dù sao thì đây cũng là  một kĩ thuật khá hữu dụng mà bạn đọc nên biết. Nó cũng chỉ đơn giản là việc chính nó gọi nó.
'''

# VÍ DỤ MINH HỌA
def cal_sum(lst):
    if not lst: # tương đương if len(lst) == 0:
        return 0
    else:
        return lst[0] + cal_sum(lst[1:])

cal_sum([1, 2, 3, 4])
cal_sum([1, 2, 3, 4, 5])

# Đệ quy theo phong cách Python
# Đệ quy và vòng lặp