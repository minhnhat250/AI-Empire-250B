import torch
import time
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Hệ thống đang sử dụng {device.upper()}")

if device == 'cuda':
    print(torch.cuda.get_device_name(0))


#Cách chuyển từ CP=>GPU và ngược lại

tensor_cpu = torch.randn(3,3)
tensor_cpu_gpu = tensor_cpu.to(device)
print("Vị trí sau khi dịch chuyển",tensor_cpu_gpu.device)

tensor_gpu = torch.randn(3,3,device=device)
tensor_gpu_cpu = tensor_gpu.cpu()
print("vị trí GPU sau dịch chuyển",tensor_gpu_cpu.device)

#NOTE QUAN TRỌNG: Hai Tensor, matrix chỉ thực hiện lhi cùng ở trên 1 bộ nhớ RAM or VRAM

a_cpu = torch.tensor([1,2])
b_gpu = torch.tensor([2,3]).to(device)

try:
    c = a_cpu+b_gpu
except Exception as e:
    print("lỗi địa điểm trên bộ nhớ")
    print(e)


d = a_cpu.to(device)

str1 = time.time()
c_gpu = d +b_gpu
end1 = time.time() - str1
print("Kết quả gpu",end1)

f = b_gpu.cpu()
str2 = time.time()
d_cpu = f +a_cpu
end2 = time.time()-str2
print("kết quả cpu",end2)