import torch
import time

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def chien_dic_gpu(tensor_device):
    kich_thuoc =13000
    A = torch.randn(kich_thuoc, kich_thuoc, device=tensor_device)
    B = torch.randn(kich_thuoc, kich_thuoc, device=tensor_device)

    if tensor_device.type == 'cuda':
        torch.cuda.synchronize()

    start = time.time()

    C = A @ B

    if tensor_device.type == 'cuda':
        torch.cuda.synchronize()

    return time.time() - start

print("Đang cho GPU chạy nháp 1 vòng để tải vũ khí GPU ")
_ = chien_dic_gpu(device)

print("Đang đo sức CPU")
time_cpu = chien_dic_gpu(torch.device("cpu"))

print("Đang đo sức GPU")
time_gpu = chien_dic_gpu(device)

print(f"Thời gian CPU chạy: {time_cpu:.5f} giây")
print(f"Thời gian GPU chạy: {time_gpu:.5f} giây")
print(f"GPU  nhanh gấp {time_cpu/time_gpu:.2f} lần so với CPU!")