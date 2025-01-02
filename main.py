from src.scraper import scrape_website

if __name__ == "__main__":
    # Accept user input
    url = input("Enter the website URL: ").strip()
    tag = input("Enter the HTML tag to scrape (e.g., 'h2', 'div'): ").strip()
    attribute = input("Enter the attribute to filter by (optional, e.g., 'class', 'id'): ").strip() or None
    value = input("Enter the value of the attribute (optional): ").strip() or None

    print("Starting the scraper...")
    data = scrape_website(url, tag, attribute, value)
    print(f"Scraping complete! Extracted {len(data)} items.")
