import sqlalchemy as sa
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


movies_and_genres = Table('movies_and_genres', Base.metadata,
                          Column('movie_id', ForeignKey('movies.id'), primary_key=True),
                          Column('genre_id', ForeignKey('genres.id'), primary_key=True)
                          )

favorite_movies_list = Table('favorite_movies_list', Base.metadata,
                             Column('author_id', ForeignKey('users.id'), primary_key=True),
                             Column('movie_id', ForeignKey('movies.id'), primary_key=True)
                             )


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.Text, unique=True)
    email = sa.Column(sa.Text, unique=True)
    name = sa.Column(sa.Text)
    password_hash = sa.Column(sa.Text)
    favorite_movies = relationship("Movie",
                                   secondary=favorite_movies_list)


class Movie(Base):
    __tablename__ = 'movies'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, nullable=False)
    year = sa.Column(sa.Text)
    country = sa.Column(sa.Text)
    budget = sa.Column(sa.Integer)
    fees = sa.Column(sa.Integer)
    genres = relationship("Genre",
                          secondary=movies_and_genres)
    reviews = relationship("Review")


class Genre(Base):
    __tablename__ = 'genres'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, unique=True)


class Review(Base):
    __tablename__ = 'reviews'

    id = sa.Column(sa.Integer, primary_key=True)
    reviewText = sa.Column(sa.Text)
    rating = sa.Column(sa.Integer, nullable=False)
    authorId = sa.Column(sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'))
    movieId = sa.Column(sa.Integer, sa.ForeignKey('movies.id', ondelete='CASCADE', onupdate='CASCADE'))
