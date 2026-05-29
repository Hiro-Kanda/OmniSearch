from fastapi import APIRouter
import httpx

from app.services.graph_auth import get_access_token

router = APIRouter()


@router.get("/sharepoint/sites/{site_id}/drives")
async def list_drives(site_id: str):

    token = await get_access_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives"

    async with httpx.AsyncClient() as client:
        res = await client.get(url, headers=headers)

    res.raise_for_status()
    return res.json()


@router.get("/sharepoint/drives/{drive_id}/items")
async def list_items(drive_id: str):

    token = await get_access_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    url = f"https://graph.microsoft.com/v1.0/drives/{drive_id}/root/children"

    async with httpx.AsyncClient() as client:
        res = await client.get(url, headers=headers)

    res.raise_for_status()
    return res.json()
