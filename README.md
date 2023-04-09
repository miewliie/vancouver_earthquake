# Vancouver earthquake

- Tweet and Toot about earthquake around 500km from Vancouver.
- The source of earthquake data: https://earthquake.usgs.gov/
- Toot account: https://mastodon.world/@vancouver_earthquake

**Example:**

<img width="557" alt="example_map" src="https://user-images.githubusercontent.com/20311850/222842352-8f2b019a-5b65-41d9-b252-cf0a7b105620.png">


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
