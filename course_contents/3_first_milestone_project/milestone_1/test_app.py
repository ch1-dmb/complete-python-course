import pytest
import unittest.mock 
import patch, mock_open
from builtins import input
from io import StringIO
from app import add_movie, show_movies, find_movie, movies, menu

@pytest.fixture(autouse=True)
def clear_movies():
    movies.clear()

def test_add_movie(monkeypatch):
    # Predefined user inputs
    inputs = iter(["Inception", "Christopher Nolan", "2010"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Call the function to add a movie
    add_movie()
    
    # Assertions to verify the movie was added correctly
    assert len(movies) == 1
    assert movies[0] == {
        'title': "Inception",
        'director': "Christopher Nolan",
        'year': "2010"
    }
    
def test_show_movies(capsys):
    movies.append({
        'title': "Interstellar",
        'director': "Christopher Nolan",
        'year': "2014"
    })
    show_movies()
    captured = capsys.readouterr()
    assert "Title: Interstellar" in captured.out
    assert "Director: Christopher Nolan" in captured.out
    assert "Release year: 2014" in captured.out

# def find_movie(clear_movies, monkeypatch, capsys):
#     movies.append({
#         "title": "Dunkirk",
#         "director": "Christopher Nolan",
#         "year": "2017"
#     })

#     # with patch("builtins.input", return_value="Dunkirk"):
#     #   find_movie()
#     info_input = "Dunkirk"
#     monkeypatch.setattr('builtins.input', lambda _: info_input)
#     find_movie()
#     captured = capsys.readouterr()
#     assert "Title: Dunkirk" in captured.out
#     assert "Director: Christopher Nolan" in captured.out
#     assert "Release year: 2017" in captured.out

import pytest
from unittest.mock import patch
from app import add_movie, show_movies, find_movie, movies

@pytest.fixture(autouse=True)
def clear_movies():
    """Fixture to clear the movies list before each test."""
    movies.clear()


def test_add_movie():
    """Test adding a movie to the list."""
    movie_data = iter(["Inception", "Christopher Nolan", "2010"])

    with patch("builtins.input", side_effect=movie_data):
        add_movie()

    assert len(movies) == 1
    assert movies[0] == {
        "title": "Inception",
        "director": "Christopher Nolan",
        "year": "2010"
    }


def test_show_movies(capsys):
    """Test displaying all movies."""
    movies.append({
        "title": "Interstellar",
        "director": "Christopher Nolan",
        "year": "2014"
    })

    show_movies()

    captured = capsys.readouterr()
    assert "Title: Interstellar" in captured.out
    assert "Director: Christopher Nolan" in captured.out
    assert "Release year: 2014" in captured.out


def test_find_movie(capsys):
    """Test finding a movie by title."""
    movies.append({
        "title": "Dunkirk",
        "director": "Christopher Nolan",
        "year": "2017"
    })
    with patch("builtins.input", return_value="Dunkirk"):
        find_movie()

    captured = capsys.readouterr()
    assert "Title: Dunkirk" in captured.out
    assert "Director: Christopher Nolan" in captured.out
    assert "Release year: 2017" in captured.out

def test_movie_not_found(capsys):
    movies.append({
        "title": "Dunkirk",
        "director": "Christopher Nolan",
        "year": "2017"
    })
    with patch("builtins.input", return_value=""):
        find_movie()
    captured = capsys.readouterr()
    assert captured.out == ""
 
