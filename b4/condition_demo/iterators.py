import time
start = time.time()

# Đếm số lượng lỗi - Làm bằng chứng cho việc đọc hết toàn bộ file
errors = 0
# Đọc file - 
# Về mặt RAM: Ở đây sẽ cực kì tiết kiệm RAM do load từng dòng dữ liệu vào RAM và xử lý ngay lập tức -> giải phóng và lặp lại.
# Về mặt thời gian: sẽ là thời gian đọc sớm nhất đạt đủ điều kiện (trong trường hợp xấu nhất = đọc hết 1 file).
with open("demo.log") as f:
	for line in f:		  # iterator
		if "ERROR" in line:
			errors += 1
		if errors == 5:
			break

print("Errors:", errors)
print("Time:", time.time() - start)
