# Dict(Dictionary) cũng là một container như LIST, TUPLE. 
# Có điều khác biệt là những container như List, Tuple có các index để phân biệt các phần tử thì Dict dùng các key để phân biệt.
'''
Một Dict gồm các yếu tố sau:
Được giới hạn bởi cặp ngoặc nhọn {}, tất cả những gì nằm trong đó là những phần tử của Dict.
Các phần tử của Dict được phân cách nhau ra bởi dấu phẩy (,).
Các phần tử của Dict phải là một cặp key-value
Cặp key-value của phần tử trong Dict được phân cách bởi dấu hai chấm (:)
Các key buộc phải là một hash object
'''

# Cách khởi tạo Dict

# Sử dụng cặp  dấu ngoặc {} và đặt giá  trị bên trong
# Cú pháp: {<key_1: value_1>, <key_2: value_2>, .., <key_n: value_n>}

# Sử dụng Dict Comprehension
# Điều kiện để sử dụng dict comprehension là mỗi giá trị khi được duyệt qua phải bao gồm một giá trị tương ứng với key 
# và một giá trị tương ứng với value.

# Sử dụng constructor Dict  

# Khởi tạo một Dict rỗng
# Cú pháp: dict()

# Khởi tạo một dict từ một mapping object  
# Cú pháp: dict(mapping)

# Khởi tạo bằng iterable
# Cú pháp: dict(iterable)

# Khởi tạo bằng keyword arguments
# Cú pháp 1: dict(**kwargs)
# Cú pháp 2: dict(<key_1> = <value_1>, <key_2> = <value_2>, ...)

# Sử dụng Phương thức fromkeys
# Cú pháp: dict.fromkeys(iterable, value)
# Công dụng: Cách này cho phép ta khởi tạo một dict với các keys nằm trong một iterable. 
# Các giá trị này đều sẽ nhận được một giá  trị với mặc định là None

'''
Lấy value trong Dict bằng key
Cú pháp:
Your_dict[key]
'''