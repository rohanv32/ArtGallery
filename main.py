from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
from googlesearch import search
import pandas as pd
import json
import time

# This is a function to retrieve artwork details from the Met API
def get_met_artwork(title):
    search_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
    search_params = {"q": title}
    
    try:
        # Sending a GET request to search for the artwork
        response = requests.get(search_url, params=search_params)
        response.raise_for_status()  # Raising an exception for any HTTP errors
        object_ids = response.json().get('objectIDs', [])

        if object_ids:
            # Fetches the first object details using its object ID
            object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_ids[0]}"
            artwork_response = requests.get(object_url)
            artwork_response.raise_for_status()  # Raising an exception if request fails
            artwork_data = artwork_response.json()
            return {
                "title": artwork_data.get("title"),
                "artist": artwork_data.get("artistDisplayName"),
                "department": artwork_data.get("department"),
                "time_period": artwork_data.get("objectDate"),
                "medium": artwork_data.get("medium")
            }
        else:
            return None 
    except requests.exceptions.RequestException as e:
        print(f"Error fetching artwork from the Met: {e}")
        return None

# This is a function to perform a Google search and let the user select a WikiArt URL
def search_wikiart(artist_name, user_input):
    query = f"wikiart + {artist_name} + {user_input}"
    
    try:
        
        search_results = list(search(query, num_results=5))
        print("Select a URL from the following search results:")
        print("\n")
        for i, url in enumerate(search_results, start=1):
            print(f"{i}: {url}")

        print("\n")
        
        choice = input("Enter the number of your choice: ")

        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(search_results):
                selected_url = search_results[choice_index]
                print(f"You selected: {selected_url}")
                return selected_url
            else:
                print("Invalid choice. Please select a number from the list.")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None
    except Exception as e:
        print(f"Error performing Google search: {e}")
        return None

# This is a function to scrape famous works from WikiArt
def scrape_famous_works(selected_url):
    session = HTMLSession()
    
    try:
        # Sends a GET request to the selected WikiArt URL (rate-limited)
        response = session.get(selected_url)
        response.raise_for_status()  # Raises an exception for any HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        famous_works = []
        famous_works_section = soup.find('section', class_='wiki-layout-artists-related')

        # Extracts the famous works if the section exists
        if famous_works_section:
            print("\nFamous Works by the Artist:")
            print("=" * 30)
            artworks = famous_works_section.find_all('li')
            
            for artwork in artworks:
                title_tag = artwork.find('a', class_='truncate-target')
                year_tag = artwork.find('span', class_='artwork-year')
                
                if title_tag and year_tag:
                    artwork_title = title_tag.get('title', 'Unknown Title')
                    artwork_year = year_tag.text
                    famous_works.append({"title": artwork_title, "year": artwork_year})  # Append to list
                    print(f"- {artwork_title} ({artwork_year})")
        else:
            print("No famous works section found.")
        
        return famous_works
    except requests.exceptions.RequestException as e:
        print(f"Error scraping famous works from WikiArt: {e}")
        return []

# This is a function to scrape similar artworks from Saatchi Art
def scrape_saatchi_art(artist_name, artwork_title):
    query = f"{artist_name} {artwork_title}".replace(" ", "%20")
    url = f"https://www.saatchiart.com/all?query={query}"
    
    session = HTMLSession()
    
    try:
        
        response = session.get(url)
        response.raise_for_status()  # Raises an exception for any HTTP errors
        
        soup = BeautifulSoup(response.text, 'html.parser')
        artworks = soup.find_all('div', {'data-type': 'original'}, limit=5)
        
        saatchi_artworks = []  # List to store Saatchi artworks
        if not artworks:
            print("No artworks found.")
            return []

        print("\nSearch Results:")
        print("=" * 50)
        for artwork in artworks:
            title_tag = artwork.find('h6', {'class': 'SATypography_SATypography__h6__wqxpx'})
            artwork_title = title_tag.text.strip() if title_tag else 'Unknown Title'
            
            artist_info = artwork.find('div', {'data-type': 'artist-info'})
            if artist_info:
                artist_name_tag = artist_info.find('p', {'data-type': 'artist-name'})
                if artist_name_tag:
                    artist_name = artist_name_tag.text.strip()
                else:
                    artist_name_tag = artist_info.find('a', {'data-type': 'profile-url'})
                    artist_name = artist_name_tag['title'].split('View artist ')[-1] if artist_name_tag else 'Unknown Artist'
                
                artist_name = artist_name.replace(" profile", "").strip()
                artist_location_tag = artist_info.find('p', {'class': 'SATypography_SATypography__xsmall__a9_p3'})
                artist_location = artist_location_tag.text.strip() if artist_location_tag else 'Unknown Location'
            else:
                artist_name = 'Unknown Artist'
                artist_location = 'Unknown Location'
            
            price_section = artwork.find('div', {'data-type': 'prices'})
            price_tag = price_section.find('h6') if price_section else None
            price = price_tag.text.strip() if price_tag else 'Price not available'
            
            link_tag = artwork.find('a', href=True)
            artwork_link = link_tag['href'] if link_tag else 'No link available'

            saatchi_artworks.append({
                "title": artwork_title,
                "artist": artist_name,
                "location": artist_location,
                "price": price,
                "link": artwork_link
            })  # Append to list

            print(f"Title: {artwork_title}")
            print(f"Artist: {artist_name}")
            print(f"Location: {artist_location}")
            print(f"Price: {price}")
            print(f"Link: {artwork_link}")
            print("-" * 50)

        return saatchi_artworks
    
    except requests.exceptions.RequestException as e:
        print(f"Error scraping similar artworks from Saatchi Art: {e}")
        return []

if __name__ == "__main__":
    
    user_input = input("Enter the name of the artwork you'd like to take a look at (e.g. Bridge over a Pond of Water Lilies: ")
    artwork_data = get_met_artwork(user_input)
    
    if artwork_data:

        print("\n--- Artwork Details ---")
        print(f"Title: {artwork_data.get('title', 'N/A')}")
        print(f"Artist: {artwork_data.get('artist', 'Unknown')}")
        print(f"Department: {artwork_data.get('department', 'N/A')}")
        print(f"Medium: {artwork_data.get('medium', 'N/A')}")
        print("\n\n")
        
        selected_url = search_wikiart(artwork_data['artist'], user_input)
        
        famous_works = []
        if selected_url:
            # Rate-limiting to avoid overwhelming the server
            time.sleep(2)  # Pauses for 2 seconds before scraping
            
            famous_works = scrape_famous_works(selected_url)
            saatchi_artworks = scrape_saatchi_art(artwork_data["artist"], user_input)
            
            # Creates the DataFrames for famous works and similar artworks
            famous_works_df = pd.DataFrame(famous_works)
            saatchi_artworks_df = pd.DataFrame(saatchi_artworks)

            combined_data = {
                "Famous Works": famous_works_df.to_dict(orient='records'),
                "Similar Artworks": saatchi_artworks_df.to_dict(orient='records')
            }

            # Saves the dataset as JSON
            with open('artworks_dataset.json', 'w') as f:
                f.write(json.dumps(combined_data, indent=4))
            print("Dataset saved as 'artworks_dataset.json'.")

            # Saves the dataset as CSV
            combined_df = pd.concat([famous_works_df, saatchi_artworks_df], axis=0, ignore_index=True)
            combined_df.to_csv('artworks_dataset.csv', index=False)
            print("Dataset saved as 'artworks_dataset.csv'.")
