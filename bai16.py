''' Boolean trong Python '''
# Boolean là một kiểu dữ liệu mà các ngôn ngữ lập trình ngày này đều thường xuyên sử dụng. Python cũng không ngoại lệ.
# Kiểu dữ liệu này chỉ có hai giá trị:
# Một là True – có nghĩa là đúng
# Nếu không thì là False – có nghĩa là sai.

''' Boolean trong các toán tử so sánh '''
# So sánh giữa hai iterable cùng loại
# toán tử is

''' NOT, AND và OR '''

# Not là phủ định.
# Đây là cách bạn có thể đổi giá trị Boolean. Trong một số trường hợp đặc biệt. 
# Việc kiểm tra giá trị Boolean đó là False hay là True hơi phức tạp, rườm ra trong khi đó việc kiểm tra giá trị 
# ngược lại thì dễ dàng, đơn giản hơn.
'''  VALUE    NOT 
     True     False
     False    True  '''

# And là và.

# Or là hoặc.
'''  Left-value         Right-value         And             Or
      True                  True            True            True
      True                  False           False           True
      False                 True            False           True
      False                 False           False           False       '''


''' Các giá trị cũng là các Boolean '''
# Mọi giá trị khi chuyển về Boolean đều là True trừ một số trường hợp sau
# Số 0
# None
# Rỗng
# 1 là True, 0 là False