''' XỬ LÍ FILE PYTHON '''
''' Mở File trong Python'''
# Hàm open
# Cú pháp:open(file, mode='r')
'''
r : mở để đọc. Mode mặc định.
r+ : mở để đọc và ghi
w : mở để ghi, trước đó nó sẽ xóa nội dung hiện có của file. Nếu không có file sẽ tạo ra 1 file với tên là tên file ta truyền vào
w+ : mở để ghi và đọc, trước đó nó sẽ xóa nội dung hiện có của file. Nếu không có file sẽ tạo ra 1 file với tên là tên file ta truyền vào
a : mở để ghi, Nếu không có file sẽ tạo ra 1 file với tên là tên file ta truyền vào
a+ : mở để ghi và đọc, Nếu không có file sẽ tạo ra 1 file với tên là tên file ta truyền vào
'''

''' Đóng File trong Python. Đây là việc chúng ta nên làm sau khi thao tác xong với file. Đó là đóng file.'''
# Cú pháp: <File>.close()

''' Đọc File trong Python '''
# Phương thức read
# Cú pháp: <File>.read(size=-1)
# Công dụng: Nếu size bị bỏ trống hoặc là một số âm. Nó sẽ đọc hết nội dung của file đồng thời đưa con trỏ file tới cuối file. 
# Nếu không nó sẽ đọc tới n kí tự (với n = size) hoặc cho tới khi nội dung của file đã đọc xong.
# Sau khi đọc được nội dung, nó sẽ trả về dưới một dạng chuỗi.
# Nếu không đọc được gì, phương thức sẽ trả về một chuỗi có độ dài bằng 0

# Phương thức readline
# Cú pháp: <File>.readline(size=-1)
# Công dụng: Với parameter size thì hoàn toàn tương tự như phương thức read.
# Khác biệt ở chỗ, phương thức readline chỉ đọc một dòng có nghĩa là đọc tới khi nào gặp newline hoặc hết file thì ngừng.
# Con trỏ file cũng sẽ đi từ dòng này qua dòng khác.
# Kết quả đọc được trả về dưới dạng một chuỗi.
# Nếu không đọc được gì, phương thức sẽ trả về một chuỗi có độ dài bằng

# Phương thức readlines
# Cú pháp: <File>.readlines(hint=-1)
# Ở mức độ cơ bản, ta không phải quan tâm đến parameter hint.
# Công dụng: Phương thức này sẽ đọc toàn bộ file, sau đó cho chúng vào một list. Với các phần tử trong list là mỗi dòng của file.
# Con trỏ file sẽ được đưa  tới cuối file. Khi đó, nếu bạn tiếp tục dùng readlines. Bạn sẽ nhận được một list rỗng.

''' Ghi File trong Python '''
# Phương thức write
# Cú pháp: <File>.write(text)
# Công dụng: Phương thức này sẽ trả về số kí tự mà chúng ta ghi vào.

''' Kiểm soát con trỏ '''
# Phương thức seek
# Cú pháp: <File>.seek(offset, whence=0)
# Công dụng: Phương thức này giúp ta di chuyển con trỏ từ vị trí đầu file qua offset kí tự. Và parameter offset phải là một số tự nhiên.
# Nhờ phương thức này, ta có thể ghi nội dung từ bất cứ đâu trong file. Và từ đó ta có thể đọc lại file sau khi ta đưa con trỏ file xuống cuối file.

''' Câu lệnh with '''
# Cấu trúc :
# with expression [as variable]:
# with-block 