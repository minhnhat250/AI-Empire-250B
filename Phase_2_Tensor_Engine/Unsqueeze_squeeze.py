import torch

"""
Các mô hình AI luôn yêu cầu dữ liệu đầu vào phải có chiều Batch (Lô). 
Tức là dù chỉ đưa 1 bức ảnh vào, nó vẫn đòi kích thước phải là [Batch, Channel, Height, Width].
Nếu ảnh tải về từ mạng chỉ là [Channel, Height, Width], sẽ bị báo lỗi.
"""
single = torch.randn(3,28,28)
print("Ảnh gốc",single.shape)

# Bơm thêm chiều lô (Batch) vào vị trí số 0
# unsqueeze(0) nghĩa là chèn thêm số 1 vào đầu.

batched_images = single.unsqueeze(0)
print("Kích thước ảnh sau thay đổi",batched_images.shape)

#Ngược lại squeeze sẽ xoá hết toàn bộ chiêu ó kích thước 1

unbatched_images = batched_images.squeeze()
print("Sau khi Squeeze",unbatched_images.shape)


