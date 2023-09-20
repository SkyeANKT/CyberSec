import requests
import concurrent.futures

# Define the URL you want to make GET requests to
# url = "https://group2.ddns.net"
# url = "https://apexfamily.ddns.net"
url = "https://g3-tech.ddns.net"
# Function to send a GET request to the URL
def send_get_request(url):
    try:
        response = requests.get(url)
        # You can process the response here if needed
        # For example, print the status code
        print(f"Status code for {url}: {response.status_code}")
    except Exception as e:
        print(f"Error for {url}: {e}")

# Number of concurrent requests to make
num_requests = 1 # Adjust this to your needs

# Create a ThreadPoolExecutor with the desired number of threads
with concurrent.futures.ThreadPoolExecutor(max_workers=num_requests) as executor:
    # Submit the GET requests concurrently
    futures = [executor.submit(send_get_request, url) for _ in range(num_requests)]

    # Wait for all requests to complete
    concurrent.futures.wait(futures)
