
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


# Table of contents  
        
[**Yu-Gi-Oh! Card Collection Project**](<#Yu-Gi-Oh!-Card-Collection-Project>)<br />
&emsp;[**Demo**](<#Demo>)<br />
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
&emsp;&emsp;[Melakukan *deployment* ke ~~Adaptable~~ Render.com](<#Melakukan-deployment-ke-Adaptable-Rendercom>)<br />
&emsp;&emsp;[Membuat Unit *Test* (bonus)](<#Membuat-Unit-Test-bonus>)<br />
&emsp;&emsp;[Menjawab pertanyaan](<#Menjawab-pertanyaan>)<br />
[**License**](<#License>)<br />

# Tugas 2: Implementasi Model-View-Template (MVT) pada Django
Mengimplementasi Model-View-Template (MVT) Django pada 
[Yu-Gi-Oh! Card Collection Project](https://pras-yugioh-card.onrender.com/) serta menjawab beberapa
pertanyaan yang sudah dipelajari di kelas.

## Tugas 2 Checklist
from [Tugas 2: Implementasi Model-View-Template (MVT) pada Django](https://pbp-fasilkom-ui.github.io/ganjil-2024/assignments/individual/assignment-2)
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


# License  

[MIT](https://choosealicense.com/licenses/mit/)
