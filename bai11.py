#  Set là một container, tuy nhiên không được sử dụng nhiều bằng LIST hay TUPLE.
'''
Một Set gồm các yếu tố sau:

Được giới hạn bởi cặp ngoặc {}, tất cả những gì nằm trong đó là những phần tử của Set.
Các phần tử của Set được phân cách nhau ra bởi dấu phẩy (,).
Set không chứa nhiều hơn 1 phần tử trùng lặp
Set chỉ có thể chứa các hashable object nhưng chính nó không phải là một hashable object. 
Do đó, bạn không thể chứa một set trong một set.
'''

# Cách khởi tạo Set
# Sử dụng cặp  dấu ngoặc {} và đặt giá  trị bên trong
# Cú pháp: {<giá trị thứ nhất>, <giá trị thứ hai>, .., <giá trị thứ n – 1>, <giá trị thứ n>}


# Sử dụng Set Comprehension
set_1 = {value for value in range(3)}
print(set_1)

# Sử dụng constructor Set
# Cú pháp: set(iterable)
# Công dụng: Giống hoàn toàn với việc bạn sử dụng constructor List. Khác biệt duy nhất là constructor Set sẽ tạo ra một Set.

# Một số toán tử với Set trong Python

# Toán tử in
# Cú pháp: value in <Set>
# Công dụng: Kết quả trả về là True nếu value xuất hiện trong Set. Ngược lại sẽ là False

# Toán tử -
# Cú pháp: <Set1> - <Set2>
# Công dụng: Kết quả trả về là một Set gồm các phần tử chỉ tồn tại trong Set1 mà không tồn tại trong Set2

# Toán tử &
# Cú pháp: <Set1> & <Set2>
# Công dụng: Kết quả trả về là một Set chứa các phần tử vừa tồn tại trong Set1 vừa tồn tại trong Set2

# Toán tử |
# Cú pháp: <Set1> | <Set2>
# Công dụng:  Kết quả trả về là một Set chứa tất cả các phần tử tồn tại trong hai Set

#Toán tử ^
# Cú pháp: <Set1> ^ <Set2>
# Công dụng:  Kết quả trả về là một Set chứa tất cả các phần tử chỉ tồn tại ở một trong hai Set