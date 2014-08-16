"""Converters that turn poetry to tracks"""
from itertools import chain, combinations
import logging

from spotify import Spotify


def partition(iterable, chain=chain, map=map):
    """Creates all ordered groupings of a given iterable. From:
    http://code.activestate.com/recipes/576795/"""
    s = iterable if hasattr(iterable, '__getslice__') else tuple(iterable)
    n = len(s)
    first, middle, last = [0], range(1, n), [n]
    getslice = s.__getslice__
    return [map(getslice, chain(first, div), chain(div, last))
            for i in range(n) for div in combinations(middle, i)]


def split_multiple(text, sep_list):
    """Splits a text on multiple separators"""
    rvs = [text]
    for s in sep_list:
        rvs = [split for splits in [rv.split(s) for rv in rvs] for split in splits]
    return rvs


class Hit(object):
    """Represents a hit for a whole sentence or segment of words"""

    def __init__(self, match_count, sp_tracks, partition):
        """
        Parameters
        ----------
        match_count : int
            Number of words matched by tracks
        sp_tracks : list
            List of spotify.Tracks
        partition : list
            List of word groupings
        """
        self.match_count = match_count
        self.sp_tracks = sp_tracks
        self.partition = partition


class SimpleTrackConverter(object):
    def __init__(self, sp=Spotify):
        self.sp = Spotify()

    def line_to_song(self, line):
        """
        Finds the tracks on Spotify that match the most words using the least
        amount of tracks.

        Parameters
        ----------
        line: str
            A line or segment of words

        Returns
        -------
        hit : Hit
            Best hit for the segment
        """
        par = partition(line.split())

        best_hit = Hit(0, [None], [line])
        for p in par:
            matched_words = 0
            sp_tracks = []

            # group in partition
            for n in p:
                sp_track = self.sp.search_track(" ".join(n))
                if sp_track:
                    matched_words += len(n)
                sp_tracks.append(sp_track)

            # store the hit only if it is better
            if matched_words > best_hit.match_count:
                best_hit = Hit(matched_words, sp_tracks, [" ".join(n) for n in p])
            # take the one using the least amount of tracks if the number of
            # matched words is equal
            if matched_words == best_hit.match_count:
                if len(sp_tracks) < best_hit.sp_tracks:
                    best_hit = Hit(matched_words, sp_tracks, [" ".join(n) for n in p])

        return best_hit

    def poem_to_song(self, text):
        """
        Splits up the text at newlines, ',' '(' ')' and '-'.

        Parameters
        ----------
        text: str
            A poem of possibly multiple lines

        Returns
        -------
        hit : Hit
            Best hits for each segment of the text
        """
        sentences = split_multiple(text, ["\n", ",", "(", ")", "-"])
        logging.debug(sentences)
        hits = []
        for s in sentences:
            hits.append(self.line_to_song(s))
        return hits
