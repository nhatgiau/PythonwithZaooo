# Định dạng bằng toán tử %
# Cú pháp : <chuỗi> % (giá trị thứ 1, giá trị thứ 2, .., giá trị thứ n – 1, giá trị thứ n)
# Lưu ý : Không hề có dấu tách phần chuỗi và phần giá trị cần định dạng

# %s : giá trị phương thức __str__ của đối tượng đó

# %r : giá trị phương thức __repr__ của đối tượng đó

# %d : giá trị của 1 số. Nếu là số thực thì chỉ lấy phần nguyên ( chuyển sang số nguyên )

# %<số chữ số phần thập phân>f : Giá trị của một số. Nếu là số sẽ được chuyển sang số thực.


# Định dạng bằng chuỗi f (f-string)
# Cú pháp : f ’giá trị trong chuỗi’

# Định dạng bằng phương thức format
# Căn lề trái : {:(c)<n}
# Căn lề phải : {:(c)>n}
# Căn giữa : {:(c)^n}
# c là kí tự bạn muốn thay thế vào chỗ trống, nếu để trống thì sẽ là kí tự khoảng trắng, n là số kí tự dùng để căn lề.
# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Kteam', 'TP HCM')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Kquiz', 'Da Lat')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)