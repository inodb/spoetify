"""Test Spotify module"""
from spoetify.spotify import Spotify
from nose.tools import assert_equal


def test_search_track():
    sp = Spotify()
    t = sp.search_track("avocado")
    assert_equal(t.id, "1UyzA43l3OIcJ6jd3hh3ac")
