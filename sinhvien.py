from datetime import datetime

class SinhVien:
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maso = maSo
        self.__hoten = hoTen
        self.__ngaysinh = ngaySinh

    def XuatTen(self):
        return self.__hoten

    def __str__(self):
        return f"Ma So: {self.__maso}, Ho Ten: {self.__hoten}, Ngay Sinh: {self.__ngaysinh}"



class SinhVienChinhQuy(SinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, diemRl: int) -> None:
        super().__init__(maSo, hoTen, ngaySinh)
        self.__diemrl = diemRl


    def __str__(self):
        return super().__str__() + f", Diem ren luyen: {self.__diemrl}"


class SinhVienPhiCQ(SinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, trinhDo: str, Tgdt: int) -> None:
        super().__init__(maSo, hoTen, ngaySinh)
        self.__trinhdo = trinhDo
        self.__tgdt = Tgdt


    def __str__(self):
        return super().__str__() + f", Trinh do: {self.__trinhdo}, TG_Dao tao: {self.__tgdt}"