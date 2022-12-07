''' Giới thiệu generator '''
# Generator là iterator, một dạng của iterable nhưng khác ở chỗ bạn không thể tái sử dụng. 
# Vì sao lại như vậy? Generator không lưu trữ tất cả các giá trị của bạn ở bộ nhớ, mà nó sinh ra lần lượt

''' Lệnh yield '''
# Lệnh này cách sử dụng gần giống với lệnh return, tuy nhiên nó khác return ở chỗ trả về một object thì yield sẽ trả về một generator.
'''
Lưu ý: ngoài cách dùng for như bên trên để duyệt các generator, Kteam đã giới thiệu với các bạn hàm next ở bài ITERATION & 
MỘT SỐ HÀM HỖ TRỢ CHO ITERATION OBJECT TRONG PYTHON – một hàm để giúp bạn làm công việc tương tự.
'''

# Phương thức send
'''
Cú pháp:
generator.send(value)

'''

''' Giới thiệu lambda '''
'''
Cú pháp 
lambda argument_1, argument_2, …, argument_n : expression

Như đã nói ở trên, lambda hoạt động như khi bạn dùng từ khóa “def” khai báo hàm. Tuy nhiên, vẫn có một vài ưu điểm nổi trội của lambda so với cách bình thường:

lambda là một expression, không phải là một câu lệnh. (Khái niệm expression đã được Kteam giới thiệu). 
Do đó lambda có thể có ở một vài chỗ mà “def” không thể có (bạn đọc sẽ biết ở phần sau)
lambda là một dòng expression duy nhất, không phải là một khối lệnh. 
Phần expression của lambda giống với phần khối lệnh của hàm với một lệnh return ở cuối hàm nhưng với lambda bạn chỉ cần ghi 
giá trị mà không cần ghi return. Bạn đọc sẽ hiểu rõ hơn ở phần sau khi biết lambda có thể sử dụng các câu lệnh điều kiện mà không 
cần phải sử dụng tới lệnh “if”. Nhờ được thiết kế như vậy, lambda được ưu tiên dùng cho việc tạo ra những hàm đơn giản, còn nếu 
phức tạp thì ta sẽ sử dụng đến từ khóa “def”.
'''

# Vì sao dùng lambda?
#  lambda là một công cụ nhanh gọn để bạn có  thể tạo ra một hàm và sử dụng nó. Việc sử dụng nó thay cho “def” hay không là tùy ở bạn.


# Câu điều kiện cho lambda

# Lambda chồng lambda
# Bạn có thể chồng 2 hoặc 3 lambda lên nhau cùng một lúc
# Thực tế thì những lambda chồng lambda này khá phức tạp. Python vốn không thích sự khó hiểu, phức tạp, sự thiếu thanh lịch thế nên 
# thường thì việc chồng lambda như thế này rất không được khuyến khích.

# Hàm map
'''
Cú pháp
map(func, iterable)

Hàm map này sẽ trả về một map object (một dạng generator).
Vậy hàm map hoạt động như thế nào? Nôm na là hàm map lấy từng  phần  tử của iterable sau đó dùng gọi hàm func với argument là 
giá trị mới lấy ra từ iterable, kết quả trả về của hàm func sẽ được yield.

Lưu ý: Ở list comprehension trên, nếu bạn thay ngoặc vuông ( [ ) bằng ngoặc tròn ( (  ) thì thời gian của ngoặc tròn có thể 
tương đương với hàm map và tiết kiệm dữ liệu hơn list comprehension vì nó cũng tạo ra một generator expression.

Cú pháp
map(func, *iterable)
'''


# Hàm filter
'''
Filter có nghĩa là bộ phận lọc. Nghe qua, chắc bạn cũng ít nhiều biết được nó sẽ làm gì rồi.

Cú pháp 
filter(function or None, iterable)

Cũng như hàm map, hàm filter sẽ trả về một filter object (một dạng generator object)
Lưu ý: không như hàm map, iterable ở đây chỉ là 1 container, không hề có packing argument.
'''

# Hàm reduce
'''

from functools import reduce
Ở các ví dụ  tiếp theo, thì sẽ không có dòng này vì lặp lại nên bạn đọc coi như chúng ta đã có dòng lệnh này ở đầu chương trình 
tức có nghĩa là chúng ta đã import hàm reduce từ thư viện functools rồi.

Cú pháp
reduce(function, sequence[, initial])
Lưu ý: Hàm reduce không giống như hai hàm trước là trả về một generator expression mà là một giá trị.
Lưu ý: đưa theo thứ tự (index 0, index 1)
Hàm function này sẽ trả ra một giá trị (ta kí hiệu là A). Sau đó lấy tiếp giá trị thứ ba của sequence (index 2), 
rồi gửi vào function cũng theo thứ tự (A, index 2), rồi lại lặp lại như thế cho tới khi hết sequence.
'''