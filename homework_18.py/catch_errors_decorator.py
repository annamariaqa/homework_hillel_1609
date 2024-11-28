def retry(max_retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}. Retry {retries + 1}/{max_retries}")
                    retries += 1
            raise Exception("Max number of tries is reached")
        return wrapper
    return decorator

@retry(max_retries=3)
def getting_api_response():
    raise ConnectionError("Failed to get response")

getting_api_response()