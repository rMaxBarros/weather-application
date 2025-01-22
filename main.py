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

