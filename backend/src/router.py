from fastapi import APIRouter

from src.client import cmc_client

router=APIRouter(
    prefix="/crypto"
)

@router.get("/")
async def root():
    return await cmc_client.get_listing()


@router.get("/{currency_id}")
async def currency(currency_id: int):
    return await cmc_client.get_currency(currency_id)



