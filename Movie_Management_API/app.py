from flask import Flask, request , jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 


db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)        
    scriptwriter = db.Column(db.String(100), nullable=False) 
    year = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return{
            "id":self.id,
            "title":self.title,
            "scriptwriter":self.scriptwriter,
            "year":self.year}

with app.app_context():
    db.create_all()
        
@app.route("/")
def home():
    return jsonify({"Message : Movie Management API is started"})

# Get / movies
@app.route("/movies", methods=["GET"])
def get_movies():
    # 1. Veri tabanındaki tüm film satırlarını birer Python nesnesi olarak çekiyoruz
    # SQL karşılığı: SELECT * FROM movie;
    all_movies = Movie.query.all() 
    
    # 2. Çektiğimiz nesne listesini tek tek to_dict() ile sözlüğe (dict) çevirip yeni bir liste yapıyoruz
    movies_list = [movie.to_dict() for movie in all_movies]
    
    # 3. Hazırladığımız bu temiz listeyi JSON olarak Postman'e dönüyoruz
    return jsonify(movies_list), 200

# post/movies
@app.route("/movies", methods=["POST"])
def add_movies():
    data = request.json
    
    # 1. Gelen verilerle yeni bir Movie nesnesi (satırı) oluşturuyoruz
    new_movie = Movie(
        title=data.get("title"),
        scriptwriter=data.get("scriptwriter"),
        year=data.get("year")
    )
    
    # 2. SQLite'a bu nesneyi eklemesini söylüyoruz
    db.session.add(new_movie)  # Sıraya ekle
    db.session.commit()        # Veri tabanına kalıcı olarak kaydet (Save)
    
    # 3. Eklenen filmi to_dict() fonksiyonumuzla JSON formatında geri dönüyoruz
    return jsonify(new_movie.to_dict()), 201

# put / movies / {id}
@app.route("/movies/<int:id>", methods=["PUT"])
def update_movies(id):
    # 1. Veri tabanında bu ID'ye sahip filmi buluyoruz
    movie = Movie.query.get(id)
    
    # 2. Eğer film bulunamazsa 404 hatası dönüyoruz
    if not movie:
        return jsonify({"message": "Movie not found"}), 404
        
    data = request.json
    
    # 3. Bulduğumuz filmin alanlarını Postman'den gelen yeni verilerle güncelliyoruz
    movie.title = data.get("title", movie.title)
    movie.scriptwriter = data.get("scriptwriter", movie.scriptwriter)
    movie.year = data.get("year", movie.year)
    
    # 4. Değişiklikleri veri tabanına kaydediyoruz
    db.session.commit()
    
    return jsonify(movie.to_dict()), 200

@app.route("/movies/<int:id>", methods=["DELETE"])
def delete_movie(id):
    # 1. Veri tabanında silinmek istenen filmi buluyoruz
    movie = Movie.query.get(id)
    
    # 2. Film yoksa hata dönüyoruz
    if not movie:
        return jsonify({"message": "Movie not found"}), 404
        
    # 3. Filmi veri tabanından siliyoruz ve kaydediyoruz
    db.session.delete(movie)
    db.session.commit()
    
    return jsonify({"message": "Movie deleted successfully"}), 200

if __name__=="__main__":
    app.run(debug=True)