Standupbot Dataviewer
=====================

Status
------

It's pretty sketchy right now. PRs welcome.

Usage
-----

change app.py's variable 'standupbot_url' to be the instance of your
standupbot.

.. code-block:: python

    ...
    app = Flask(__name__)
    standupbot_url = # url goes here

    def sort_by_names(data):
    ...

run `$ app.py` after sourcing the virtualenv

.. code-block:: none

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ app.py

**Endpoints**:

========================  ===========================================
``localhost:5000/``       ->  all time statuses sorted by user tagged
                          by time.
``localhost:5000/:nick``  ->  all time entries for a user tagged with
                          time.
========================  ===========================================
