import torch
import time

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def chien_dic_gpu(tensor_device):
    kich_thuoc =13000
    A = torch.randn(kich_thuoc, kich_thuoc, device=tensor_device)
    B = torch.randn(kich_thuoc, kich_thuoc, device=tensor_device)

    # Rào chắn 1: Xếp quân xong xuôi
    if tensor_device.type == 'cuda':
        torch.cuda.synchronize()

    start = time.time()

    # Tấn công tổng lực!
    C = A @ B

    # Rào chắn 2: Chém xong nhát cuối cùng
    if tensor_device.type == 'cuda':
        torch.cuda.synchronize()

    return time.time() - start

# ==========================================
# KHU VỰC ĐIỀU BINH: CHIẾN THUẬT HÂM NÓNG
# ==========================================
print("⏳ Đang cho GPU chạy nháp 1 vòng để tải vũ khí hạng nặng (cuBLAS)...")
_ = chien_dic_gpu(device) # Chạy vứt đi, không thèm đo thời gian!

print("🔥 ĐỘNG CƠ ĐÃ NÓNG! Bắt đầu trận chiến chính thức:")
print("-" * 40)

# 1. Cho CPU xuất trận
print("⏳ Đang đo sức CPU... (Chờ khoảng vài giây)")
time_cpu = chien_dic_gpu(torch.device("cpu"))

# 2. Cho GPU xuất trận (Lúc này nó đã thức tỉnh hoàn toàn)
print("⚡ Đang đo sức GPU... (Chớp mắt!)")
time_gpu = chien_dic_gpu(device)

# 3. Báo cáo tổng kết
print("-" * 40)
print(f"Thời gian CPU chạy: {time_cpu:.5f} giây")
print(f"Thời gian GPU chạy: {time_gpu:.5f} giây")
print(f"💥 KẾT QUẢ CHẤN ĐỘNG: GPU chém nhanh gấp {time_cpu/time_gpu:.2f} lần so với CPU! 💥")