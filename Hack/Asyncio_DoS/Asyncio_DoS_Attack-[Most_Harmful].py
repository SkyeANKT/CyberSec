import aiohttp
import asyncio

# List of URLs to send GET requests to
urls = [
    "https://apexfamily.ddns.net/",
    "https://apexfamily.ddns.net/index.php/cart/",
    "https://apexfamily.ddns.net/index.php/shop/",
    "https://apexfamily.ddns.net/index.php/2023/09/05/hello-world/"
    "https://apexfamily.ddns.net/index.php/my-account/"
    "https://apexfamily.ddns.net/wp-content/plugins/jetpack/jetpack_vendor/automattic/jetpack-image-cdn/dist/image-cdn.js?minify=false&ver=132249e245926ae3e188"
    "https://apexfamily.ddns.net/wp-content/themes/computer/js/navigation.js?ver=20190715"
    # Add more URLs as needed
]


# Takes 52% of GPU

# Number of requests to send to each URL
num_requests_per_url = 1  # You can adjust this as needed

# Function to send a GET request to a URL
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
        # Create tasks for sending GET requests to each URL
        tasks = []
        for url in urls:
            for _ in range(num_requests_per_url):
                tasks.append(send_get_request(session, url))

        # Execute the tasks concurrently
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
