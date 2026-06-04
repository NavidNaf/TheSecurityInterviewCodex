from urllib.request import Request, urlopen


def print_response_headers():
    url = "https://www.bkash.com"

    # Add a basic User-Agent so the request looks like a normal browser request.
    request = Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
    )

    # Send the request and collect the response headers.
    with urlopen(request, timeout=10) as response:
        headers = response.headers

        print("Response headers for:", url)
        print()

        for header_name, header_value in headers.items():
            print(header_name + ":", header_value)


if __name__ == "__main__":
    print_response_headers()
