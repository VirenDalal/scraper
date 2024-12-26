from fastapi import APIRouter

from app.scraper import Scraper
from app.database import JSONDatabase
from app.notification import ConsoleNotifier
from app.cache import Cache
from app.models import ScrapeSettings

router = APIRouter()



db = JSONDatabase(file_path="products.json")
notifier = ConsoleNotifier()
cache = Cache()
scraper = Scraper(database=db, notifier=notifier, cache=cache)
from fastapi import APIRouter

from app.scraper import Scraper
from app.database import JSONDatabase
from app.notification import ConsoleNotifier
from app.cache import Cache
from app.models import ScrapeSettings,ScrapeSettingsName,ScrapeSettingsWord
from pydantic import BaseModel


router = APIRouter()




database = JSONDatabase(file_path="products.json")
notifier = ConsoleNotifier()
cache = Cache()
scraper = Scraper(database, notifier, cache)

@router.post("/scrape/product/name/",description = "mention any product name from the website and this endpoint will scrap")
async def scrape(settings: ScrapeSettingsName):

    # Call the scrape method with the necessary arguments
    scraped_products = await scraper.scrapeproduct(
        settings.dict()
    )

    # Return a response with the scraped products (or just their count)
    return {"scraped_count": len(scraped_products), "scraped_products": scraped_products}


@router.post("/scrape/word/",description = "provide any search string in input. it will scrap. for example you want to scrap all chair data the use this endpoint")
async def scrape(settings: ScrapeSettingsWord):

    # Call the scrape method with the necessary arguments
    scraped_products = await scraper.scrapeString(
        settings.dict()
    )

    # Return a response with the scraped products (or just their count)
    return {"scraped_count": len(scraped_products), "scraped_products": scraped_products}



@router.post("/scrape/category/",description = "mention any product category and this will scapr product from that category")
async def scrape(settings: ScrapeSettings):

    # Call the scrape method with the necessary arguments
    scraped_products = await scraper.scrape(
        settings.dict()
    )

    # Return a response with the scraped products (or just their count)
    return {"scraped_count": len(scraped_products), "scraped_products": scraped_products}









