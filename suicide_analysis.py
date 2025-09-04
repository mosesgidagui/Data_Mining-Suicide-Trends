# suicide_analysis.py

import pandas as pd

# ---------------- CLASS ----------------
class CountryStats:
    def __init__(self, country, yearly_data):
        self.country = country
        self.yearly_data = yearly_data  # dictionary {year: suicide_rate}

    def average_rate(self):
        """Return the average suicide rate for this country."""
        total = sum(self.yearly_data.values())
        return total / len(self.yearly_data)


# ---------------- FUNCTIONS ----------------
def load_data(filepath):
    """Load Kaggle dataset and return DataFrame."""
    df = pd.read_csv(filepath)
    # Keep only needed columns
    df = df[["country", "year", "suicides/100k pop"]]
    return df


def group_by_country(df):
    """Group dataset into dictionary by country."""
    country_dict = {}
    for _, row in df.iterrows():
        country, year, rate = row["country"], row["year"], row["suicides/100k pop"]

        if country not in country_dict:
            country_dict[country] = {}
        country_dict[country][year] = rate
    return country_dict


def display_trends(country_dict, countries=["United States", "Japan", "India"]):
    """Print suicide rate trends by country and year."""
    for country in countries:
        if country in country_dict:
            print(f"\n--- {country} ---")
            for year, rate in sorted(country_dict[country].items()):
                print(f"{year}: {rate}")
        else:
            print(f"\nNo data for {country}")


def compare_averages(country_dict, countries=["United States", "Japan", "India"]):
    """Compare average suicide rates among selected countries."""
    stats_list = []
    for country in countries:
        if country in country_dict:
            stats = CountryStats(country, country_dict[country])
            stats_list.append((country, stats.average_rate()))

    # Sort by average suicide rate
    stats_list.sort(key=lambda x: x[1], reverse=True)

    print("\nAverage Suicide Rates by Country:")
    for country, avg in stats_list:
        print(f"{country}: {avg:.2f}")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    # Step 1: Load dataset
    df = load_data("master.csv")

    # Step 2: Group by country
    country_dict = group_by_country(df)

    # Step 3: Display trends
    display_trends(country_dict)

    # Step 4: Compare averages
    compare_averages(country_dict)
