import pandas as pd

def save_to_csv(data, output_file):
    """
    Save the scraped data to a CSV file.

    Args:
        data (list): List of scraped data.
        output_file (str): Path to save the CSV file.
    """
    df = pd.DataFrame({"Data": data})
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")
