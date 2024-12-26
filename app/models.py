from pydantic import BaseModel

class Product(BaseModel):
    title: str
    price: float
    image_url: str

class ScrapeSettings(BaseModel):
    categories: str
    page_limit: int
    filters: dict | None = {}
    sort_by: str | None = None


class ScrapeSettingsName(BaseModel):
    name: str



class ScrapeSettingsWord(BaseModel):
    word: str
    page_limit: int
    filters: dict | None = {}
    sort_by: str | None = None
