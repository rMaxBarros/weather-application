# Step-by-step guide:

# Step 1: Create the page structure:
# Input field for city name.
# Button to search for the temperature.

# Step 2: Function to connect to the Weather API:
# Receive the city name entered by the user.
# Construct the API URL with the city name and API key.
# Make a GET request to the API.
# Handle potential errors and return the temperature.

# Step 3: Display a new screen to show the results:
    # Display the search results.

import flet as ft
import requests

def main (page: ft.Page):
    # Creating search field
    title = ft.Text("Weather API by Max Barros")
    page.add(title)
    city_search = ft.TextField(label="Type the city")
    page.add(city_search)

    def search_results(e):
        city = city_search.value
        api_key = "caf6f0f5d231eadf048ff6d73548951b"
        base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(base_url)
        api_data = response.json()

        if api_data["cod"] == "200":
            search_result = "The city was not found"

            # Creating the screen result for the search
            search_result = ft.Text(f"The city '{city}' was not found.")
            page.add(search_result)
            page.update()


    # Creating search button
    button = ft.ElevatedButton("Search", on_click=search_results)
    page.add(button)
    page.update()
    
ft.app(target=main)