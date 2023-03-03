#Nama   : Arya Yudhistira
#NIM    : 121140115
class DataDiri :

    def __init__(self,nama, nim, kelas,sks) -> None:
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.sks= sks

    def MasukKelas(self):
        print(f"Nama saya {self.nama} dengan NIM {self.nim}, saya akan hadir di kelas praktikum PBO {self.kelas} yang berjumlah {self.sks} sks")

    def PindahKelas(self,kelas):
        print(f"Saya akan pindah kelas dari {self.kelas} ke {kelas}")
        self.kelas = kelas
        

a=DataDiri("Arya Yudhistira", 121140115,"RB", 4)
a.MasukKelas()
a.PindahKelas("RA")
