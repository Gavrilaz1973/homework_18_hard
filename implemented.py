from dao.movie import MovieDAO
from service.movie import MovieService
from setup_db import db

movie_dao = MovieDAO(session=db.session)
movie_service = MovieService(dao=movie_dao)

# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)