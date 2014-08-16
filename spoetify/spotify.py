"""Interactions with Spotify Website"""
import requests


class Track(object):
    """Stores Spotify track information"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "TracK(id={id},name={name})".format(id=self.id, name=self.name)


class Spotify(object):
    """Access the Spotify Web API"""
    def __init__(self, api_url="https://api.spotify.com/v1/"):
        self.api_url = api_url
        self._search_track_cache = {}

    def clear_cache(self):
        """Reset the cache dictionary"""
        self._search_track_cache = {}

    def sanatize_title(self, track):
        """Sanatizes track title. Capitalization does not matter. Traling '-',
        such as '- Live' are removed."""
        return track.split("-")[0].strip().lower()

    def search_track(self, track, exact_title=True):
        """
        Search for a track title on Spotify. Results are cached.

        Parameters
        ----------
        track: str
            Title of the track to search
        exact_title : bool, optional
            Whether the title should exactly match. Track title is sanatized
            with sanatize_track_title() before matching.

        Returns
        -------
        track : Track
            Track object of the first hit otherwise None
        """
        try:
            t = self._search_track_cache[(track, exact_title)]
        except KeyError:
            url = self.api_url + 'search?q="{name}"&type=track&limit={limit}'.format(name=track.replace(" ", "%20"), limit=1)
            r = requests.get(url)
            j = r.json()
            if j["tracks"]["total"] > 0:
                # Check exact match
                t0 = j["tracks"]["items"][0]
                if not exact_title or self.sanatize_title(t0["name"]) == self.sanatize_title(track.lower()):
                    t = Track(t0["id"], t0["name"])
                else:
                    t = None
            else:
                t = None
            self._search_track_cache[(track, exact_title)] = t
        return t
