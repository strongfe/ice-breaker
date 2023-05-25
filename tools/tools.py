
from langchain.serpapi import SerpAPIWrapper

def gte_profile_url(text: str) -> str:
    """Searches for linkedin Profile Page"""
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res
