from math import gcd
from phanso import PhanSo

class DanhSachPhanSo:
    def __init__(self):
        self.ds_phan_so = []

    def them_phan_so(self, phan_so):
        if isinstance(phan_so, PhanSo):
            self.ds_phan_so.append(phan_so)
        else:
            raise ValueError("Đối tượng không phải là phân số")

    def dem_phan_so_am(self):
        dem = 0
        for phan_so in self.ds_phan_so:
            if phan_so.is_am():
                dem += 1
        return dem

    def tim_phan_so_duong_nho_nhat(self):
        phan_so_duong = [ps for ps in self.ds_phan_so if not ps.is_am()]
        if phan_so_duong:
            return min(phan_so_duong, key=lambda ps: ps.tu_so / ps.mau_so)
        else:
            return None

    def tim_vi_tri_phan_so(self, x):
        vi_tri = []
        for i, phan_so in enumerate(self.ds_phan_so):
            if phan_so.tu_so == x.tu_so and phan_so.mau_so == x.mau_so:
                vi_tri.append(i)
        return vi_tri

    def tinh_tong_phan_so_am(self):
        tong = 0
        for phan_so in self.ds_phan_so:
            if phan_so.is_am():
                tong += phan_so.tu_so / phan_so.mau_so
        return tong

    def xoa_phan_so(self, x):
        self.ds_phan_so = [ps for ps in self.ds_phan_so if ps.tu_so != x.tu_so or ps.mau_so != x.mau_so]

    def xoa_phan_so_theo_tu(self, x):
        self.ds_phan_so = [ps for ps in self.ds_phan_so if ps.tu_so != x]

    def sap_xep_tang(self):
        self.ds_phan_so.sort(key=lambda ps: ps.tu_so / ps.mau_so)

    def sap_xep_giam(self):
        self.ds_phan_so.sort(key=lambda ps: ps.tu_so / ps.mau_so, reverse=True)

    def sap_xep_tang_mau(self):
        self.ds_phan_so.sort(key=lambda ps: ps.mau_so)

    def sap_xep_giam_mau(self):
        self.ds_phan_so.sort(key=lambda ps: ps.mau_so, reverse=True)

# Ví dụ sử dụng
ds = DanhSachPhanSo()
ds.them_phan_so(PhanSo(4, 5))
ds.them_phan_so(PhanSo(3, 4))
ds.them_phan_so(PhanSo(-2, 5))
ds.them_phan_so(PhanSo(1, 3))

so_luong_am = ds.dem_phan_so_am()
print("Số lượng phân số âm trong danh sách là:", so_luong_am)

# # 

# phan_so_duong_nho_nhat = ds.tim_phan_so_duong_nho_nhat()
# if phan_so_duong_nho_nhat is not None:
#     print("Phân số dương nhỏ nhất trong danh sách là:", phan_so_duong_nho_nhat)
# else:
#     print("Không có phân số dương trong danh sách.")

# # 

# x = PhanSo(3, 4)
# vi_tri_x = ds.tim_vi_tri_phan_so(x)
# if vi_tri_x:
#     print(f"Phân số {x} xuất hiện tại vị trí:", vi_tri_x)
# else:
#     print(f"Phân số {x} không xuất hiện trong danh sách.")

# # 

# tong_phan_so_am = ds.tinh_tong_phan_so_am()
# print("Tổng các phân số âm trong danh sách là:", tong_phan_so_am)

# # 

# x = PhanSo(-1, 2)
# ds.xoa_phan_so(x)
# print("Danh sách sau khi xóa phân số", x, ":", ds.ds_phan_so)

# x = 1
# ds.xoa_phan_so_theo_tu(x)
# print("Danh sách sau khi xóa các phân số có tử số", x, ":", ds.ds_phan_so)

# # 

# print("Danh sách gốc:")
# for ps in ds.ds_phan_so:
#     print(ps)

# ds.sap_xep_tang()
# print("\nDanh sách sau khi sắp xếp tăng theo giá trị:")
# for ps in ds.ds_phan_so:
#     print(ps)

# ds.sap_xep_giam()
# print("\nDanh sách sau khi sắp xếp giảm theo giá trị:")
# for ps in ds.ds_phan_so:
#     print(ps)

# ds.sap_xep_tang_mau()
# print("\nDanh sách sau khi sắp xếp tăng theo mẫu số:")
# for ps in ds.ds_phan_so:
#     print(ps)

# ds.sap_xep_giam_mau()
# print("\nDanh sách sau khi sắp xếp giảm theo mẫu số:")
# for ps in ds.ds_phan_so:
#     print(ps)