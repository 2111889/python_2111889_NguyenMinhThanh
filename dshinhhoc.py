from hinhhoc import HinhHoc 
from hinhhoc import HinhTron   
from hinhhoc import HinhChuNhat   
from hinhhoc import HinhVuong   

class DSHinhHoc:
    def __init__(self, arg = None):
        if arg is None:         
            self.DSHinhHoc = []
        else:
            self.DSHinhHoc = arg
            
    
    def themHinh(self, hh: HinhHoc):
        self.DSHinhHoc.append(hh)

    def xuat(self):
        for hh in self.DSHinhHoc:
            hh.Xuat()

    def nhapHinhTron(self, line):
        bankinh = float(line.strip().split(',')[1])
        hinhtron = HinhTron(bankinh)
        self.themHinh(hinhtron)

    def nhapHinhVuong(self, line):
        canh = float(line.strip().split(',')[1])
        hinhvuong = HinhVuong(canh)
        self.themHinh(hinhvuong)

    def nhapHinhChuNhat(self, line):
        dai, rong = float(line.strip().split(',')[1]), float(line.strip().split(',')[2])
        hinhchunhat = HinhChuNhat(dai, rong)
        self.themHinh(hinhchunhat)

    def docFlie(self,file_name):
        with open(file_name, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                kieu = data[0]
                if kieu == "2":
                    self.nhapHinhTron(line)
                elif kieu == "3":
                    self.nhapHinhChuNhat(line)
                elif kieu == "4":
                    self.nhapHinhVuong(line)
        return self  
    
    def timHinhCoDienTichLonNhat(self):
        max_vl = max(self.DSHinhHoc, key=lambda hh: hh.TinhDienTich())
        return DSHinhHoc([hh for hh in self.DSHinhHoc if hh.TinhDienTich() == max_vl])

    def TimHinhCoDienTichNhoNhat(self):
        return min(self.DSHinhHoc, key=lambda hh: hh.TinhDienTich())

    # def TimHinhTronNhoNhat(self):
    #     htlist =  DSHinhHoc([hh for hh in self.DSHinhHoc if isinstance(hh, HinhTron)])
        

dshh = DSHinhHoc()
dshh.docFlie("HinhHoc.txt")
dshh.xuat()

dtln = dshh.timHinhCoDienTichLonNhat()
