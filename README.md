# Chicago Hauntings Map

An interactive heatmap of reported hauntings across Chicago, Illinois.

## [👻 View the interactive map](https://khushanshahad.github.io/Hauntings/)

Zoom and pan to explore. Brighter, warmer areas have more reported hauntings, and the black outline marks the Chicago city boundary.

## About

This project takes a dataset of reported haunted locations, filters it down to Chicago, IL, and plots each location as a heatmap layer over the city boundary. It is a fork of an existing Hauntings project, modified to focus only on Chicago.

## How it works

1. Loads `hauntings.csv` with pandas.
2. Keeps only rows where the city is Chicago and the state is Illinois (so other towns named Chicago are excluded), and drops rows with missing coordinates.
3. Downloads the Chicago city boundary as GeoJSON from the [Chicago Data Portal](https://data.cityofchicago.org/).
4. Builds the map with [folium](https://python-visualization.github.io/folium/) and saves it as `index.html`.
5. Prints summary stats using helper functions in `auxiliaryFunctions.py`.

## Run it yourself

```bash
git clone https://github.com/khushanshahad/Hauntings.git
cd Hauntings
pip install pandas folium
python main.py
```

Then open `index.html` in your browser.

> Note: update the `file_path` near the top of the script to point to wherever `hauntings.csv` is on your computer.

## Built with

- Python
- [pandas](https://pandas.pydata.org/)
- [folium](https://python-visualization.github.io/folium/)
- [Chicago Data Portal](https://data.cityofchicago.org/) for the city boundary

## Credits

Forked from the original Hauntings project. Chicago-specific changes by [Khushan Shahad](https://github.com/khushanshahad).
