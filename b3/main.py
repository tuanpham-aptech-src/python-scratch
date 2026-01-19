# Bạn xây dựng một ứng dụng tìm kiếm online, người dùng có thể: 
# xem danh sách lịch sử tìm kiếm, 
# xoá lịch sử tìm kiếm, 
# và tự động thêm mục tìm kiếm mới vào danh sách.

search_keys = []

def show_menu():
    print(f"===== MENU =====\n"
f"1. Tìm kiếm\n"
f"2. Xem lịch sử tìm kiếm\n"
f"3. Xoá lịch sử tìm kiếm\n"
f"4. Xoá lịch sử tìm kiếm theo từ khóa\n"
f"5. Thoát\n"
f"================")
    
def search():
    k_search = input("Bạn tìm kiếm gì: ")
    if k_search == 'end':
        return
    # bỏ qua rule validate
    search_keys.append(k_search)
    search()


def get_history():
    print(f"Lịch sử tìm kiếm hiện tại: {search_keys}")

def erase_history():
    search_keys.clear()
    print('Đã xóa hết lịch sử tìm kiếm')
    get_history()

def erase_history_by_keyword():
    keyword = input("Từ khóa muốn xóa: ")
    if(keyword not in search_keys):
        print("Từ khóa không có trong danh sách tìm kiếm!")
        return

    search_keys.remove(keyword)
    get_history()

while True:
    show_menu()
    user_input = input("Chọn chức năng (1-5): ")

    if user_input == '1':
       search()
    elif user_input == '2':
       get_history()
    elif user_input == '3':
       erase_history()
    elif user_input == '4':
       erase_history_by_keyword()
    elif user_input == '5':
        break
    else:
        print("Lựa chọn không hợp lệ!")