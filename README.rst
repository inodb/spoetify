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


Ideas for improvements
----------------------
- Add better caching. Now it's just per request in a dict. Maybe Redis.
- Add parallelization of query searching. Does everything sequentially now.
- Take suboptimal with specified time limit.
- Try other things than just searching titles, perhaps matching lyrics or
  emotional content of the lyrics and the poem.
