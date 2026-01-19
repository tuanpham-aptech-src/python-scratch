import time

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
	if errors == 5:
			break

print("Errors:", errors)
print("Time:", time.time() - start)