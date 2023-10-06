from math import gcd

class PhanSo:
    def __init__(self, tu_so, mau_so):
        if mau_so == 0:
            raise ValueError("Mẫu số không thể bằng 0")
        ucln = gcd(tu_so, mau_so)
        self.tu_so = tu_so // ucln
        self.mau_so = mau_so // ucln

    def rut_gon(self):
        ucln = gcd(self.tu_so, self.mau_so)
        self.tu_so = self.tu_so // ucln
        self.mau_so = self.mau_so // ucln

    def __repr__(self): 
        # str la cho chuoi repr la cho so
        return f"{self.tu_so}/{self.mau_so}"

    def __add__(self, other):
        tu_so_moi = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        mau_so_moi = self.mau_so * other.mau_so
        return PhanSo(tu_so_moi, mau_so_moi)

    def __sub__(self, other):
        tu_so_moi = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        mau_so_moi = self.mau_so * other.mau_so
        return PhanSo(tu_so_moi, mau_so_moi)

    def __mul__(self, other):
        tu_so_moi = self.tu_so * other.tu_so
        mau_so_moi = self.mau_so * other.mau_so
        return PhanSo(tu_so_moi, mau_so_moi)

    def __truediv__(self, other):
        tu_so_moi = self.tu_so * other.mau_so
        mau_so_moi = self.mau_so * other.tu_so
        return PhanSo(tu_so_moi, mau_so_moi)

    # >
    def  __gt__(self,other):
        return (self.__tu * other.__mau) > (self.__mau * other.__tu)
        # return (self.__tu/self.__mau) > (other.__tu/other.__mau)
    # <
    def  __lt__(self,other):
        return (self.__tu * other.__mau) < (self.__mau * other.__tu)
        # return (self.__tu/self.__mau) < (other.__tu/other.__mau)
    # ==
    def __eq__(self, other):
        return (self.__tu * other.__mau) == (self.__mau * other.__tu)
        # return (self.__tu/self.__mau) == (other.__tu/other.__mau)
        
    def is_am(self):
        return self.tu_so < 0

# Nhap Phan So

ps1 = PhanSo(3, 6)
ps2 = PhanSo(2, 4)

print("Phân số 1:", ps1)
print("Phân số 2:", ps2)

tong = ps1 + ps2
print("Tổng:", tong)

hieu = ps1 - ps2
print("Hiệu:", hieu)

tich = ps1 * ps2
print("Tích:", tich)

thuong = ps1 / ps2
print("Thương:", thuong)