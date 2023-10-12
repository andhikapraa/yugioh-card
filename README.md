
# Yu-Gi-Oh! Card Collection Project
![Django version](https://img.shields.io/static/v1?label=Django&message==4.2.5&logo=django&color=092e20)
[![Official Website](https://img.shields.io/static/v1?label=Website&message=pras-yugioh-card.onrender.com&logo=googlechrome&color=blue)](https://pras-yugioh-card.onrender.com/)
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
## Demo
Aplikasi ini dapat diakses melalui [https://pras-yugioh-card.onrender.com/](https://pras-yugioh-card.onrender.com/)

Screenshot:
![Screenshot](https://i.postimg.cc/25stKj25/demo.jpg)
## Task Checklist 
- [X] [Tugas 2: Implementasi Model-View-Template (MVT) pada Django](https://pbp-fasilkom-ui.github.io/ganjil-2024/assignments/individual/assignment-2)
- [X] [Tugas 3: Implementasi Form dan Data Delivery pada Django](https://pbp-fasilkom-ui.github.io/ganjil-2024/assignments/individual/assignment-3)
- [X] [Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django](https://pbp-fasilkom-ui.github.io/ganjil-2024/assignments/individual/assignment-4)
- [X] [Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS](https://pbp-fasilkom-ui.github.io/ganjil-2024/assignments/individual/assignment-5)
- [ ] [Tugas 6: JavaScript dan Asynchronous JavaScript](https://pbp-fasilkom-ui.github.io/ganjil-2024/assignments/individual/assignment-6)

# Table of contents  
        
[**Yu-Gi-Oh! Card Collection Project**](<#Yu-Gi-Oh-Card-Collection-Project>)<br />
&emsp;[**Demo**](<#Demo>)<br />
&emsp;[**Task Checklist**](<#Task-Checklist>)<br />
[**Table of contents**](<#Table-of-contents>)<br />
[**Tugas 2: Implementasi Model-View-Template (MVT) pada Django**](<#Tugas-2-Implementasi-Model-View-Template-MVT-pada-Django>)<br />
&emsp;[**Tugas 2 Checklist**](<#Tugas-2-Checklist>)<br />
&emsp;&emsp;[Membuat proyek Django dan konfigurasi proyek](<#Membuat-proyek-Django-dan-konfigurasi-proyek>)<br />
&emsp;&emsp;[Membuat aplikasi dengan nama `main`](<#Membuat-aplikasi-dengan-nama-main>)<br />
&emsp;&emsp;[Melakukan *routing* pada proyek untuk aplikasi `main`](<#Melakukan-routing-pada-proyek-untuk-aplikasi-main>)<br />
&emsp;&emsp;[Membuat model pada aplikasi `main`](<#Membuat-model-pada-aplikasi-main>)<br />
&emsp;&emsp;[Membuat sebuah fungsi pada `views.py` untuk menampilkan nama aplikasi serta nama dan kelas](<#Membuat-sebuah-fungsi-pada-viewspy-untuk-menampilkan-nama-aplikasi-serta-nama-dan-kelas>)<br />
&emsp;&emsp;[Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk `views.py`](<#Membuat-sebuah-routing-pada-urlspy-aplikasi-main-untuk-viewspy>)<br />
&emsp;&emsp;[Melakukan *deployment* ke ~~Adaptable~~ Render.com](<#Melakukan-deployment-ke-Adaptable-Rendercom>)<br />
&emsp;&emsp;[Membuat Unit *Test* (bonus)](<#Membuat-Unit-Test-bonus>)<br />
&emsp;&emsp;[Menjawab pertanyaan](<#Menjawab-pertanyaan>)<br />
[**Tugas 3: Implementasi Form dan Data Delivery pada Django**](<#Tugas-3-Implementasi-Form-dan-Data-Delivery-pada-Django>)<br />
&emsp;[**Tugas 3 Checklist**](<#Tugas-3-Checklist>)<br />
&emsp;&emsp;[Penyesuaian *template* sebelum membuat *form*](<#Penyesuaian-template-sebelum-membuat-form>)<br />
&emsp;&emsp;[Penyesuaian *model* `Item` sebelum membuat *form*](<#Penyesuaian-model-Item-sebelum-membuat-form>)<br />
&emsp;&emsp;[Penyesuaian Unit *Test* sebelum membuat *form*](<#Penyesuaian-Unit-Test-sebelum-membuat-form>)<br />
&emsp;&emsp;[Membuat *form* untuk menambahkan objek *model* `Item`](<#Membuat-form-untuk-menambahkan-objek-model-Item>)<br />
&emsp;&emsp;[Menambahkan format XML, JSON, XML *by ID*, dan JSON *by ID*](<#Menambahkan-format-XML-JSON-XML-by-ID-dan-JSON-by-ID>)<br />
&emsp;&emsp;[Menambahkan *routing* untuk format XML, JSON, XML *by ID*, dan JSON *by ID*](<#Menambahkan-routing-untuk-format-XML-JSON-XML-by-ID-dan-JSON-by-ID>)<br />
&emsp;&emsp;[Mengakses URL menggunakan Postman](<#Mengakses-URL-menggunakan-Postman>)<br />
&emsp;&emsp;[Menjawab beberapa pertanyaan](<#Menjawab-beberapa-pertanyaan>)<br />
[**Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django**](<#Tugas-4-Implementasi-Autentikasi-Session-dan-Cookies-pada-Django>)<br />
&emsp;[**Tugas 4 Checklist**](<#Tugas-4-Checklist>)<br />
&emsp;&emsp;[Mengimplementasikan fungsi registrasi, login, dan logout](<#Mengimplementasikan-fungsi-registrasi-login-dan-logout>)<br />
&emsp;&emsp;[Menghubungkan model `Item` dengan `User`](<#Menghubungkan-model-Item-dengan-User>)<br />
&emsp;&emsp;[Menerapkan *cookies*](<#Menerapkan-cookies>)<br />
&emsp;&emsp;[Membuat **dua** akun pengguna dengan masing-masing **tiga** *dummy data*](<#Membuat-dua-akun-pengguna-dengan-masing-masing-tiga-dummy-data>)<br />
&emsp;&emsp;[Menambahkan tombol dan fungsi untuk menambahkan `amount` suatu objek sebanyak satu](<#Menambahkan-tombol-dan-fungsi-untuk-menambahkan-amount-suatu-objek-sebanyak-satu>)<br />
&emsp;&emsp;[Menambahkan tombol dan fungsi untuk menghapus suatu objek dari inventori](<#Menambahkan-tombol-dan-fungsi-untuk-menghapus-suatu-objek-dari-inventori>)<br />
&emsp;&emsp;[Menjawab beberapa pertanyaan terkait tugas 4](<#Menjawab-beberapa-pertanyaan-terkait-tugas-4>)<br />
[**Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS**](<#Tugas-5-Desain-Web-menggunakan-HTML-CSS-dan-Framework-CSS>)<br />
&emsp;[**Tugas 5 Checklist**](<#Tugas-5-Checklist>)<br />
&emsp;&emsp;[Kustomisasi *template* `templates/base.html` menggunakan *framework* Bootstrap](<#Kustomisasi-template-templates-base-html-menggunakan-framework-Bootstrap>)<br />
&emsp;&emsp;[Kustomisasi *template* `login.html`, `register.html`, dan `add.html` menggunakan *framework* Bootstrap](<#Kustomisasi-template-loginhtml-registerhtml-dan-addhtml-menggunakan-framework-Bootstrap>)<br />
&emsp;&emsp;[Kustomisasi *template* `index.html` menggunakan *framework* Bootstrap](<#Kustomisasi-template-indexhtml-menggunakan-framework-Bootstrap>)<br />
&emsp;&emsp;[Menjawab pertanyaan terkait tugas 5](<#Menjawab-pertanyaan-terkait-tugas-5>)<br />
[**Tugas 6: JavaScript dan Asynchronous JavaScript**](<#Tugas-6-JavaScript-dan-Asynchronous-JavaScript>)<br />
&emsp;[**Tugas 4 Checklist**](<#Tugas-6-Checklist>)<br />
[**License**](<#License>)<br />


# Tugas 2: Implementasi Model-View-Template (MVT) pada Django
Mengimplementasi Model-View-Template (MVT) Django pada 
[Yu-Gi-Oh! Card Collection Project](https://pras-yugioh-card.onrender.com/) serta menjawab beberapa
pertanyaan yang sudah dipelajari di kelas.

## Tugas 2 Checklist
*from* [Tugas 2: Implementasi Model-View-Template (MVT) pada Django](https://pbp-fasilkom-ui.github.io/ganjil-2024/assignments/individual/assignment-2)
- [X] Membuat sebuah proyek Django baru.
- [X] Membuat aplikasi dengan nama `main` pada proyek tersebut.
- [X] Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.
- [X] Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.
    - `name` sebagai nama *item* dengan tipe `CharField`.
    - `amount` sebagai jumlah *item* dengan tipe `IntegerField`.
    - `description` sebagai deskripsi *item* dengan tipe `TextField`.
- [X] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- [X] Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
- [X] Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [X] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi Adaptable yang sudah di-*deploy*, serta jawaban dari beberapa pertanyaan berikut.
    - Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
    - Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
    - Jelaskan mengapa kita menggunakan ***virtual environment***? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan ***virtual environment***?
    - Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

### Membuat proyek Django dan konfigurasi proyek
Sebelum membuat proyek Django, *virtual environment* bernama `env` dibuat terlebih dahulu dengan menggunakan perintah berikut:
```
python -m venv env
```
Setelah *virtual environment* dibuat, *virtual environment* tersebut di-*activate* dengan menggunakan perintah berikut:
```
env\Scripts\activate.bat
```
> Proses ini dilakukan di Windows. Untuk Linux, perintahnya adalah `source env/bin/activate`.

Setelah *virtual environment* di-*activate*, proyek Django bernama `yugioh_card` dibuat dengan menggunakan perintah berikut:
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
Model `Item` pada aplikasi `main` dibuat dengan menambahkan sebuah *class* `Item` pada `main/models.py`. *Class* `Item` memiliki atribut wajib sebagai berikut:
- `name` sebagai nama kartu dengan tipe `CharField`.
- `amount` sebagai jumlah kartu dengan tipe `IntegerField`.
- `description` sebagai deskripsi kartu dengan tipe `TextField`.

Selanjutnya ada beberapa atribut lain yang ditambahkan agar *class* `Item` dapat berperan sebagai *yugioh card*, yaitu:
- `card_type` sebagai jenis kartu dengan tipe `CharField`.
- `passcode` sebagai kode kartu dengan tipe `IntegerField`.
- `attribute` sebagai atribut kartu dengan tipe `CharField`.
- `types` sebagai tipe kartu monster dengan tipe `CharField`.
- `level` sebagai level kartu monster dengan tipe `IntegerField`.
- `atk` sebagai nilai serangan kartu monster dengan tipe `IntegerField`.
- `deff` sebagai nilai pertahanan kartu monster dengan tipe `IntegerField`.
- `effect_type` sebagai jenis efek kartu dengan tipe `CharField`.
- `card_property` sebagai sifat kartu dengan tipe `CharField`.
- `rulings` sebagai aturan kartu dengan tipe `TextField`.
- `image_url` sebagai URL gambar kartu dengan tipe `CharField`.

Berikut ini adalah *class* `Item` yang telah dibuat:
```
class Item(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    description = models.TextField()
    card_type = models.CharField(max_length=200)
    passcode = models.IntegerField()
    attribute = models.CharField(max_length=200, null=True)
    types = models.CharField(max_length=200, null=True)
    level = models.IntegerField(null=True)
    atk = models.IntegerField(null=True)
    deff = models.IntegerField(null=True)
    effect_type = models.CharField(max_length=200, null=True)
    card_property = models.CharField(max_length=200, null=True)
    rulings = models.TextField(null=True)
    image_url = models.CharField(max_length=200, null=True)
    
```
Beberapa atribut memiliki nilai `null=True` karena tidak semua kartu memiliki atribut tersebut. Sebagai contoh, kartu monster memiliki atribut `attribute`, `types`, `level`, `atk`, dan `deff`, sedangkan kartu *spell* dan *trap* tidak memiliki atribut tersebut. Dengan ini, *class* `Item` dapat berperan sebagai *yugioh card*.
> Setelah *class* `Item` dibuat, *migration* di-*skip* terlebih dahulu karena berkas `urls.py` belum dibuat. *Migration* dapat dilakukan setelah *routing* selesai dibuat.

### Membuat sebuah fungsi pada `views.py` untuk menampilkan nama aplikasi serta nama dan kelas
Sebelum membuat sebuah fungsi pada `views.py`, *template* `main/templates/index.html` dibuat terlebih dahulu. *Template* `main/templates/index.html` berisi *heading* yang menampilkan nama aplikasi serta nama dan kelas. Berikut ini adalah *template* `main/templates/index.html` yang telah dibuat:
```
<h1><span style="color:orange">{{ project }}</span></h1>

<h2>Name: <span style="color:blue">{{ name }}</span></h2>
<h2>NPM: <span style="color:red">{{ npm }}</span></h2>
<h2>Class: <span style="color:blue">{{ class }}</span></h2>
```
Setelah *template* `main/templates/index.html` dibuat, sebuah fungsi bernama `index` dibuat pada `views.py` untuk mengembalikan *template* `main/templates/index.html` yang telah dibuat. Berikut ini adalah fungsi `index` yang telah dibuat:
```
def index(request):
    context = {
        "project": "Yu-Gi-Oh! Card Collection",
        "name": "Muhammad Andhika Prasetya",
        "npm": "2206031302",
        "class": "PBP C",
    }
    return render(request, "index.html", context)
```
Setelah fungsi `index` dibuat, *routing* pada `urls.py` dapat dilakukan.

### Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk `views.py`
*Routing* pada `urls.py` aplikasi `main` untuk `views.py` dilakukan dengan menambahkan sebuah *path* yang mengarah ke fungsi `index` pada `main/urls.py`. Namun sebelumnya, *import* terlebih dahulu `views` dari `main` setelah *import* `path` dari `django.urls`. Berikut ini adalah *import* yang telah dilakukan:
```
from django.urls import path
from . import views
```
Setelah *import* dilakukan, *path* yang mengarah ke fungsi `index` pada `main/urls.py` dapat dibuat. Tak lupa untuk menambahkan `app_name` agar *path* dapat diakses dengan menggunakan *namespace* `main`. Berikut ini adalah *path* yang telah dibuat:
```
app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
]
```
Setelah *path* dibuat, *migration* dapat dilakukan untuk membuat tabel `Item` pada basis data. *Migration* dilakukan dengan menggunakan perintah berikut:
```
py manage.py makemigrations
```
Setelah *migration* selesai dibuat, tabel `Item` dapat dibuat pada basis data dengan menggunakan perintah berikut:
```
py manage.py migrate
```
Setelah tabel `Item` dibuat, *routing* pada `urls.py` proyek `yugioh_card` dapat dilakukan. Dengan ini, *routing* pada proyek `yugioh_card` telah selesai dilakukan.

### Melakukan *deployment* ke ~~Adaptable~~ [Render.com](https://render.com/)
> Untuk sementara, *deployment* dilakukan ke render.com karena Adaptable sedang mengalami gangguan.

*Deployment* ke ~~Adaptable~~ [Render.com](https://render.com/) dilakukan dengan mengikuti [tutorial](https://render.com/docs/deploy-django) yang telah disediakan. Berikut ini adalah langkah-langkah yang dilakukan:
1. Membuat berkas `render.yaml` pada direktori utama dengan isi sebagai berikut:
```
services:
  - type: web
    name: pras-yugioh-card
    runtime: python
    region: singapore
    plan: free
    branch: main
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python manage.py migrate && gunicorn yugioh_card.wsgi"
```
2. Membuat berkas `requirements.txt` pada direktori utama dengan isi sebagai berikut:
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
3. Membuka halaman [Render.com](https://render.com/) dan melakukan *login* ke *dashboard*.
4. Pada halaman [*dashboard*](https://dashboard.render.com/), masuk ke halaman [*Blueprints*](https://dashboard.render.com/blueprints), lalu klik `*New Blueprint Instance*`.
5. Klik `*Connect*` pada repo `yugioh_card` dari akun GitHub.
6. Isi nama *blueprint* dengan `pras-yugioh-blueprints`.
7. Klik `*Apply*` untuk membuat *blueprint* dan memulai *deployment*.
> Berikut ada *link* *step-by-step* untuk melakukan *deployment* ke render.com: [ScribeHow](https://scribehow.com/shared/Create_a_new_blueprint_instance_for_Yu-Gi-Oh_Card_deployment__8aTrTrdTRu-4EyzVmKQ3hQ)

Screenshot *deployment* ke ~~Adaptable~~ [Render.com](https://render.com/) dapat dilihat pada gambar berikut ini:
![Deployment](https://i.postimg.cc/NGrMLP1R/successfully-deployed.png)

Dengan ini, *deployment* ke ~~Adaptable~~ [Render.com](https://render.com/) telah selesai dilakukan dan aplikasi dapat diakses melalui [https://pras-yugioh-card.onrender.com/](https://pras-yugioh-card.onrender.com/).

### Membuat Unit *Test* (bonus)
Unit *test* dibuat dengan menambahkan sebuah *class* `MainTestCase` pada `main/tests.py`. *Class* `MainTestCase` memiliki sebuah *method* `test_index` yang menguji apakah *template* `main/templates/index.html` dapat diakses dengan benar. Berikut ini adalah *class* `MainTestCase` yang telah dibuat:
```
class MainTestCase(TestCase):
    def test_index(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "Yu-Gi-Oh! Card Collection")
        self.assertContains(response, "Muhammad Andhika Prasetya")
        self.assertContains(response, "2206031302")
        self.assertContains(response, "PBP C")
```
> Sebelumnya, *import* terlebih dahulu `TestCase` dan `Client` dari `django.test`.

Setelah *class* `MainTestCase` dibuat, buat *class* `ItemTestCase` pada `main/tests.py`. *Class* `ItemTestCase` memiliki sebuah *method* `test_item` yang menguji apakah *class* `Item` dapat berperan sebagai *yugioh card* dengan benar. Berikut ini adalah *class* `ItemTestCase` yang telah dibuat:
```
class ItemTestCase(TestCase):
    def test_item(self):
        item = Item.objects.create(
            name="Blue-Eyes White Dragon",
            amount=3,
            description="This legendary dragon is a powerful engine of destruction. Virtually invincible, very few have faced this awesome creature and lived to tell the tale.",
            card_type="Monster",
            passcode=89631139,
            attribute="LIGHT",
            types="Dragon/Normal",
            level=8,
            atk=3000,
            deff=2500,
            effect_type="Normal",
            card_property="Normal",
            rulings="This card is treated as a 'Blue-Eyes' monster.",
            image_url="https://static.wikia.nocookie.net/yugioh/images/6/a0/BlueEyesWhiteDragon-MP22-EN-PScR-1E.png",
        )
        self.assertEqual(item.name, "Blue-Eyes White Dragon")
        self.assertEqual(item.amount, 3)
        self.assertEqual(item.description, "This legendary dragon is a powerful engine of destruction. Virtually invincible, very few have faced this awesome creature and lived to tell the tale.")
        self.assertEqual(item.card_type, "Monster")
        self.assertEqual(item.passcode, 89631139)
        self.assertEqual(item.attribute, "LIGHT")
        self.assertEqual(item.types, "Dragon/Normal")
        self.assertEqual(item.level, 8)
        self.assertEqual(item.atk, 3000)
        self.assertEqual(item.deff, 2500)
        self.assertEqual(item.effect_type, "Normal")
        self.assertEqual(item.card_property, "Normal")
        self.assertEqual(item.rulings, "This card is treated as a 'Blue-Eyes' monster.")
```
> Sebelumnya, *import* terlebih dahulu `Item` dari `main.models`.

Setelah *class* `ItemTestCase` dibuat, lakukan *test* dengan menggunakan perintah berikut:
```
py manage.py test
```
Berikut ini adalah hasil *test* yang telah dilakukan:
```
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.038s

OK
Destroying test database for alias 'default'...
```

Dengan ini, unit *test* telah selesai dibuat dan berhasil dijalankan.

### Menjawab pertanyaan
#### Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
![Bagan](https://i.postimg.cc/HnvCZbQq/Bagaimana-Django-Framework-Bekerja.jpg)

#### Jelaskan mengapa kita menggunakan ***virtual environment***? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan ***virtual environment***?
***Virtual environment*** digunakan dalam pengembangan *software* seperti aplikasi web berbasis Django dengan tujuan sebagai berikut:
1. Memisahkan *dependencies* dari proyek yang sedang dikembangkan dengan *dependencies* dari proyek lain. Dengan ini, *dependencies* dari proyek yang sedang dikembangkan tidak akan berbenturan dengan *dependencies* dari proyek lain yang mungkin memiliki versi *dependencies* yang berbeda.
2. Memudahkan dalam mengelola *dependencies* dari proyek yang sedang dikembangkan. Dengan menggunakan *virtual environment*, *dependencies* dari proyek yang sedang dikembangkan dapat di-*install* dan di-*uninstall* dengan mudah. Sehingga, *environment* dari proyek yang sedang dikembangkan dapat di-*setup* atau di-*reproduce* dengan mudah.
3. Memudahkan dalam memindahkan proyek yang sedang dikembangkan ke *host* lain. Dengan menggunakan *virtual environment*, *dependencies* dari proyek yang sedang dikembangkan dapat di-*install* dengan mudah di *host* lain tanpa khawatir akan adanya benturan *dependencies*.
4. Memudahkan untuk me-*manage* versi Python yang digunakan. Dengan menggunakan *virtual environment*, versi Python yang digunakan dapat berbeda-beda untuk setiap proyek yang sedang dikembangkan. Ini memungkinkan untuk menggunakan versi Python yang berbeda-beda sesuai dengan kebutuhan proyek yang sedang dikembangkan.

Meskipun kita dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*, namun akan lebih baik jika kita menggunakan *virtual environment* karena *virtual environment* memiliki banyak keuntungan seperti yang telah dijelaskan di atas. Hal ini akan membantu dalam menjaga kestabilan proyek yang sedang dikembangkan.

#### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC, MVT, dan MVVM adalah tiga pola arsitektur perangkat lunak yang umum digunakan untuk memisahkan logika aplikasi dari tampilan. Perbedaan dari ketiganya adalah sebagai berikut:
- MVC (*Model-View-Controller*) memisahkan aplikasi menjadi tiga komponen utama, yaitu *model*, *view*, dan *controller*. *Model* berisi data dan logika aplikasi, *view* berisi tampilan aplikasi, dan *controller* berisi logika aplikasi untuk menghubungkan *model* dan *view*. Keuntungan dari MVC adalah terdapat pemisahan yang jelas antara logika aplikasi dan tampilan, sehingga proses pengembangan dapat dilakukan dengan lebih terstruktur dan mudah.
- MVT (*Model-View-Template*) memisahkan aplikasi menjadi tiga bagian, yaitu *model*, *view*, dan *template*. *Model* berisi data dan logika aplikasi, *view* berisi logika aplikasi untuk menghubungkan *model* dan *template*, dan *template* berisi tampilan aplikasi. Perbedaan utama MVT dengan MVC adalah penggunaan *template* pada MVT sebagai komponen terpisah yang memisahkan logika aplikasi dan tampilan.
- MVVM (*Model-View-ViewModel*) memisahkan aplikasi menjadi tiga bagian, yaitu *model*, *view*, dan *view model*. *Model* berisi data dan logika aplikasi, *view* berisi tampilan aplikasi, dan *view model* berisi logika aplikasi untuk menghubungkan *model* dan *view*. Perbedaan utama MVVM dengan MVC/MVT adalah penggunaan *view model* pada MVVM sebagai layer tambahan yang memisahkan *model* dan *view*, sehingga memungkinkan pemisahan yang lebih jelas antara logika aplikasi dan tampilan.

Secara umum, ketiganya memiliki fungsi yang sama, yaitu memisahkan logika aplikasi dari tampilan. Namun, perbedaan utama ketiganya adalah pada cara bagaimana komponen-komponen tersebut diorganisir dan berinteraksi satu sama lain.

# Tugas 3: Implementasi Form dan Data Delivery pada Django
Mengimplementasi Form dan Data Delivery pada [Yu-Gi-Oh! Card Collection Project](https://pras-yugioh-card.onrender.com/) serta menjawab beberapa pertanyaan serta menerapkan beberapa *best practice* yang sudah dipelajari di kelas.

## Tugas 3 Checklist
*from* [Tugas 3: Implementasi Form dan Data Delivery pada Django](https://pbp-fasilkom-ui.github.io/ganjil-2024/assignments/individual/assignment-3)
- [X] Membuat input `form` untuk menambahkan objek model pada app sebelumnya.
- [X] Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML *by ID*, dan JSON *by ID*.
- [X] Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.
- [X] Menjawab beberapa pertanyaan berikut pada `README.md` pada *root folder*.
    - [X] Apa perbedaan antara form `POST` dan form `GET` dalam Django?
    - [X] Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    - [X] Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    - [X] Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
- [X] Mengakses kelima URL di poin 2 menggunakan Postman, membuat *screenshot* dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md`.
- [X] Melakukan `add`-`commit`-`push` ke GitHub.

### Penyesuaian *template* sebelum membuat *form*
Sebelum membuat *form*, kerangka *views* perlu dibuat untuk memastikan adanya konsistensi dalam desain situs web yang dibuat serta memperkecil kemungkinan terjadinya redundansi kode. Langkah-langkah yang dilakukan adalah sebagai berikut:
1. Membuat *base template* `/templates/base.html` yang berfungsi sebagai kerangka dari seluruh halaman situs web dengan isi sebagai berikut:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >
        <title>{% block title %}{% endblock %}</title>
        <meta content="{% block description %}{% endblock %}" name="description">
        {% block head %}{% endblock %}
    </head>

    <body>
        <header>
            <h1><span style="color:orange">Yu-Gi-Oh! Card Collection</span></h1>
        </header>

        <main>
            {% block content %}{% endblock %}
        </main>

        <footer>
            <p>&copy; 2023 Muhammad Andhika Prasetya - 2206031302 - PBP C</p>
        </footer>
    </body>
</html>
```
2. Memodifikasi berkas `yugioh_card/settings.py` dengan memodifikasi `TEMPLATES` dan menambahkan `templates` pada `DIRS` seperti berikut:
```
...
TEMPLATES = [
    {
        ...,
        "DIRS": [BASE_DIR / "templates"],
        ...
    },
]
...
```
3. Memodifikasi berkas `main/views.py` dengan menghapus `context` pada fungsi `index` dan mengubah `render` menjadi `render(request, "index.html")` seperti berikut:
```
...
def index(request):
    return render(request, "index.html")
...
```
4. Memodifikasi *template* `main/templates/index.html` dengan meng-*extend* *base template* `/templates/base.html` dan menghapus *heading* yang menampilkan nama aplikasi serta nama dan kelas. Berikut ini adalah *template* `main/templates/index.html` yang telah dimodifikasi:
```
{% extends "base.html" %}

{% block title %}Yu-Gi-Oh! Card Collection{% endblock %}

{% block description %}Yu-Gi-Oh! Card Collection is a website to collect Yu-Gi-Oh! cards.{% endblock %}

{% block content %}
    <h2>Home</h2>
{% endblock %}
```

### Penyesuaian *model* `Item` sebelum membuat *form*
Sebelum membuat *form* untuk menambahkan objek *model* `Item`, *model* `Item` perlu disesuaikan terlebih dahulu. *Model* `Item` disesuaikan dengan mengganti atribut `image_url` dengan `image` yang bertipe `ImageField` pada *model* `Item`. Atribut `image` bertipe `ImageField` ditambahkan agar dapat menyimpan gambar kartu yang di-*upload* oleh pengguna. Berikut ini adalah *model* `Item` yang telah disesuaikan:
```
class Item(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    description = models.TextField()
    card_type = models.CharField(max_length=200)
    passcode = models.IntegerField()
    attribute = models.CharField(max_length=200, null=True)
    types = models.CharField(max_length=200, null=True)
    level = models.IntegerField(null=True)
    atk = models.IntegerField(null=True)
    deff = models.IntegerField(null=True)
    effect_type = models.CharField(max_length=200, null=True)
    card_property = models.CharField(max_length=200, null=True)
    rulings = models.TextField(null=True)
    image = models.ImageField(upload_to="images/", null=True)
```
Selain itu, *module* `PIL` perlu di-*install* terlebih dahulu agar dapat menggunakan `ImageField` dengan menambahkan `pillow` pada `requirements.txt`. Setelah `pillow` ditambahkan pada `requirements.txt`, *virtual environment* perlu di-*update* dengan menggunakan perintah berikut:
```
pip install -r requirements.txt
```
Setelah *virtual environment* di-*update*, *migration* perlu dilakukan untuk membuat tabel `Item` pada basis data. *Migration* dilakukan dengan menggunakan perintah berikut:
```
py manage.py makemigrations
```
Setelah *migration* selesai dibuat, tabel `Item` dapat dibuat pada basis data dengan menggunakan perintah berikut:
```
py manage.py migrate
```
Setelah tabel `Item` dibuat, *model* `Item` telah disesuaikan dan siap digunakan.

### Penyesuaian Unit *Test* sebelum membuat *form*
Sebelum membuat *form* untuk menambahkan objek *model* `Item`, unit *test* perlu disesuaikan terlebih dahulu. Unit *test* disesuaikan dengan mengganti atribut `image_url` dengan `image` yang bertipe `ImageField` pada *class* `ItemTestCase`. Berikut ini adalah *class* `ItemTestCase` yang telah disesuaikan:
```
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from .models import Item

...

class ItemTestCase(TestCase):
    def test_item(self):
        item = Item.objects.create(
            ...,
            image=SimpleUploadedFile(
                name='BlueEyesWhiteDragon.webp',
                content=open('static/images/BlueEyesWhiteDragon.webp', 'rb').read(),
                content_type='image/webp'
            ),
        )
        ...,
        self.assertRegex(item.image.url, r"^/media/images/BlueEyesWhiteDragon.*.webp$")
        item.image.delete() # delete image after test to avoid cluttering the media folder
```

### Membuat *form* untuk menambahkan objek *model* `Item`
*Form* untuk menambahkan objek *model* `Item` dibuat dengan membuat berkas `main/forms.py` yang berisi *class* `ItemForm` yang merupakan *subclass* dari `forms.ModelForm`. *Class* `ItemForm` memiliki *field* `image` yang bertipe `forms.ImageField` agar dapat menyimpan gambar kartu yang di-*upload* oleh pengguna. Berikut ini adalah berkas `main/forms.py` yang telah dibuat:
```
from django.forms import ModelForm
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
```
Setelah berkas `main/forms.py` dibuat, *form* untuk menambahkan objek *model* `Item` dapat dibuat pada `main/templates/add.html`. *Form* untuk menambahkan objek *model* `Item` dibuat dengan menggunakan *template* `main/templates/add.html` yang berisi *form* untuk menambahkan objek *model* `Item`. Selain itu, tambahkan pula *link* menuju *home* serta menambahkan *image* dari objek *model* `Item` yang telah ditambahkan dalam bentuk *card*. Berikut ini adalah *template* `main/templates/add.html` yang telah dimodifikasi:
```
{% extends "base.html" %}

{% block title %}Add Item{% endblock %}

{% block description %}Add a new item to the collection.{% endblock %}

{% block content %}
    <h2>Add Item</h2>
    <a href="{% url "main:index" %}">Home</a>
    <br></br>
    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input type="submit" value="Add Item" /></td>
        </table>
    </form>
    <br></br>
    {% for item in items %}
        <div style="border: 1px solid black; padding: 10px; margin: 10px;">
            <h3>{{ item.name }}</h3>
            <p>Amount: {{ item.amount }}</p>
            <p>Description: {{ item.description }}</p>
            <p>Card Type: {{ item.card_type }}</p>
            <p>Passcode: {{ item.passcode }}</p>
            <p>Attribute: {{ item.attribute }}</p>
            <p>Types: {{ item.types }}</p>
            <p>Level: {{ item.level }}</p>
            <p>ATK: {{ item.atk }}</p>
            <p>DEFF: {{ item.deff }}</p>
            <p>Effect Type: {{ item.effect_type }}</p>
            <p>Card Property: {{ item.card_property }}</p>
            <p>Rulings: {{ item.rulings }}</p>
            <img src="{{ item.image.url }}" alt="{{ item.name }}" width="200px">
        </div>
    {% endfor %}
{% endblock %}
```
Setelah *form* untuk menambahkan objek *model* `Item` dibuat, fungsi `add` pada `main/views.py` perlu dibuat terlebih dahulu. Fungsi `add` dibuat dengan menambahkan sebuah fungsi bernama `add` pada `main/views.py` yang mengembalikan *template* `main/templates/add.html` dan menerima *request* sebagai parameter. Selain itu, fungsi `add` juga memiliki *conditional* yang mengecek apakah *request* yang diterima adalah *POST request* atau bukan. Jika *request* yang diterima adalah *POST request*, maka fungsi `add` akan meng-*handle* *POST request* tersebut dengan menggunakan *form* yang telah dibuat sebelumnya. Selain itu, tak lupa untuk meng-*import* `ItemForm` dari `.forms` pada `main/views.py` dan `redirect` dari `django.shortcuts` dan menambahkan *model* `Item` dari `.models` pada `main/views.py`. Berikut ini adalah fungsi `add` yang telah dibuat:
```
from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item

...

def add(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("main:index")
    else:
        form = ItemForm()
    context = {
        "form": form,
        "items": Item.objects.all(),
    }
    return render(request, "add.html", context)
```
Setelah fungsi `add` dibuat, *routing* pada `urls.py` aplikasi `main` untuk `views.py` perlu dibuat terlebih dahulu. *Routing* pada `urls.py` aplikasi `main` untuk `views.py` dilakukan dengan menambahkan sebuah *path* yang mengarah ke fungsi `add` pada `main/urls.py`. Berikut ini adalah *path* yang telah dibuat:
```
urlpatterns = [
    ...,
    path("add/", views.add, name="add"),
]
```
Setelah *routing* pada `urls.py` aplikasi `main` untuk `views.py` dibuat, *template* `main/templates/index.html` perlu dimodifikasi terlebih dahulu. *Template* `main/templates/index.html` dimodifikasi dengan menambahkan *button* menuju *form* untuk menambahkan objek *model* `Item` serta menampilkan *image* dari objek *model* `Item` yang telah ditambahkan dalam bentuk *card*. Berikut ini adalah *template* `main/templates/index.html` yang telah dimodifikasi:
```
{% extends "base.html" %}

{% block title %}Yu-Gi-Oh! Card Collection{% endblock %}

{% block description %}Yu-Gi-Oh! Card Collection is a website to collect Yu-Gi-Oh! cards.{% endblock %}

{% block content %}
    <h2>Home</h2>
    <a href="{% url "main:add" %}">
        <button>Add Card</button>
    </a>
    {% for item in items %}
        <div style="border: 1px solid black; padding: 10px; margin: 10px;">
            <h3>{{ item.name }}</h3>
            <p>Amount: {{ item.amount }}</p>
            <p>Description: {{ item.description }}</p>
            <p>Card Type: {{ item.card_type }}</p>
            <p>Passcode: {{ item.passcode }}</p>
            <p>Attribute: {{ item.attribute }}</p>
            <p>Types: {{ item.types }}</p>
            <p>Level: {{ item.level }}</p>
            <p>ATK: {{ item.atk }}</p>
            <p>DEFF: {{ item.deff }}</p>
            <p>Effect Type: {{ item.effect_type }}</p>
            <p>Card Property: {{ item.card_property }}</p>
            <p>Rulings: {{ item.rulings }}</p>
            <img src="{{ item.image.url }}" alt="{{ item.name }}" width="200px">
        </div>
    {% endfor %}
{% endblock %}
```
Setelah *template* `main/templates/add.html` dimodifikasi, fungsi `index` pada `main/views.py` perlu dimodifikasi terlebih dahulu. Fungsi `index` dimodifikasi dengan menambahkan *model* `Item` dari `.models` pada `main/views.py`. Berikut ini adalah fungsi `index` yang telah dimodifikasi:
```
...
def index(request):
    context = {
        "items": Item.objects.all(),
    }
    return render(request, "index.html", context)
...
```
Setelah fungsi `index` dimodifikasi, berkas `settings.py` perlu dimodifikasi terlebih dahulu. Berkas `settings.py` dimodifikasi dengan menambahkan `MEDIA_ROOT` dan `MEDIA_URL` pada `settings.py` seperti berikut:
```
...
# Media files (Images)
# https://docs.djangoproject.com/en/4.2/topics/files/

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
```
Selain itu, berkas `urls.py` perlu dimodifikasi dengan menambahkan `static` dan `settings` dari `django.conf` pada `urls.py` dan menambahkan `static` dan `media` pada `urlpatterns` pada `urls.py` seperti berikut:
```
...
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...,
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
Setelah berkas `settings.py` dan `urls.py` dimodifikasi, *migration* perlu dilakukan untuk membuat tabel `Item` pada basis data. *Migration* dilakukan dengan menggunakan perintah berikut:
```
py manage.py makemigrations
```
Setelah *migration* selesai dibuat, tabel `Item` dapat dibuat pada basis data dengan menggunakan perintah berikut:
```
py manage.py migrate
```
Setelah tabel `Item` dibuat, *form* untuk menambahkan objek *model* `Item` telah selesai dibuat dan siap digunakan.

### Menambahkan format XML, JSON, XML *by ID*, dan JSON *by ID*
Untuk menambahkan format XML, JSON, XML *by ID*, dan JSON *by ID*, berkas `views.py` perlu dimodifikasi terlebih dahulu. Berkas `views.py` dimodifikasi dengan menambahkan `HttpResponse` dari `django.http` dan `serializers` dari `django.core` pada `views.py` dan menambahkan fungsi `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` pada `views.py`. Berikut ini adalah berkas `views.py` yang telah dimodifikasi:
```
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .forms import ItemForm
from .models import Item

...

def show_xml(request):
    items = Item.objects.all()
    data = serializers.serialize("xml", items)
    return HttpResponse(data, content_type="application/xml")

def show_json(request):
    items = Item.objects.all()
    data = serializers.serialize("json", items)
    return HttpResponse(data, content_type="application/json")

def show_xml_by_id(request, id):
    item = Item.objects.get(id=id)
    data = serializers.serialize("xml", [item])
    return HttpResponse(data, content_type="application/xml")

def show_json_by_id(request, id):
    item = Item.objects.get(id=id)
    data = serializers.serialize("json", [item])
    return HttpResponse(data, content_type="application/json")
```
Dengan ini telah dibuat fungsi `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` yang mengembalikan *response* dalam format XML, JSON, XML *by ID*, dan JSON *by ID*.

### Menambahkan *routing* untuk format XML, JSON, XML *by ID*, dan JSON *by ID*
Setelah berkas `views.py` dimodifikasi, *routing* pada `urls.py` aplikasi `main` perlu dimodifikasi. *Routing* pada `urls.py` aplikasi `main` dilakukan dengan menambahkan beberapa *path* yang mengarah ke fungsi `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` pada `main/urls.py`. Berikut ini adalah *path* yang telah dibuat:
```
urlpatterns = [
    ...,
    path("xml/", views.show_xml, name="show_xml"),
    path("json/", views.show_json, name="show_json"),
    path("xml/<int:id>/", views.show_xml_by_id, name="show_xml_by_id"),
    path("json/<int:id>/", views.show_json_by_id, name="show_json_by_id"),
]
```
Setelah *routing* pada `urls.py` aplikasi `main` dibuat, *template* `main/templates/index.html` perlu dimodifikasi terlebih dahulu. *Template* `main/templates/index.html` dimodifikasi dengan menambahkan *link* menuju *page* untuk melihat objek yang telah ditambahkan dalam format XML, JSON, XML *by ID*, dan JSON *by ID*. Berikut ini adalah *template* `main/templates/index.html` yang telah dimodifikasi:
```
{% extends "base.html" %}

{% block title %}Yu-Gi-Oh! Card Collection{% endblock %}

{% block description %}Yu-Gi-Oh! Card Collection is a website to collect Yu-Gi-Oh! cards.{% endblock %}

{% block content %}
    <h2>Home</h2>
    <a href="{% url "main:add" %}">
        <button>Add Card</button>
    </a>
    <a href="{% url "main:show_xml" %}">
        <button>Show XML</button>
    </a>
    <a href="{% url "main:show_json" %}">
        <button>Show JSON</button>
    </a>
    {% for item in items %}
        <div style="border: 1px solid black; padding: 10px; margin: 10px;">
            <h3>{{ item.name }}</h3>
            <p>Amount: {{ item.amount }}</p>
            <p>Description: {{ item.description }}</p>
            <p>Card Type: {{ item.card_type }}</p>
            <p>Passcode: {{ item.passcode }}</p>
            <p>Attribute: {{ item.attribute }}</p>
            <p>Types: {{ item.types }}</p>
            <p>Level: {{ item.level }}</p>
            <p>ATK: {{ item.atk }}</p>
            <p>DEFF: {{ item.deff }}</p>
            <p>Effect Type: {{ item.effect_type }}</p>
            <p>Card Property: {{ item.card_property }}</p>
            <p>Rulings: {{ item.rulings }}</p>
            <img src="{{ item.image.url }}" alt="{{ item.name }}" width="200px">
            <a href="{% url "main:show_xml_by_id" item.id %}">
                <button>Show XML by ID</button>
            </a>
            <a href="{% url "main:show_json_by_id" item.id %}">
                <button>Show JSON by ID</button>
            </a>
        </div>
    {% endfor %}
{% endblock %}
```
Setelah *template* `main/templates/index.html` dimodifikasi, *template* `main/templates/add.html` juga perlu dimodifikasi. *Template* `main/templates/add.html` dimodifikasi dengan menambahkan *link* menuju *page* untuk melihat objek yang telah ditambahkan dalam format XML, JSON, XML *by ID*, dan JSON *by ID*. Berikut ini adalah *template* `main/templates/add.html` yang telah dimodifikasi:
```
{% extends "base.html" %}

{% block title %}Add Item{% endblock %}

{% block description %}Add a new item to the collection.{% endblock %}

{% block content %}
    <h2>Add Item</h2>
    <a href="{% url "main:index" %}">Home</a>
    <a href="{% url "main:show_xml" %}">
        <button>Show XML</button>
    </a>
    <a href="{% url "main:show_json" %}">
        <button>Show JSON</button>
    </a>
    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input type="submit" value="Add Item" /></td>
        </table>
    </form>
    <br></br>
    {% for item in items %}
        <div style="border: 1px solid black; padding: 10px; margin: 10px;">
            <h3>{{ item.name }}</h3>
            <p>Amount: {{ item.amount }}</p>
            <p>Description: {{ item.description }}</p>
            <p>Card Type: {{ item.card_type }}</p>
            <p>Passcode: {{ item.passcode }}</p>
            <p>Attribute: {{ item.attribute }}</p>
            <p>Types: {{ item.types }}</p>
            <p>Level: {{ item.level }}</p>
            <p>ATK: {{ item.atk }}</p>
            <p>DEFF: {{ item.deff }}</p>
            <p>Effect Type: {{ item.effect_type }}</p>
            <p>Card Property: {{ item.card_property }}</p>
            <p>Rulings: {{ item.rulings }}</p>
            <img src="{{ item.image.url }}" alt="{{ item.name }}" width="200px">
            <a href="{% url "main:show_xml_by_id" item.id %}">
                <button>Show XML by ID</button>
            </a>
            <a href="{% url "main:show_json_by_id" item.id %}">
                <button>Show JSON by ID</button>
            </a>
        </div>
    {% endfor %}
{% endblock %}
```
Setelah *template* `main/templates/add.html` dimodifikasi, maka format XML, JSON, XML *by ID*, dan JSON *by ID* telah berhasil ditambahkan.

### Mengakses URL menggunakan Postman
Setelah format XML, JSON, XML *by ID*, dan JSON *by ID* berhasil ditambahkan, URL dapat diakses menggunakan Postman. Berikut ini adalah *screenshot* dari hasil akses URL menggunakan Postman:
- *Screenshot* dari hasil akses URL `/` menggunakan Postman
![HTML](https://i.postimg.cc/jj5Q1qSc/html.png)
- *Screenshot* dari hasil akses URL `/xml/` menggunakan Postman
![XML](https://i.postimg.cc/L5dthzBQ/xml.png)
- *Screenshot* dari hasil akses URL `/json/` menggunakan Postman
![JSON](https://i.postimg.cc/nLPYf8sJ/json.png)
- *Screenshot* dari hasil akses URL `/xml/1/` menggunakan Postman
![XML by ID](https://i.postimg.cc/sxppWvTj/xmlid.png)
- *Screenshot* dari hasil akses URL `/json/1/` menggunakan Postman
![JSON by ID](https://i.postimg.cc/SsYLyZ8z/jsonid.png)

### Menjawab beberapa pertanyaan
#### Apa perbedaan antara form `POST` dan form `GET` dalam Django?
Form `POST` dan `GET` merupakan dua metode HTTP yang paling umum digunakan untuk mengirimkan data dari *client* ke *server*. Perbedaan antara form `POST` dan form `GET` dalam Django adalah sebagai berikut:
- Form `POST` digunakan untuk mengirimkan data dari *client* ke *server* dengan cara menyembunyikan data yang dikirimkan dari *client* ke *server*. Dalam Django, kita dapat mengakses data yang dikirimkan dari *client* ke *server* dengan menggunakan `request.POST`. Form `POST` digunakan untuk mengirimkan data yang bersifat sensitif seperti *password* dan data yang bersifat rahasia lainnya karena data yang dikirimkan dari *client* ke *server* tidak dapat dilihat oleh *client*, sehingga data yang dikirimkan dari *client* ke *server* tidak dapat disadap oleh pihak ketiga. Form `POST` juga digunakan untuk mengirimkan data yang berukuran besar dan dapat mengirimkan data dengan tipe *file*.
- Form `GET` digunakan untuk mengambil data dari *server* dengan cara menampilkan data yang diambil dari *server* ke *client*. Dalam Django, kita dapat mengakses data yang diambil dari *server* ke *client* dengan menggunakan `request.GET`. Form `GET` digunakan untuk mengambil data yang bersifat publik seperti *search query* dan *filter* karena data yang diambil tampak pada *URL* dan dapat dilihat oleh *client*. Form `GET` juga digunakan untuk mengambil data yang berukuran kecil karena data yang diambil tidak dapat berukuran lebih dari 2048 karakter dan form ini tidak dapat mengirimkan data dengan tipe *file*.

Dalam Django, baik form `POST` maupun form `GET` dapat digunakan untuk mengirimkan data dari *client* ke *server* dan mengambil data dari *server* ke *client*. Namun, form `POST` lebih sering digunakan untuk mengirimkan data dari *client* ke *server* karena form `POST` dapat mengirimkan data yang bersifat sensitif dan berukuran besar serta dapat mengirimkan data dengan tipe *file*. Sedangkan, form `GET` lebih sering digunakan untuk mengambil data dari *server* ke *client* karena form `GET` dapat mengambil data yang bersifat publik dan berukuran kecil.


#### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML (*eXtensible Markup Language*), JSON (*JavaScript Object Notation*), dan HTML (*HyperText Markup Language*) adalah format yang umum digunakan untuk menyimpan dan mengirimkan data. Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data adalah sebagai berikut:
- XML adalah format yang digunakan untuk menyimpan dan mengirimkan data di berbagai aplikasi atau platform dengan cara yang terstandarisasi. XML menyimpan data dalam struktur *tree* dengan *namespace* untuk kategori data berbeda yang dapat diakses dengan menggunakan *parser* XML sehingga dapat digunakan untuk menyimpan dan mengirimkan data yang bersifat kompleks dan memiliki struktur yang kompleks. XML juga dapat digunakan untuk menyimpan dan mengirimkan data yang bersifat publik dan bersifat rahasia. Penggunaan *parser* XML untuk mengakses data XML membutuhkan waktu yang lama sehingga XML tidak cocok digunakan untuk menyimpan dan mengirimkan data yang bersifat sederhana dan memiliki struktur yang sederhana. Namun XML mendukung semua tipe data JSON dan tipe data yang tidak didukung oleh JSON seperti *date* dan *time*.
- JSON juga merupakan format serialisasi data yang memungkinkan pertukaran data di berbagai platform. JSON menggunakan struktur seperti *map* dengan *key* dan *value* sehingga dapat diuraikan dengan lebih mudah dan cepat dibandingkan XML. Pada umumnya, JSON merupakan pilihan yang lebih baik untuk API, *mobile application*, dan *web application* karena JSON lebih mudah dibaca dan lebih ringan dibandingkan XML. Namun, JSON tidak mendukung beberapa tipe data tertentu seperti *Boolean*, *date*, *time*, *image*, dan lain-lain.
- HTML adalah bahasa yang digunakan untuk membuat struktur dan presentasi halaman web. HTML memiliki *tag* standar yang harus digunakan oleh semua orang, sehingga HTML sulit digunakan untuk menyimpan dan mengirimkan data yang bersifat kompleks dan memiliki struktur yang kompleks. HTML biasanya digunakan untuk menampilkan data yang telah disimpan dan dikirimkan menggunakan XML atau JSON. Berbeda dengan XML dan JSON yang menggunakan pengetikan statis, HTML menggunakan pengetikan dinamis sehingga HTML dapat digunakan untuk membuat halaman web yang interaktif.

Dari penjelasan di atas, dapat disimpulkan bahwa XML, JSON, dan HTML memiliki perbedaan utama dalam konteks pengiriman data. XML digunakan untuk menyimpan dan mengirimkan data yang bersifat kompleks dan memiliki struktur yang kompleks, JSON digunakan untuk menyimpan dan mengirimkan data yang bersifat sederhana dan memiliki struktur yang sederhana, dan HTML digunakan untuk menampilkan data yang telah disimpan dan dikirimkan menggunakan XML atau JSON.

#### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON adalah format data berbasis teks yang paling populer dalam menyimpan dan mentransfer data. Beberapa alasan utama mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern adalah sebagai berikut:
- JSON memiliki struktur data yang sederhana dan mudah dipahami berdasarkan struktur *map* dengan *key* dan *value* sehingga JSON lebih mudah dibaca oleh manusia dan lebih mudah diuraikan oleh komputer dibandingkan XML.
- JSON lebih ringkas dan efisien dibandingkan XML karena tidak memerlukan *tag* untuk menyimpan data. Ini menghasilkan ukuran berkas yang lebih kecil dan waktu *loading* yang lebih cepat.
- JSON didukung oleh hampir semua bahasa pemrograman dan *framework* sehingga JSON dapat digunakan untuk menyimpan dan mentransfer data di berbagai aplikasi atau platform.
- JSON mendukung tipe data yang paling umum digunakan seperti *string* dan *number* sehingga JSON dapat digunakan untuk menyimpan dan mentransfer data yang bersifat sederhana dan memiliki struktur yang sederhana.

Namun, perlu diingat bahwa JSON memiliki beberapa keterbatasan seperti tidak mendukung beberapa tipe data tertentu, tidak memiliki skema sehingga tidak dapat memvalidasi data, dan tidak memiliki dukungan *namespace* sehingga tidak dapat mengelompokkan data. Oleh karena itu, JSON tidak cocok digunakan untuk menyimpan dan mentransfer data yang bersifat kompleks dan memiliki struktur yang kompleks.

### Menambahkan pesan total kartu
Sebelum melanjutkan ke tugas berikutnya, berkas `main/templates/index.html` perlu dimodifikasi terlebih dahulu. Berkas `main/templates/index.html` dimodifikasi dengan menambahkan *heading* yang menampilkan total kartu yang telah ditambahkan. Berikut ini adalah *template* `main/templates/index.html` yang telah dimodifikasi:
```
...
    {% if items %}
        <h3>Total Cards: {{ items|length }}</h3>
    {% endif %}
...
```
Setelah *template* `main/templates/index.html` dimodifikasi, *template* `main/templates/add.html` juga perlu dimodifikasi. Berkas `main/templates/add.html` dimodifikasi dengan menambahkan *heading* yang menampilkan total kartu yang telah ditambahkan. Berikut ini adalah *template* `main/templates/add.html` yang telah dimodifikasi:
```
...
    {% if items %}
        <h3>Total Cards: {{ items|length }}</h3>
    {% endif %}
...
```

# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django
Mengimplementasikan autentikasi, session, dan cookies pada [Yu-Gi-Oh! Card Collection Project](https://pras-yugioh-card.onrender.com/) serta menjawab beberapa pertanyaan serta menerapkan beberapa *best practice* yang sudah dipelajari di kelas.

## Tugas 4 Checklist
*from* [Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django](https://pbp-fasilkom-ui.github.io/ganjil-2024/assignments/individual/assignment-4)
- [X] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
- [X] Membuat **dua** akun pengguna dengan masing-masing **tiga** *dummy data* menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun **di lokal**.
- [X] Menghubungkan model `Item` dengan `User`.
- [X] Menampilkan detail informasi pengguna yang sedang *logged in* seperti *username* dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi.
- [X] Menjawab beberapa pertanyaan berikut pada `README.md` pada *root folder* (silakan modifikasi `README.md` yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).

    - [X] Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
    - [X] Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
    - [X] Apa itu *cookies* dalam konteks aplikasi web, dan bagaimana Django menggunakan *cookies* untuk mengelola data sesi pengguna?
    - [X] Apakah penggunaan *cookies* aman secara *default* dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
    - [X] Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
- [X] Melakukan `add`-`commit`-`push` ke GitHub.
- [X] **Bonus**
    - [X] Tambahkan tombol dan fungsi untuk menambahkan `amount` suatu objek sebanyak satu dan tombol untuk mengurangi jumlah stok suatu objek sebanyak satu.
    - [X] Tambahkan tombol dan fungsi untuk menghapus suatu objek dari inventori.

### Mengimplementasikan fungsi registrasi, login, dan logout
Sebelum melanjutkan ke tugas berikutnya, berkas `main/templates/base.html` perlu dimodifikasi terlebih dahulu. Berkas `main/templates/base.html` dimodifikasi dengan menambahkan *link* menuju *page* untuk melakukan registrasi, login, dan logout. Berikut ini adalah *template* `main/templates/base.html` yang telah dimodifikasi:
```
...
<a href="{% url "main:index" %}">
    <button>Home</button>
</a>
{% if user.is_authenticated %}
    <a href="{% url "main:logout" %}">
        <button>Logout</button>
    </a>
{% else %}
    <a href="{% url "main:register" %}">
        <button>Register</button>
    </a>
    <a href="{% url "main:login" %}">
        <button>Login</button>
    </a>
{% endif %}
...
```
Setelah *template* `main/templates/base.html` dimodifikasi, *template* `main/templates/register.html` perlu dibuat terlebih dahulu. *Template* `main/templates/register.html` dibuat dengan menggunakan *template* `main/templates/base.html` yang telah dibuat sebelumnya. Selain itu, tambahkan pula *form* untuk melakukan registrasi. Berikut ini adalah *template* `main/templates/register.html` yang telah dibuat:
```
{% extends "base.html" %}

{% block title %}Register{% endblock %}

{% block description %}Register to Yu-Gi-Oh! Card Collection.{% endblock %}

{% block content %}
    <h2>Register</h2>
    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input type="submit" value="Register" /></td>
        </table>
    </form>

    <p>Already have an account? <a href="{% url "main:login" %}">Login</a></p>
{% endblock %}
```
Selanjutnya, *template* `main/templates/login.html` perlu dibuat terlebih dahulu. *Template* `main/templates/login.html` dibuat dengan menggunakan *template* `main/templates/base.html` yang telah dibuat sebelumnya. Selain itu, tambahkan pula *form* untuk melakukan login. Berikut ini adalah *template* `main/templates/login.html` yang telah dibuat:
```
{% extends "base.html" %}

{% block title %}Login{% endblock %}

{% block description %}Login to Yu-Gi-Oh! Card Collection.{% endblock %}

{% block content %}
    <h2>Login</h2>
    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input type="submit" value="Login" /></td>
        </table>
    </form>

    {% if messages %}
        {% for message in messages %}
            <p>{{ message }}</p>
        {% endfor %}
    {% endif %}

    <p>Don't have an account? <a href="{% url "main:register" %}">Register</a></p>
{% endblock %}
```
Setelah *template* `main/templates/login.html` dibuat, fungsi `register`, `login_user`, dan `logout_user` pada `main/views.py` perlu dibuat terlebih dahulu. Fungsi `register`, `login_user`, dan `logout_user` dibuat dengan menambahkan sebuah fungsi bernama `register`, `login_user`, dan `logout_user` pada `main/views.py` yang mengembalikan *template* `main/templates/register.html`, `main/templates/login.html`, dan `main/templates/index.html` serta menerima *request* sebagai parameter. Selain itu, fungsi `register`, `login_user`, dan `logout_user` juga memiliki *conditional* yang mengecek apakah *request* yang diterima adalah *POST request* atau bukan. Jika *request* yang diterima adalah *POST request*, maka fungsi `register`, `login_user`, dan `logout_user` akan meng-*handle* *POST request* tersebut dengan menggunakan *form* yang telah dibuat sebelumnya. Selain itu, tak lupa untuk meng-*import* `UserCreationForm` dari `django.contrib.auth.forms` pada `main/views.py` dan `redirect` dari `django.shortcuts` dan menambahkan `authenticate` dan `login_user` dari `django.contrib.auth` pada `main/views.py`. Berikut ini adalah fungsi `register`, `login_user`, dan `logout_user` yang telah dibuat:
```
...
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

...

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + user)
            return redirect("main:index")
    else:
        form = UserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Successfully logged in as " + user.username)
                return redirect("main:index")
        else:
            messages.info(request, "Username OR password is incorrect")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect("main:index")
```
Selanjutnya, *url* pada `main/urls.py` perlu dimodifikasi terlebih dahulu. *URL* pada `main/urls.py` dimodifikasi dengan menambahkan beberapa *path* yang mengarah ke fungsi `register`, `login_user`, dan `logout_user` pada `main/urls.py`. Berikut ini adalah *path* yang telah dibuat:
```
urlpatterns = [
    ...,
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
]
```
Setelah *url* pada `main/urls.py` dimodifikasi, *template* `main/templates/index.html` perlu dimodifikasi terlebih dahulu. *Template* `main/templates/index.html` dimodifikasi dengan menambahkan *heading* yang menampilkan *username* dari pengguna yang sedang *logged in*. Berikut ini adalah *template* `main/templates/index.html` yang telah dimodifikasi:
```
...
{% if user.is_authenticated %}
    <h3>User: {{ user.username }}</h3>
{% endif %}
...
```
Dengan ini, implementasi fungsi registrasi, login, dan logout telah selesai dilakukan.


### Menghubungkan model `Item` dengan `User`
Selanjutnya, model `Item` perlu dimodifikasi terlebih dahulu. Model `Item` dimodifikasi dengan menambahkan *field* `user` yang merupakan *foreign key* dari `User` pada `main/models.py`. Berikut ini adalah model `Item` yang telah dimodifikasi:
```
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    ...
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
Setelah model `Item` dimodifikasi, *migration* perlu dilakukan untuk membuat tabel `Item` pada basis data. *Migration* dilakukan dengan menggunakan perintah berikut:
```
py manage.py makemigrations
```
Setelah *migration* selesai dibuat, tabel `Item` dapat dibuat pada basis data dengan menggunakan perintah berikut:
```
py manage.py migrate
```
Setelah tabel `Item` dibuat, *form* untuk menambahkan objek *model* `Item` perlu dimodifikasi terlebih dahulu. *Form* untuk menambahkan objek *model* `Item` dimodifikasi dengan menambahkan *field* `user` yang merupakan *foreign key* dari `User` pada `main/forms.py`. Berikut ini adalah *form* untuk menambahkan objek *model* `Item` yang telah dimodifikasi:
```
...
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        exclude = ["user"]
```
Setelah *form* untuk menambahkan objek *model* `Item` dimodifikasi, fungsi `add` pada `main/views.py` perlu dimodifikasi terlebih dahulu. Fungsi `add` dimodifikasi dengan menambahkan *field* `user` yang merupakan *foreign key* dari `User` pada `main/views.py` dan di-*restrict* hanya untuk pengguna yang sedang *logged in*. Berikut ini adalah fungsi `add` yang telah dimodifikasi:
```
from django.contrib.auth.decorators import login_required
...
@login_required(login_url="/login/")
def add(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect("main:index")
    else:
        form = ItemForm()
    context = {
        "form": form,
        "items": Item.objects.all(),
        "user": request.user,
    }
    return render(request, "add.html", context)
```
Setelah fungsi `add` pada `main/views.py` dimodifikasi, *template* `main/templates/add.html` perlu dimodifikasi terlebih dahulu. *Template* `main/templates/add.html` dimodifikasi dengan menambahkan *heading* yang menampilkan *username* dari pengguna yang sedang *logged in*. Berikut ini adalah *template* `main/templates/add.html` yang telah dimodifikasi:
```
...
<h3>User: {{ user.username }}</h3>
...
```
Selain itu, *template* `main/templates/index.html` juga perlu dimodifikasi agar pengguna yang belum *login* tidak dapat melihat *button* `Add Card` dan *table* `Item`. *Template* `main/templates/index.html` dimodifikasi dengan menambahkan *conditional* yang mengecek apakah pengguna yang sedang mengakses *page* tersebut sudah *login* atau belum. Jika pengguna yang sedang mengakses *page* tersebut belum *login*, maka *button* `Add Card` dan *table* `Item` tidak akan ditampilkan. Berikut ini adalah *template* `main/templates/index.html` yang telah dimodifikasi:
```
...
    {% if user.is_authenticated %}
        <h3>User: {{ user.username }}</h3>
        <a href="{% url "main:add" %}">
            <button>Add Card</button>
        </a>
        <a href="{% url "main:show_xml" %}">
            <button>Show XML</button>
        </a>
        <a href="{% url "main:show_json" %}">
            <button>Show JSON</button>
        </a>
        {% if items %}
            <h3>Total Cards: {{ items|length }}</h3>
        {% endif %}
        {% for item in items %}
            <div style="border: 1px solid black; padding: 10px; margin: 10px;">
                <h3>{{ item.name }}</h3>
                <p>Amount: {{ item.amount }}</p>
                <p>Description: {{ item.description }}</p>
                <p>Card Type: {{ item.card_type }}</p>
                <p>Passcode: {{ item.passcode }}</p>
                <p>Attribute: {{ item.attribute }}</p>
                <p>Types: {{ item.types }}</p>
                <p>Level: {{ item.level }}</p>
                <p>ATK: {{ item.atk }}</p>
                <p>DEFF: {{ item.deff }}</p>
                <p>Effect Type: {{ item.effect_type }}</p>
                <p>Card Property: {{ item.card_property }}</p>
                <p>Rulings: {{ item.rulings }}</p>
                <img src="{{ item.image.url }}" alt="{{ item.name }}" width="200px">
                <a href="{% url "main:show_xml_by_id" item.id %}">
                    <button>Show XML by ID</button>
                </a>
                <a href="{% url "main:show_json_by_id" item.id %}">
                    <button>Show JSON by ID</button>
                </a>
            </div>
        {% endfor %}
    {% endif %}
...
```
Selanjutnya, fungsi-fungsi pada `main/views.py` perlu dimodifikasi terlebih dahulu agar data yang tampil hanya data milik pengguna yang sedang *login*. Berikut ini adalah fungsi-fungsi pada `main/views.py` yang telah dimodifikasi:
```
...
def index(request):
    if request.user.is_authenticated:
        items = Item.objects.filter(user=request.user)
    else:
        items = []
    context = {
        "items": items,
    }
    return render(request, "index.html", context)

@login_required(login_url="/login/")
def add(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect("main:index")
    else:
        form = ItemForm()
    context = {
        "form": form,
        "items": Item.objects.filter(user=request.user),
        "user": request.user,
    }
    return render(request, "add.html", context)

@login_required(login_url="/login/")
def show_xml(request):
    items = Item.objects.filter(user=request.user)
    data = serializers.serialize("xml", items)
    return HttpResponse(data, content_type="application/xml")

@login_required(login_url="/login/")
def show_json(request):
    items = Item.objects.filter(user=request.user)
    data = serializers.serialize("json", items)
    return HttpResponse(data, content_type="application/json")

@login_required(login_url="/login/")
def show_xml_by_id(request, id):
    item = Item.objects.get(id=id)
    if item.user != request.user:
        return redirect("main:index")
    data = serializers.serialize("xml", [item])
    return HttpResponse(data, content_type="application/xml")

@login_required(login_url="/login/")
def show_json_by_id(request, id):
    item = Item.objects.get(id=id)
    if item.user != request.user:
        return redirect("main:index")
    data = serializers.serialize("json", [item])
    return HttpResponse(data, content_type="application/json")
...
```
Dengan ini, model `Item` telah terhubung dengan `User`.

### Menerapkan *cookies*
Selanjutnya, *view* `login_user` pada `main/views.py` perlu dimodifikasi terlebih dahulu. *View* `login_user` dimodifikasi dengan menambahkan *cookies* `last_login` yang menampilkan waktu terakhir pengguna melakukan *login* pada *template* `main/templates/index.html`. Berikut ini adalah *view* `login_user` yang telah dimodifikasi:
```
from django.utils import timezone
...
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Successfully logged in as " + user.username)
                request.session["last_login"] = str(timezone.now())
                return redirect("main:index")
        else:
            messages.info(request, "Username OR password is incorrect")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "login.html", context)
```
Lalu, *heading* yang menampilkan waktu terakhir pengguna melakukan *login* ditambahkan pada *template* `main/templates/index.html` dan `main/templates/add.html` dengan menggunakan kode berikut:
```
<h3>Last Login: {{ request.session.last_login }}</h3>
```
Dengan ini, *cookies* `last_login` telah berhasil ditambahkan.

### Membuat **dua** akun pengguna dengan masing-masing **tiga** *dummy data*
Sebelum melanjutkan ke tugas berikutnya, *database* perlu di-*reset* terlebih dahulu. *Database* di-*reset* dengan menggunakan perintah berikut:
```
py manage.py flush
```
Setelah itu, dua akun pengguna dengan masing-masing tiga *dummy data* perlu dibuat secara manual. Akun pengguna dengan tiga *dummy data* dibuat dengan menggunakan *form* yang telah dibuat sebelumnya. Berikut ini adalah *screenshot* dari hasil pembuatan dua akun pengguna dengan masing-masing tiga *dummy data*:
- *Screenshot* dari hasil pembuatan akun pengguna dengan tiga *dummy data* pertama
![User 1](https://i.postimg.cc/902tnDcg/user1.png)
- *Screenshot* dari hasil pembuatan akun pengguna dengan tiga *dummy data* kedua
![User 2](https://i.postimg.cc/d1rj62cT/user2.png)

### Menambahkan tombol dan fungsi untuk menambahkan `amount` suatu objek sebanyak satu
Sebelum melanjutkan, *template* `main/templates/index.html` perlu dimodifikasi terlebih dahulu. Berkas `main/templates/index.html` dimodifikasi dengan menambahkan *button* `Add Amount` yang mengarah ke *page* `main:add_amount` dan *button* `Reduce Amount` yang mengarah ke *page* `main:reduce_amount`. Berikut ini adalah *template* `main/templates/index.html` yang telah dimodifikasi:
```
...
{% for item in items %}
    <div style="border: 1px solid black; padding: 10px; margin: 10px;">
        <h3>{{ item.name }}</h3>
        <p>Amount: {{ item.amount }}</p>
        <p>Description: {{ item.description }}</p>
        <p>Card Type: {{ item.card_type }}</p>
        <p>Passcode: {{ item.passcode }}</p>
        <p>Attribute: {{ item.attribute }}</p>
        <p>Types: {{ item.types }}</p>
        <p>Level: {{ item.level }}</p>
        <p>ATK: {{ item.atk }}</p>
        <p>DEFF: {{ item.deff }}</p>
        <p>Effect Type: {{ item.effect_type }}</p>
        <p>Card Property: {{ item.card_property }}</p>
        <p>Rulings: {{ item.rulings }}</p>
        <img src="{{ item.image.url }}" alt="{{ item.name }}" width="200px">
        <a href="{% url "main:show_xml_by_id" item.id %}">
            <button>Show XML by ID</button>
        </a>
        <a href="{% url "main:show_json_by_id" item.id %}">
            <button>Show JSON by ID</button>
        </a>
        {% if item.amount > 0 %}
            <a href="{% url "main:add_amount" item.id %}">
                <button>Add Amount</button>
            </a>
        {% endif %}
        {% if item.amount > 1 %}
            <a href="{% url "main:reduce_amount" item.id %}">
                <button>Reduce Amount</button>
            </a>
        {% endif %}
    </div>
{% endfor %}
...
```
> Hal ini juga dilakukan pada *template* `main/templates/add.html`.

Selanjutnya, fungsi `add_amount` dan `reduce_amount` pada `main/views.py` perlu dibuat. Fungsi `add_amount` dan `reduce_amount` dibuat dengan menambahkan sebuah fungsi bernama `add_amount` dan `reduce_amount` pada `main/views.py` yang mengembalikan *template* `main/templates/index.html` serta menerima *request* dan `id` sebagai parameter. Selain itu, fungsi `add_amount` dan `reduce_amount` juga memiliki *conditional* yang mengecek apakah *user* sudah *login* atau belum. Jika *user* sudah *login*, maka fungsi `add_amount` dan `reduce_amount` akan meng-*handle* *request* tersebut dengan menambahkan atau mengurangi `amount` suatu objek sebanyak satu. Berikut ini adalah fungsi `add_amount` dan `reduce_amount` yang telah dibuat:
```
...
@login_required(login_url="/login/")
def add_amount(request, id):
    item = Item.objects.get(id=id)
    if item.user == request.user:
        item.amount += 1
        item.save()
        return redirect("main:index")
    return render(request, "index.html")

@login_required(login_url="/login/")
def reduce_amount(request, id):
    item = Item.objects.get(id=id)
    if item.user == request.user:
        item.amount -= 1
        item.save()
        return redirect("main:index")
    return render(request, "index.html")
```
Setelah fungsi `add_amount` dan `reduce_amount` pada `main/views.py` dibuat, *url* pada `main/urls.py` perlu dimodifikasi terlebih dahulu. *URL* pada `main/urls.py` dimodifikasi dengan menambahkan beberapa *path* yang mengarah ke fungsi `add_amount` dan `reduce_amount` pada `main/urls.py`. Berikut ini adalah *path* yang telah dibuat:
```
urlpatterns = [
    ...,
    path("add_amount/<int:id>", views.add_amount, name="add_amount"),
    path("reduce_amount/<int:id>", views.reduce_amount, name="reduce_amount"),
]
```
Dengan ini, tombol dan fungsi untuk menambahkan `amount` suatu objek sebanyak satu telah berhasil ditambahkan.

### Menambahkan tombol dan fungsi untuk menghapus suatu objek dari inventori
Sebelum melanjutkan, *template* `main/templates/index.html` perlu dimodifikasi terlebih dahulu. Berkas `main/templates/index.html` dimodifikasi dengan menambahkan *button* `Delete Card` yang mengarah ke *page* `main:delete` dan *button* `Delete All Cards` yang mengarah ke *page* `main:delete_all`. Berikut ini adalah *template* `main/templates/index.html` yang telah dimodifikasi:
```
...
{% if items %}
    <h3>Total Cards: {{ items|length }}</h3>
    <a href="{% url "main:delete_all" %}">
        <button>Delete All Cards</button>
    </a>
{% endif %}
...
{% for item in items %}
    <div style="border: 1px solid black; padding: 10px; margin: 10px;">
        <h3>{{ item.name }}</h3>
        <p>Amount: {{ item.amount }}</p>
        <p>Description: {{ item.description }}</p>
        <p>Card Type: {{ item.card_type }}</p>
        <p>Passcode: {{ item.passcode }}</p>
        <p>Attribute: {{ item.attribute }}</p>
        <p>Types: {{ item.types }}</p>
        <p>Level: {{ item.level }}</p>
        <p>ATK: {{ item.atk }}</p>
        <p>DEFF: {{ item.deff }}</p>
        <p>Effect Type: {{ item.effect_type }}</p>
        <p>Card Property: {{ item.card_property }}</p>
        <p>Rulings: {{ item.rulings }}</p>
        <img src="{{ item.image.url }}" alt="{{ item.name }}" width="200px">
        <a href="{% url "main:show_xml_by_id" item.id %}">
            <button>Show XML by ID</button>
        </a>
        <a href="{% url "main:show_json_by_id" item.id %}">
            <button>Show JSON by ID</button>
        </a>
        {% if item.amount > 0 %}
            <a href="{% url "main:add_amount" item.id %}">
                <button>Add Amount</button>
            </a>
        {% endif %}
        {% if item.amount > 1 %}
            <a href="{% url "main:reduce_amount" item.id %}">
                <button>Reduce Amount</button>
            </a>
        {% endif %}
        <a href="{% url "main:delete" item.id %}">
            <button>Delete Card</button>
        </a>
    </div>
{% endfor %}
...
```
> Hal ini juga dilakukan pada *template* `main/templates/add.html`.

Selanjutnya, fungsi `delete` dan `delete_all` pada `main/views.py` perlu dibuat. Fungsi `delete` dibuat dengan menambahkan sebuah fungsi bernama `delete` dan `delete_all` pada `main/views.py` yang mengembalikan *template* `main/templates/index.html`. Selain itu, fungsi `delete` dan `delete_all` juga memiliki *conditional* yang mengecek apakah *user* sudah *login* atau belum. Jika *user* sudah *login*, maka fungsi `delete` dan `delete_all` akan meng-*handle* *request* tersebut dengan menghapus objek *model* `Item` yang memiliki `id` yang sama dengan `id` yang diterima. Berikut ini adalah fungsi `delete` dan `delete_all` yang telah dibuat:
```
...
@login_required(login_url="/login/")
def delete(request, id):
    item = Item.objects.get(id=id)
    if item.user == request.user:
        item.delete()
        return redirect("main:index")
    return render(request, "index.html")

@login_required(login_url="/login/")
def delete_all(request):
    items = Item.objects.filter(user=request.user)
    items.delete()
    return render(request, "index.html")

```
Setelah fungsi `delete` dan `delete_all` pada `main/views.py` dibuat, *url* pada `main/urls.py` perlu dimodifikasi terlebih dahulu. *URL* pada `main/urls.py` dimodifikasi dengan menambahkan beberapa *path* yang mengarah ke fungsi `delete` dan `delete_all` pada `main/urls.py`. Berikut ini adalah *path* yang telah dibuat:
```
urlpatterns = [
    ...,
    path("delete/<int:id>", views.delete, name="delete"),
    path("delete_all/", views.delete_all, name="delete_all"),
]
```
Dengan ini, tombol dan fungsi untuk menghapus suatu objek dari inventori telah berhasil ditambahkan.

### Menjawab beberapa pertanyaan terkait tugas 4
#### Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
Django `UserCreationForm` adalah formulir yang digunakan untuk membuat pengguna baru yang dapat menggunakan aplikasi web kita. Formulir ini memiliki tiga bidang: `username`, `password1`, dan `password2` (yang pada dasarnya digunakan untuk konfirmasi password). Untuk menggunakan `UserCreationForm`, kita perlu mengimpornya dari `django.contrib.auth.forms`.
Kelebihan `UserCreationForm` diantaranya:
- Formulir ini sudah disediakan oleh Django, sehingga kita tidak perlu membuatnya dari awal.
- Formulir ini sudah memiliki validasi dan sanitasi data yang diperlukan, sehingga kita tidak perlu khawatir tentang keamanan dan integritas data.
- Formulir ini sudah terintegrasi dengan sistem autentikasi Django, sehingga kita dapat dengan mudah membuat pengguna yang dapat login dan logout.
- Formulir ini sudah memiliki *error handling* yang baik, sehingga kita dapat dengan mudah mengetahui kesalahan yang terjadi.

Kekurangan `UserCreationForm` diantaranya:
- Formulir ini hanya memiliki bidang username, password1, dan password2, sehingga kita tidak dapat menambahkan bidang lain yang mungkin dibutuhkan oleh aplikasi kita, seperti email, nama lengkap, atau foto profil.
- Formulir ini menggunakan model pengguna bawaan Django, sehingga kita tidak dapat mengubah atau menyesuaikan atribut pengguna sesuai dengan kebutuhan kita.
- Formulir ini mungkin tidak cocok dengan tampilan atau gaya aplikasi kita, sehingga kita perlu mengubah atau menyesuaikan template HTML dan CSS yang digunakan oleh formulir ini.

#### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi adalah proses memverifikasi identitas pengguna, yaitu untuk mengidentifikasi siapa pengguna yang mencoba mengakses aplikasi web. Autentikasi digunakan untuk memeriksa apakah pengguna yang mencoba mengakses aplikasi adalah pengguna yang sah atau bukan. Sebagai contoh, proses login adalah contoh autentikasi. Ketika pengguna memasukkan kredensial mereka (seperti nama pengguna dan kata sandi), sistem memverifikasi apakah kredensial tersebut sesuai dengan yang ada dalam basis data. Jika cocok, pengguna dianggap terotentikasi dan dapat mengakses sumber daya yang terlindungi.

Sementara itu, otorisasi adalah proses mengendalikan akses pengguna yang sudah terotentikasi ke sumber daya atau fungsi tertentu dalam aplikasi. Ini menentukan apa yang diizinkan atau tidak diizinkan untuk dilakukan oleh pengguna yang terotentikasi. Misalnya, seorang pengguna yang terotentikasi mungkin memiliki izin untuk mengedit profil mereka sendiri, tetapi tidak diberi izin untuk mengedit profil pengguna lain. Ini adalah contoh dari otorisasi yang mengatur apa yang dapat dilakukan pengguna setelah mereka masuk.

Baik autentikasi maupun otorisasi sama-sama penting dalam aplikasi web. Autentikasi merupakan langkah pertama dalam proses keamanan. Autentikasi memastikan bahwa pengguna yang mencoba mengakses sumber daya adalah pengguna yang sah. Tanpa autentikasi, sistem tidak akan dapat membedakan antara pengguna sah dan aktor jahat yang mencoba mendapatkan akses. Jadi, autentikasi penting untuk memverifikasi identitas pengguna dan mencegah akses yang tidak sah. Setelah pengguna berhasil terotentikasi, langkah selanjutnya adalah menentukan apa yang pengguna tersebut diizinkan untuk lakukan. Ini adalah di mana otorisasi masuk. Otorisasi memungkinkan sistem untuk mengendalikan akses ke sumber daya atau fitur tertentu berdasarkan peran atau hak akses pengguna. Dengan otorisasi, aplikasi dapat memastikan bahwa pengguna hanya mengakses data atau fitur yang seharusnya mereka akses, dan mencegah akses yang tidak sah ke data atau fitur yang sensitif.

#### Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Dalam konteks aplikasi web, cookies adalah potongan kecil data yang dikirim dari sebuah website dan disimpan di komputer pengguna oleh browser web pengguna saat pengguna berselancar. Cookie ini dirancang untuk menjadi mekanisme yang andal bagi website untuk mengingat informasi stateful atau untuk merekam aktivitas penelusuran pengguna.

Django menggunakan cookies untuk mengelola data sesi pengguna dengan cara menyimpan ID sesi pengguna di cookie. Django kemudian menggunakan ID sesi ini untuk mengidentifikasi pengguna yang terotentikasi dan mengambil data sesi pengguna dari basis data sesi. Dengan menggunakan cookies, Django dapat mengelola data sesi pengguna tanpa menyimpan data sesi pengguna di cookie itu sendiri. Hal ini memungkinkan Django untuk mengelola data sesi pengguna dengan aman dan efisien.

#### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookie dalam pengembangan web memiliki manfaat dan risiko yang perlu dipertimbangkan. Secara default, cookie tidak dianggap sebagai ancaman untuk privasi dan keamanan website, karena tidak menyimpan data pribadi (tetapi terkadang mereka menyimpan nomor kartu kredit dan alamat IP) dan tidak bisa digunakan untuk mengirim malware atau virus. Namun, cookie dapat menimbulkan risiko keamanan bila digunakan secara tidak benar, misalnya dengan menyimpan informasi sensitif tanpa enkripsi atau dengan membiarkan cookie pihak ketiga mengakses data pengguna. Cookie juga dapat mempengaruhi kinerja situs web, karena meningkatkan data yang dikirim antara browser pengguna dan server web. Selain itu, cookie dapat menimbulkan masalah kompatibilitas, karena tidak semua browser menangani cookie dengan cara yang sama, dan beberapa pengguna mungkin memilih untuk menonaktifkan cookie sepenuhnya.

Oleh karena itu, pengembang web perlu mengikuti praktik terbaik untuk mengelola cookie, seperti menggunakan cookie hanya untuk tujuan yang diperlukan, mengatur masa berlaku cookie yang sesuai, mengenkripsi data cookie yang sensitif, membatasi akses cookie pihak ketiga, dan memberikan informasi dan pilihan kepada pengguna tentang penggunaan cookie. Dengan demikian, penggunaan cookie dalam pengembangan web dapat memberikan manfaat bagi pengalaman pengguna tanpa mengorbankan privasi dan keamanan mereka.


# Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS
Mengimplementasi desain web menggunakan HTML, CSS dan framework CSS (Bootstrap, Tailwind, Bulma, dll) dengan memperhatikan *best practices* dan *design principles*.

## Tugas 5 Checklist
*from* [Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS](https://pbp-fasilkom-ui.github.io/ganjil-2024/assignments/individual/assignment-5)
- [X] Kustomisasi desain pada template HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut
    - [X] Kustomisasi halaman *login*, *register*, dan tambah inventori semenarik mungkin.
    - [X] Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan *apporach* lain seperti menggunakan **Card**. 

- [X] Menjawab beberapa pertanyaan berikut pada `README.md` pada *root folder* (silakan modifikasi `README.md` yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
    - [X] Jelaskan manfaat dari setiap *element selector* dan kapan waktu yang tepat untuk menggunakannya. 
    - [X] Jelaskan HTML5 Tag yang kamu ketahui.
    - [X] Jelaskan perbedaan antara *margin* dan *padding*.
    - [X] Jelaskan perbedaan antara *framework* CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
    - [X] Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
- [X] Melakukan `add`-`commit`-`push` ke GitHub.
- [X] **Bonus**: Memberikan warna yang berbeda (teks atau background) pada baris terakhir dari *item* pada inventori anda **menggunakan CSS**.

### Kustomisasi *template* `templates/base.html` menggunakan *framework* Bootstrap
Sebelum melanjutkan, *template* `templates/base.html` perlu dimodifikasi terlebih dahulu. *Template* `templates/base.html` dimodifikasi dengan menambahkan *link* ke *framework* Bootstrap pada `templates/base.html`. Berikut ini adalah *template* `templates/base.html` yang telah dimodifikasi:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
    ...
    <!-- Bootstrap CSS & JS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
    ...
    </head>
...
</html>
```
Selanjunya pada bagian `body`, bagian `header` dan `main` akan dilebur menjadi satu bagian `navbar` yang bersamaan dengan `footer` akan dikustomisasi menggunakan *framework* Bootstrap. Berikut ini adalah bagian `body` yang telah dimodifikasi:
```
...
<nav class="navbar navbar-expand-lg sticky-top" data-bs-theme="dark" style="background-color: #001427;">
    <div class="container-fluid">
        <a class="navbar-brand" href="{% url "main:index" %}">
            Yu-Gi-Oh! Card Collection
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarDark" aria-controls="navbarDark" aria-expanded="false" aria-label="Toggle navigation" style="background-color: #001427;">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarDark">
            <ul class="navbar-nav flex-row flex-wrap bd-navbar-nav">
                <li class="nav-item">
                    <a href="{% url "main:index" %}" class="nav-link">Home</a>
                </li>
                {% if user.is_authenticated %}
                    <li class="nav-item">
                        <a href="{% url "main:add" %}" class="nav-link">Add Card</a>
                    </li>
                {% endif %}
            </ul>
            <ul class="navbar-nav flex-row flex-wrap ms-md-auto">
                {% if user.is_authenticated %}
                    <li class="nav-item">
                        <button class="btn btn-outline-danger" type="button" onclick="location.href='{% url "main:logout" %}'">Logout</button>
                    </li>
                {% else %}
                    <li class="nav-item">
                        <button class="btn btn-outline-success me-2" type="button" onclick="location.href='{% url "main:register" %}'">Register</button>
                    </li>
                    <li class="nav-item">
                        <button class="btn btn-outline-primary" type="button" onclick="location.href='{% url "main:login" %}'">Login</button>
                    </li>
                {% endif %}
            </ul>
        </div>
    </div>
</nav>
...
```
Selanjutnya untuk `footer` akan dikustomisasi menggunakan *framework* Bootstrap. Berikut ini adalah `footer` yang telah dimodifikasi:
```
...
<footer class="text-light text-center text-lg-start fixed-bottom" style="background-color: #001427;">
    <p>&copy; 2023 Muhammad Andhika Prasetya - 2206031302 - PBP C</p>
</footer>
...
```
Selanjutnya untuk `body` akan dikustomisasi menggunakan *framework* Bootstrap. Berikut ini adalah `body` yang telah dimodifikasi:
```
...
<body style="background-color: #001b35;" class="text-light">
...
<div class="container-fluid">
    {% block content %}{% endblock %}
</div>
...
</body>
...
```
Dengan ini *template* `templates/base.html` telah berhasil dikustomisasi menggunakan *framework* Bootstrap.

### Kustomisasi *template* `login.html`, `register.html`, dan `add.html` menggunakan *framework* Bootstrap
Selanjutnya, *template* `login.html`, `register.html`, dan `add.html` akan dimodifikasi. Untuk *template* `login.html` dikustomisasi menggunakan *framework* Bootstrap. Berikut ini adalah *template* `login.html` yang telah dimodifikasi:
```
{% extends "base.html" %}

{% block title %}Login{% endblock %}

{% block description %}Login to Yu-Gi-Oh! Card Collection.{% endblock %}

{% block content %}
    {% if messages %} 
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
    <section class="vh-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-12 col-md-8 col-lg-6 col-xl-5">
              <div class="card bg-dark text-white" style="border-radius: 1rem;">
                <div class="card-body p-5 text-center">
      
                  <form class="mb-md-5 mt-md-4 pb-5" method="POST">
                    {% csrf_token %}
      
                    <h2 class="fw-bold mb-4 text-uppercase">Login</h2>
      
                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="username">Username</label>
                      <input type="username" name="username" id="username" class="form-control form-control-lg" />
                    </div>
      
                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="password">Password</label>
                      <input type="password" name="password" id="password" class="form-control form-control-lg" />
                    </div>

                    <button class="btn btn-outline-light btn-lg px-5" type="submit">Login</button>
      
                  </form>
      
                  <div>
                    <p class="mb-0">Don't have an account? <a href="{% url "main:register" %}" class="text-white-50 fw-bold">Sign Up</a>
                    </p>
                  </div>
      
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
{% endblock %}
```
Selanjutnya untuk *template* `register.html` juga dikustomisasi menggunakan *framework* Bootstrap. Berikut ini adalah *template* `register.html` yang telah dimodifikasi:
```
{% extends "base.html" %}

{% block title %}Register{% endblock %}

{% block description %}Register to Yu-Gi-Oh! Card Collection.{% endblock %}

{% block content %}
    {% if messages %} 
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
    <section class="vh-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-12 col-md-8 col-lg-6 col-xl-5">
              <div class="card bg-dark text-white" style="border-radius: 1rem;">
                <div class="card-body p-5 text-center">
      
                  <form class="mb-md-5 mt-md-4 pb-5" method="POST">
                    {% csrf_token %}
      
                    <h2 class="fw-bold mb-4 text-uppercase">Register</h2>
      
                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="username">Username</label>
                      <input type="text" name="username" id="username" class="form-control form-control-lg" />
                    </div>
      
                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="password">Password</label>
                      <input type="password" name="password" id="password" class="form-control form-control-lg" />
                    </div>

                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="password2">Verify Password</label>
                      <input type="password" name="password2" id="password2" class="form-control form-control-lg" />
                    </div>

                    <button class="btn btn-outline-light btn-lg px-5" type="submit">Register</button>
      
                  </form>
      
                  <div>
                    <p class="mb-0">Already have an account? <a href="{%  url "main:login"  %}" class="text-white-50 fw-bold">Login</a>
                    </p>
                  </div>
      
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

{% endblock %}
```
Selanjutnya, fungsi login dan register pada `views.py` perlu dimodifikasi untuk mengambil data dari *form* yang telah dibuat secara manual. Berikut ini adalah fungsi login dan register yang telah dimodifikasi:
```
...
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password == password2:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.info(request, "Successfully registered as " + username)
                return redirect("main:index")
            else:
                messages.info(request, "Username already exists")
        else:
            messages.info(request, "Passwords do not match")
    return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.info(request, "Successfully logged in as " + username)
            request.session["last_login"] = str(timezone.now())
            return redirect("main:index")
        else:
            messages.info(request, "Invalid credentials")
    return render(request, "login.html")
...
```
Selanjutnya untuk *template* `add.html` juga dikustomisasi menggunakan *framework* Bootstrap. Berikut ini adalah *template* `add.html` yang telah dimodifikasi:
```
{% extends "base.html" %}

{% block title %}Add Item{% endblock %}

{% block description %}Add a new item to the collection.{% endblock %}

{% block content %}
{% if messages %} 
    {% for message in messages %}
        <div class="alert alert-{{ message.tags }}">
            {{ message }}
        </div>
    {% endfor %}
{% endif %}
<section class="vh-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
          <div class="card bg-dark text-white" style="border-radius: 1rem;">
            <div class="card-body p-5 text-center">
  
              <form class="mb-md-3 mt-md-2" method="POST" enctype="multipart/form-data">
                {% csrf_token %}
  
                <h2 class="fw-bold mb-2 text-uppercase">Add Item</h2>
                <h5 class="mb-2">User: {{ user.username }}</h5> 
                <h5 class="mb-4">Last Login: {{ request.session.last_login }}</h5>
  
                <div class="form-outline form-white mb-2">
                    <label class="form-label" for="name">Name</label>
                  <input type="text" name="name" id="id_name" class="form-control form-control-lg" />
                </div>
  
                <div class="form-outline form-white mb-2">
                    <label class="form-label" for="amount">Amount</label>
                  <input type="number" name="amount" id="id_amount" class="form-control form-control-lg" />
                </div>
  
                <div class="form-outline form-white mb-2">
                    <label class="form-label" for="description">Description</label>
                  <textarea name="description" id="id_description" class="form-control form-control-lg"></textarea>
                </div>
  
                <div class="form-outline form-white mb-2">
                    <label class="form-label" for="card_type">Card Type</label>
                  <input type="text" name="card_type" id="id_card_type" class="form-control form-control-lg" />
                </div>
  
                <div class="form-outline form-white mb-2">
                    <label class="form-label" for="passcode">Passcode</label>
                  <input type="number" name="passcode" id="id_passcode" class="form-control form-control-lg" />
                </div>
  
                <div class="form-outline form-white mb-2">
                    <label class="form-label" for="attribute">Attribute</label>
                  <input type="text" name="attribute" id="id_attribute" class="form-control form-control-lg" />
                </div>
  
                <div class="form-outline form-white mb-2">
                    <label class="form-label" for="types">Types</label>
                  <input type="text" name="types" id="id_types" class="form-control form-control-lg" />
                </div>
  
                <div class="form-outline form-white mb-2">
                    <label class="form-label" for="level">Level</label>
                  <input type="number" name="level" id="id_level" class="form-control form-control-lg" />
                </div>
  
                <div class="form-outline form-white mb-2">
                    <label class="form-label" for="atk">Attack</label>
                  <input type="number" name="atk" id="id_atk" class="form-control form-control-lg" />
                </div>
  
                <div class="form-outline form-white mb-2">
                    <label class="form-label" for="deff">Deffend</label>
                  <input type="number" name="deff" id="id_deff" class="form-control form-control-lg" />
                </div>
  
                <div class="form-outline form-white mb-2">
                    <label class="form-label" for="effect_type">Effect Type</label>
                  <input type="text" name="effect_type" id="id_effect_type" class="form-control form-control-lg" />
                </div>
  
                <div class="form-outline form-white mb-2">
                    <label class="form-label" for="card_property">Card Property</label>
                  <input type="text" name="card_property" id="id_card_property" class="form-control form-control-lg" />
                </div>
  
                <div class="form-outline form-white mb-2">
                    <label class="form-label" for="rulings">Rulings</label>
                  <textarea name="rulings" id="id_rulings" class="form-control form-control-lg" ></textarea>
                </div>
  
                <div class="form-outline form-white mb-4">
                    <label class="form-label" for="image">Image</label>
                  <input type="file" name="image" accept="image/*" id="id_image" class="form-control form-control-lg" />
                </div>

                <button class="btn btn-outline-light btn-lg" type="submit">Add Card</button>
  
              </form>  
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
{% endblock %}
```
Lalu untuk fungsi `add` pada `views.py` perlu dimodifikasi untuk mengambil data dari *form* yang telah dibuat secara manual. Berikut ini adalah fungsi `add` yang telah dimodifikasi:
```
...
@login_required(login_url="/login/")
def add(request):
    if request.method == "POST":
        data = request.POST.copy()
        data["user"] = request.user.id
        form = ItemForm(data, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("main:index")
        else:
            print(form.errors)
            messages.error(request, "Invalid form")
    return render(request, "add.html")
...
```
Dan untuk `ItemForm` pada `forms.py` perlu dimodifikasi. Berikut ini adalah `ItemForm` yang telah dimodifikasi:
```
from django.forms import ModelForm
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
```
Dengan ini *template* `login.html`, `register.html`, dan `add.html` telah berhasil dikustomisasi menggunakan *framework* Bootstrap.

### Kustomisasi *template* `index.html` menggunakan *framework* Bootstrap
Selanjutnya, *template* `index.html` dikustomisasi menggunakan *framework* Bootstrap. Berikut ini adalah *template* `index.html` yang telah dimodifikasi:
```
{% extends "base.html" %}

{% block title %}Yu-Gi-Oh! Card Collection{% endblock %}

{% block description %}Yu-Gi-Oh! Card Collection is a website to collect Yu-Gi-Oh! cards.{% endblock %}

{% block content %}
<section class="text-center">
    <div class="container">
        <h1 class="jumbotron-heading">Yu-Gi-Oh! Card Collection</h1>
        <p class="lead">Yu-Gi-Oh! Card Collection is a website to collect Yu-Gi-Oh! cards.</p>
        <p>
            {% if user.is_authenticated %}
                <p class="lead">User: {{ user.username }}<br/>
                Last Login: {{ request.session.last_login }}</p>
                <a href="{% url "main:logout" %}" class="btn btn-primary my-2">Logout</a>
            {% else %}
                <a href="{% url "main:register" %}" class="btn btn-primary my-2">Register</a>
                <a href="{% url "main:login" %}" class="btn btn-secondary my-2">Login</a>
            {% endif %}
        </p>
    </div>
</section>
{% if user.is_authenticated %}
    <div class="container">
        {% if items %}
            <p>
                <p class="lead">Total Cards: {{ items|length }}</p>
                <a href="{% url "main:delete_all" %}" class="btn btn-danger my-2">Delete All Cards</a>
            </p>
        {% endif %}
        <div class="row row-cols-4">
            {% for item in items %}
                <div class="col-md-6 col-lg-4 mb-5">
                    <div class="card text-white" style="border-radius: 3px; background-color: #000016b9; border: 1px solid #1D3E67;">
                        <img src="{{ item.image.url }}" class="card-img-top" alt="Image" style="border-radius: 3px 3px 0 0;">
                        <div class="card-body">
                            <h3 class="card-title">{{ item.name }}</h3>
                            <p class="card-text">Amount: {{ item.amount }}</p>
                            <p class="card-text">Description: {{ item.description }}</p>
                            <p class="card-text">Card Type: {{ item.card_type }}</p>
                            <p class="card-text">Passcode: {{ item.passcode }}</p>
                            <p class="card-text">Attribute: {{ item.attribute }}</p>
                            <p class="card-text">Types: {{ item.types }}</p>
                            <p class="card-text">Level: {{ item.level }}</p>
                            <p class="card-text">ATK: {{ item.atk }}</p>
                            <p class="card-text">DEF: {{ item.deff }}</p>
                            <p class="card-text">Effect Type: {{ item.effect_type }}</p>
                            <p class="card-text">Card Property: {{ item.card_property }}</p>
                            <p class="card-text" style="color: #FFFF00" >Rulings: {{ item.rulings }}</p>
                            <div class="row m-2">
                                <div class="col-md-6">
                                    <a href="{% url "main:show_xml_by_id" item.id %}" class="btn btn-primary">Show XML by ID</a>
                                </div>
                                <div class="col-md-6">
                                    <a href="{% url "main:show_json_by_id" item.id %}" class="btn btn-primary">Show JSON by ID</a>
                                </div>
                            </div>
                            <div class="row m-2">
                                <div class="col-md-4">
                                    {% if item.amount > 0 %}
                                        <a href="{% url "main:add_amount" item.id %}" class="btn btn-success">Add Amount</a>
                                    {% endif %}
                                </div>
                                <div class="col-md-4">
                                    {% if item.amount > 1 %}
                                        <a href="{% url "main:reduce_amount" item.id %}" class="btn btn-secondary">Reduce Amount</a>
                                    {% endif %}
                                </div>
                                <div class="col-md-4">
                                    <a href="{% url "main:delete" item.id %}" class="btn btn-danger">Delete Card</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
{% endif %}
{% endblock %}
```
Desain Web menggunakan HTML, CSS dan Framework CSS telah berhasil diimplementasikan.

### Menjawab pertanyaan terkait tugas 5
#### Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Element selector adalah jenis selector CSS yang digunakan untuk memilih elemen HTML berdasarkan tag name-nya. Element selector memiliki beberapa manfaat, antara lain:

- **Mudah digunakan.** Element selector hanya memerlukan satu kata untuk memilih elemen HTML, sehingga mudah untuk diingat dan digunakan.
- **Efektif.** Element selector dapat digunakan untuk memilih elemen HTML secara spesifik, sehingga CSS rule yang diterapkan akan lebih efektif.

Ada beberapa jenis element selector, antara lain:

- **Type selector:** Type selector digunakan untuk memilih elemen HTML berdasarkan tag name-nya. Misalnya, `h1` untuk memilih elemen `<h1>`.
- **Combinator selector:** Combinator selector digunakan untuk menggabungkan dua atau lebih element selector. Misalnya, `h1 > p` untuk memilih elemen `<p>` yang berada di bawah elemen `<h1>`.
- **Pseudo-class selector:** Pseudo-class selector digunakan untuk memilih elemen HTML berdasarkan kondisi tertentu. Misalnya, `:hover` untuk memilih elemen HTML saat dihover.

Waktu yang tepat untuk menggunakan element selector adalah saat kita ingin memilih elemen HTML secara spesifik. Misalnya, kita ingin mengubah warna semua elemen `<h1>` menjadi biru, maka kita dapat menggunakan type selector `h1`.

#### Jelaskan HTML5 Tag yang kamu ketahui.
HTML5 Tag adalah tag-tag yang digunakan untuk membuat dokumen HTML. HTML5 memiliki 145 tag, yang dapat dikelompokkan menjadi beberapa kategori, antara lain:

* **Structural Tags:** Tag-tag yang digunakan untuk menentukan struktur dokumen HTML. Misalnya, `<html>`, `<body>`, `<head>`, `<title>`, `<div>`, `<ul>`, `<ol>`, `<li>`.
* **Content Tags:** Tag-tag yang digunakan untuk menampilkan konten. Misalnya, `<p>`, `<img>`, `<a>`, `<b>`, `<strong>`, `<i>`, `<em>`.
* **Form Tags:** Tag-tag yang digunakan untuk membuat formulir. Misalnya, `<form>`, `<input>`, `<label>`, `<select>`, `<option>`, `<textarea>`.
* **Multimedia Tags:** Tag-tag yang digunakan untuk menampilkan multimedia. Misalnya, `<audio>`, `<video>`, `<canvas>`.
* **Other Tags:** Tag-tag yang digunakan untuk berbagai keperluan. Misalnya, `<hr>`, `<br>`, `<abbr>`, `<time>`, `<article>`, `<section>`.

Berikut adalah beberapa contoh HTML5 Tag:

* **Tag `<html>`:** Tag ini digunakan untuk menandai awal dan akhir dokumen HTML.
* **Tag `<body>`:** Tag ini digunakan untuk menandai konten dokumen HTML.
* **Tag `<head>`:** Tag ini digunakan untuk menampung informasi tentang dokumen HTML, seperti judul, meta data, dan gaya CSS.
* **Tag `<title>`:** Tag ini digunakan untuk menampilkan judul dokumen HTML di tab browser.
* **Tag `<div>`:** Tag ini digunakan untuk membuat blok konten.
* **Tag `<ul>`:** Tag ini digunakan untuk membuat daftar tidak berurutan.
* **Tag `<ol>`:** Tag ini digunakan untuk membuat daftar berurutan.
* **Tag `<li>`:** Tag ini digunakan untuk membuat item daftar.
* **Tag `<p>`:** Tag ini digunakan untuk membuat paragraf.
* **Tag `<img>`:** Tag ini digunakan untuk menampilkan gambar.
* **Tag `<a>`:** Tag ini digunakan untuk membuat tautan.
* **Tag `<b>`:** Tag ini digunakan untuk membuat teks tebal.
* **Tag `<strong>`:** Tag ini digunakan untuk membuat teks penting.
* **Tag `<i>`:** Tag ini digunakan untuk membuat teks miring.
* **Tag `<em>`:** Tag ini digunakan untuk membuat teks penekanan.
* **Tag `<form>`:** Tag ini digunakan untuk membuat formulir.
* **Tag `<input>`:** Tag ini digunakan untuk membuat input formulir.
* **Tag `<label>`:** Tag ini digunakan untuk memberi label pada input formulir.
* **Tag `<select>`:** Tag ini digunakan untuk membuat menu tarik-turun.
* **Tag `<option>`:** Tag ini digunakan untuk membuat item menu tarik-turun.
* **Tag `<textarea>`:** Tag ini digunakan untuk membuat kotak teks.
* **Tag `<audio>`:** Tag ini digunakan untuk menampilkan file audio.
* **Tag `<video>`:** Tag ini digunakan untuk menampilkan file video.
* **Tag `<canvas>`:** Tag ini digunakan untuk membuat grafik dan animasi.

HTML5 Tag dapat digunakan untuk membuat berbagai jenis dokumen HTML, mulai dari situs web sederhana hingga aplikasi web kompleks.

#### Jelaskan perbedaan antara margin dan padding.
Margin dan padding adalah dua properti CSS yang digunakan untuk mengatur ruang kosong di sekitar elemen HTML. Perbedaan utama antara margin dan padding adalah bahwa margin mengatur jarak antara elemen HTML dan elemen lainnya, sedangkan padding mengatur jarak antara elemen HTML dan kontennya.

**Margin**

Margin mengatur jarak antara elemen HTML dan elemen lainnya. Margin dapat diterapkan pada semua sisi elemen HTML, yaitu atas, bawah, kiri, dan kanan. Margin juga dapat diterapkan pada semua elemen HTML secara bersamaan, atau pada elemen HTML tertentu saja.

**Padding**

Padding mengatur jarak antara elemen HTML dan kontennya. Padding dapat diterapkan pada semua sisi elemen HTML, yaitu atas, bawah, kiri, dan kanan. Padding juga dapat diterapkan pada semua elemen HTML secara bersamaan, atau pada elemen HTML tertentu saja.

**Kesimpulan**

Margin dan padding adalah dua properti CSS yang penting untuk mengatur ruang kosong di sekitar elemen HTML. Margin mengatur jarak antara elemen HTML dan elemen lainnya, sedangkan padding mengatur jarak antara elemen HTML dan kontennya.

#### Jelaskan perbedaan antara *framework* CSS Bootstrap dan Tailwind. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

Bootstrap dan Tailwind adalah dua framework CSS yang populer untuk pengembangan web. Kedua framework ini memiliki kelebihan dan kekurangannya masing-masing.

**Bootstrap**

* Kelebihan:
    * Memiliki komponen dan fitur yang lengkap, sehingga dapat digunakan untuk membuat berbagai jenis situs web dan aplikasi web.
    * Mudah digunakan, karena menyediakan komponen dan fitur yang siap pakai.
    * Responsive, sehingga dapat digunakan untuk membuat situs web yang responsif terhadap berbagai ukuran layar.
* Kekurangan:
    * Ukurannya relatif besar, sehingga dapat memperlambat waktu loading halaman.
    * Kurang fleksibel, karena komponen dan fiturnya sudah ditetapkan.

**Tailwind**

* Kelebihan:
    * Sangat fleksibel, karena memungkinkan kita untuk membuat gaya CSS sesuai kebutuhan.
    * Ukurannya relatif kecil, sehingga dapat mempercepat waktu loading halaman.
    * Mudah digunakan, karena menggunakan sintaks yang sederhana.
* Kekurangan:
    * Membutuhkan waktu untuk mempelajari sintaksnya.
    * Tidak memiliki komponen dan fitur yang lengkap, sehingga kita perlu membuat sendiri komponen dan fitur yang dibutuhkan.

**Kapan sebaiknya menggunakan Bootstrap daripada Tailwind?**

* **Jika Anda membutuhkan framework CSS yang lengkap dan mudah digunakan, maka Bootstrap adalah pilihan yang tepat.** Bootstrap memiliki komponen dan fitur yang lengkap, sehingga dapat digunakan untuk membuat berbagai jenis situs web dan aplikasi web. Bootstrap juga mudah digunakan, karena menyediakan komponen dan fitur yang siap pakai.
* **Jika Anda membutuhkan framework CSS yang fleksibel dan ringan, maka Tailwind adalah pilihan yang tepat.** Tailwind sangat fleksibel, karena memungkinkan kita untuk membuat gaya CSS sesuai kebutuhan. Tailwind juga berukuran relatif kecil, sehingga dapat mempercepat waktu loading halaman.

**Kapan sebaiknya menggunakan Tailwind daripada Bootstrap?**

* **Jika Anda membutuhkan framework CSS yang sangat fleksibel, maka Tailwind adalah pilihan yang tepat.** Tailwind memungkinkan kita untuk membuat gaya CSS sesuai kebutuhan, sehingga kita dapat menyesuaikan gaya CSS dengan kebutuhan spesifik situs web atau aplikasi web kita.
* **Jika Anda membutuhkan framework CSS yang ringan, maka Tailwind adalah pilihan yang tepat.** Tailwind berukuran relatif kecil, sehingga dapat mempercepat waktu loading halaman.

**Kesimpulan**

Bootstrap dan Tailwind adalah dua framework CSS yang memiliki kelebihan dan kekurangannya masing-masing. Pilihan framework CSS yang tepat tergantung pada kebutuhan dan preferensi Anda.

# Tugas 6: JavaScript dan Asynchronous JavaScript
Menambahkan JavaScript dan Asynchronous JavaScript ke dalam aplikasi [Yu-Gi-Oh! Card Collection](https://pras-yugioh-card.onrender.com/) dan menjawab pertanyaan terkait tugas 6.

## Tugas 6 Checklist
*from* [Tugas 6: JavaScript dan Asynchronous JavaScript](https://pbp-fasilkom-ui.github.io/ganjil-2024/assignments/individual/assignment-6)
- [ ] Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.
  - [ ] AJAX GET
    - [ ] Ubahlah kode _cards_ data item agar dapat mendukung AJAX GET.
    - [ ] Lakukan pengambilan task menggunakan AJAX GET.
  - [ ] AJAX POST
    - [ ] Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item.

        > Modal di-*trigger* dengan menekan suatu tombol pada halaman utama. Saat penambahan item berhasil, modal harus ditutup dan input form harus dibersihkan dari data yang sudah dimasukkan ke dalam form sebelumnya.

    - [ ] Buatlah fungsi *view* baru untuk menambahkan item baru ke dalam basis data.
    - [ ] Buatlah *path* `/create-ajax/` yang mengarah ke fungsi *view* yang baru kamu buat.
    - [ ] Hubungkan form yang telah kamu buat di dalam modal kamu ke *path* `/create-ajax/`.
    - [ ] Lakukan *refresh* pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa *reload* halaman utama secara keseluruhan.
  - [ ] Melakukan perintah `collectstatic`.
    - Perintah ini bertujuan untuk mengumpulkan *file static* dari setiap aplikasi kamu ke dalam suatu *folder* yang dapat dengan mudah disajikan pada produksi.

- [ ] Menjawab beberapa pertanyaan berikut pada `README.md` pada *root folder* (silakan modifikasi `README.md` yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
    - Jelaskan perbedaan antara *asynchronous programming* dengan *synchronous programming*.
    - Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma *event-driven programming*. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
    - Jelaskan penerapan *asynchronous programming* pada AJAX.
    - Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada *library* jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
    - Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).

- [ ] Melakukan `add`-`commit`-`push` ke GitHub.

- [ ] Melakukan *deployment* ke PaaS PBP Fasilkom UI dan sertakan tautan aplikasi pada file `README.md`.
    - DOKKU_APP_NAME = `UsernameSSO-tugas`

      > Ubah juga tanda titik menjadi tanda strip. Contoh: `muhammad-iqbal111-tugas`.
- [ ] **BONUS**: Menambahkan fungsionalitas hapus dengan menggunakan AJAX DELETE.

### Menambahkan fungsi untuk mengembalikan data dalam format JSON
Pertama-tama, fungsi `get_items_json` pada `views.py` akan dibuat untuk mengembalikan data dalam format JSON. Berikut ini adalah fungsi `get_items_json` yang telah dibuat:
```
...
@login_required(login_url="/login/")
def get_items_json(request):
    items = Item.objects.filter(user=request.user)
    data = serializers.serialize("json", items)
    return HttpResponse(data, content_type="application/json")
```
Fungsi ini akan mengambil semua item yang dimiliki oleh user yang sedang login, kemudian mengembalikan data dalam format JSON.
Selanjutnya, *path* `/get-items-json/` akan ditambahkan pada `urls.py` untuk mengarahkan ke fungsi `get_items_json`. Berikut ini adalah *path* `/get-items-json/` yang telah ditambahkan:
```
...
urlpatterns = [
    ...
    path("get-items-json/", views.get_items_json, name="get_items_json"),
]
```

### Mengubah *cards* data item agar dapat mendukung AJAX GET (+ *revamp* *template* `index.html`)
Sebelumnya, *template* `base.html` dimodifikasi terlebih dahulu untuk menambahkan *block* `scripts`. Berikut ini adalah *template* `base.html` yang telah dimodifikasi di bagian bawah `footer`:
```
<script>
    {% block script %}{% endblock %}
</script>
```
Selanjutnya, *template* `index.html` dimodifikasi untuk menambahkan *script* yang akan mengambil data item dalam format JSON menggunakan AJAX GET serta mengubah isi dari *cards* data item menggunakan data yang telah diambil. Berikut ini adalah isi *block* `content` pada *template* `index.html` yang telah dimodifikasi:
```
{% block content %}
...
{% if user.is_authenticated %}
    <section id="item-cards"></section>
    
    <div class="modal fade" id="modalCard" tabindex="-1" aria-labelledby="modalCardLabel" aria-hidden="true">
        <div class="modal-dialog modal-fullscreen-md modal-lg">
            <div class="modal-content text-white" style="border-radius: 5px; background-color: #000016b9;">
                <div class="modal-header">
                    <h5 class="modal-title" id="modalCardLabel">Name Card</h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="row">
                        <div class="col-md-6">
                            <img id="modalCardImage" src="" class="img-fluid" alt="Image" style="border-radius: 5px;">
                        </div>
                        <div class="col-md-6">
                            <p id="modalCardAmount" data-bs-toggle="tooltip" data-bs-placement="top" title="Amount">Amount</p>
                            <p id="modalCardType" data-bs-toggle="tooltip" data-bs-placement="top" title="Type | Attribute | Level">Type | Attribute | Level</p>
                            <p id="modalCardEffectType" style="font-style: italic;" data-bs-toggle="tooltip" data-bs-placement="top" title="Effect Type">Effect Type</p>
                            <p id="modalCardTypes" style="font-weight: bold;" data-bs-toggle="tooltip" data-bs-placement="top" title="Types">[Types]</p>
                            <p id="modalCardDesc" style="text-align: justify; font-size: 14px;" data-bs-toggle="tooltip" data-bs-placement="top" title="Description">Description</p>
                            <p id="modalCardAtkDef">ATK/DEF</p>
                            <p id="modalCardPasscode" data-bs-toggle="tooltip" data-bs-placement="top" title="Passcode">Passcode</p>
                            <p id="modalCardProperty" data-bs-toggle="tooltip" data-bs-placement="top" title="Property">Property</p>
                            <p id="modalCardRulings" style="color: #FFFF00; text-align: justify; font-size: 14px;" data-bs-toggle="tooltip" data-bs-placement="top" title="Rulings">Rulings</p>
                        </div>
                    </div>
                </div>
                <div class="modal-footer justify-content-center">
                    <section id="show-data">
                        <a id="modalCardXML" href="" class="btn btn-primary">Show XML</a>
                        <a id="modalCardJSON" href="" class="btn btn-primary">Show JSON</a>
                    </section>
                    <section id="edit-data">
                        <a id="modalCardAddAmount" href="" class="btn btn-success">Add Amount</a>
                        <a id="modalCardReduceAmount" href="" class="btn btn-secondary">Reduce Amount</a>
                        <a id="modalCardDelete" href="" class="btn btn-danger" onclick="return confirmDelete()">Delete Card</a>
                    </section>
                </div>
            </div>
        </div>
    </div>


{% endif %}
{% endblock %}
```
> Di sini, terdapat perubahan tampilan *template* `index.html` di mana informasi yang ditampilkan pada *cards* data item akan ditampilkan pada modal yang akan muncul saat *card* di-*click*.

Selanjutnya, tambahkan *block* `script` pada *template* `index.html` dengan isi sebagai berikut:
```
{% block script %}
{% if user.is_authenticated %}
    <!-- Get Cards -->
    async function getCards() {
        return fetch("{% url "main:get_items_json" %}")
            .then(response => response.json())
    }
    <!-- End Get Cards -->

    <!-- Refresh Cards -->
    async function refreshCards() {
        document.getElementById("item-cards").innerHTML = ""
        const cards = await getCards()
        let html = ""
        html += `
            <div class="container">
                <p>
                    <p class="lead">Total Cards: ${cards.length}</p>
                    <a id="delete-all" href="{% url "main:delete_all" %}" class="btn btn-danger my-2" onclick="return confirmDeleteAll()">Delete All</a>
                </p>
                <div class="row row-cols-lg-4 row-cols-md-3 row-cols-sm-2 row-cols-1 pt-2" style="justify-content: center; background-color: #000016b9; border-radius: 5px; border: 1px solid #1D3E67;">
        `
        cards.forEach((card) => {
            html += `
            <div class="col mb-5">
                <div id="card-${ card.pk }" class="card text-white" style="border-radius: 5px; background-color: #2a3650; border: 1px solid #1D3E67;">
                    <div>
                        <p class="lead mb-0" style="position: absolute; bottom: 5rem; left: 1rem; justify-content: center; display: flex; font-size: 1.5rem; font-weight: bold; color: #FFFF00; background-color: #000016b9; border-radius: 50%; height: 38px; width: 38px;" data-bs-toggle="tooltip" data-bs-placement="top" title="Amount">${ card.fields.amount }</p>
                    </div>
                    <img src="/media/${ card.fields.image }" class="card-img-top" alt="Image" style="border-radius: 5px 5px 0 0;">
                        <div class="row text-center py-2">
                            <div class="col-4">
                                <a href="/add_amount/${ card.pk }" class="btn btn-success" style="border-radius: 50%; height: 38px; width: 38px;" data-bs-toggle="tooltip" data-bs-placement="top" title="Add Amount">+</a>
                            </div>
                            <div class="col-4">
            `
            if (card.fields.amount > 1) {
                html += `
                    <a href="/reduce_amount/${ card.pk }" class="btn btn-secondary" style="border-radius: 50%; height: 38px; width: 38px;" data-bs-toggle="tooltip" data-bs-placement="top" title="Reduce Amount">-</a>
                `
            }
            html += `
                            </div>
                            <div class="col-4">
                                <a href="/delete/${ card.pk }" class="btn btn-danger" style="border-radius: 50%; height: 38px; width: 38px;" data-bs-toggle="tooltip" data-bs-placement="top" title="Delete Card" onclick="return confirmDelete()">X</a>
                            </div>
                        </div>
                    </div>
                </div>
            `
        })
        html += `
                </div>
            </div>
        `
        document.getElementById("item-cards").innerHTML = html
        cards.forEach((card) => {
            document.getElementById(`card-${ card.pk }`).addEventListener("click", () => {
                showModalCard(card)
            })
        })
    }
    refreshCards()
    <!-- End Refresh Cards -->

    <!-- Trigger Modal -->
    const modalCard = new bootstrap.Modal(document.getElementById('modalCard'), {
        keyboard: false
    })
    function showModalCard(card) {
        document.getElementById("modalCardLabel").innerHTML = card.fields.name
        document.getElementById("modalCardImage").src = `/media/${ card.fields.image }`
        document.getElementById("modalCardAmount").innerHTML = `Amount: ${ card.fields.amount }`
        document.getElementById("modalCardType").innerHTML = `${ card.fields.card_type } | ${ card.fields.attribute } | ${ card.fields.level }`
        document.getElementById("modalCardEffectType").innerHTML = `${ card.fields.effect_type }`
        document.getElementById("modalCardTypes").innerHTML = `[${ card.fields.types }]`
        document.getElementById("modalCardDesc").innerHTML = `${ card.fields.description }`
        document.getElementById("modalCardAtkDef").innerHTML = `<b>ATK/ </b>${ card.fields.atk }  <b>DEF/ </b>${ card.fields.deff }`
        document.getElementById("modalCardPasscode").innerHTML = `#${ card.fields.passcode }`
        document.getElementById("modalCardProperty").innerHTML = `${ card.fields.card_property }`
        document.getElementById("modalCardRulings").innerHTML = `${ card.fields.rulings }`
        document.getElementById("modalCardXML").href = `/xml/${ card.pk }`
        document.getElementById("modalCardJSON").href = `/json/${ card.pk }`
        document.getElementById("modalCardAddAmount").href = `/add_amount/${ card.pk }`
        document.getElementById("modalCardReduceAmount").href = `/reduce_amount/${ card.pk }`
        document.getElementById("modalCardDelete").href = `/delete/${ card.pk }`
        limitText("#modalCardDesc", 300)
        limitText("#modalCardRulings", 300)
        modalCard.show()
    }
    <!-- End Trigger Modal -->

    <!-- Tooltip -->
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })
    <!-- End Tooltip -->

    <!-- Limit Text + Expand -->
    function limitText(selector, maxLength) {
        let element = document.querySelector(selector)
        let text = element.innerHTML
        let truncated = text
        let expand = document.createElement('span');
        console.log(text)

        if (text.length > maxLength) {
            truncated = text.substr(0,maxLength) + '...';
            expand.setAttribute('class', 'expandText');
            expand.setAttribute('style', 'color: cyan');
            expand.innerHTML = 'more';
            expand.onclick = function() {
                expand.parentNode.removeChild(expand);
                element.innerHTML = text;
            };
        }
        element.innerHTML = truncated;
        element.appendChild(expand);
    }
    <!-- End Limit Text + Expand -->

    <!-- Confirm Delete -->
    function confirmDelete() {
        return confirm("Are you sure you want to delete this card?")
    }
    <!-- End Confirm Delete -->

    <!-- Confirm Delete All -->
    function confirmDeleteAll() {
        return confirm("Are you sure you want to delete all cards?")
    }
    <!-- End Confirm Delete All -->
{% endif %}
{% endblock %}
```
> Di sini, terdapat tambahan seperti fungsi `tooltip`, fungsi `limitText`, dan fungsi `confirmDelete` untuk menampilkan *tooltip*, membatasi jumlah karakter yang ditampilkan, dan memunculkan *confirm dialog* saat *card* di-*click*.

Dengan ini, *cards* data item akan diubah menggunakan data yang telah diambil menggunakan AJAX GET.
> NOTE: Pada *commit* ini, terdapat cukup banyak perubahan pada *template* `index.html` karena *template* `index.html` dimodifikasi untuk menampilkan *cards* data item menggunakan modal. Selain itu, terdapat beberapa *bug* yang ditemukan dan diperbaiki pada *commit* ini. Untuk melihat perubahan yang terjadi, dapat dilihat pada *commit* [b2f2906](https://github.com/andhikapraa/yugioh-card/commit/b2f290610ca55089f3c0ecdaee8b745aa808c672).



# License  

[MIT](https://choosealicense.com/licenses/mit/)
