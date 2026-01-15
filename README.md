# Life Expectancy Map

**Python · Plotly · WHO API**

An interactive data visualization tool that gathers global life expectancy data from the **World Health Organization (WHO)** and displays it on a world choropleth map.

Designed as a lightweight analytics and visualization project suitable for portfolios, data demos, and automation showcases.

---

## Features

- Automatically fetches life expectancy data from the WHO API
- Supports multiple countries using ISO-3 country codes
- Processes data using **Pandas**
- Generates an interactive **Plotly** choropleth map
- Exports results to a standalone HTML file
- Opens visualization automatically in your browser

---

## How It Works

1. Queries the WHO Global Health Observatory API
2. Extracts life expectancy at birth (both sexes)
3. Stores results in a **Pandas DataFrame**
4. Renders an interactive world map using **Plotly**
5. Saves output as `life_expectancy_map.html`

---

## Installation

Clone the repository and install dependencies:

```bash
pip install requests pandas plotly
````

---

## Usage

Run the script directly:

```bash
python main.py
```

The interactive map will open automatically in your default web browser.

---

## Data Source

* **WHO Global Health Observatory (GHO) API**
* Indicator: Life expectancy at birth
* Year: 2021
* Sex: Both sexes combined

---

## Tech Stack

* Python 3
* requests
* pandas
* plotly.express
* webbrowser

---

## Notes

* Some countries may not return data due to missing WHO records
* Country coverage depends on API availability
* Data is fixed to the year 2021 in the current version

> This tool demonstrates visualization and data handling — it does **not** replace official statistical analysis tools.

This project is intended as a learning and portfolio showcase.

---

## License

MIT License


