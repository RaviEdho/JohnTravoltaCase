def totalGaji(jam):
    ambangMinimumLembur = 40

    if jam > ambangMinimumLembur:
        gajiNormal = ambangMinimumLembur * 15000
        gajiLembur = (jam - ambangMinimumLembur) * 15000 * 1.5
        return gajiNormal + gajiLembur
    else:
        gaji = jam * 15000
        return gaji

def tabungan(pengeluaran, gaji):
    if pengeluaran > gaji:
        print("Namun pengeluaran anda lebih besar daripada pendapatan sebanyak Rp" + str(-(gaji - pengeluaran)) + "! Sebaiknya anda mencari tambahan pekerjaan lain.")
    elif pengeluaran == gaji:
        print("Pengeluaran dan pendapatan anda sama besar sehingga anda tidak dapat menabung")
    else:
        print("Pendapatan anda melebihi pengeluaran anda sehingga anda dapat menabung sebesar Rp" + str(gaji - pengeluaran))

print("Anda seorang karyawan bernama John Travolta. Gaji anda tiap minggunya sebesar Rp15000 per jam.")
print("Dan untuk setiap jam di atas 40 jam, anda akan dibayar 150%.")
jamKerja = int(input("Berapa jam anda akan bekerja setiap minggunya? "))
print("Anda juga ingin menabung. Namun anda tidak tahu seberapa banyak dapat menabung apabila tidak tahu pengeluaran anda.")
pengeluaran = int(input("Berapa pengeluaran anda setiap minggunya? "))
print("Anda akan pendapatan sebanyak Rp" + str(totalGaji(jamKerja)) + " tiap minggunya.")
tabungan(pengeluaran, totalGaji(jamKerja))
