#NAMA   :   ARYA YUDHISTIRA
#NIM    :   121140115
#KELAS  :   RB
class Mahasiswa:
    nama_kampus="Institut Teknologi Sumatera"
    __nama_rektor="Prof. Dr. I Nyoman Pugeg Aryantha"
    def __init__(self,nama,nim,alamat) -> None:
        self.nama=nama
        self._nim=nim
        self.__alamat=alamat

    def rektor (self):
        #Atribut private __nama_rektor dapat dipanggil di dalam class
        print(f"Nama Rektor : {self.__nama_rektor}")

    def biodata(self):
        #Atribut private __alamat dapat dipanggil di dalam class
        print(f"\nNama : {self.nama}\nNIM : {self._nim}\nAlamat : {self.__alamat}")

    def ubah_alamat(self,alamat):
        self.__alamat=alamat

Arya=Mahasiswa("Arya Yudhistira",121140115,"Way Kandis")
#Atribut class dapat dipanggil di main program
print(f"Nama Kampus : {Arya.nama_kampus}")
#Atribut public dapat dipanggil di main program
print(f"Nama : {Arya.nama}")
#Atribut protected dapat dipanggil di main program
print(f"NIM : {Arya._nim}")
#Namun jika atribut private __nama_rektor dipanggil di main program, akan terjadi error. Misal print(Arya.__nama_rektor)
#Untuk mengatasi ini, kita dapat memanggilnya didalam classnya seperti pada fungsi def rektor
Arya.rektor()
#Begitu pula pada atribut private __alamat, kita tidak bisa memangilnya di main dengan Arya.__alamat
#Maka kita harus memanggilnya didalam class seperti pada fungsi def biodata
Arya.biodata()

#Atribut public dan private dapat diubah valuenya di main program, hal ini mungkin saja menyebabkan ketidaksengajaaan pengubahan data
Arya.nama="Arya Y"
Arya._nim=115
#Output setelah diubah
Arya.biodata()
#Maka dari itu, atribute private dibutuhkan untuk mencegah ketidaksengajaan pengubahan data
#Atribut private dapat diubah di dalam classnya seperti pada fungsi def ubah_alamat
Arya.ubah_alamat("Belwis")
#Output setelah diubah
Arya.biodata()

#Jadi, perbedaan antara atribut public dan protected dari segi penggunaan hampir tidak ada, hanya beda di penulisan saat pemanggilan variable saja
#Ditambahkan 1 underscore di depan untuk protected.
#Sedangkan atribut private dapat berguna untuk mencegah adanya kesalahan pengubahan data, dan lain-lainnya. 
#Dan secara penulisan atribut private ditambahkan 2 underscore di depan 
