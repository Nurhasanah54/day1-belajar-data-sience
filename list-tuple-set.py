# Contoh Penggunaan List, Tuple, dan Set di Python

# LIST 
print
buah = ["apel", "jeruk", "mangga"]
print("Awal:", buah)

buah.append("pisang")  # menambah data
print("Setelah append:", buah)

buah.remove("jeruk")   # menghapus data
print("Setelah remove:", buah)

buah.insert(1, "anggur")  # menyisipkan data di index ke-1
print("Setelah insert:", buah)

print()

# TUPLE 
print
hewan = ("kucing", "anjing", "kelinci")
print("Tuple:", hewan)

# hewan[0] = "burung"  # ❌ ERROR: tidak bisa diubah

print()

# SET
print
angka = {1, 2, 3, 4}
print("Awal:", angka)

angka.add(5)   # menambah elemen
print("Setelah add:", angka)

angka.discard(2)  # menghapus elemen
print("Setelah discard:", angka)

angka2 = {3, 4, 5, 6}
print("Union:", angka.union(angka2))
print("Intersection:", angka.intersection(angka2))
