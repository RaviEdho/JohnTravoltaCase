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
    gajiTotal = 0
    
    if type(jam) != int:
        raise TypeError("Nilai jam kerja harus bilangan bulat")
    if jam < 0:
        raise OutOfRangeLowerBoundError("Nilai jam kerja tidak boleh negatif")
    elif jam > 168:
        raise OutOfRangeUpperBoundError("Batas maksimum jam kerja adalah 168 jam")
    elif jam > ambangMinimumLembur:
        gajiNormal = ambangMinimumLembur * 15000
        gajiLembur = (jam - ambangMinimumLembur) * 15000 * 150 / 100
        gajiTotal = int(gajiNormal + gajiLembur)
    else:
        gajiTotal = int(jam * 15000)
    
    return gajiTotal


def tabungan(jam, pengeluaran):
    pesan = ""
    gajiTotal = totalGaji(jam)

    if type(pengeluaran) != int:
        raise TypeError("Nilai pengeluaran harus bilangan bulat")
    elif pengeluaran < 0:
        raise OutOfRangeLowerBoundError("Nilai pengeluaran tidak boleh negatif")
    elif pengeluaran > gajiTotal:
        pesan = "Cari tambahan pekerjaan lain."
    elif pengeluaran == gajiTotal:
        pesan = "Anda tidak dapat menabung."
    else:
        pesan = "Dapat menabung sebesar Rp" + str(gajiTotal - pengeluaran) + "."
    
    return pesan

# Main Program
if __name__ == "__main__":

    jamKerja = 0
    pengeluaran = 0
    
    while True:
        try:
            jamKerja = int(input("Masukkan jumlah jam kerja tiap minggunya: "))
            print("Maka pendapatan anda per minggu adalah Rp" + str(totalGaji(jamKerja)) + ".")
            break
        except OutOfRangeLowerBoundError as e: print(e)
        except OutOfRangeUpperBoundError as e: print(e)
        except ValueError: print("Nilai jam kerja harus bilangan bulat")

    while True:
        try:
            pengeluaran = int(input("Masukkan jumlah pengeluaran anda tiap minggunya: Rp"))
            print(tabungan(jamKerja, pengeluaran))
            break
        except OutOfRangeLowerBoundError as e: print(e)
        except ValueError: print("Nilai pengeluaran harus bilangan bulat")