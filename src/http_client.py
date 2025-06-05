from aiohttp import ClientSession

from src.config import settings


class HTTPClient:
    def __init__(self, base_url: str, headers: dict):
        self.base_url = base_url
        self.session = ClientSession(
            headers=headers
        )

# https://pro-api.coinmarketcap.com

class CMCHTTPClient(HTTPClient):
    def __init__(self, base_url: str, api_key: str):
        headers = {
            'X-CMC_PRO_API_KEY': api_key,
        }
        super().__init__(base_url, headers)
        self.url = self.base_url + "/v1/cryptocurrency/listings/latest"

    async def get_listing(self):
        async with self.session.get(self.base_url + "/v1/cryptocurrency/listings/latest") as response:
            result = await response.json()
            return result["data"]


    async def get_currency(self, currency_id: int):
        async with self.session.get(
            url=self.base_url + "/v2/cryptocurrency/quotes/latest",
            params={
                "id": currency_id,
            }
        ) as response:
            result = await response.json()
            return result["data"][str(currency_id)]




