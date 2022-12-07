''' Kiểu dữ liệu Function trong Python - Sơ lược về hàm '''

# Khai báo hàm (create function)
'''
Cú pháp:

def <function_name>(parameter_1 [: <kiểu dữ liệu gợi ý của parameter_1>], parameter_2 [: <kiểu dữ liệu gợi ý của parameter_2>], .., parameter_n [: <kiểu dữ liệu gợi ý của parameter_n>]) [-> <kiểu dữ liệu trả về được gợi ý> ]

    function-block
'''

# Gọi hàm (call function)
'''
Cú pháp:
<function>()

hoặc 

<tên biến> = <function> 
'''

# Parameter và Argument
'''
Hiểu một cách đơn giản, parameter chính là tham số của hàm – là tên các biến sẽ được sử dụng trong hàm. 
Còn argument là đối số, tức là giá trị mà ta truyền cho parameter.
'''

# Giá trị mặc định của parameter (Default argument)
'''
Khi bạn đưa default argument cho các parameter, phải để các parameter có default argument ở sau cùng.
Default argument là một unhashable container
Như các bạn đã biết, unhashable container phổ biến mà ta đã từng biết như LIST, DICT, SET. 
Ở đây có một cảnh báo cho bạn việc bạn sử dụng default argument cho parameter là một unhashable container đó là giá trị 
của nó không được  làm mới (refresh) sau mỗi lần gọi hàm mà không pass argument mới cho parameter đó. 
Đương nhiên là nếu bạn có pass cho nó một argument mới thì container đó vẫn không hề mất giá trị nếu lần sau bạn gọi nó.
'''

# Sử dụng hàm kết hợp với phương thức sort
'''
Cú pháp 
<List>.sort(key=None, reverse=False)
'''

# Positional argument và keyword argument
'''
không được phép để positional theo sau (follow) keyword.

Có nghĩa là bạn có thể pass argument vừa positional và keyword cùng một lúc được, 
nhưng những positional buộc phải đứng trước keyword.
'''

''' Bắt buộc (force) Positional argument và keyword argument '''
# Keyword argument
# một số hàm bắt chúng ta buộc phải pass argument một cách rõ ràng rành mạch như hàm sorted
'''
Cú pháp
def function (*, key_arg1, key_arg2):
# function-block

Lưu ý: ta có thể thay thế dấu * bằng *identifier. Tuy nhiên phổ biến vẫn là *.
'''
# Positional argument - Bản cũ mới hỗ trợ

''' Packing và unpacking arguments '''
#  Định nghĩa  : Một cách hiểu đơn giản, Packing chính là việc đóng gói toàn bộ dữ liệu vào một vùng chứa duy nhất. 
#                Còn unpacking thì ngược lại, nó sẽ lần lượt bê ra các giá trị từ một vùng chứa nào đó.

# Unpacking arguments với *
'''
Khi bạn sử dụng *, bạn không chỉ có thể unpack được các List mà bên cạnh đó bạn có thể unpack các container 
khác như Tuple, Chuỗi, Generator, Set, Dict (chỉ lấy được key).
Lưu ý:
Pass argument bằng cách unpacking argument như thế này là đang truyền vào dưới dạng positional argument. 
Hãy cẩn thận sử dụng kĩ thuật này với những hàm có parameter dạng keyword-only argument.
'''

# Packing arguments với *
'''
Khi bạn sử dụng packing argument. Đồng nghĩa với việc bạn nhờ  một biến đi gói tất cả các giá trị truyền vào 
cho hàm bằng positional argument thành một Tuple. Nếu không có gì để gói (bạn không truyền vào bất cứ argument nào) thì bạn 
sẽ nhận được một tuple rỗng. Để giao nhiệm vụ cho một biến làm công việc này, bạn đặt một dấu * trước nó.

Lưu ý:
Bạn không nên nhầm lẫn việc này với việc force keyword-only argument
Không được phép để 2 parameter cùng làm nhiệm vụ packing argument trong một hàm
'''
# Unpacking arguments với **
#  đây chính là dạng keyword argument. Vậy nên bạn phải chắc chắn rằng parameter với key là giống nhau.

# Packing arguments với **
# Khác với dấu * là gói những positional argument thì ** lại gói các keyword argument. Và đương nhiên, 
# nó sẽ gói trong một Dict. Nếu không truyền gì vào sẽ là một dict rỗng.
# Lưu ý: bạn không được phép bỏ các positional parameter sau biến packing mà có ** giống như với *.

''' Biến locals và globals '''
# Lưu ý: Biến là đối tượng nên bị ràng buộc bởi điều này. Do đó các HÀM (FUNCTION), LỚP (CLASS) cũng chịu sự ràng buộc này tương tự. 
# Khai báo ở hàm nào thì chỉ dùng ở hàm đó.

''' Thay đổi giá trị argument gián tiếp qua parameter '''

# Sử dụng lệnh global
'''
Cú pháp:
global <variable>

Lưu ý:
BẠN KHÔNG NÊN SỬ DỤNG GLOBAL trừ khi hết cách. Nó giống như hàm eval vậy. Việc sử dụng biến global làm cho chương trình rối, 
khó kiểm soát cho nên hạn hãy chế tối đa việc sử dụng.
'''

# Giới thiệu hàm locals và globals  
'''
Hàm locals cho ta biết được những biến local (những biến được khai báo trong hàm) nằm trong chương trình của chúng ta. 
Còn globals là hàm giúp chúng ta biết được những  biến global trong chương trình.
Kết quả trả ra của hai hàm này là một Dict. Với key là tên biến và value là giá trị của biến.
Lưu ý: Với hàm globals() thì với biến globals có giá trị mới được trả về.
'''

# Giới thiệu lệnh return
'''
Đây là lệnh chỉ sử dụng được ở trong hàm (nếu sử dụng ở ngoài hàm sẽ có nhắc lỗi)

SyntaxError: 'return' outside function
1
Lệnh return có cú pháp như sau

return [object]
'''

# Dùng return để trả về nhiều giá trị một lúc
# Với Python, việc bạn có thể return nhiều giá trị một lúc bản chất nó không nằm ở câu lệnh Python, 
# mà là do Python thiết kế đặc biệt để có thể unpack các object trả về