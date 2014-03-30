import time
import urllib
import datetime
import config

while True:
    locations = {'minneapolis': '44.972845,-93.235055', 'st_paul': '44.984915,-93.185257'}

    for k, v in locations.items():
        path = 'public/json/%s-latest-weather.json' % k
        uri = 'https://api.forecast.io/forecast/%s/%s' % (config.FORECASTIO_API_KEY, v)
        now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    
        try:
            urllib.urlretrieve(uri, path)
            print "Saving current weather for %s" % k

            path = 'public/json/%s-%s-weather.json' % (k, now)
            urllib.urlretrieve(uri, path)
            print "Archiving current weather for %s" % k

        except:
            pass

    # sleep for the remaining seconds until the next 1/4 hour
    time.sleep(900-time.time()%900)
