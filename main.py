import asyncio

async def get_data(url):
    
    pass


async def main():
    print(base_url)
    rows = 50
    offset = 0

    base_url = f"https://www.myntra.com/gateway/v2/search/men-clothing?f=Categories%3AShirts&rows={rows}&o={offset}&plaEnabled=false&xdEnabled=false&pincode=560002"

asyncio.run(main())