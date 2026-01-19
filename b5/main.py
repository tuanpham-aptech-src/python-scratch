import random

with open("demo.log", "w") as f:
	for i in range(3_000_000):
		if random.random() < 0.001:
			f.write(f"{i} ERROR something bad happened \n")
		else:
			f.write(f"{i} INFO normal request\n")
