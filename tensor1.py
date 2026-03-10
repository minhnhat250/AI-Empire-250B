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

#tensor tạo số 0
quan_doan_c = torch.zeros(2,)
