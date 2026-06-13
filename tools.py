from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
from dotenv import load_dotenv
import os
from rich import print

load_dotenv()

# Initialize Tavily client
tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information on a topic.
    Returns Titles, URLs, and Snippets.
    """

    results = tavily_client.search(
        query=query,
        search_depth="advanced",
        max_results=3
    )

    output = []

    for r in results["results"]:
        title = r.get("title", "No Title")
        url = r.get("url", "No URL")
        content = r.get("content", "No Content")

        output.append(
            f"Title: {title}\n"
            f"URL: {url}\n"
            f"Snippet: {content[:300]}\n"
        )

    return "\n\n".join(output)


@tool
def web_scrape(url: str) -> str:
    """
    Scrape and return clean text content from a given URL for deeper reading.
    """

    try:
        response = requests.get(
            url,
            timeout=8,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup([
            "script",
            "style",
            "header",
            "footer",
            "nav",
            "aside"
        ]):
            tag.decompose()

        text = soup.get_text(
            separator="\n",
            strip=True
        )

        return text[:5000]

    except Exception as e:
        return f"Error scraping {url}: {str(e)}"