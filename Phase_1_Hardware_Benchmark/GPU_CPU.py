import torch
import time

device = torch.device ('cuda' if torch.cuda.is_available() else 'cpu')
steps = 1000

def test_GPU (tensor_device):
    x = torch.tensor([1.0],device = tensor_device)
    start_time = time.time()

    for i in range (steps):
        if x.item() % 2 == 0:
            x = x * 1.01
        else:
            x= x + 0.5

    if tensor_device.type == 'cuda':
        torch.cuda.synchronize()

    return time.time() - start_time

time_cpu = test_GPU(torch.device('cpu'))
print(f'CPU chạy mất {time_cpu} giây')

if torch.cuda.is_available():
    time_gpu = test_GPU(device)
    print(f'GPU chạy mất {time_gpu} giây')