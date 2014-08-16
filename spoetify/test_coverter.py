"""Test converter module"""
from spoetify.converter import SimpleTrackConverter
from nose.tools import assert_equal


def test_line_to_song():
    hit = SimpleTrackConverter().line_to_song("My love")
    assert_equal(len(hit.sp_tracks), 1)
    assert_equal(hit.sp_tracks[0].id, "0idc0XRnLRovVqpWnGQ6hC")


def test_poem_to_song():
    hits = SimpleTrackConverter().poem_to_song("I love food, you know me\nThat's why I love you so, avocado")
    print hits
    assert_equal(len(hits), 4)
    assert_equal(hits[0].sp_tracks[0].id, "09lLvyXul4ekZQ3nfPNXLI")
    assert_equal(hits[1].sp_tracks[0].id, "099TPpEaCSjEwysWZeTZv1")
    assert_equal(hits[2].sp_tracks[1].id, "4lLmG1fatRUgnRz0Ol0WUi")
    assert_equal(hits[3].sp_tracks[0].id, "1UyzA43l3OIcJ6jd3hh3ac")
