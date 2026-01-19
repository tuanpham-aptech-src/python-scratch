from time import sleep
from functools import wraps
# Bài 1: Decorator @slow_down(s) Viết một Decorator nhận vào tham số s (giây). 
# Mỗi khi hàm được gọi, nó phải "ngủ" (time.sleep) đúng s giây trước khi thực thi. 
# Ứng dụng để tránh việc spam API hoặc cào dữ liệu (Rate Limiting).

# factory -> wrapper -> callable
# Tạo decor factory 
def slow_down(sleep_time):
    def decorator_function(func: callable):
        wraps(func)
        def wrapper(*args, **kwargs):
            sleep(sleep_time)
            func(*args, **kwargs)
        return wrapper
    return decorator_function

@slow_down(3)
def test():
    print('Đây là hàm test.')

# Bài 2: Decorator @withHTMLtag(name) Viết một Decorator nhận vào tên một thẻ HTML (ví dụ: "b", "i", "u"). 
# Nó sẽ bọc kết quả trả về của hàm trong thẻ đó.
# Ví dụ: input: "Hello" với thẻ "b" sẽ trả về "<b>Hello</b>". Ứng dụng để tạo nội dung HTML động.

def withHTMLtag(tag_name):
    def decorator_fnc(func: callable):
        wraps(func)
        def wrapper(*args, **kwargs):
            content = func(*args, **kwargs)
            return f"<{tag_name}>{content}</{tag_name}>"
        return wrapper
    return decorator_fnc

@withHTMLtag('b')
def test2(content: str):
    return content
formatedContent = test2('Hello')

print(formatedContent)

# Bài 3: Decorator @check_security(level) 
# Viết một Decorator nhận vào mức độ bảo mật (level) 
# với 3 cấp độ 
# - LOW (cho qua hết), 
# - MEDIUM (phải đăng nhập), 
# - HIGH (phải là admin), 
# kiểm tra vai trò người dùng (role) trước khi cho phép thực thi hàm. 
# Nếu vai trò không đủ, in ra thông báo từ chối. 
# Ứng dụng để bảo vệ các chức năng nhạy cảm.

LEVEL_CONFIG = {
   'LOW':{
       'loggin_required':False,
       'roles_required': []
   },
   'MEDIUM_LOW':{
       'loggin_required':True,
       'roles_required': []
   },
   'MEDIUM':{
       'loggin_required':True,
       'roles_required': []
   },
   'HIGH':{
       'loggin_required':True,
       'roles_required': ['admin']
   },
    'TROLL':{
       'loggin_required':False,
       'roles_required': ['super_admin']
   }
}

# - SEMI (phải là employee), 
# - HIGH (phải là admin), 

def check_security(level): # factory
    def decor(func: callable): # decorator
        wraps(func)
        def wrapper(*agr, **kagr): # wrapper
           matchLvl = LEVEL_CONFIG.get(level)
           if not matchLvl:
               return f"❌ Không tìm thấy Level tương ứng: {level}"
           # có 2 điều kiện cần kiểm tra là: logged và role.
           userInfo = agr[0]
           requiredLogged = matchLvl.get('loggin_required') # boolean
           isLogged = userInfo.get('logged_in') # boolean
           # 1: Kiểm tra loggin
           if (requiredLogged and not isLogged):
                return f"❌ Từ chối: Tính năng yêu cầu đăng nhập"
           # 2: Kiểm tra role
           requiredRoles = matchLvl.get('roles_required') # list
           userRole = userInfo.get('role') # string
           if(len(requiredRoles) >0 and (userRole not in requiredRoles)):
               return f"❌ Từ chối: Tính năng yêu cầu quyền {requiredRoles}"
           return func(*agr, **kagr)
        return wrapper
    return decor

guest = {"logged_in": False}
newuser = {"logged_in": True}
hacker = {"logged_in": False, "role": "super_admin"}
admin = {"logged_in": True, "role": "admin"}
employee = {"logged_in": True, "role": "employee"}
				

@check_security(level="HIGH")
def xoa_nguoi_dung(user_role, target_user_email):
    return f"✅ Đã xóa người dùng {target_user_email}."

@check_security(level="MEDIUM")
def xem_thong_tin_noi_bo(user_role):
    return "✅ Đây là thông tin nội bộ - phải đăng nhập."
		
@check_security(level="LOW")
def xem_thong_tin(user_role):
    return "✅ Đây là thông tin công khai."

@check_security(level="TROLL")
def test_edge_case(user_role):
    return "✅ PASSED."

# Thử nghiệm
print(xoa_nguoi_dung(guest, "hacker@gmail.com")) # Từ chối
print(xoa_nguoi_dung(admin, "hacker@gmail.com")) # Thành công
print(xoa_nguoi_dung(employee, "hacker@gmail.com")) # Từ chối
print(xem_thong_tin_noi_bo(admin)) # Thành công
print(xem_thong_tin_noi_bo(newuser)) # Thất bại
print(xem_thong_tin(guest))              # Thành công
print(test_edge_case(hacker))