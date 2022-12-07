''' Vòng lặp For '''
# Cấu trúc vòng lặp for và cách hoạt động
'''
for variable_1, variable_2, .. variable_n in sequence:

    # for-block
Bước 1: Vòng for sẽ bắt đầu bằng cách lấy giá trị đầu tiên của sequence.
Bước 2: Giá trị đầu tiên này có 3 giá trị. Bạn đưa vào 3 biến. Kiểm tra hợp lệ.
Bước 3: unpacking 3 giá trị này và lần lượt gán giá trị này cho ba biến e1, e2, e3.
Bước 4: Thực hiện nội dung for-block (trong ví dụ: là việc in ra cả 3 biến).
Bước 5: Lấy giá trị tiếp theo của sequence sau đó làm tương tự như Bước 2, 3, 4.
Bước 6: Lúc này, sequence đã hết giá trị. Kết thúc vòng lặp. Kết quả ở đầu ra sẽ là 2 dòng cuối ở ví dụ trên.
'''
# Lưu ý: Nếu sequence là một iterator object thì việc dùng vòng lặp duyệt qua cũng sẽ tương tự như bạn sử dụng hàm next.


# Sử dụng vòng lặp để xử lí các iterator và Dict

# Câu lệnh break, continue
s = 'Zaonekk'
for ch in s:
    if ch == ' ':
        break
    else:
        print(ch)


s = 'H o w K t e a m'
for ch in s:
    if ch == ' ':
        continue
    else:
        print(ch)


# Cấu trúc vòng lặp for-else và cách hoạt động
'''
for variable_1, variable_2, .. variable_n in sequence:

    # for-block

else:

    # else-block

Cũng sẽ tương tự như while-else, vòng lặp hoạt động bình thường. Khi vòng lặp kết thúc, khối else-block sẽ được thực hiện. 
Và đương nhiên nếu trong quá trình thực hiện for-block mà xuất hiện câu lệnh break thì vòng lặp sẽ kết thúc mà bỏ qua else-block.
'''

# Kiểu dữ liệu range (dãy số)
'''
Cách khởi tạo thứ nhất
Cú pháp:  
range(stop)
'''

'''
Cách khởi tạo thứ hai
Cú pháp:
range(start, stop[, step])
'''
'''
Sử dụng range để duyệt một List, Tuple, Chuỗi
'''


# Sự khác nhau giữa sequence scan và indexing scan
# Comprehension

# hàm enumerate
'''
Cú pháp:
enumerate(iterable[, start])
'''