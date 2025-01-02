# Generic Web Scraper

This is a generic web scraper built using Python, designed to extract data from any website by specifying the URL, HTML tag, and optional filters. The extracted data is saved into a CSV file for further analysis.

## Features
- Accepts any website URL for scraping.
- Supports filtering by HTML tags and attributes (e.g., `class`, `id`).
- Saves scraped data to a CSV file.
- Configurable headers for HTTP requests.
- Modular and reusable codebase.

## Project Structure
```
generic_scraper/
├── README.md
├── requirements.txt
├── .gitignore
├── config/
│   ├── settings.py
├── data/
│   ├── output.csv
├── logs/
│   ├── scraper.log
├── src/
│   ├── __init__.py
│   ├── scraper.py
│   ├── utils.py
├── tests/
│   ├── test_scraper.py
├── main.py
```

## Prerequisites
- Python 3.7 or higher
- Pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/generic_scraper.git
   cd generic_scraper
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```

2. Provide the required inputs when prompted:
   - **Website URL**: The URL of the website to scrape (e.g., `https://example.com`).
   - **HTML Tag**: The tag to scrape (e.g., `h2`, `div`).
   - **Attribute** (optional): The attribute to filter by (e.g., `class`, `id`).
   - **Attribute Value** (optional): The value of the attribute to filter by.

3. The scraped data will be saved as a CSV file in the `data/` folder.

## Example Input
```
Enter the website URL: https://example.com
Enter the HTML tag to scrape (e.g., 'h2', 'div'): h2
Enter the attribute to filter by (optional, e.g., 'class', 'id'): class
Enter the value of the attribute (optional): header-title
```

## Output
- The extracted data will be saved in the `data/` folder as a CSV file. For example:
  ```
  data/output_example_com.csv
  ```

## Configuration

### HTTP Headers
You can customize the request headers in `config/settings.py`:
```python
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
```

## Logging
Logs are saved in the `logs/` folder. You can view the scraping activity in `scraper.log`.

## Testing
1. Install `pytest` if not already installed:
   ```bash
   pip install pytest
   ```
2. Run the tests:
   ```bash
   pytest tests/
   ```

## Future Enhancements
- Add pagination support for multi-page scraping.
- Integrate Selenium or Playwright for JavaScript-heavy websites.
- Schedule periodic scraping using `cron` or `APScheduler`.
- Dockerize the project for easier deployment.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

