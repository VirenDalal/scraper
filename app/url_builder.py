from urllib.parse import urlencode

class URLBuilder:
    def build_url(self, base_url: str, category: str, page: int, filters: dict, sort_by: str = None) -> str:
        """
        Builds the URL for scraping.
        :param base_url: Base URL of the website.
        :param category: Product category to scrape.
        :param page: Page number to scrape (None or 1 means the first page).
        :param filters: Additional filters like min_price and max_price.
        :param sort_by: Sorting criteria.
        :return: Fully constructed URL.
        """
        # Base category URL
        url = f"{base_url}{category}/"

        # Add pagination only if the page is greater than 1
        if page and page > 1:
            url += f"page/{page}/"

        # Add query parameters
        query_params = {}
        if filters.get("min_price"):
            query_params["min_price"] = filters["min_price"]
        if filters.get("max_price"):
            query_params["max_price"] = filters["max_price"]
        if sort_by:
            query_params["orderby"] = sort_by

        # Append query parameters to the URL
        if query_params:
            url += f"?{urlencode(query_params)}"

        return url
