''' Vòng lặp While trong Python '''
'''
Cú pháp : while expression:

     # while-block
'''
# Lưu ý: Việc chia block như thế này cũng giống như khi bạn sử dụng câu lệnh if
'''
Cách thức hoạt động
Python sẽ kiểm tra giá trị boolean của expression. Nếu là False, thì bỏ qua while-block và đến với câu lệnh tiếp theo. 
Ngược lại, sẽ thực hiện toàn bộ câu lệnh trong while-block. 
Sau khi thực hiện xong, quay ngược lại kiểm tra giá trị boolean của expression một lần nữa. 
Nếu False thì bỏ qua while-block, còn True thì tiếp tục thực hiện while-block. 
Và sau khi thực hiện xong while-block lại quay về kiểm tra giá trị boolean expression như những lần trước.
'''

# Sử dụng vòng lặp để xử lí chuỗi, list, tuple
# Đây là những iterable cho phép ta truy xuất một giá trị bất kí trong nó bằng phương pháp indexing. 
# Thế nên, ta có thể nhờ điều này kết hợp với vòng lặp để xử lí chúng.

# Câu lệnh break và continue
'''
Câu lệnh break
Câu lệnh break dùng để kết thúc vòng lặp. Cứ nó nằm trong block của vòng lặp nào thì vòng lặp đó sẽ kết thúc khi chạy câu lệnh này.
Trong trường hợp vòng lặp a chứa vòng lặp b. Trong vòng lặp b chạy câu lệnh break thì chỉ vòng lặp b kết thúc, còn vòng lặp a thì không.
'''
five_even_numbers = []
k_number = 1

while True: # vòng lặp vô hạn vì giá trị này là hằng nên ta không thể tác động được
    if k_number % 2 == 0: # nếu k_number là một số chẵn
       five_even_numbers.append(k_number) # thêm giá trị của k_number vào list
    if len(five_even_numbers) == 5: # nếu list này đủ 5 phần tử
        break # thì kết thúc vòng lặp
    k_number += 1
print(five_even_numbers)
print(k_number)

# Câu lệnh continue
'''
while expression:

    #while-block-1

    continue

    #while-block-2
Khi thực hiện xong while-block-1, câu lệnh continue sẽ tiếp tục vòng lặp, 
không quan tâm những câu lệnh ở dưới continue và như vậy nó đã bỏ qua while-block-2.
'''
k_number = 1
while k_number < 10:
    if k_number % 2 == 0: # nếu k_number là số chẵn
        k_number += 1  # thì tăng một đơn vị cho k_number và tiếp tục vòng lặp
        continue
    print(k_number, 'is odd number')
    k_number += 1


# Câu lệnh pass
# Về cơ bản, pass có thể được hiểu như là “không có gì”. Nó dường như chỉ được để cho có.
'''
while expression:

 pass
Khi thực hiện các lệnh trong vòng lặp (và cả hàm) , nó sẽ xem lệnh pass này như là “vô hình”. 
Nhưng nó sẽ giúp tránh lỗi nếu như vòng lặp (hàm) của bạn không có bất kì một lệnh nào.
'''

# Cấu trúc vòng lặp while-else và cách hoạt động
'''
while expression:

    # while-block

else:

    # else-block
Cấu trúc này gần tương tự như while bình thường. 
Thêm một điều, khi vòng vòng lặp while kết thúc thì khối lệnh else-block sẽ được thực hiện.
'''
k = 8
while k < 3:
    print('value of k is', k)
    k += 1
else:
    print('k is not less than 3 anymore')


# Hiện tượng vòng lặp vô tận
# Cần lưu ý là, đối với vòng lặp while, trong nhiều trường hợp, bạn có thể sẽ không biết trước số lần lặp, 
# và có thể sẽ có nhiều lỗi không mong muốn. Điển hình nhất là vòng lặp vô tận: