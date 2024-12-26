Overview
This scraper is designed to extract product details (name, price, and image URL) from https://dentalstall.com. 
It supports optional filters like price range and sorting.  Ypu can scrap using the category , exact product name, or a string.
The scraper uses FastAPI for serving an API endpoint to trigger the scraping process.


Requirements
Step 1:Create and activate a virtual environment (optional but recommended)
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
Step 2: Install the required packages
    pip install -r requirements.txt



Project Structure
scrapper/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── database.py
│   ├── models.py
│   ├── notification.py
├── requirements.txt
└── run.py


Running the Scraper
Go to folder and the run below command and then open the swagger for this (http://localhost:8080/docs)
    python run.py








Input Format

Sample Input: Scraping With Product name (3 Pages)
{
  "name": "Waldent Air-Motor Engine"
  
}

Sample Input: Scraping With any matching string name (3 Pages)

{
  "word": "chair",
  "page_limit": 2
}

Sample Input : Scraping with Price Range Filter
{
  "categories": "orthodontics",
  "page_limit": 2,
  "filters": {
    "min_price": 50,
    "max_price": 150
  },
  "sort_by": "price"
}


Sample Input : Scraping Without Filters (3 Pages)
{
  "categories": "orthodontics",
  "page_limit": 3,
  "filters": {},
  "sort_by": "date"
}



Expected Output
Successful Scraping Response

{
  "scraped_count": 10,
  "scraped_products": [
    {
      "product_title": "Orthodontic Braces Kit",
      "product_price": 125.00,
      "path_to_image": "/path/to/image.jpg"
    },
    {
      "product_title": "Dental Braces Retainer",
      "product_price": 99.00,
      "path_to_image": "/path/to/another_image.jpg"
    },
    ...
  ]
}

It  will also save the data in product.json file.

default username and password for testing are mention below
username - test
password - password



