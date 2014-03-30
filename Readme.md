# Forecast.io Archive

This is a simple Python script to retrieve and save JSON from the [forecast.io](http://forecast.io) API.

Right now the script is configured to download, save and archive JSON for Minneapolis & St. Paul, MN every 15 minutes. This keeps the threshold well below the 1,000 free API calls per day and gives me plenty of data to work with.

To get started, copy config-template.py to config.py and provide your own API key. Then run `python forecast.py`.

## TODO

* Set up an API of my own to return JSONP responses from this data.
* Provide support for locations based on latitude and longitude coordinates