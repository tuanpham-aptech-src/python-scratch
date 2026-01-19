import time
import psutil
import os

def ram_mb():
	return psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024

ram_b4 = ram_mb()
print("RAM before:", ram_b4, "MB")
start = time.time()

# Đọc file - 
# Về mặt RAM: Ở đây sẽ cực kì tốn RAM do load toàn bộ dữ liệu của file vào RAM.
# Về mặt thời gian: sẽ là thời gian đọc 1 file hoàn chỉnh.
with open("demo.log") as f:
	lines = f.readlines()

# Đếm số lượng lỗi - Làm bằng chứng cho việc đọc hết toàn bộ file
errors = 0
for line in lines:
	if "ERROR" in line:
	    errors += 1
ram_after = ram_mb()
print("Errors:", errors)
print("Time:", time.time() - start)
print("RAM after:", ram_after, "MB")
print("RAM gap:", ram_after - ram_b4, "MB")