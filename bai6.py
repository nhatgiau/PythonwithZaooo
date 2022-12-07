# Các phương thức biến đổi

# Phương thức capitalize
# Cú pháp : <chuỗi>.capitalize() : Trả về một chuỗi với kí tự đầu tiên được viết hoa và viết thường tất cả những kí tự còn lại.

# Phương thức upper
# Cú pháp : <chuỗi>.upper() : Trả về một chuỗi với tất cả các kí tự được chuyển thành các kí tự viết hoa

# Phương thức swapcase
# Cú pháp : <chuỗi>.swapcase() : Trả về một chuỗi với các kí tự viết hoa được chuyển thành viết thường, các kí tự viết thường được chuyển thành viết hoa

# Phương thức title
# Cú pháp <chuỗi>.title() :  Trả về một chuỗi với định dạng tiêu đề, có nghĩa là các từ sẽ được viết hoa chữ cái đầu tiên, còn lại là viết thường

# Các phương thức định dạng

# Phương thức Phương thức center
# Cú pháp : <chuỗi>.center(width, [fillchar])
# Trả về một chuỗi được căn giữa với chiều rộng width.
# Nếu fillchar là None (không được nhập vào) thì sẽ dùng kí tự khoảng trắng để căn, không thì sẽ căn bằng kí tự fillchar.
# Một điều nữa là kí tự fillchar là một chuỗi có độ dài là 1.

# Phương thức rjust
# Cú pháp : <chuỗi>.rjust(width, [fillchar]) :  Cách hoạt động tương tự như phương thức center, có điều là căn lề phải

# Phương thức ljust
# Cú pháp : <chuỗi>.ljust(width, [fillchar]) : Cách hoạt động tương tự phương thức center, nhưng căn lề trái.

# Các phương thức xử lí 

# Phương thức encode
# Cú pháp : <chuỗi>.encode(encoding=’utf-8’, errors=’strict’) 
#  Đây là phương thức dùng để encode một chuỗi với phương thức mã hóa mặc định là utf-8. 
# Còn về  errors mặc định sẽ là strict có nghĩa là sẽ có thông báo lỗi hiện lên nếu có vấn đề xuất hiện trong quá trình encode chuỗi. 
# Một số giá trị ngoài strict là ignore, replace, xmlcharrefreplace. Vì phần này là phần nâng cao, Kteam xin phép không đi sâu.

# Phương thức decode (chỉ dùng đối với chuỗi đã được encode – tức là chuỗi đã mã hóa)
# Cú pháp : <chuỗi (đã mã hóa)>.decode(encoding=’utf-8’, errors=’strict’) : ùng để giải mã các kí tự đã được mã hóa bởi phương thức encode.

# Phương thức join 
# Cú pháp : <kí tự nối>.join(<iterable>) : Trả về một chuỗi bằng cách nối các phần tử trong iterable bằng kí tự nối. 
# Một iterable có thể là một tuple, list,… hoặc là một iterator 

# Phương thức replace
# Cú pháp : <chuỗi>.replace(old, new, [count]) : Trả về một chuỗi với các chuỗi old nằm trong chuỗi ban đầu được thay thế bằng chuỗi new. 
# Nếu count khác None (có nghĩa là ta cho thêm count) thì ta sẽ thay thế old bằng new với số lượng count từ trái qua phải.
# Nếu chuỗi old không nằm trong chuỗi ban đầu hoặc count là 0 thì sẽ trả về một chuỗi giống với chuỗi ban đầu

# Phương thức strip
# Cú pháp : <chuỗi>.strip([chars]) : Trả về một chuỗi với phần đầu và phần đuôi của chuỗi được bỏ đi các kí tự chars. 
# Nếu chars bị bỏ trống thì mặc định các kí tự bị bỏ đi là dấu khoảng trắng và các escape sequence. 
# Một số escape sequence ngoại lệ như \a sẽ được encode utf-8

# Phương thức rstrip 
# Cú pháp : <chuỗi>.rstrip() : Cách hoạt động hoàn toàn như phương thức strip, nhưng khác là chỉ bỏ đi ở phần đuôi (từ phải sang trái)

# Phương thức lstrip
# Cú pháp : <chuỗi>.lstrip() : Cách hoạt động tương tự phương thức rstrip, khác ở chỗ rstrip lo phần đuôi, còn lstrip lo phần đầu (từ trái sang phải)

# Phương thức removeprefix
# Cú pháp : <chuỗi>.removeprefix([prefix]) :  Trả về một chuỗi mới, chính là chuỗi ban đầu với phần đầu đã được bỏ đi [prefix].
# Nếu [prefix] không xuất hiện ở phần đầu của chuỗi, phương thức removeprefix trả về chính chuỗi đó.

# Phương thức removesuffix
# Cú pháp : <chuỗi>.removesuffix([suffix]) :  tương tự như removeprefix, nhưng nó sẽ xóa ở cuối chuỗi.
