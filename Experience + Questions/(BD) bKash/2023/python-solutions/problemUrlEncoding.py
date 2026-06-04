from urllib.parse import quote


def encode_urls():
    # These are the URLs provided in the assessment question.
    urls = [
        "https://api.example.com/v1/users/123456/profile/image.jpg?size=large&crop=true",
        "https://www.example.com/blog/post/my-first-post/comment/54321#comment-54321",
    ]

    # Encode each full URL and print the result.
    for url in urls:
        encoded_url = quote(url, safe="")
        print("Original URL:", url)
        print("Encoded URL:", encoded_url)
        print()


if __name__ == "__main__":
    encode_urls()
