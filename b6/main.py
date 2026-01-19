class Car:
	# properties
	# class properties
	so_banh_xe = 4
	
	# constructor
	def __init__(self, hang_xe: str, logo: str, engine: str):
		# object properties
		self.hang_xe = hang_xe
		# protect
		self._logo = logo
		# private
		self.__engine = engine
    
	# methods
	def khoi_dong(self):
		print(f"Xe {self.hang_xe} đã khởi động!")

	def thong_tin_xe(self):
		print(f"Hãng xe: {self.hang_xe}. \nSố bánh xe: {self.so_banh_xe}")

	
	def get_engine(self):
		print(self.__engine)

	@classmethod
	def thao_banh_xe(cls):
		cls.so_banh_xe -= 1
		print(f"Đã tháo thành công bánh xe!")

	@staticmethod
	def test():
		print("Hàm vớ vỉn")

class BMW(Car):

	def __init__(self, hang_xe: str, logo: str, engine: str, price: int):
		super().__init__(hang_xe, logo, engine)
		self.price = price

	def thong_tin_xe(self):
		# print(f"Hãng xe: {self.hang_xe}. \nSố bánh xe: {self.so_banh_xe}") # ❌ DRY
		super().thong_tin_xe() # next mor
		print(f"Giá bán: {self.price}")
		print("Xe của chúng tôi có bộ khung siêu đẹp")

class I8(Car,BMW):
	def __init__(self, hang_xe: str, logo: str, engine: str, price: int):
			super().__init__(hang_xe, logo, engine)
			self.price = price

# tạo ra instance từ class
bmw = BMW('BMW','Logo bmw', 'Engine bmw', 5_000_000)
some_car = Car('SomeCar','Logo SomeCar', 'Engine SomeCar')

bmw.thong_tin_xe()
