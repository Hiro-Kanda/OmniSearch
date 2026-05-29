import os
import httpx

TOKEN_URL = "https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"

async def get_access_token():

    tenant = os.getenv("TENANT_ID")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    url = TOKEN_URL.format(tenant=tenant)

    data = {
        "client_id": client_id,
        "scope": "https://graph.microsoft.com/.default",
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }

    async with httpx.AsyncClient() as client:
        res = await client.post(url, data=data)
        res.raise_for_status()

    return res.json()["access_token"]
