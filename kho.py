
kho = {
    "1": {"ten": "Bút bi", "so_luong": 50},
    "2": {"ten": "Vở học sinh", "so_luong": 35},
    "3": {"ten": "Thước kẻ", "so_luong": 25},
    "4": {"ten": "Tẩy", "so_luong": 8},
    "5": {"ten": "Bút chì", "so_luong": 15},
    "6": {"ten": "Máy tính Casio", "so_luong": 12},
    "7": {"ten": "Balo", "so_luong": 5},
    "8": {"ten": "Sách giáo khoa", "so_luong": 20},
    "9": {"ten": "Bình nước", "so_luong": 7},
    "10": {"ten": "Hộp bút", "so_luong": 18}
}


# CREATE
def them_hang():
    ma = input("Nhập mã hàng: ")

    if ma in kho:
        print("Mã hàng đã tồn tại!")
        return

    ten = input("Nhập tên hàng: ")
    so_luong = int(input("Nhập số lượng ban đầu: "))

    if so_luong < 0:
        print("Số lượng không hợp lệ!")
        return

    kho[ma] = {
        "ten": ten,
        "so_luong": so_luong
    }

    print("Thêm hàng hóa thành công!")


# UPDATE - NHẬP HÀNG
def nhap_hang():
    ma = input("Nhập mã hàng: ")

    if ma not in kho:
        print("Không tìm thấy hàng hóa!")
        return

    sl = int(input("Nhập số lượng nhập thêm: "))

    if sl <= 0:
        print("Số lượng phải lớn hơn 0!")
        return

    kho[ma]["so_luong"] += sl

    print("Nhập hàng thành công!")


# UPDATE - XUẤT HÀNG
def xuat_hang():
    ma = input("Nhập mã hàng: ")

    if ma not in kho:
        print("Không tìm thấy hàng hóa!")
        return

    sl = int(input("Nhập số lượng xuất: "))

    if sl <= 0:
        print("Số lượng phải lớn hơn 0!")
        return

    if sl > kho[ma]["so_luong"]:
        print("Không đủ hàng trong kho!")
        return

    kho[ma]["so_luong"] -= sl

    print("Xuất hàng thành công!")

    if kho[ma]["so_luong"] < 10:
        print("Cảnh báo: Tồn kho thấp!")


# READ - TÌM KIẾM
def tim_kiem():
    ma = input("Nhập mã hàng cần tìm: ")

    if ma in kho:
        print("\nTHÔNG TIN HÀNG HÓA")
        print("ID:", ma)
        print("Tên:", kho[ma]["ten"])
        print("Số lượng:", kho[ma]["so_luong"])
    else:
        print("Không tìm thấy hàng hóa!")


# READ - HIỂN THỊ DANH SÁCH
def hien_thi_danh_sach():
    if len(kho) == 0:
        print("Kho đang trống!")
        return

    print("\n===== DANH SÁCH HÀNG HÓA =====")

    for ma, thong_tin in kho.items():
        print(f"ID: {ma}")
        print(f"Tên: {thong_tin['ten']}")
        print(f"Số lượng: {thong_tin['so_luong']}")
        print("-" * 30)


# DELETE
def xoa_hang():
    ma = input("Nhập mã hàng cần xóa: ")

    if ma in kho:
        del kho[ma]
        print("Xóa hàng hóa thành công!")
    else:
        print("Không tìm thấy hàng hóa!")


# CẢNH BÁO TỒN KHO THẤP
def canh_bao_ton_kho():
    print("\n===== TỒN KHO THẤP =====")

    ton_thap = False

    for ma, thong_tin in kho.items():
        if thong_tin["so_luong"] < 10:
            print(
                f"ID: {ma} | "
                f"Tên: {thong_tin['ten']} | "
                f"Số lượng: {thong_tin['so_luong']}"
            )
            ton_thap = True

    if not ton_thap:
        print("Không có mặt hàng nào tồn kho thấp.")


# THỐNG KÊ
def thong_ke():
    tong_mat_hang = len(kho)

    tong_so_luong = 0

    for thong_tin in kho.values():
        tong_so_luong += thong_tin["so_luong"]

    print("\n===== THỐNG KÊ =====")
    print("Tổng số mặt hàng:", tong_mat_hang)
    print("Tổng số lượng tồn kho:", tong_so_luong)


# MENU CHÍNH
while True:
    print("\n========== QUẢN LÝ KHO HÀNG ==========")
    print("1. Thêm hàng hóa")
    print("2. Nhập hàng")
    print("3. Xuất hàng")
    print("4. Tìm kiếm hàng hóa")
    print("5. Hiển thị danh sách hàng hóa")
    print("6. Xóa hàng hóa")
    print("7. Cảnh báo tồn kho thấp")
    print("8. Thống kê")
    print("0. Thoát")

    chon = input("Nhập lựa chọn: ")

    if chon == "1":
        them_hang()

    elif chon == "2":
        nhap_hang()

    elif chon == "3":
        xuat_hang()

    elif chon == "4":
        tim_kiem()

    elif chon == "5":
        hien_thi_danh_sach()

    elif chon == "6":
        xoa_hang()

    elif chon == "7":
        canh_bao_ton_kho()

    elif chon == "8":
        thong_ke()

    elif chon == "0":
        print("Đã thoát chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ!")