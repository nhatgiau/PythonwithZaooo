''' Giới thiệu package trong Python '''
#Package là một folder chứa các module, package con (sub package) và bên cạnh đó là file __init__.py.

# Package import cơ bản
'''
Đầu tiên, ta sẽ chạy file main.py với nội dung sau đây và xem cách mà chúng ta import một module nằm ở trong môt folder.

Đầu tiên, ta sẽ chạy file main.py với nội dung sau đây và xem cách mà chúng ta import một module nằm ở trong môt folder.
'''

# File __init__.py (initialization)
'''
Mỗi package đều phải chứa file này. Nhìn chung, file này sẽ được tự động chạy khi bạn package được import.

Một điều thú vị nữa là, các biến khởi tạo trong file __init__.py cũng được khởi tạo đồng thời.

Nhìn rộng ra, file __init__.py này nhằm mục đích khởi tạo những thứ cần thiết cho package trong trường hợp bạn import package này.

Nếu như lúc nãy khi ta chỉ import mỗi package, ta sẽ không sử dụng được các module. Tuy nhiên bằng một vài xử lí ở file __init__.py, 
ta có thể sử dụng được các module khi import package.
Bạn để ý ở file __init__.py, tuy nằm cùng với các folder với module_a, module_b, nhưng khi import lại sử dụng package import. 
Nếu bạn thử chạy file __init__.py chắc chắn sẽ có lỗi xảy ra. Tại sao lại xảy ra điều này thì mình sẽ để lại cho các bạn tự nghiền ngẫm vì nó không quá khó.
'''

# Biến __all__
'''
Với module, khi bạn import tất cả có nghĩa là tất cả các biến, hàm, lớp,… nói chung là toàn bộ nội dung của module đó 
(một số trường hợp ngoại lệ, tuy nhiên ta sẽ không đề cập ở đây vì nó rất hiếm gặp). 
Còn với package ta có thể quy định “tất cả” ở đây là gồm những gì. 
Mặc định khi bạn không quy ước thì “tất cả” thì “tất cả” bằng không có gì.
Việc quy ước tất cả này liên quan tới biến __all__, và dĩ nhiên, để dễ dàng thì nó thường sẽ nằm trong file __init__.py.
'''