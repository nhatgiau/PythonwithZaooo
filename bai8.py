'''
LIST là một container được sử dụng rất nhiều trong các chương trình Python. Một List gồm các yếu tố sau:

Được giới hạn bởi cặp ngoặc [ ], tất cả những gì nằm trong đó là những phần tử của List.
Các phần tử của List được phân cách nhau ra bởi dấu phẩy (,).
List có khả năng chứa mọi giá trị, đối tượng trong Python. Và bao gồm chứa chính nó! .
'''

a = [1, 2, 3, 4, 5]        # Một List chứa 5 số nguyên
print(a)

b = ['a', 'b', 'c', 'd']   # Một List chứa 4 chuỗi
print(b)

c = [[1, 2], [3, 4]]       # Một List chứa 2 List là [1, 2] và [3, 4]
print(c)

d = [1, 'one', [2, 'two']] # List chứa số nguyên, chuỗi, và List
print(d)


'''
Cách khởi tạo List

'''

# Sử dụng cặp dấu ngoặc [] đặt giá trị bên trong
# Cú pháp : [<giá trị thứ nhất>, <giá trị thứ hai>, .., <giá trị thứ n – 1>, <giá trị thứ n>]

# Sử dụng List Comprehension
# Cú pháp : [Comprehension]

# Sử dụng constructor List
# Cú pháp : list (iterable)


'''
Một số toán tử với List trong Python
'''

# Toán tử +
# Toán tử *
# Toán tử in
# Các toán tử so sánh

'''
Indexing và cắt List trong Python
List với chuỗi giống nhau rất nhiều điểm, và phần Indexing và cắt List này hoàn toàn giống với Indexing và cắt chuỗi
'''

'''
Thay đổi nội dung List trong Python
'''
lst = [1, 'two', 3]
lst[1]
lst[1] = 2
lst


'''
Ma trận
'''

'''
Vấn đề cần lưu tâm khi sử dụng List
Không được phép gán List này qua List kia nếu không có chủ đích
'''
# Toán tử is
# Cú pháp : A is B : iểm tra xem hai biến A và B có cùng trỏ đến một đối tượng hay không. 
# Nếu một trong hai biến được gán giá trị bằng biến còn lại, thì kết quả trả về là True.
