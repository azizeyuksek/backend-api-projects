from flask import Flask, request , jsonify

app = Flask(__name__)

# example_data
movies=[{
    "id":1,
    "title":"Sadece Sen",
    "scriptwriter":"Ceren Aslan ",
    "year":2014
}]

@app.route("/")
def home():
    return jsonify({"Message : Movie Management API is started"})

# Get / movies
@app.route("/movies",methods=["GET"])
def get_movies():
    return jsonify(movies)


# post/movies
@app.route("/movies",methods=["POST"])
def add_movies():
    data=request.json

    new_movies=[{
        "id": max([m["id"] for m in movies]) + 1 if movies else 1,
        "title": data.get("title"),
        "scriptwriter": data.get("scriptwriter"),
        "year": data.get("year")
    }]

    movies.append(new_movies)
    return jsonify(new_movies),201

# put / movies / {id}
@app.route("/movies/<int:id>", methods=["PUT"])
def update_movies(id):
    data = request.json
    
    for movie in movies:
        if movie["id"] == id:  # ✅ Doğrusu: movie (tekil)
            movie["title"] = data.get("title", movie["title"])  # ✅ Doğrusu: movie
            movie["scriptwriter"] = data.get("scriptwriter", movie["scriptwriter"])  # ✅ Doğrusu: movie
            movie["year"] = data.get("year", movie["year"])  # ✅ Doğrusu: movie
            return jsonify(movie), 200
            
    return jsonify({"message": "Movie not found"}), 404

@app.route("/movies/<int:id>", methods=["DELETE"])
def delete_movie(id):
    for movie in movies:
        if movie["id"] == id:  # <-- Burası movie (tekil) olmalı
            movies.remove(movie)  # <-- Burası da movie (tekil) olmalı
            return jsonify({"message": "movie deleted"})
            
    return jsonify({"message": "movie not found"}), 404

if __name__=="__main__":
    app.run(debug=True)