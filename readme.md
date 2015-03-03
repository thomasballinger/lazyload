bpython loads slowly at the moment due to importing requests taking a while - this is my temp solution


    import lazyload
    lazyload.make_lazy('requests')
    import requests # nearly instant
    requests.get    # takes 1.2 seconds
