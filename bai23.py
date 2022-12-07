''' Giới thiệu module trong Python '''

'''
Module chỉ đơn giản là những file Python thôi và dĩ nhiên việc tạo file Python không còn gì xa lạ và khó khăn với chúng ta nữa. 
Bạn không cần phải có một dòng code đặc biệt trong một file Python để biến nó thành một module, chỉ đơn giản là một file Python 
bình thường như mọi khi bạn vẫn tạo, thậm chí file Python đó chẳng ghi bất cứ chữ nào thì vẫn là một module.

Tuy nhiên, việc đặt tên cho module có một chút ràng buộc. Bản thân khi muốn sử dụng module thì ta sẽ lưu module đó vào một biến, 
biến đó thuộc lớp Module. Mà đã là biến, thì phải tuân theo những quy tắc đặt tên biến, và chỉ vậy thôi!
Lưu ý: Các module được tạo cùng một thư mục.
'''

# Câu lệnh import
'''
# a.py

print("imported")

def say(something):
    print(something)

ta có thể import nhiều module cùng một lúc trên cùng một dòng lệnh.
import module_a, module_b, module_c
'''

# Câu lệnh from import

# Import một module nhiều lần
'''
Sử dụng import hay from import để import một module thì chỉ hoạt động một lần. Nhìn chung, việc import được coi là expensive operation. 
Vậy nên Python chỉ thực hiện mỗi file một lần, khi thấy file đã được import thì khi đó bạn có gõ lại import không khác gì lắm 
việc bạn gõ một dòng comment. 
'''

# Lưu ý về list object khi import
'''
 mặc dù sử dụng from import tạo copy sau đó sử dụng thêm import để reset lại giá trị các biến, 
 tuy nhiên với các object như list thì việc này không được. 
 Vì nhìn chung, khi gán các giá trị như list là ta gán địa chỉ.
'''

# Reload module
'''
Python chỉ cho phép ta import một module một lần, không tự động reload, không có nghĩa là chúng ta 
không thể reload lại module. Ta có thể sử dụng hàm reload trong thư viện của Python.
'''

# Đổi tên module, attribute khi import
'''
Đôi khi, tên của module hay attribute của chúng ta rất dài. Chúng ta có thể thay đổi lại tên của module hoặc attribute đó, 
tuy nhiên đôi lúc những thư viện chuẩn chúng ta cần import thì việc thay đổi những điều đó xem như là một việc làm khá nguy hiểm 
nếu bạn không nắm rõ bạn đang làm cái gì. Có một cách đơn giản hơn đó là sử dụng as
'''

'''
Lưu ý: Bạn để ý một điều là, mặc dù ta đã đổi tên module ban đầu thành module rồi, tuy nhiên câu lệnh import tiếp theo 
vẫn phải sử dụng tên gốc vì khi đổi tên lại thì tên đó chỉ có giá trị trong file chạy, còn khi Python tìm module thì tìm ngoài thư mục, 
không liên quan gì nhau.
'''

# Trường hợp bắt buộc dùng import
'''
Những trường hợp này, sử dụng import là cách duy nhất tránh tình trạng này, vì khi dùng import thì ta sẽ tạo được hai module object. 
Dĩ nhiên là các object có thể có cùng attribute, nhưng ta vẫn có thể sử dụng được chúng một cách độc lập.
'''

# Folder __pycache__
