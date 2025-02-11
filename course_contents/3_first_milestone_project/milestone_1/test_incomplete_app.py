import pytest
import unittest.mock 
import patch, mock_open
from io import StringIO
from incomplete_app import add_movie, load_movies, list_movies, find_movie

