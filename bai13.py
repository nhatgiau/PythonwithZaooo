'''
Các phương thức tiện ích

'''
# Phương thức copy
# Cú pháp: <Dict>.copy()
# Công dụng: Giống với phương thức copy trong LIST. Để làm gì thì chắc các bạn cũng có thể suy nghĩ ra.

# Phương thức clear
# Cú pháp: <Dict>.clear()
# Công dụng: Loại bỏ tất cả những phần tử có trong Dict

'''
Các phương thức xử lí

'''
# Phương thức get
# Cú pháp: <Dict>.get(key [,default])
# Công dụng: Trả về giá trị của khóa key. 
# Nếu key không có trong Dict thì trả về giá trị default. Default có giá trị mặc định là None nếu chúng ta không truyền vào.

# Phương thức items
# Cú pháp: <Dict>.items()
# Công dụng: Trả về một giá trị thuộc lớp dict_items. 
# Các giá trị của dict_items sẽ là một tuple với giá trị thứ nhất là key, giá trị thứ hai là value.

# Phương thức keys
# Cú pháp: <Dict>.keys()
# Công dụng: Trả về một giá trị thuộc lớp dict_keys. Các giá trị của dict_keys sẽ là các key trong Dict.

# Phương thức values
# Cú pháp: <Dict>.values()
# Công dụng: Trả về một giá trị thuộc lớp dict_values. Các giá trị của dict_values sẽ là các value trong Dict.

# Phương thức pop
# Cú pháp: <Dict>.pop(key [,default])
# Công dụng: Bỏ đi phần tử có key và trả về value của key đó. Trường hợp key không có trong dict.

# Phương thức popitem
# Cú pháp: <Dict>.popitem()
# Công dụng: Trả về một 2-tuple với key và value tương ứng bất kì (vấn đề này liên quan đến giá trị của hash của key.
# Do đó bạn cũng hiểu vì sao key buộc phải là một hash object) trong Dict. Và cặp key-value sẽ bị loại bỏ ra khỏi Dict.

# Phương thức setdefault
# Cú pháp: <Dict>.setdefault(key [,default])
# Công dụng: Trả về giá trị của key trong Dict. Trường hợp key không có trong Dict thì sẽ trả về giá trị default. 
# Thêm nữa, một cặp key-value mới sẽ được thêm vào Dict với key bằng key và value bằng default.

# Phương thức update
# Cú pháp: <D>.update([E, ]**F)
# Công dụng: Phương thức giúp bạn cập nhật nội dung cho Dict. 

# Toán tử “|” với 2 dict
# Cú pháp: <Dict_A> | <Dict_B>
# Công dụng: Trả về một dict mới với các cặp key – value có mặt ở một trong 2 dict. 
# Nếu một key bất kì có trong cả 2 dict, thì giá trị được lấy sẽ là cặp key – value ở Dict_B