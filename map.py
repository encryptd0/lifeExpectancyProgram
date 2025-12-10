import requests
import pandas as pd
import plotly.express as px
import webbrowser

country_codes = [
    "USA", "ZWE", "AFR", "ZMB", "JPN", "ZAF",
    "AFG", "ALB", "DZA", "AND", "AGO", "ATG", "ARG", "ARM", "AUS", "AUT",
    "AZE", "BHS", "BHR", "BGD", "BRB", "BLR", "BEL", "BLZ", "BEN", "BMU",
    "BTN", "BOL", "BIH", "BWA", "BRA", "BRN", "BGR", "BFA", "BDI", "CPV",
    "KHM", "CMR", "CAN", "CAF", "TCD", "CHL", "CHN", "COL", "COM", "COG",
    "CRI", "CIV", "HRV", "CUB", "CYP", "CZE", "DNK", "DJI", "DMA", "DOM",
    "ECU", "EGY", "SLV", "GNQ", "GBR", "ERI", "EST", "SWZ", "ETH", "FJI", 
    "FIN", "FRA", "GAB", "GMB", "GEO", "DEU", "GHA", "GRC", "GRD", "GTM", 
    "GUY", "HTI", "HND", "HUN", "ISL", "IND", "IDN", "IRN", "IRQ", "IRL",
    "ISR", "ITA", "JAM", "JOR", "KAZ", "KEN", "KIR", "KOR", "KWT", "KGZ",
    "LAO", "LVA", "LBN", "LSO", "LBR", "LBY", "LIE", "LTU", "LUX", "MDG"
    "MWI", "MYS", "MDV", "MLI", "MLT", "MHL", "MRT", "MUS", "MEX", "FSM",
    "MDA", "MCO", "MNG", "MNE", "MAR", "MOZ", "MMR", "NAM", "NRU", "NPL",
    "NLD", "NZL", "NIC", "NER", "NGA", "MKD", "NOR", "OMN", "PAK", "PLW",
    "PSE", "PAN", "PNG", "PRY", "PER", "PHL", "POL", "PRT", "QAT", "ROU",
    "RUS", "RWA", "KNA", "LCA", "VCT", "WSM", "SMR", "STP", "SAU", "SEN",
    "SRB", "SYC", "SLE", "SGP", "SVK", "SVN", "SLB", "SOM", "SSD", "ESP",
    "LKA", "SDN", "SUR", "SWE", "CHE", "SYR", "TJK", "TZA", "THA", "TLS",
    "TGO", "TON", "TTO", "TUN", "TUR", "TKM", "TUV", "UGA", "UKR", "ARE",
    "URY", "UZB", "VUT", "VAT", "VEN", "VNM", "YEM", "ZMB", "ZWE", "GIN",
]

data_list = []

for code in country_codes:
    
    url = f"https://ghoapi.azureedge.net/api/WHOSIS_000001?$filter=SpatialDim eq '{code}' and TimeDim eq 2021 and Dim1 eq 'SEX_BTSX'"
    r = requests.get(url)
    json_data = r.json()

    if json_data["value"]:
        life_expectancy = json_data["value"][0]["NumericValue"]
        data_list.append((code, life_expectancy))
        print(code, life_expectancy)
    else:
        pass

# Create a data frame cloropleth should use 
data_frame = pd.DataFrame(data_list, columns=["country_code", "life_expectancy"])

# Create a chloropleth figure with the necessary lables and details 
fig = px.choropleth(
    data_frame,
    locations="country_code",
    color="life_expectancy",
    color_continuous_scale="Viridis",
    title=f"Life Expectancy by Country in 2021"
)

# Write to html and open 
fig.write_html("life_expectancy_map.html")
webbrowser.open("life_expectancy_map.html")

