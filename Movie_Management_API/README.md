## Movie Management API (SQLite Version)

Bu proje, Python ve Flask mikro-çerçevesi kullanarak geliştirdiğim  verileri geçici listeler yerine **SQLite** veri tabanında kalıcı olarak sakladığım bir REST API uygulamasıdır.

# Kullanılan Teknolojiler
 - Python 
 - Flask 
 - Flask-SQLAlchemy*
 - SQLite 
 - Postman

# Özellikler & Veri Yapısı
Uygulama, `movies.db` veri tabanı dosyasını otomatik olarak oluşturur ve tüm CRUD işlemlerini (Ekleme, Listeleme, Güncelleme, Silme) bu dosya üzerinden gerçekleştirir.

# Veri Modeli 
 - `id` (Integer, Primary Key) - Otomatik artan benzersiz numara
 - `title` (String) - Film Adı
 - `scriptwriter` (String) - Senarist
 - `year` (Integer) - Çıkış Yılı


git clone [https://github.com/azizeyuksek/backend-api-projects.git](https://github.com/azizeyuksek/backend-api-projects.git)
cd backend-api-projects/movie-management-api