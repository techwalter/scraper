import requests
from bs4 import BeautifulSoup
from config.settings import HEADERS
from src.utils import save_to_csv

def scrape_website(url, tag, attribute=None, value=None):
    """
    Scrape a website based on the provided tag and optional filters.

    Args:
        url (str): The URL of the website to scrape.
        tag (str): The HTML tag to scrape (e.g., 'h2', 'div').
        attribute (str, optional): The attribute to filter by (e.g., 'class', 'id'). Defaults to None.
        value (str, optional): The value of the attribute to filter by. Defaults to None.

    Returns:
        list: A list of scraped text content.
    """
    try:
        # Make an HTTP GET request
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Filter elements
        if attribute and value:
            elements = soup.find_all(tag, {attribute: value})
        else:
            elements = soup.find_all(tag)

        # Extract text from elements
        data = [element.text.strip() for element in elements]

        # Save to file
        save_to_csv(data, f"data/output_{url.replace('https://', '').replace('.', '_')}.csv")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
