import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
x = torch.tensor(2.0,device=device,requires_grad=True)

a = x**2
b = 3*x
y=a+b

print(f'Hàm tạo ra y = {y.grad_fn}')
print(f"Hàm tạo ra a: {a.grad_fn}")
print(f"hàm tạo ra b: {b.grad_fn}")

y.backward()

print(f"Đạo hàm dy/dx tại x =2 là: {x.grad}")

#tensor tạo ra từ danh sách có sẵn
quan_doan_a = torch.tensor([[1,2],[3,4]])
quan_doan_d = torch.tensor([[3,4],[5,6]])

#tensor ta ra số 1
quan_doan_b = torch.ones(3,3)
print("Tensor 1",quan_doan_b)

#tensor tạo số 0
quan_doan_c = torch.zeros(2,2)
print("Tensor số 0",quan_doan_c)

#tensor phân phối chuẩn
phan_phoi_chuan = torch.randn(3,3)
print("Tensor phân phối chuẩn",phan_phoi_chuan)

#Tạo dãy số từ 1 đên 9 vơ bước nhảy là 2
range_tensor = torch.arange(1,10,step=2)
print("tensor bước nhảy",range_tensor)

#Tensor 5 số cách đều
linspace_tensor = torch.linspace(1,3,steps=1)
print("Tensor số cách đều",linspace_tensor)

#Tensor sa chép ma trận
ones_like_x = torch.ones_like(x)
print("Tensor sao chép ma trận",ones_like_x)






