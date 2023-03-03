# Vancouver earthquake

- Tweet and Toot about earthquake around 500km from Vancouver.
- The source of earthquake data: https://earthquake.usgs.gov/
- Toot account: https://mastodon.world/@vancouver_earthquake
- Tweet account: https://twitter.com/bc_earthquake

Example:

![example_map](https://user-images.githubusercontent.com/20311850/222644497-329c4458-c149-42a3-89ff-7a2e14f90779.png)


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
