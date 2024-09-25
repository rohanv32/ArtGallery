# ArtGallery
Projects in Programming and Data Sciences - Project 3

# Art Scraper and Dataset Builder

## Project Overview

This project retrieves artwork details from **The Metropolitan Museum of Art (Met) Collection API** and web scrapes related famous artworks and similar pieces from **WikiArt** and **Saatchi Art**. The purpose is to create a dataset that captures important artwork metadata (e.g., title, artist, time period, medium) from reputable online sources. 

The primary object of this dataset would be to aid art enthusiasts find and locate similar works of art, and those that are more accessible, baesd on the details of the wokrs of art they have liked and enjoy.

The project combines three main data sources:
- **The Metropolitan Museum of Art Collection API**: Provides structured and reliable data about artworks, created by the Metropolitan Museum of Art.
- **WikiArt**: Popular platform offering a rich reference collection of contemporary and classic artworks.
- **Saatchi Art**: An online gallery where you can find works of art suited to your interests from artists across the world.

## Data Collected

The project collects the following information:
- **The Metropolitan Museum of Art Collection API**: The title, artist, department, medium, and time period of the queried artwork.
- **WikiArt Scraper**: List of related famous artworks by the same artist, including their titles and years.
- **Saatchi Art Scraper**: Similar artworks, including the title, artist, location, price, and link to the artwork for sale.

This dataset helps users understand art from a historical and commercial perspective, connecting notable works to similar contemporary or available-for-purchase pieces.

### Why This Dataset is Valuable

Art datasets are typically siloed, meaning information about famous artworks and commercially available works are often separated. The combination of data from both **Met**, **WikiArt**, and **Saatchi Art** provides a unified perspective:
- **For researchers**: Offers an understanding of how modern and historical works influence each other.
- **For art enthusiasts or collectors**: Enables discovery of affordable, similar works available for purchase.
- **For curators**: Provides a broader view of related artwork across different collections.

This data is not freely available as a unified dataset because many art platforms protect their data for commercial purposes. However, combining freely accessible APIs and web scraping bridges this gap for non-commercial, educational, or research use.

## How to Run the Project

### Prerequisites
- Python 3.x
- Git

### Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/art-scraper-dataset.git
    cd art-scraper-dataset
    ```

2. **Install Dependencies**:
    Install the required Python packages using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Program**:
    The program allows you to input an artwork's name, searches for data from the Met API, WikiArt, and Saatchi Art, and then outputs the combined data in both JSON and CSV formats.
    ```bash
    python main.py
    ```

    You will be prompted to input the name of an artwork, and the program will guide you through selecting relevant web search results and scraping data.

4. **Output**:
    - `artworks_dataset.json`: Structured dataset in JSON format.
    - `artworks_dataset.csv`: Tabular dataset in CSV format.

## Example

If you enter `The Water Lily Pond`, for example, the program will retrieve details from the Met's collection, search WikiArt for related pieces from Claude Monet, and show commercially available similar artworks on Saatchi Art.
