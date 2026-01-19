from functools import wraps
# pseudo code 
def decorator_demo(func: callable):
    wraps(func)
    def wrapper(*args, **kwargs):
        print('Bắt đầu ghi lại log')
        # trong wrapper không cần sử dụng dấu * để ghi lại biến
        print(args)
        print(kwargs)
        func(*args,**kwargs)
        print('Kết thúc ghi log')
    return wrapper

@decorator_demo
def say_hi(name,age, gender):
    print(f"{name} Xin chào mọi người. Tuổi: {age}. Giới tính: {gender}")

# say_hi('Tuấn', 20, gender='nam')


# Public | Low | Med | Strict

def decorator_factory(role): # factory pattern
    def decorator_demo(func: callable):
        wraps(func)
        def wrapper(*args, **kwargs):
            if role == 'something':
                func(*args,**kwargs)
            else:
                print('Sai key')
        return wrapper
    return decorator_demo

@decorator_factory('Low')
def say_hello(name,age, gender, authUser):
    print(f"{name} Xin chào mọi người. Tuổi: {age}. Giới tính: {gender}")

say_hello('Tuấn', 20, gender='nam')