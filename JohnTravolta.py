# Tugas 1 Software Testing (2021)
# Ravi Edho Nugraha
# 11190910000038

# Custom Exception Handling
class Error(Exception):
    pass


class OutOfRangeLowerBoundError(Error):
    pass


class OutOfRangeUpperBoundError(Error):
    pass

# Functions
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
        return "Namun pengeluaran anda lebih besar daripada pendapatan sebanyak Rp" + str(-(gaji - pengeluaran)) + ". Sebaiknya anda mencari tambahan pekerjaan lain."
    elif pengeluaran == gaji:
        return "Pengeluaran dan pendapatan anda sama besar sehingga anda tidak dapat menabung."
    else:
        return "Pendapatan anda melebihi pengeluaran anda sehingga anda dapat menabung sebesar Rp" + str(gaji - pengeluaran) + " tiap minggunya."

# Main Program
while True:
    try:
        jamKerja = int(input("Masukkan jumlah jam kerja tiap minggunya: "))
        if jamKerja < 0:
            raise OutOfRangeLowerBoundError
        elif jamKerja > 168:
            raise OutOfRangeUpperBoundError
        else:
            break
    except OutOfRangeLowerBoundError:
        print("Anda tidak dapat memasukkan angka negatif")
    except OutOfRangeUpperBoundError:
        print("Dalam satu minggu hanya terdapat 168 jam")
    except ValueError:
        print("Anda harus mengisi bilangan bulat")

while True:
    try:
        pengeluaran = int(
            input("Masukkan jumlah pengeluaran anda tiap minggunya: Rp"))
        if pengeluaran < 0:
            raise OutOfRangeLowerBoundError
        else:
            break
    except OutOfRangeLowerBoundError:
        print("Anda tidak dapat memasukkan angka negatif")

print("Maka pendapatan anda per minggu adalah Rp" + str(totalGaji(jamKerja)) + ".")
print(tabungan(pengeluaran, totalGaji(jamKerja)))