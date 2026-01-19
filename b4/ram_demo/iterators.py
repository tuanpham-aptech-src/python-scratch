import time
import psutil
import os

def ram_mb():
	return psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024

ram_b4 = ram_mb()
print("RAM before:", ram_b4, "MB")
start = time.time()

# Đếm số lượng lỗi - Làm bằng chứng cho việc đọc hết toàn bộ file
errors = 0
# Đọc file - 
# Về mặt RAM: Ở đây sẽ cực kì tiết kiệm RAM do load từng dòng dữ liệu vào RAM và xử lý ngay lập tức -> giải phóng và lặp lại.
# Về mặt thời gian: sẽ là thời gian đọc 1 file hoàn chỉnh.
with open("demo.log") as f:
	for line in f:          # iterator
	    if "ERROR" in line:
	            errors += 1

ram_after = ram_mb()
print("Errors:", errors)
print("Time:", time.time() - start)
print("RAM after:", ram_after, "MB")
print("RAM gap:", ram_after - ram_after, "MB")