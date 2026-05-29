from fastapi import APIRouter
import httpx
from app.services.graph_auth import get_access_token

router = APIRouter()

@router.get("/sharepoint/sites")
async def list_sites():

    token = await get_access_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient() as client:
        res = await client.get(
            "https://graph.microsoft.com/v1.0/sites?search=*",
            headers=headers
        )

    res.raise_for_status()
    return res.json()
