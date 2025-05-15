import geopy
import geopy.distance
import pandas as pd
from random import shuffle
import time
from geopy.geocoders import Nominatim


def create_cities_dataframe():
    # Create a list of 25 big cities from U.S."
    # This is a list of 25 big cities from U.S.
    #
    cities = [
        "New York, NY",
        "Los Angeles, CA",
        "Chicago, IL",
        "Houston, TX",
        "Phoenix, AZ",
        "Philadelphia, PA",
        "San Antonio, TX",
        "San Diego, CA",
        "Dallas, TX",
        "San Jose, CA",
        "Austin, TX",
        "Jacksonville, FL",
        "Fort Worth, TX",
        "Columbus, OH",
        "San Francisco, CA",
        "Charlotte, NC",
        "Indianapolis, IN",
        "Seattle, WA",
        "Denver, CO",
        "Washington, DC",
        "Boston, MA",
        "El Paso, TX",
        "Nashville, TN",
        "Detroit, MI",
        "Oklahoma City, OK",
        "Portland, OR",
        "Las Vegas, NV",
    ]

    # Create a list to hold the latitudes and longitudes
    latitudes = []
    longitudes = []

    # Loop through the list of cities and add the latitudes and longitudes to the lists
    for city in cities:
        location = geopy.geocoders.Nominatim(user_agent="my_geocoder").geocode(
            city, timeout=50
        )
        latitudes.append(location.latitude)
        longitudes.append(location.longitude)
        time.sleep(1)  # Sleep for 1 second to avoid hitting the API too hard

    # Create a dataframe with the latitudes and longitudes
    df = pd.DataFrame(
        {
            "City": cities,
            "Latitude": latitudes,
            "Longitude": longitudes,
        }
    )
    return df


def tsp(cities_df):
    """Traveling salesman problem using brute force to find the shortest path
    Args:
        cities_df (pd.DataFrame): A dataframe with the cities and their latitudes and longitudes
    Returns:
        pd.DataFrame: A dataframe with the distances between the cities
    """
    # Create a list of the cities
    cities_list = cities_df["City"].tolist()

    # Shuffle the list of cities
    shuffle(cities_list)
    print(f"Randomly shuffled cities: {cities_list}")

    # Create a list to hold the distances
    distances = []

    # Loop through the list of cities and calculate the distances
    for i in range(len(cities_list)):
        for j in range(i + 1, len(cities_list)):
            city1 = cities_list[i]
            city2 = cities_list[j]
            coords_1 = (
                cities_df.loc[cities_df["City"] == city1, "Latitude"].values[0],
                cities_df.loc[cities_df["City"] == city1, "Longitude"].values[0],
            )
            coords_2 = (
                cities_df.loc[cities_df["City"] == city2, "Latitude"].values[0],
                cities_df.loc[cities_df["City"] == city2, "Longitude"].values[0],
            )
            distance = geopy.distance.distance(coords_1, coords_2).miles
            distances.append((city1, city2, distance))

    # Sort the distances by distance
    distances.sort(key=lambda x: x[2])

    # Create a dataframe with the distances
    df = pd.DataFrame(distances, columns=["City 1", "City 2", "Distance"])
    return df
