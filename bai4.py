# TOÁN TỬ VỚI CHUỖI
# TOÁN TỬ +
# Cú pháp : A +B (với A và B là chuỗi)
s = 'giau'
s += 'xinh'
print(s)

# TOÁN TỬ *
# Cú pháp : A * N ( Với A là một chuỗi, N là một số nguyên)
a = 'a' *3
print(a)

# TOÁN TỬ IN
# Cú pháp : s in A (Với s và A là chuỗi)
d = 'a' in 'abc'
print(d)

# CÁC TOÁN TỬ SO SÁNH TRONG CHUỖI
# Cú pháp : A <toán tử so sánh> B (A và B là 2 chuỗi)
l = 'a' < 'b'
print(l)

# Để xem vị trí của một kí tự trong bảng mã Unicode, ta sử dụng hàm ord()
# Cú pháp : ord(<kí tự>)

# INDEXING
# Cú pháp : <chuỗi>[vị trí]
s = 'abc xyz'
m = s[0]
print(m)

# CẮT CHUỖI 
# Cú pháp : <chuỗi>[vị trí bắt đầu : vị trí dừng]
s = 'abc xyz'
x = s[1:5]
print(x)

# đặt None ở vị trí bắt đầu thì ta sẽ cắt chuỗi từ vị trí đầu tiên.
s = 'abc xyz'
q = s[None: 4]              # lấy các kí tự có vị trí từ 0 đến 3
print(q)

p = s[:-1]                  # ta cũng có thể để trống, Python sẽ tự hiểu là None
print(p)

g = s[:]                    # một cách sao chép chuỗi
print(g)

# CẮT TỪ PHẢI QUA TRÁI
# Cú pháp : <chuỗi>[vị trí bắt đầu : vị trí dừng : bước]
s = 'abc xyz'
o = s[2: 5: 1]              # ta có bước bằng 1
print(o)

# ÉP KIỂU DỮ LIỆU
# Cú pháp hàm int : int(<giá trị>)
a = '69'
int(a)
#  Lưu ý: Bạn sẽ không thể chuyển đổi một số thực dưới dạng chuỗi bằng hàm int

# Cú pháp hàm float : float(<giá trị>)
k = '3.1'
float(k)

# Cú pháp hàm string : str(<giá trị>)
h = 5698
str(h)
