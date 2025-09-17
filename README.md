# day1-belajar-data-sience

Dalam bahasa pemrograman Python, terdapat beberapa struktur data dasar yang sangat penting untuk dipahami, yaitu *List, **Tuple, dan **Set*.  
Ketiganya sering digunakan dalam pemrograman, termasuk dalam penerapan *Data Science*, karena berfungsi menyimpan dan mengelola kumpulan data.

## 1. List
- *List* adalah tipe data yang bersifat *mutable* (dapat diubah).  
- Elemen dalam list bisa ditambah, dihapus, atau diubah.  
- List ditulis dengan tanda kurung siku [].

*Contoh operasi List:*
- append() → menambah elemen baru.  
- remove() → menghapus elemen.  
- insert() → menyisipkan elemen di posisi tertentu.  
- pop() → menghapus elemen berdasarkan indeks.
## Output
<img width="839" height="140" alt="Image" src="https://github.com/user-attachments/assets/75c3695f-5c32-48bd-8114-2d028bf9f9fc" /> 
## 2. Tuple
- *Tuple* adalah tipe data yang bersifat *immutable* (tidak bisa diubah setelah dibuat).  
- Data dalam tuple tidak bisa ditambah atau dihapus.  
- Tuple ditulis dengan tanda kurung biasa ().

Kegunaan tuple:
- Cocok digunakan untuk data yang bersifat tetap atau konstan.  
- Lebih aman karena tidak bisa dimodifikasi.
## Output
<img width="845" height="82" alt="Image" src="https://github.com/user-attachments/assets/7a94c452-111d-41a0-a5d1-3caeecd85403" />

## 3. Set
- *Set* adalah tipe data yang menyimpan *elemen unik* (tidak boleh ada duplikat).  
- Set tidak memiliki urutan (unordered).  
- Ditulis dengan tanda kurung kurawal {}.

*Contoh operasi Set:*
- add() → menambah elemen baru.  
- remove() atau discard() → menghapus elemen.  
- union() → menggabungkan dua set.  
- intersection() → mengambil irisan dari dua set.

## 4. Perbandingan List, Tuple, dan Set

| Struktur Data | Urutan | Bisa Duplikat? | Bisa Diubah? |
|---------------|--------|----------------|--------------|
| *List*      | Ya     | Ya             | Ya           |
| *Tuple*     | Ya     | Ya             | Tidak        |
| *Set*       | Tidak  | Tidak          | Ya           |

## 5. Kesimpulan
- Gunakan *List* jika data sering berubah.  
- Gunakan *Tuple* jika data tetap.  
- Gunakan *Set* jika ingin data unik tanpa duplikat.  
