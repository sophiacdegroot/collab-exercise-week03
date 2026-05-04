import pandas as pd

data = pd.DataFrame(
    {
        "country": ["Switzerland", "Germany", "France", "Italy", "Spain"],
        "gdp_bn_usd": [800, 4000, 2800, 2100, 1400],
        "population_mn": [8.7, 84.4, 68.2, 59.0, 47.4],
        "year": 2023,
    }
)
data["gdp_per_capita_usd"] = data["gdp_bn_usd"] / data["population_mn"] * 1000
data.to_csv("gdp_data.csv", index=False)
