# Vancouver earthquake
- Tweet and Toot about earthquake around 500km from Vancouver.
- The source of earthquake data: https://earthquake.usgs.gov/
- Toot account: https://mastodon.world/@vancouver_earthquake
- Tweet account: https://twitter.com/bc_earthquake

### Prerequisites 
1. Request earthquake data from usgs.gov
```
cd api/
python3 earthquake_api.py
```

### Toot earthquake to Mastodon
```
python3 toot.py
```
