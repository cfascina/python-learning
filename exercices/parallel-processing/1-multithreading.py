from urllib.request import urlopen
from multiprocessing.pool import ThreadPool
import time

pool = ThreadPool(1)
url_list = [
    'http://www.python.org/',
    'http://www.yahoo.com/',
    'http://www.scala.org/',
    'http://www.google.com/']
start_time = time.time()

print(f"With 1 workers:")
for url in pool.map(urlopen, url_list):
    print(f"{url.geturl()} took {time.time() - start_time:.5f} seconds.")

pool.close()
pool.join()

pool = ThreadPool(4)
url_list = [
    'http://www.python.org/',
    'http://www.yahoo.com/',
    'http://www.scala.org/',
    'http://www.google.com/']
start_time = time.time()

print(f"\nWith 4 workers:")
for url in pool.map(urlopen, url_list):
    print(f"{url.geturl()} took {time.time() - start_time:.5f} seconds.")

pool.close()
pool.join()
