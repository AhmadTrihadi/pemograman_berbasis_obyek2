class Mahasiswa:
    def __init__(self, nama, NIM):
        self.nama = nama
        self.NIM = NIM
    def info(self):
        print(f"Nama: {self.nama}\nNIM: {self.NIM}")
mahasiswaB = Mahasiswa("ADI", "210511128")
mahasiswaB.info()