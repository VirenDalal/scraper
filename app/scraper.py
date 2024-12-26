import requests
from bs4 import BeautifulSoup
import aiohttp
import asyncio
from typing import List, Optional

class Scraper:
    def __init__(self, database=None, notifier=None, cache=None):
        self.database = database
        self.notifier = notifier
        self.cache = cache

    async def fetch_page(self, session, url: str) -> str:
        async with session.get(url) as response:
            return await response.text()

    async def scrape_page(self, page_url: str, filters: dict = None) -> List[dict]:
        products = []
        links = []
        if "https://dentalstall.com/product/" not in page_url:
            async with aiohttp.ClientSession() as session:
                page_content = await self.fetch_page(session, page_url)
                soup = BeautifulSoup(page_content, 'html.parser')
                a_tags = soup.find_all('a')
                for a_tag in a_tags:
                    href = a_tag.get('href')
                    if href and "https://dentalstall.com/product/" in str(href):
                        # print(href)
                        links.append(href)
        else:
            links.append(page_url)

        async with aiohttp.ClientSession() as session:
            for link in set(links):

                try:
                    product_info = {"product_title":"", "product_price":0, "path_to_image":"", }
                    finla_page_content = await self.fetch_page(session, link)
                    soup = BeautifulSoup(finla_page_content, 'html.parser')
                    image_links = []
                    a_tags = soup.find_all('a')

                    product_title = soup.find('h1', class_="product_title entry-title")
                    price =  soup.find('span', class_='woocommerce-Price-amount')


                    product_info["product_title"]  = product_title.text.strip()
                    product_info["product_price"]  = float(price.text.strip()[1:])


                    for a_tag in a_tags:
                        href = a_tag.get('href')
                        if href and "https://dentalstall.com/wp-content/uploads/" in str(href):
                            # print(href)
                            image_links.append(href)

                    product_info["path_to_image"] = image_links
                    products.append(product_info)
                except:
                    print(" exception while parsing link ", link)


        return products

    async def scrape(self, settings: dict) -> List[dict]:
        base_url = "https://dentalstall.com/product-category/{}"
        category = settings['categories'][0]  # Assuming one category per scrape
        page_limit = settings.get('page_limit', 1)
        filters = settings.get('filters', {})
        sort_by = settings.get('sort_by', 'price')

        all_products = []

        for page_num in range(1, page_limit + 1):
            if page_num !=1:
                page_url = f"{base_url.format(category)}/page/{page_num}/"
            else:
                page_url = f"{base_url.format(category)}/"
            if filters:
                page_url += f"?min_price={filters.get('min_price', 0)}&max_price={filters.get('max_price', 1000)}&orderby={sort_by}"
            products = await self.scrape_page(page_url, filters)
            all_products.extend(products)

        # You can process the data here (e.g., saving to database or cache)
        if self.database:
            self.database.save_products(all_products)
        #
        if self.notifier:
            self.notifier.notify(f"{len(all_products)} products scraped from url {page_url}")

        return all_products

