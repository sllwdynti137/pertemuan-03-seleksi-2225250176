# Input: nilai akhir dan persentase kehadiran
# Proses: mengecek dua syarat kelulusan
# Output: Lulus atau Belum lulus

nilai = float(input("Nilai akhir: "))
kehadiran = float(input("Kehadiran (%): "))

if nilai >= 60 and kehadiran >= 80:
    print("Lulus")
else:
    print("Belum lulus")