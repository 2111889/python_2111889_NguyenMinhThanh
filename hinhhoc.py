from enum import Enum

class LoaiHinh(Enum):
    TatCa = 1
    HinhTron = 2
    HinhChuNhat = 3
    HinhVuong = 4

class HinhHoc:
    def __init__(self, canh: float):
        self.Canh = canh    
    
    def TinhDienTich(self):
        pass
    
    def dtlh(self, other):
        return self.TinhDienTich() > other.TinhDienTich()
    
    def dtbh(self, other):
        return self.TinhDienTich() < other.TinhDienTich()

    def Xuat(self):
        print(f"Hinh hoc co canh: {self.Canh}")
    
class HinhTron(HinhHoc):
    def __init__(self, canh: float):
        super().__init__(canh)
        self.BanKinh = canh
    
    def TinhDienTich(self):
        return self.BanKinh**2*3.14

    def Xuat(self):
        print(f"Hinh tron ban kinh: {self.BanKinh}, co dien tich: {self.TinhDienTich()}")

class HinhChuNhat(HinhHoc):
    def __init__(self, canh: float, rong: float):
        super().__init__(canh)
        self.ChieuDai = canh
        self.ChieuRong = rong

    def TinhDienTich(self):
        return self.ChieuDai*self.ChieuRong
    
    def Xuat(self):
        print(f"Hinh chu nhat co chieu dai: {self.ChieuDai}, chieu rong: {self.ChieuRong}, co dien tich: {self.TinhDienTich()}")

class HinhVuong(HinhChuNhat):
    def __init__(self, canh: float):
        super().__init__(canh, canh)

    def Xuat(self):
        print(f"Hinh vuong co canh: {self.Canh}, co dien tich: {self.TinhDienTich()}")

# print(LoaiHinh(1).name)

# hinhhoc = HinhHoc(99)
# hinhhoc.Xuat()

# hinhtron = HinhTron(5)
# hinhtron.Xuat()

# hinhchunhat = HinhChuNhat(20, 10)
# hinhchunhat.Xuat()

# hinhvuong = HinhVuong(10)
# hinhvuong.Xuat()
