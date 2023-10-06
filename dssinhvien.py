from sinhvien import SinhVien
from sinhvien import SinhVienChinhQuy
from sinhvien import SinhVienPhiCQ
from datetime import datetime

class DanhSachSV:
    # def __init__(self):
    #     self.__DanhSachSV = []
    
    def __init__(self, arg1=None):
        if arg1 is None:
            self.__DanhSachSV = []
        else:
            self.__DanhSachSV = arg1

    def themSinhVien(self,sv: SinhVien):
        self.__DanhSachSV.append(sv)

    def Xuat(self):
        for sv in self.__DanhSachSV:
            print(str(sv))

    def getSV(self, stt):
        return self.__DanhSachSV[stt]

    def sapXepTangTheoHoTen(self):
        self.__DanhSachSV = sorted(self.__DanhSachSV, key=lambda sv: sv.XuatTen())
    
    def sapXepGiamTheoHoTen(self):
        self.__DanhSachSV = sorted(self.__DanhSachSV, key=lambda sv: sv.XuatTen(), reverse=True)

    def SinhVienTren80(self):
        return DanhSachSV([sv for sv in self.__DanhSachSV if isinstance(sv, SinhVienChinhQuy) and int(sv._SinhVienChinhQuy__diemrl) > 80])

        # dssv = DanhSachSV()
        # for sv in self.__DanhSachSV:
        #     if isinstance(sv, SinhVienChinhQuy) and int(sv._SinhVienChinhQuy__diemrl) > 80:
        #         dssv.themSinhVien(sv)
        # return dssv
    
    def SinhVienCaoDangTruoc1999(self):
        return DanhSachSV([sv for sv in self.__DanhSachSV if isinstance(sv, SinhVienPhiCQ) and sv._SinhVienPhiCQ__trinhdo == "Cao Dang" and int(datetime.strptime(sv._SinhVien__ngaysinh, "%d.%m.%Y").year) < 1999])

        # dssv = DanhSachSV()
        # for sv in self.__DanhSachSV:
        #     if isinstance(sv, SinhVienPhiCQ) and sv._SinhVienPhiCQ__trinhdo == "Cao Dang" and int(datetime.strptime(sv._SinhVien__ngaysinh, "%d.%m.%Y").year) < 1999:
        #         dssv.themSinhVien(sv)
        # return dssv
    
    def combine(self, other):
        if isinstance(other, DanhSachSV):
            self.__DanhSachSV += other.__DanhSachSV
        

def doc_file_sinhvien():
    dssv = DanhSachSV()
    with open("DanhSachSV.txt", 'r') as file:
        for line in file:
            maso, hoten, ngaysinh = line.strip().split(';')
            student = SinhVien(maso, hoten, ngaysinh)
            dssv.themSinhVien(student)
    return dssv

def doc_file_sinhvienCQ():
    dssv = DanhSachSV()
    with open("SVCQ.txt", 'r') as file:
        for line in file:
            maso, hoten, ngaysinh, diemrl = line.strip().split(';')
            student = SinhVienChinhQuy(maso, hoten, ngaysinh, diemrl)
            dssv.themSinhVien(student)
    return dssv

def doc_file_sinhvienPCQ():
    dssv = DanhSachSV()
    with open("SVPCQ.txt", 'r') as file:
        for line in file:
            maso, hoten, ngaysinh, trinhdo, tgdt = line.strip().split(';')
            student = SinhVienPhiCQ(maso, hoten, ngaysinh,trinhdo, tgdt)
            dssv.themSinhVien(student)
    return dssv    


dssv1 = doc_file_sinhvien()
dssv2 = doc_file_sinhvienCQ()
dssv3 = doc_file_sinhvienPCQ()

dssv1.combine(dssv2)
dssv1.combine(dssv3)

# tren80 = dssv1.SinhVienTren80()
# tren80.Xuat()

truoc90 = dssv1.SinhVienCaoDangTruoc1999()
truoc90.Xuat()
print("===================================")

# dssv.sapXepTangTheoHoTen()
# dssv.Xuat()


