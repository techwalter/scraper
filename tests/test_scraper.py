from src.scraper import scrape_data

def test_scrape_data():
    data = scrape_data()
    assert isinstance(data, list)
    assert len(data) > 0
