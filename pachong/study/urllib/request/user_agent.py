from fake_useragent import UserAgent
user_agent={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

ua=UserAgent()

print(ua.chrome)
