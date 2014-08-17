====================
Spoetify
====================

Spoetify is a website built in Flask that takes a poem and turns it into a
list of Spotify songs using the `Spotify Web API`_.

Check out the demo at `spoetify.herokuapp.com <http://bit.ly/spoetify-heroku>`_

.. _`Spotify Web API`: https://developer.spotify.com/web-api/

Requirements
-------------
* Python 2.7+
* `requirements.txt <requirements.txt>`_


Installation
------------
Download the repository:

::

    git clone https://github.com/inodb/spoetify
    cd spoetify

Install dependencies with pip:

::

    pip install -r requirements.txt

Run the tests:

::

    nosetests


Run the webserver
-----------------
::

    python spoetify/app.py
    
    
How is the text converted to songs?
------------------------------------
The input text is split on every newline and comma. Then every ordered
grouping of words from thus constructed "sentences" is searched with the `Spotify Web API`_. Only exact lowercase 
matches of titles are used in the result. Some songs end with ``- Live`` or 
something similar, so everything behind ``-`` is trimmed as well before matching.
For caching in-between results from Spotify a dictionary is used on a per request basis. From
all the ordered grouping of words, the best grouping is the one that matches
the most number of words using the fewest number of songs. All the necessary functions
for this functionality are in this notebook:

http://nbviewer.ipython.org/github/inodb/spoetify/blob/master/notebooks/algorithm.ipynb


Ideas for improvements
----------------------
- Create a playlist with resulting songs
- Add better caching. Now it's just per request in a dict. Maybe Redis.
- Add parallelization of query searching. Does everything sequentially now.
- Take suboptimal with specified time limit.
- Try other things than just searching titles, perhaps matching lyrics or
  emotional content of the lyrics and the poem.
