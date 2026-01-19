
# Employee = tuple(name, total_hours, ot_hours, late_hours, hourly_rate)
# ListEmployee = dict({
#     str: Employee
# })

employees = {
    "E01": ("Nguyễn Văn An", 170, 12, 2, 50000),
    "E02": ("Trịnh Thăng Bình", 155, 19.5, 10, 60000),
    "E03": ("Mai Quỳnh Chi", 180, 28, 4, 55000),
    "E04": ("Vũ Thu Ngân", 28, 1, 0, 45000)
}
# Cấu trúc tuple: (name, total_hours, ot_hours, late_hours, hourly_rate)

def calculate_salary(employee:tuple):
    name, total_hours, ot_hours, late_hours, hourly_rate = employee
    kpi_rate = 1 if total_hours >=60 else 0.8
    base_salary = total_hours * hourly_rate * kpi_rate
    ot_salary = ot_hours * hourly_rate * 1.5
    late_salary = late_hours * hourly_rate * 1.2

    print(f"====== PHIẾU LƯƠNG ======\n"
f"Họ tên            : {name}\n"
f"Giờ làm thực tế   : {total_hours} giờ\n"
f"Giờ làm thêm      : {ot_hours} giờ\n"
f"Giờ đi muộn       : {late_hours} giờ\n"
f"Lương theo giờ    : {hourly_rate} (VNĐ)\n"
f"Lương cơ bản      : {base_salary} (VNĐ)\n"
f"Lương làm thêm    : {ot_salary} (VNĐ)\n"
f"Phạt đi muộn      : {late_salary} (VNĐ)\n"
f"Hệ số KPI         : {kpi_rate}\n"
f"------------------------\n"
f"LƯƠNG THỰC NHẬN   : {base_salary + ot_hours - late_salary} (VNĐ)\n"
f"====== KẾT THÚC ======\n")
    

# calculate_salary(employees["E01"])


def salary_reports():
    for key, value in employees.items():
        calculate_salary(value)