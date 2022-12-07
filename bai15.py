'''
Khái niệm iteration trong Python
Iteration là một khái niệm chung cho việc lấy từng phần tử một của một đối tượng nào đó, bất cứ khi nào bạn sử dụng vòng lặp hay 
kĩ thuật nào đó để có được giá trị một nhóm phần tử thì đó chính là Iteration.
'''

'''
Giới thiệu iterable object trong Python
Iterable object là một object có phương thức __iter__ trả về một iterator, hoặc là một object có phương thức __getitem__ 
cho phép bạn lấy bất cứ phần tử nào của nó bằng indexing ví dụ như Chuỗi, List, Tuple.
'''

'''
Giới thiệu iterator object trong Python
Iterator object đơn giản chỉ là một đối tượng mà cho phép ta lấy từng giá trị một của nó. 
Có nghĩa là bạn không thể lấy bất kì giá trị nào như ta hay làm với List hay Chuỗi.
Iterator không có khả năng tái sử dụng trừ một số iterator có phương thức hỗ trợ như file object sẽ có phương thức seek.
'''

'''
Một số hàm hỗ trợ cho iterable object trong Python
'''
# Hàm tính tổng – sum
# Cú pháp: sum(iterable, start=0)
# Công dụng: Trả về tổng các giá trị của iterable và iterable này chỉ chứa các giá trị là số. 
# Còn start chính là giá trị ban đầu. Có nghĩa là sẽ cộng từ start lên. Mặc định là 0

# Hàm tìm giá trị lớn nhất – max
# Cú pháp: max(iterable, *[, default=obj, key=func]) hoặc max(arg1, arg2, *args, *[, key=func])
# Công dụng: Nhận vào một iterable.Tìm giá trị lớn nhất bằng key (mặc định là sử dụng operator >). 
# Default là giá trị muốn nhận về trong trường hợp không lấy được bất kì giá trị nào trong iterable.

# Hàm tìm giá trị nhỏ nhất – min
# Cú pháp: min(iterable, *[, default=obj, key=func]) hoặc min(arg1, arg2, *args, *[, key=func])
# Ý nghĩa: giống như hàm max. Khác ở chỗ đây là tìm giá trị nhỏ nhất

# Hàm sắp xếp – sorted
# Cú pháp: sorted(iterable, /, *, key=None, reverse=False)
# Công dụng: Giống với phương thức sort của List object.