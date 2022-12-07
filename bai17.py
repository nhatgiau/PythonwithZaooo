''' Cấu trúc rẽ nhánh '''

# IF
# Cú pháp : 
# if expression:
     # If-block
# Lưu ý: Tất cả các câu lệnh nằm trong if-block là các câu lệnh có lề thụt vào trong so với câu lệnh if.
# nếu expression là một giá trị khi đưa về kiểu dữ liệu Boolean là True thì Python sẽ nhảy vào thực hiện các câu lệnh trong if-block. 
# Còn nếu không thì không thì sẽ bỏ qua if-block đó.
# Ví dụ : 
a = 1
b = 3
if a - 1 < 0:
    print('a thật nhỏ bé')
if b + 5 > 10:
    print('thật bất ngờ')
    
# IF - ELSE IF
# Cú pháp
'''
if expression:

    # If-block

elif 2-expression:

    # 2-if-block

elif 3-expression:

    # 3-if-block

…

elif n-expression:

    # n-if-block
'''

'''
có thể đặt bao nhiêu lần nếu cũng được. Và từ câu lệnh if đến lần elif lần thứ n – 1 (câu lệnh với n-expression) là một khối, 
ta sẽ đặt cho nó một cái tên là khối BIG để dễ hiểu. 
Nó sẽ hoạt động như sau:
Bước 1: Kiểm tra xem expression có phải là một giá trị Boolean True hay không?
Bước 2: Nếu có, thực hiện if-block sau đó kết thúc khối BIG. Không thì chuyển sang Bước 3.
Bước 3: Kiểu tra xem 2-expression có phải là một giá trị Boolean True hay không?
Bước 4: Nếu có, thực hiện 2-if-block sau đó kết thúc khối BIG. Không thì chuyển sang Bước 5.
Bước 5: Kiểm tra xem 3-expression có phải là một giá trị Boolean True hay không?
Bước 6: Nếu có, thực hiện 3-if-block sau đó kết thúc khối BIG. Không thì chuyển sang Bước 7
…
Bước (n - 1) x 2: Kiểm tra xem n-expression có phải là một giá trị Boolean True hay không?
Bước (n – 1) x 2 + 1: Nếu có, thực hiện n-if-block.
Bước (n – 1) x 2 + 2: Kết thúc khối BIG.
'''
# Ví dụ : 
c = 2
if c - 1 < 0:
    print('c thật là nhỏ bé')
elif c - 2 < 0:
    print(' điều này thật đúng đắn')


# IF - ELSE
'''
if expression:

    # If-block

else:

    # else-block
'''
# Nếu expression là một giá trị Boolean True, thực hiện if-block và kết thúc. 
# Không quan tâm đến else-block. Còn nếu không sẽ thực hiện else-block và kết thúc.
d = 0
g = 3
if a - 1 < 0:
    print('a bé hơn 1')
else:
    print('a lớn hơn 1')
if g < d:
    print('g bé hơn d')
else:
    print('g lớn hơn d')



# SHORTHAND IF - ELSE 
'''
<Giá trị 1> if <Điều kiện> else <Giá trị 2> ;
'''
# Shorthand if-else là một cú pháp tuy ngắn gọn, nhưng lại không được khuyến khích sử dụng vì nó khá dễ nhầm. 
print('t bằng 5' if p == 5 else 't khác 5')
print('t bằng 3' if p == 3 else 't khác 3')


# IF-ELSE IF-ELSE
'''
if expression:

    # If-block

elif 2-expression:

    # 2-if-block

…

elif n-expression:

    # n-if-block

else:

    # else-block
'''
#  có thể đặt bao nhiêu lần elif cũng được nhưng else thì chỉ một. 
# Và từ câu lệnh if đến câu lệnh else là một khối, ta cũng sẽ đặt cho nó một cái tên là khối BIG để dễ hiểu. Nó sẽ hoạt động như sau:
'''
Bước 1: Kiểm tra xem expression có phải là một giá trị Boolean True hay không?
Bước 2: Nếu có, thực hiện if-block sau đó kết thúc khối BIG. Không thì chuyển sang Bước 3.
Bước 3: Kiểu tra xem 2-expression có phải là một giá trị Boolean True hay không?
Bước 4: Nếu có, thực hiện 2-if-block sau đó kết thúc khối BIG. Không thì chuyển sang Bước 5
Bước (n - 1) x 2: Kiểm tra xem n-expression có phải là một giá trị Boolean True hay không?
Bước (n – 1) x 2 + 1: Nếu có, thực hiện n-if-block sau đó kết thúc khối BIG.
Bước (n – 1) x 2 + 2: Nếu không thì thực hiện else-block và kết thúc khối BIG.
'''
h = 0
if h - 1 < 0:
    print('a nhỏ hơn 1')
elif h - 1 > 0:
    print('a lớn hơn 1')
else:
    print('a bằng 1')


# Cấu trúc điều kiện match-case
'''
Cú pháp:
match <subject>:

    case <pattern_1>:

        <action_1>

    case <pattern_2>:

        <action_2>

    case <pattern_3>:

        <action_3>

    case _:

        <action_wildcard>
'''
t = 1
match t:
     case 1: # case (1)
         print("t = 1")
     case 1: # case (2)
         print("t là 1")

# Block trong Python
'''
Một số điều lưu ý về việc định dạng code block trong Python:
Câu lệnh mở block kết thúc bằng dấu hai chấm (:), sau khi sử dụng câu lệnh có dấu hai chấm (:) buộc phải xuống dòng và lùi lề vào trong và có tối thiểu một câu lệnh để không bỏ trống block.
Những dòng code cùng lề thì là cùng một block.
Một block có thể có nhiều block khác.
Khi căn lề block không sử dụng cả tab lẫn space.
Nên sử dụng 4 space để căn lề một block
'''
