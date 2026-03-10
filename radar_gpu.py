import tkinter as tk
from pynvml import *
import psutil
import platform
import time

# --- KHỞI TẠO CẢM BIẾN ---
nvmlInit()
handle = nvmlDeviceGetHandleByIndex(0)
gpu_name = nvmlDeviceGetName(handle)
if isinstance(gpu_name, bytes): gpu_name = gpu_name.decode('utf-8')

# Biến toàn cục để tính toán tốc độ Disk
last_io = psutil.disk_io_counters()
last_time = time.time()


def update_info():
    global last_io, last_time
    try:
        # 1. THÔNG SỐ GPU
        info = nvmlDeviceGetMemoryInfo(handle)
        temp = nvmlDeviceGetTemperature(handle, 0)
        util = nvmlDeviceGetUtilizationRates(handle)
        clock = nvmlDeviceGetClockInfo(handle, NVML_CLOCK_GRAPHICS)
        vram_used = info.used / 1024 ** 2

        try:
            pwr = f"{nvmlDeviceGetPowerUsage(handle) / 1000:.1f}W"
        except:
            pwr = "N/A"

        # 2. THÔNG SỐ CPU & RAM
        cpu_usage = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory()

        # 3. TÍNH TỐC ĐỘ DISK (MB/s)
        now = time.time()
        curr_io = psutil.disk_io_counters()
        dt = now - last_time

        read_speed = (curr_io.read_bytes - last_io.read_bytes) / (1024 * 1024) / dt
        write_speed = (curr_io.write_bytes - last_io.write_bytes) / (1024 * 1024) / dt

        # Cập nhật mốc thời gian/dữ liệu cho lần quét tới
        last_io = curr_io
        last_time = now

        # 4. CẬP NHẬT GIAO DIỆN
        lbl_gpu_name.config(text=f"👑 {gpu_name}")
        lbl_cpu_ram.config(text=f"💻 CPU:{cpu_usage:>4.1f}% | RAM:{ram.used / (1024 ** 3):.1f}GB")
        lbl_gpu_load.config(text=f"🎮 GPU:{util.gpu:>3}% | 🚀 {clock}MHz")
        lbl_vram.config(text=f"📟 VRAM:{vram_used:>5.1f} / 2048 MB")
        # Dòng Disk mới: Hiển thị cả Read và Write siêu nhạy
        lbl_disk.config(text=f"💾 R:{read_speed:>4.1f}MB/s | W:{write_speed:>4.1f}MB/s")
        lbl_temp.config(text=f"🌡️ TEMP:{temp}°C | ⚡ {pwr}")

        # Đổi màu cảnh báo
        lbl_temp.config(fg="#00FF00" if temp < 75 else "#FF3333")

    except:
        pass
    root.after(300, update_info)  # Quét siêu nhanh 0.3s


# --- GIAO DIỆN KIẾN TRÚC SƯ ---
root = tk.Tk()
root.attributes("-topmost", True)
root.overrideredirect(True)
root.geometry("270x175+20+20")
root.configure(bg="#050505")

font_h = ("Consolas", 11, "bold")
font_m = ("Consolas", 10, "bold")


def c_lbl(f, c="#00FF00"):
    l = tk.Label(root, text="", font=f, bg="#050505", fg=c, anchor="w")
    l.pack(fill="x", padx=15, pady=3)
    return l


lbl_gpu_name = c_lbl(font_h, "#FFD700")  # Gold
lbl_cpu_ram = c_lbl(font_m)
lbl_gpu_load = c_lbl(font_m, "#33CCFF")  # Sky Blue
lbl_vram = c_lbl(font_m)
lbl_disk = c_lbl(font_m, "#FFA500")  # Orange cho Disk
lbl_temp = c_lbl(font_m)


# Kéo thả cửa sổ
def start_move(event): root.x, root.y = event.x, event.y


def on_move(event):
    root.geometry(f"+{root.winfo_x() + (event.x - root.x)}+{root.winfo_y() + (event.y - root.y)}")


root.bind("<Button-1>", start_move)
root.bind("<B1-Motion>", on_move)

update_info()
root.mainloop()