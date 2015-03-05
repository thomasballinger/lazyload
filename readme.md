bpython starts up slowly in Python 2 at the moment due to importing requests taking a while - this is my temp solution

    import lazyload
    lazyload.make_lazy('requests')
    import requests # nearly instant
    requests.get    # takes 1.2 seconds

Seems to work in Python 2.7, 3.4, and 3.5 (maybe others too?)

Authors:
* Thomas Ballinger
* Joe Jevnik
