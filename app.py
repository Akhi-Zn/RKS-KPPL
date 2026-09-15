print("HELLO WORLD")

nama = input("Masukkan nama: ").strip()

if not nama:
    print("Error: Nama tidak boleh kosong.")
elif len(nama) < 3:
    print("Error: Nama minimal 3 karakter.")
else:
    print(f"Halo, {nama}!")