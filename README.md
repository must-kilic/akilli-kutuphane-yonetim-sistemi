# 📚 Akıllı Kütüphane Yönetim Sistemi

Bu proje, öğrencilerin **katmanlı mimari**, **REST API**, **JWT kimlik doğrulama**, **PostgreSQL**, **Trigger & Stored Procedure**, **Docker** ve **frontend-backend entegrasyonu** konularını öğrenmesini amaçlayan kapsamlı bir kütüphane otomasyon sistemidir.

---

## 🎯 Projenin Amacı

Bu projede aşağıdaki işlevler geliştirilmiştir:

- 📖 Kitapların, kullanıcıların ve ödünç işlemlerinin yönetilmesi  
- ⏰ Geç iade edilen kitaplar için **otomatik ceza hesaplanması**  
- 👥 **Admin / User** rollerine göre yetkilendirme  
- 🧠 Veritabanı **Trigger** ve **Stored Procedure** kullanımı  
- 🐳 Docker üzerinde çalışan **backend + veritabanı**  
- 🌐 REST API kullanan işlevsel bir frontend  

---

## 🧱 Kullanılan Teknolojiler

### 🔙 Backend
- Python (Flask)
- Flask SQLAlchemy
- Flask JWT Extended
- Flask CORS
- PostgreSQL
- Docker & Docker Compose

### 🎨 Frontend
- HTML5
- CSS3
- Vanilla JavaScript (Fetch API)

### 🗄️ Veritabanı
- PostgreSQL 16
- Trigger (ceza hesaplama)
- Stored Procedure (ceza temizleme)

---

## 🏗️ Proje Mimarisi

### Katmanlı Mimari

```text
Entity       → Veritabanı tabloları
Repository   → Veritabanı işlemleri
Service      → İş kuralları
Controller   → API endpoint’leri

📁 Proje Dosya Yapısı

📌 Kök Dizin
docker-compose.yml
README.md
🔙 Backend Yapısı
text
Kodu kopyala
backend/
│
├── app.py
├── config.py
├── database.py
├── Dockerfile
├── requirements.txt
├── __init__.py
│
├── controllers/
│   ├── admin_controller.py
│   ├── auth_controller.py
│   ├── book_controller.py
│   ├── borrowing_controller.py
│   ├── report_controller.py
│   ├── user_controller.py
│   ├── utils.py
│   └── __init__.py
│
├── entities/
│   ├── author.py
│   ├── book.py
│   ├── borrow.py
│   ├── category.py
│   ├── penalty.py
│   ├── user.py
│   └── __init__.py
│
├── repositories/
│   ├── book_repository.py
│   ├── borrow_repository.py
│   ├── report_repository.py
│   ├── user_repository.py
│   └── __init__.py
│
├── services/
│   ├── auth_service.py
│   ├── book_service.py
│   ├── borrow_service.py
│   ├── penalty_service.py
│   ├── report_service.py
│   ├── user_service.py
│   └── __init__.py
│
├── sql/
│   └── __init__.sql
│
├── static/
│   └── swagger.json
🗄️ Veritabanı
database/
└── schema.sql
🌐 Frontend Yapısı
frontend/
│
├── login.html
│
├── admin/
│   ├── books.html
│   ├── dashboard.html
│   ├── reports.html
│   └── users.html
│
├── user/
│   ├── books.html
│   ├── dashboard.html
│   ├── my-borrowings.html
│   └── penalties.html
│
├── js/
│   ├── api.js
│   ├── auth.js
│   │
│   ├── admin/
│   │   ├── books.js
│   │   ├── dashboard.js
│   │   ├── reports.js
│   │   └── users.js
│   │
│   └── user/
│       ├── books.js
│       ├── borrowings.js
│       ├── dashboard.js
│       └── penalties.js
│
└── css/
    └── style.css

🔐 Kimlik Doğrulama (JWT)
Giriş yapan kullanıcıya JWT Access Token üretilir

Token içerisinde:

Kullanıcı ID

Rol (admin / user)

Email bilgisi bulunur

Yetkilendirme:

@jwt_required()

@role_required()

👤 Kullanıcı Rolleri
👨‍💼 Admin
Kitap ekleme / silme

Kullanıcıları görüntüleme / silme

Tüm ödünç ve ceza raporlarını görüntüleme

Stored Procedure ile kullanıcı cezalarını temizleme

👨‍🎓 Kullanıcı
Kitap listeleme

Kitap ödünç alma

Kitap iade etme

Kendi cezalarını görüntüleme

🔄 Ceza Hesaplama Mantığı (Trigger)
Kitap iade edildiğinde tetiklenir

İlk iade kontrolü yapılır

7 gün sonrası için:

Günlük 5 TL ceza hesaplanır

Ceza otomatik olarak penalty tablosuna eklenir

sql
Kodu kopyala
AFTER UPDATE OF return_date ON borrow
🧹 Ceza Temizleme (Stored Procedure)
Admin tarafından çalıştırılır

Aynı e-mail adresine sahip kullanıcının

Tüm cezaları tek seferde silinir

sql
Kodu kopyala
CALL clear_user_penalties_by_email(email);
🚀 Projeyi Çalıştırma
1️⃣ Docker ile Başlatma
bash
Kodu kopyala
docker-compose up --build
2️⃣ Backend
API: http://localhost:5000

3️⃣ Frontend
HTML dosyaları Live Server veya tarayıcı ile açılır

🔌 API Örnek Endpoint’ler
Method	Endpoint	Açıklama
POST	/login	Giriş
GET	/books	Kitapları listele
POST	/books	Kitap ekle (admin)
POST	/api/borrowings	Kitap ödünç al
PUT	/api/borrowings/return/{id}	Kitap iade
GET	/my-penalties	Kullanıcı cezaları
GET	/admin/reports	Admin raporları
POST	/admin/clear-penalties	Ceza temizleme

🧪 Test & Sunum
Docker üzerinde sorunsuz çalışmaktadır

Frontend & Backend entegrasyonu tamamlanmıştır

✅ Sonuç
Bu proje ile:

Gerçek bir kütüphane sistemi simüle edilmiştir

Backend & frontend entegrasyonu sağlanmıştır

PostgreSQL Trigger & Stored Procedure kullanılmıştır

Katmanlı mimari ve rol bazlı yetkilendirme başarıyla uygulanmıştır