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
from app.models import ScrapeSettings
from pydantic import BaseModel


router = APIRouter()




database = JSONDatabase(file_path="products.json")
notifier = ConsoleNotifier()
cache = Cache()
scraper = Scraper(database, notifier, cache)


@router.post("/scrape/")
async def scrape(settings: ScrapeSettings):

    # Call the scrape method with the necessary arguments
    scraped_products = await scraper.scrape(
        settings.dict()
    )

    # Return a response with the scraped products (or just their count)
    return {"scraped_count": len(scraped_products), "scraped_products": scraped_products}


