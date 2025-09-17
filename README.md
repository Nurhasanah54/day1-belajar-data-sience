# day1-belajar-data-sience

Dalam bahasa pemrograman Python, terdapat beberapa struktur data dasar yang sangat penting untuk dipahami, yaitu *List, **Tuple, dan **Set*.  
Ketiganya sering digunakan dalam pemrograman, termasuk dalam penerapan *Data Science*, karena berfungsi menyimpan dan mengelola kumpulan data.

## 2. List
- *List* adalah tipe data yang bersifat *mutable* (dapat diubah).  
- Elemen dalam list bisa ditambah, dihapus, atau diubah.  
- List ditulis dengan tanda kurung siku [].

*Contoh operasi List:*
- append() → menambah elemen baru.  
- remove() → menghapus elemen.  
- insert() → menyisipkan elemen di posisi tertentu.  
- pop() → menghapus elemen berdasarkan indeks.
- 
## 3. Tuple
- *Tuple* adalah tipe data yang bersifat *immutable* (tidak bisa diubah setelah dibuat).  
- Data dalam tuple tidak bisa ditambah atau dihapus.  
- Tuple ditulis dengan tanda kurung biasa ().

Kegunaan tuple:
- Cocok digunakan untuk data yang bersifat tetap atau konstan.  
- Lebih aman karena tidak bisa dimodifikasi.

## 4. Set
- *Set* adalah tipe data yang menyimpan *elemen unik* (tidak boleh ada duplikat).  
- Set tidak memiliki urutan (unordered).  
- Ditulis dengan tanda kurung kurawal {}.

*Contoh operasi Set:*
- add() → menambah elemen baru.  
- remove() atau discard() → menghapus elemen.  
- union() → menggabungkan dua set.  
- intersection() → mengambil irisan dari dua set.

## 5. Perbandingan List, Tuple, dan Set

| Struktur Data | Urutan | Bisa Duplikat? | Bisa Diubah? |
|---------------|--------|----------------|--------------|
| *List*      | Ya     | Ya             | Ya           |
| *Tuple*     | Ya     | Ya             | Tidak        |
| *Set*       | Tidak  | Tidak          | Ya           |

## 6. Kesimpulan
- Gunakan *List* jika data sering berubah.  
- Gunakan *Tuple* jika data tetap.  
- Gunakan *Set* jika ingin data unik tanpa duplikat.  
