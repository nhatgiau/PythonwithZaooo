'''
Giới thiệu về Tuple trong Python
Tuple là một container cũng được sử dụng rất nhiều trong các chương trình Python không thua kém gì List.
Một Tuple gồm các yếu tố sau:
Được giới hạn bởi cặp ngoặc (), tất cả những gì nằm trong đó là những phần tử của Tuple.
Các phần tử của Tuple được phân cách nhau ra bởi dấu phẩy (,).
Tuple có khả năng chứa mọi giá trị, đối tượng trong Python.
'''

'''
Cách khởi tạo Tuple
'''

# Sử dụng cặp  dấu ngoặc () và đặt giá  trị bên trong
# Cú pháp: (<giá trị thứ nhất>, <giá trị thứ hai>, .., <giá trị thứ n – 1>, <giá trị thứ n>)
tup = (1, 2, 3, 4)
print(tup)
empty_tup = ()  # khởi tạo tuple rỗng
print(empty_tup)
q = type(tup) # kiểu dữ liệu Tuple thuộc lớp tuple
print(q)

# Sử dụng Tuple Comprehension
# Với Tuple thì khái niệm Comprehension này không được áp dụng

# Sử dụng constructor Tuple
# Cú pháp: tuple(iterable) : Giống hoàn toàn với việc bạn sử dụng constructor List. 
# Khác biệt duy nhất là constructor Tuple sẽ tạo ra một Tuple.

'''
Một số toán tử với Tuple trong Python
'''

# Toán tử +
# Toán tử *
# Toán tử in


'''
Indexing và cắt Tuple trong Python
Indexing và cắt Tuple hoàn toàn tương tự như với kiểu dữ liệu List.
'''

'''
Thay đổi nội dung Tuple trong Python
Tuple và chuỗi đều là một dạng hash object (immutable). 
Do đó việc bạn muốn thay đổi nội dung của nó trên lí thuyết là không.
'''

'''
Ma trận
Giống với list
'''

'''
Tuple có phải luôn luôn là một hash object?
không thể thay đổi giá trị ở bên trong Tuple. Tuy nhiên, không phải lúc nào cũng vậy.
Giá trị bên trong tuple đó là một List. Và, List là một unhash object. Suy ra, ta có thể thay đổi nội dung của nó.
'''

'''
Các phương thức của Tuple
'''

# Phương thức count
# Cú pháp: <Tuple>.count(value) : Trả về một số nguyên, chính là số lần xuất hiện của value trong Tuple.

# Phương thức index
# Cú pháp: <Tuple>.index(sub[, start[, end]]) : Tương tự phương thức index của kiểu dữ liệu chuỗi.


'''
Khi nào thì chọn Tuple thay cho List?
Tuple khác List ở chỗ Tuple không cho phép bạn sửa chữa nội dung, còn List thì có. Vì đặc điểm đó, Tuple mạnh hơn List ở những điểm sau:
Tốc độ truy xuất của Tuple nhanh hơn so với List
Dung lượng chiếm trong bộ nhớ của Tuple nhỏ hơn so với List
Bảo vệ dữ liệu của bạn sẽ không bị thay đổi
Có thể dùng làm key của Dictonary (một kiểu dữ liệu sẽ được giới thiệu). Điều mà List không thể vì List là unhash object.
Những điểm trên là những điều giúp bạn có thể cân nhắc việc chọn Tuple hay List để lưu dữ dữ liệu dưới một mảng.
'''