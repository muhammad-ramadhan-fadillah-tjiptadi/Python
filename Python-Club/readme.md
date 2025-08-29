# Tipe Data

- Boolean: menyatakan benar `True` yang bernilai 1, atau salah `False` yang bernilai 0.
- String: menyatakan karakter/kalimat bisa berupa huruf angka, dll (diapit tanda " atau ')
- Integer: menyatakan bilangan bulat
- Float: menyatakan bilangan yang mempunyai koma
- Hexadecimal: menyatakan bilangan dalam format heksa (bilangan berbasis 16)
- Complex: menyatakan pasangan angka real dan imajiner
- List: menyimpan berbagai tipe data dan isinya bisa diubah-ubah. Contoh: `['xyz', 786, 2.23]`
- Tuple: menyimpan berbagai tipe data tapi isinya tidak bisa diubah. Contoh: `('xyz', 768, 2.23)`
- Dictionary: menyimpan berbagai tipe data berupa pasangan penunjuk dan nilai. Contoh: `{'nama': 'adi', 'id': 2}`

# Operator Aritmatika

- Penjumlahan (+): menjumlahkan nilai dari masing-masing operan atau bilangan. Contoh: `1 + 3 = 4`
- Pengurangan (-): mengurangi nilai operan di sebelah kiri menggunakan operan di sebelah kanan. Contoh: `4 - 1 = 3`
- Perkalian (*): mengalikan operan/bilangan. Contoh: `2 * 4 = 8`
- Pembagian (/): untuk membagi operan di sebelah kiri menggunakan operan di sebelah kanan. Contoh: `10 / 5 = 2`
- Sisa Bagi (%): mendapatkan sisa pembagian dari operan di sebelah kiri operator ketika dibagi oleh operan di sebelah kanan operator. Contoh: `11 % 2 = 1`
- Pangkat (**): memangkatkan operan disebelah kiri operator dengan operan di sebelah kanan operator. Contoh: `8 ** 2 = 64`
- Pembagian Bulat (//): sama seperti pembagian. Hanya saja angka dibelakang koma dihilangkan. Contoh: `10 // 3 = 3`

# Operator Perbandingan
Operator perbandingan (comparison operators) digunakan untuk membandingkan suatu nilai dari masing-masing operan.

Operator	Contoh	Penjelasan
Sama dengan ==	1 == 1	bernilai True Jika masing-masing operan memiliki nilai yang sama, maka kondisi bernilai benar atau True.
Tidak sama dengan !=	2 != 2	bernilai False Akan menghasilkan nilai kebalikan dari kondisi sebenarnya.
Tidak sama dengan <>	2 <> 2	bernilai False Akan menghasilkan nilai kebalikan dari kondisi sebenarnya.
Lebih besar dari >	5 > 3	bernilai True Jika nilai operan kiri lebih besar dari nilai operan kanan, maka kondisi menjadi benar.
Lebih kecil dari <	5 < 3	bernilai True Jika nilai operan kiri lebih kecil dari nilai operan kanan, maka kondisi menjadi benar.
Lebih besar atau sama dengan >=	5 >= 3	bernilai True Jika nilai operan kiri lebih besar dari nilai operan kanan, atau sama, maka kondisi menjadi benar.
Lebih kecil atau sama dengan <=	5 <= 3	bernilai True Jika nilai operan kiri lebih kecil dari nilai operan kanan, atau sama, maka kondisi menjadi benar.

# Operator Logika
Operator logika digunakan untuk menghubungkan kondisi-kondisi yang sudah ada.

Operator	Contoh	Penjelasan
Dan (and)	True and True	bernilai True Jika semua kondisi bernilai True, maka kondisi menjadi benar.
Atau (or)	True or False	bernilai True Jika salah satu kondisi bernilai True, maka kondisi menjadi benar.
Tidak (not)	not True	bernilai False Akan menghasilkan nilai kebalikan dari kondisi sebenarnya.

# Operator Bitwise
Operator bitwise digunakan untuk operasi bit demi bit terhadap nilai operan.

Operator	Contoh	Penjelasan
AND (&)	5 & 3	bernilai 1 Jika bit-bit yang bersesuaian dari masing-masing operan bernilai 1, maka bit-bit yang bersesuaian dari hasilnya akan bernilai 1.
OR (|)	5 | 3	bernilai 7 Jika bit-bit yang bersesuaian dari masing-masing operan bernilai 1, maka bit-bit yang bersesuaian dari hasilnya akan bernilai 1.
XOR (^)	5 ^ 3	bernilai 6 Jika bit-bit yang bersesuaian dari masing-masing operan memiliki nilai yang berbeda, maka bit-bit yang bersesuaian dari hasilnya akan bernilai 1.
NOT (~)	~5	bernilai -6 Akan menghasilkan nilai kebalikan dari kondisi sebenarnya.

# Operator Penugasan
Operator penugasan digunakan untuk memberikan atau memodifikasi nilai ke dalam sebuah variabel.

Operator	Contoh	Penjelasan
Sama dengan =	a = 1	Memberikan nilai di kanan ke dalam variabel yang berada di sebelah kiri.
Tambah sama dengan +=	a += 2	Memberikan nilai variabel dengan nilai variabel itu sendiri ditambah dengan nilai di sebelah kanan.
Kurang sama dengan -=	a -= 2	Memberikan nilai variabel dengan nilai variabel itu sendiri dikurangi dengan nilai di sebelah kanan.
Kali sama dengan *=	a *= 2	Memberikan nilai variabel dengan nilai variabel itu sendiri dikali dengan nilai di sebelah kanan.
Bagi sama dengan /=	a /= 4	Memberikan nilai variabel dengan nilai variabel itu sendiri dibagi dengan nilai di sebelah kanan.
Sisa bagi sama dengan %=	a %= 3	Memberikan nilai variabel dengan nilai variabel itu sendiri dibagi dengan nilai di sebelah kanan. Yang diambil nantinya adalah sisa baginya.
Pangkat sama dengan **=	a **= 3	Memberikan nilai variabel dengan nilai variabel itu sendiri dipangkatkan dengan nilai di sebelah kanan.
Pembagian bulat sama dengan //=	a //= 3	Membagi bulat operan sebelah kiri operator dengan operan sebelah kanan operator kemudian hasilnya diisikan ke operan sebelah kiri.

# Prioritas Eksekusi Operator di Python
Dari semua operator diatas, masing-masing mempunyai urutan prioritas yang nantinya prioritas pertama akan dilakukan paling pertama, begitu seterusnya sampai dengan prioritas terakhir.

Operator	Keterangan
**	Aritmatika
~, +, -	Bitwise
*, /, %, //	Aritmatika
+, -	Aritmatika
>>, <<	Bitwise
