from dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.movie_dao = dao

    def get_movies(self):
        return self.movie_dao.get_all()

    def get_one(self, mid):
        return self.movie_dao.get_id(mid)

    def create(self, data):
        return self.movie_dao.create(data)

    def update(self, data):
        return self.movie_dao.update(data)

    def delete(self, mid):
        self.movie_dao.delete(mid)


