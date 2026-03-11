import torch


#BẺ CONG KHÔNG GIAN VỚI "VIEW" VÀ "RESHAPE"
tensor_a = torch.arange(1,10)
print("Shape ban đầu",tensor_a.shape)

tensor_b = tensor_a.view(3,-1)
print("Ma trận sau khi dùng View",tensor_b)

#có thể dùng reshape (Khuyên dùng:an toàn và tự quản lí bộ nhớ)
c = tensor_a.reshape(3,-1)

"""
TẠI SAO LẠI CÙNG DÙNG VIEW VÀ RESHAPE
+View bản chất sẽ ko tạo ra dữ liệu mới, nó chỉ thay đôi cách nhìn thành ma trận
=> Dữ liệu phải liên tục, nếu ko sẽ báo lỗi
+Reshape bản chất nó sẽ cố gắng dùng view trước, nhưng nếu dùng không được nó sẽ
COPY toàn bộ dữ liệu sang một vùng RAM liên tục rồi mới bẻ cong NOTE: Tốn bộ nhớ
"""

#Test sự khác nhau của view và reshape
a = torch.arange(1,10).view(3,3)
#Dùng lệnh transpose(0,1) để đảo ngược hàng thành cột => để cho dữ liệu ko liên tục
b = a.transpose(0,1) #dim=0 là hàng dim=1 là cột, 3 trục: dim=0 (Kênh màu), dim=1 (Cao), dim=2 (Rộng).

try:
    c = b.view(9) #đổi thành ma trận 1D
    print(c)
except Exception as e:
    print("Lỗi kích thước")
    print(e)
#Note: nếu ko biết nó là lỗi gì thì cứ dùng Exception, bao mọi loại

#AUTO-INFER DIMENSION

images = torch.rand(32,3,224,224)
# Khi đưa ảnh vào mạng Neural (Fully Connected Layer), phải DUỖI PHẲNG (Flatten) mỗi bức ảnh ra.
# Muốn giữ nguyên số lượng ảnh là 32 (chiều số 0), còn lại duỗi thẳng hết.
# Thay vì lấy 3 * 224 * 224 = 150528, chỉ cần dùng -1:

fattened_images = images.view(32,-1)
print("Kích thước sau khi bẻ cong",fattened_images.shape)
