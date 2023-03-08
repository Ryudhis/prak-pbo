#NAMA   : ARYA YUDHISTIRA
#NIM    : 121140115
#KELAS  : RB
class AkunBank:
    list_pelanggan = {}
    def __init__(self,no_pelanggan,nama_pelanggan,jumlah_saldo) -> None:
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        AkunBank.list_pelanggan.update({self.__no_pelanggan:self.__nama_pelanggan})

    def lihat_saldo(self):
        print(f"{self.__nama_pelanggan} memiliki saldo Rp.{self.__jumlah_saldo}")
        AkunBank.lihat_menu(self)

    def tarik_tunai(self):
        while True:
            penarikan=int(input("Masukkan jumlah nominal yang ingin ditarik : "))
            if penarikan <= self.__jumlah_saldo:
                self.__jumlah_saldo-=penarikan
                print(f"Saldo sebesar {penarikan} berhasil ditarik!\nSisa saldo anda adalah Rp.{self.__jumlah_saldo}")
                break
            else:
                print(f"Nominal saldo yang Anda punya tidak cukup!")
        AkunBank.lihat_menu(self)

    def transfer (self):
        jumlah_transfer=int(input("Masukkan nominal yang ingin ditransfer : "))
        if jumlah_transfer <= self.__jumlah_saldo:
            no_rek = int(input("Masukkan no rekening tujuan : "))
            if no_rek in self.list_pelanggan:
                print(f"Transfer Rp.{jumlah_transfer} ke {self.list_pelanggan[no_rek]} sukses!")
                AkunBank.lihat_menu(self)
            else:
                print(f"No rekening tujuan tidak dikenal! Kembali ke menu utama...")
                AkunBank.lihat_menu(self)
        else:
            print(f"Maaf, saldo anda tidak cukup. Kembali ke menu utama...")
            AkunBank.lihat_menu(self)


    def lihat_menu(self):
        print(f"\nSelamat datang di Bang Lampunk\nHalo {self.__nama_pelanggan}, ingin melakukan apa?\n1. Lihat saldo\n2. Tarik tunai\n3. Transfer saldo\n4. Keluar")
        choice=int(input("Masukkan pilihan menu (1-4) : "))
        print()
        if choice == 1:
            AkunBank.lihat_saldo(self)
        elif choice == 2:
            AkunBank.tarik_tunai(self)
        elif choice == 3:
            AkunBank.transfer(self)
        elif choice == 4:
            print(f"Terima kasih!")
            exit()
        else:
            print("Inputan salah!, inputkan angka (1-4)")
        
Akun1 = AkunBank(1234, "Arya Yudhistira", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

Akun1.lihat_menu()
