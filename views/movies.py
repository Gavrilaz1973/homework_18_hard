
from flask_restx import Resource, Namespace
from implemented import movie_service
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movie = movie_service.get_movies()
        result = MovieSchema.dump(movie)
        return result, 200

    def post(self):
        return "", 201
