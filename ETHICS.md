# Ethical Considerations

## Purpose and Transparency
The primary purpose of this project is to provide an educational dataset for researchers, artists, curators, and enthusiasts. The goal is to offer a combination of historical and commercial art data in a format that is easy to access and analyze, fostering greater understanding and appreciation of art.

The websites used in this project were chosen because they provide public or easily accessible data for research purposes. The Metropolitan Museum of Art (Met) offers an open API, while WikiArt and Saatchi Art host information on their respective platforms that is intended for public use by enthusiasts and buyers.

## Data Privacy and Intellectual Property
- **Met API**: The Met explicitly encourages public access to its collection data through its API for non-commercial purposes.
- **WikiArt and Saatchi Art**: While these platforms are not designed for bulk data scraping, scraping is done with great care to limit the number of requests to avoid overloading the servers. The data collected is used solely for educational and non-commercial purposes, and proper attribution to the source is provided wherever necessary.

All artwork, artist names, and descriptions remain the intellectual property of their respective creators, and no images are downloaded or re-used from these platforms. The scraped information is strictly limited to text data, such as artwork titles, years, prices, and links.

## Rate Limiting and Responsible Scraping
The project implements rate limiting to ensure that the scraping process does not overwhelm the servers or violate terms of service. A reasonable time interval is placed between each request to avoid excessive strain on the platforms being accessed.

No user login or private data is scraped, and scraping focuses on publicly available data. The search results are used responsibly, and the project encourages users to respect the platforms' data policies.

## Ethical Scraping Practices
We have adhered to the following ethical scraping principles:
1. **Respect Robots.txt**: Checked if the websites explicitly disallow scraping through their `robots.txt` files.
2. **Limit Requests**: Implemented rate limiting to ensure the requests to the platforms are within acceptable limits.
3. **Transparency**: Clearly communicated to users that the data is gathered from public platforms with publicly available information, and no proprietary or sensitive information is gathered.
4. **Educational Use Only**: This project is for educational purposes only and not for commercial use or exploitation of any artwork or artist.

---
