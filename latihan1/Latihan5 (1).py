class PesawatTerbang:
    def __init__(self, maskapai, tujuan):
            self.maskapai = maskapai
            self.tujuan = tujuan
    def info(self):
        print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}")
pesawatA = PesawatTerbang("MEGA TERBANG", "CIREBON - KOREA SELATAN")
pesawatA.info()
