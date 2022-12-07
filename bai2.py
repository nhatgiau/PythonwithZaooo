# kiểu số
# số nguyên (1,2,3,-1,-2,-3,0,...)
a = 4
print(a)
b = type(a)
print(b)

# số thực, thì đây là tập hợp các số nguyên và số thập phân 1, 1.4, -123, 69.96,…
f = 1.23
print(f)
c = type(f)
print(c)

#phân số Fraction(<Tử_số>, <Mẫu_số>)
from fractions import * 
Fraction(1, 4)
print(Fraction(1, 4))

#số phức <Phần thực> + <Phần ảo> j
#<Phần thực> <Phần ảo> là số thực
#j là đơn vị ảo trong toán học với  j2 = -1
#cú pháp complex(<Phần_thực>,<Phần_ảo>)
# cách gán giá trị cho 1 biến <tên_biến> = <Phần_thực> + <Phần_Ảo>j
# xuất ra từng phần của biêsn 
# <tên_biến>.real
# <tên_biến>.imag   
d = 3j + 1
print(d)

