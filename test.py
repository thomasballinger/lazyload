
import time
t0 = time.time()

import lazyload; lazyload.make_lazy('requests')

t1 = time.time()
import requests

t2 = time.time()
requests.get
t3 = time.time()
import requests
t4 = time.time()

print 'time to make requests lazyloaded:', t1 - t0
print 'time to lazyload requests:', t2 - t1
print 'time to really load requests:', t3 - t2
print 'time to import requests again:', t4 - t3
