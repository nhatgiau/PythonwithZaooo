# các phương thức tách chuỗi

# Phương thức split
# Cú pháp : <chuỗi>.split(sep=None, maxsplit=-1) :  Trả về một list (kiểu dữ liệu sẽ được Kteam giới thiệu ở bài KIỂU DỮ LIỆU LIST) 
# bằng cách chia các phần tử bằng kí tự sep.
# Nếu sep mặc định bằng None thì sẽ dùng kí tự khoảng trắng.
# Nếu maxsplit được mặc định bằng -1, Python sẽ không bị giới hạn việc tách, còn không, 
# Python sẽ tách với số lần được cung cấp thông qua maxsplit.

# Phương thức rsplit
# Cú pháp : <chuỗi>.split(sep=None, maxsplit=-1) :  cũng hoàn toàn như phương thức split, có điều là việc tách từ bên phải sang trái

# Phương thức splitlines
# Cú pháp : <chuỗi>.splitlines(keppends=False) : hoàn toàn giống với phương thức split, nhưng các phần tử được chia tách bằng “\n” (xuống dòng). 
# Nếu keppends được cung cấp giá trị True, các phần tử khi được phân tách cũng sẽ có kí tự “\n” theo sau.

# Phương thức partition 
# Cú pháp : <chuỗi>.partition(sep) : Trả về một tuple với 3 phần tử. Các phần tử đó lần lượt là chuỗi trước chuỗi sep, sep và  chuỗi sau sep.
# Trong trường hợp không tìm thấy sep trong chuỗi, mặc định trả về giá trị đầu tiên là chuỗi ban đầu và 2 giá trị kế tiếp là chuỗi rỗng.

# Phương thức rpartition
# Cú pháp : <chuỗi>.rpartition(sep) : Cách phân chia giống như phương thức partition nhưng lại chia từ phải qua trái. 
# Và với sep không có trong chuỗi thì sẽ trả về 2 giá trị đầu tiên là chuỗi rỗng và cuối cùng là chuỗi ban đầu.


# Các phương thức tiện ích

# Phương thức count
# Cú pháp : <chuỗi>.count(sub, [start, [end]]) : Trả về một số nguyên, chính là số lần xuất hiện của sub trong chuỗi. 
# Còn start và end là số kĩ thuật slicing (lưu ý không hề có bước).

# Phương thức startswith 
# Cú pháp : <chuỗi>.startswith(prefix[, start[, end]]) : Trả về  giá trị True nếu chuỗi đó bắt đầu bằng chuỗi prefix. Ngược lại là False.
# Hai yếu tố start, end tượng trưng cho việc slicing (không có bước) để kiểm tra với chuỗi slicing đó.

# Phương thức endswith
# Cú pháp : <chuỗi>.endswith(prefix[, start[, end]]) : Trả về  giá trị True nếu chuỗi đó kết thúc bằng chuỗi prefix. Ngược lại là False.
# Hai yếu tố start end tượng trưng cho việc slicing (không có bước) để kiểm tra với chuỗi slicing đó.

# Phương thức find
# Cú pháp : <chuỗi>.find(sub[, start[, end]]) : Trả về một số nguyên, là vị trí đầu tiên của sub khi dò từ trái sang phải trong chuỗi. 
# Nếu sub không có trong chuỗi, kết quả sẽ là -1. 
# Vẫn như các phương thức khác, start end đại diện cho slicing và ta sẽ tìm trong chuỗi slicing này.

# Phương thức rfind
# Cú pháp : <chuỗi>.rfind(sub[, start[, end]]) : Tương tự phương thức find nhưng tìm từ phải sang trái 

# Phương thức index
# Cú pháp : <chuỗi>.index(sub[, start[, end]]) : Tương tự phương thức find.
# Nhưng khác biệt là sẽ có lỗi ValueError nếu không tìm thấy chuỗi sub trong chuỗi ban đầu

# Phương thức rindex 
# Cú pháp : <chuỗi>.rindex(sub[, start[, end]]) :  Tương tự phương thức rindex. 
# Và cũng khác ở điểm là sẽ có ValueError nếu không tìm thấy chuỗi sub trong chuỗi ban đầu


# Các phương thức xác thực

# Phương thức islower 
# Cú pháp : <chuỗi>.islower() : Trả về True nếu tất cả các kí tự trong chuỗi đều là viết thường. Ngược lại là False

# Phương thức isupper
# Cú pháp : <chuỗi>.isupper() : Trả về True nếu tất cả các kí tự trong chuỗi đều là viết hoa. Ngược lại là False

# Phương thức istitle
# Cú pháp : <chuỗi>.istitle() :  Trả về True nếu chuỗi đó là một dạng title. Ngược lại là False

# Phương thức isidentifier 
# Cú pháp : <chuỗi>.isidentifier() : Giúp xác định xem một chuỗi có phải là một định danh hay không.
'''
Phương thức isidentifier trả về True khi cả ba điều kiện sau được thỏa mãn:

Chuỗi phải được bắt đầu bằng dấu gạch dưới (_) hoặc các kí tự chữ cái
Chuỗi không được chứa bất kì khoảng trắng nào
Không được chứa các kí tự đặc biệt (_, %, $, _...) ngoại trừ việc kí tự đầu tiên có thể là dấu gạch dưới.
'''

# Phương thức isdigit
# Cú pháp : <chuỗi>.isdigit() : rả về True nếu tất cả các kí tự trong chuỗi đều là những con số từ 0 đến 9

# Phương thức isspace
# Cú pháp : <chuỗi>.isspace() : Trả về True nếu tất cả các kí tự trong chuỗi đều là kí tự khoảng trắng

# Phương thức iskeyword (Thuộc thư viện keyword)
# Cú pháp : import keyword
#           keyword.iskeyword(<chuỗi>)
# Trả về True nếu chuỗi đó tương ứng với một từ khóa.



