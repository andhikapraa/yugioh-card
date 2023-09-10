
# Yu-Gi-Oh! Card Collection Project
![Django version](https://img.shields.io/static/v1?label=Django&message=%20%3E=4.2.5&logo=django&color=092e20)
[![Official Website](https://img.shields.io/static/v1?label=Website&message=currently%20not%20available&logo=googlechrome&color=blue)]()
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

Proyek ini dibuat untuk menyelesaikan tugas mata kuliah
Pemrograman Berbasis Platform yang diselenggarakan oleh
Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2023/2024

Aplikasi Yu-Gi-Oh! Card Collection ini merupakan aplikasi
pengelolaan koleksi kartu *trading game* Yu-Gi-Oh!
di mana pengguna dapat menyimpan data koleksi kartu yang 
dimiliki.

Dibuat oleh:
```
Nama   : Muhammad Andhika Prasetya
NPM    : 2206031302
Kelas  : PBP C
```

## Task Checklist 
- [ ] [Tugas 2: Implementasi Model-View-Template (MVT) pada Django](https://pbp-fasilkom-ui.github.io/ganjil-2024/assignments/individual/assignment-2)


# Table of contents  
        
[**Yu-Gi-Oh! Card Collection Project**](<#Yu-Gi-Oh!-Card-Collection-Project>)<br />
&emsp;[**Task Checklist**](<#Task-Checklist>)<br />
[**Table of contents**](<#Table-of-contents>)<br />
[**Tugas 2: Implementasi Model-View-Template (MVT) pada Django**](<#Tugas-2-Implementasi-Model-View-Template-(MVT)-pada-Django>)<br />
&emsp;[**Tugas 2 Checklist**](<#Tugas-2-Checklist>)<br />
&emsp;&emsp;[Membuat proyek Django](<#Membuat-proyek-Django>)<br />
&emsp;&emsp;[Membuat aplikasi dengan nama `main`](<#Membuat-aplikasi-dengan-nama-main>)<br />
&emsp;&emsp;[Melakukan *routing* pada proyek untuk aplikasi `main`](<#Melakukan-routing-pada-proyek-untuk-aplikasi-main>)<br />
&emsp;&emsp;[Membuat model pada aplikasi `main`](<#Membuat-model-pada-aplikasi-main>)<br />
&emsp;&emsp;[Membuat sebuah fungsi pada `views.py` untuk menampilkan nama aplikasi serta nama dan kelas](<#Membuat-sebuah-fungsi-pada-viewspy-untuk-menampilkan-nama-aplikasi-serta-nama-dan-kelas>)<br />
&emsp;&emsp;[Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk `views.py`](<#Membuat-sebuah-routing-pada-urlspy-aplikasi-main-untuk-viewspy>)<br />
&emsp;&emsp;[Melakukan *deployment* ke Adaptable](<#Melakukan-deployment-ke-Adaptable>)<br />
&emsp;&emsp;[Menjawab pertanyaan](<#Menjawab-pertanyaan>)<br />
[**License**](<#License>)<br />

# Tugas 2: Implementasi Model-View-Template (MVT) pada Django
Mengimplementasi Model-View-Template (MVT) Django pada 
[Yu-Gi-Oh! Card Collection Project]() serta menjawab beberapa
pertanyaan yang sudah dipelajari di kelas.

## Tugas 2 Checklist
from [Tugas 2: Implementasi Model-View-Template (MVT) pada Django](https://pbp-fasilkom-ui.github.io/ganjil-2024/assignments/individual/assignment-2)
- [X] Membuat sebuah proyek Django baru.
- [X] Membuat aplikasi dengan nama `main` pada proyek tersebut.
- [X] Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.
- [ ] Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.
    - `name` sebagai nama *item* dengan tipe `CharField`.
    - `amount` sebagai jumlah *item* dengan tipe `IntegerField`.
    - `description` sebagai deskripsi *item* dengan tipe `TextField`.
- [ ] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- [ ] Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
- [ ] Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [ ] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi Adaptable yang sudah di-*deploy*, serta jawaban dari beberapa pertanyaan berikut.
    - Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
    - Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
    - Jelaskan mengapa kita menggunakan ***virtual environment***? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan ***virtual environment***?
    - Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

### Membuat proyek Django dan konfigurasi proyek
Proyek Django bernama `yugioh_card` dibuat dengan menggunakan perintah berikut:
```
django-admin startproject yugioh_card .
```
Lalu menambahkan wildcard `*` pada `ALLOWED_HOSTS` di `yugioh_card/settings.py` untuk keperluan *deployment* seperti berikut ini:
```
...
ALLOWED_HOSTS = ["*"]
...
```
Ini diperlukan agar *deployment* dapat dilakukan dengan mudah,
karena ini memungkinkan aplikasi diakses dari semua *host* yang tersedia.

### Membuat aplikasi dengan nama `main`
Aplikasi baru bernama `main` dibuat dengan menggunakan perintah berikut:
```
py manage.py startapp main
```
Selanjutnya menambahkan `"main"` pada `INSTALLED_APPS` di `yugioh_card/settings.py` untuk mendaftarkan aplikasi pada proyek `yugioh_card` seperti berikut ini:
```
...
INSTALLED_APPS = [
    ...,
    "main",
]
...
```
Dengan ini, aplikasi `main` telah dibuat dan didaftarkan pada proyek `yugioh_card`

### Melakukan *routing* pada proyek untuk aplikasi `main`
Routing pada proyek `yugioh_card` untuk aplikasi `main` dilakukan dengan menambahkan sebuah *path* pada `yugioh_card/urls.py` dengan mengimport `include` dari `django.urls` dan menambahkan *path* "" yang mengarah ke `main.urls` seperti berikut ini:
1. Mengimport `include` dari `django.urls`
```
from django.urls import path, include
```
2. Menambahkan *path* "" yang mengarah ke `main.urls`
```
urlpatterns = [
    ...,
    path("", include("main.urls")),
]
```
Dengan ini, *routing* pada proyek `yugioh_card` untuk aplikasi `main` telah dilakukan.

### Membuat model pada aplikasi `main`

### Membuat sebuah fungsi pada `views.py` untuk menampilkan nama aplikasi serta nama dan kelas

### Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk `views.py`

### Melakukan *deployment* ke Adaptable

### Menjawab pertanyaan


# License  

[MIT](https://choosealicense.com/licenses/mit/)
