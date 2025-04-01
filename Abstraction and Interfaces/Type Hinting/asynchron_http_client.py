from typing import Optional, Dict, Any
import aiohttp #pip install aiohttp
import asyncio

async def fetch_url(
    url: str,
    headers: Optional[Dict[str, str]] = None
) -> Optional[Dict[str, Any]]:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                return await response.json()
    except Exception:
        return None

# Пример
if __name__ == "__main__":
    async def main():
        data = await fetch_url("https://api.github.com/users/octocat")
        print("GitHub data:", data)

    asyncio.run(main())