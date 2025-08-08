import requests
from bs4 import BeautifulSoup
import json
import time
import webbrowser

def google_search_web():
    """Search Google using web scraping"""
    print("=" * 50)
    print("🔍 GOOGLE SEARCH TOOL")
    print("=" * 50)
    
    try:
        query = input("🔍 Enter your search query: ")
        num_results = int(input("📊 Number of results to show (1-10): "))
        
        if num_results < 1 or num_results > 10:
            num_results = 5
        
        print(f"\n🔍 Searching for: '{query}'")
        print(f"📊 Showing {num_results} results...")
        
        # Google search URL
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}&num={num_results}"
        
        # Headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Make the request
        response = requests.get(search_url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find search results
            search_results = soup.find_all('div', class_='g')
            
            if search_results:
                print(f"\n✅ Found {len(search_results)} results:")
                print("=" * 50)
                
                for i, result in enumerate(search_results[:num_results], 1):
                    # Extract title
                    title_element = result.find('h3')
                    title = title_element.get_text() if title_element else "No title"
                    
                    # Extract URL
                    link_element = result.find('a')
                    url = link_element.get('href') if link_element else "No URL"
                    
                    # Extract snippet
                    snippet_element = result.find('div', class_='VwiC3b')
                    snippet = snippet_element.get_text() if snippet_element else "No description"
                    
                    print(f"\n{i}. {title}")
                    print(f"   🔗 {url}")
                    print(f"   📝 {snippet[:150]}...")
                    print("-" * 30)
            else:
                print("❌ No search results found")
                print("💡 This might be due to Google's anti-bot protection")
        else:
            print(f"❌ Failed to search: HTTP {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def google_search_api():
    """Search Google using Google Custom Search API"""
    print("\n" + "=" * 50)
    print("🔍 GOOGLE SEARCH API")
    print("=" * 50)
    
    try:
        api_key = input("🔑 Enter Google API Key: ")
        search_engine_id = input("🔑 Enter Search Engine ID: ")
        query = input("🔍 Enter your search query: ")
        num_results = int(input("📊 Number of results (1-10): "))
        
        if num_results < 1 or num_results > 10:
            num_results = 5
        
        print(f"\n🔍 Searching for: '{query}'")
        
        # Google Custom Search API URL
        url = "https://www.googleapis.com/customsearch/v1"
        
        params = {
            'key': api_key,
            'cx': search_engine_id,
            'q': query,
            'num': num_results
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            if 'items' in data:
                print(f"\n✅ Found {len(data['items'])} results:")
                print("=" * 50)
                
                for i, item in enumerate(data['items'], 1):
                    title = item.get('title', 'No title')
                    url = item.get('link', 'No URL')
                    snippet = item.get('snippet', 'No description')
                    
                    print(f"\n{i}. {title}")
                    print(f"   🔗 {url}")
                    print(f"   📝 {snippet}")
                    print("-" * 30)
            else:
                print("❌ No search results found")
        else:
            print(f"❌ API Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def open_google_search():
    """Open Google search in browser"""
    print("\n" + "=" * 50)
    print("🌐 OPEN GOOGLE SEARCH IN BROWSER")
    print("=" * 50)
    
    try:
        query = input("🔍 Enter your search query: ")
        
        # Create Google search URL
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        
        print(f"\n🔗 Opening: {search_url}")
        
        # Open in browser
        webbrowser.open(search_url)
        
        print("✅ Google search opened in browser!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def search_other_engines():
    """Search using other search engines"""
    print("\n" + "=" * 50)
    print("🔍 OTHER SEARCH ENGINES")
    print("=" * 50)
    
    print("📡 Available Search Engines:")
    print("   1. Bing")
    print("   2. DuckDuckGo")
    print("   3. Yahoo")
    print("   4. Wikipedia")
    print("   5. YouTube")
    
    try:
        choice = input("\nChoose search engine (1-5): ")
        query = input("🔍 Enter your search query: ")
        
        search_urls = {
            "1": f"https://www.bing.com/search?q={query.replace(' ', '+')}",
            "2": f"https://duckduckgo.com/?q={query.replace(' ', '+')}",
            "3": f"https://search.yahoo.com/search?p={query.replace(' ', '+')}",
            "4": f"https://en.wikipedia.org/wiki/Special:Search?search={query.replace(' ', '+')}",
            "5": f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        }
        
        if choice in search_urls:
            url = search_urls[choice]
            print(f"\n🔗 Opening: {url}")
            webbrowser.open(url)
            print("✅ Search opened in browser!")
        else:
            print("❌ Invalid choice")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def setup_instructions():
    """Show setup instructions for Google API"""
    print("\n" + "=" * 50)
    print("📋 GOOGLE SEARCH API SETUP")
    print("=" * 50)
    
    print("🔧 To use Google Search API:")
    print("   1. Go to Google Cloud Console")
    print("   2. Create a new project")
    print("   3. Enable Custom Search API")
    print("   4. Create API credentials")
    print("   5. Create a Custom Search Engine")
    print("   6. Get your API key and Search Engine ID")
    
    print("\n🔗 Links:")
    print("   - Google Cloud Console: console.cloud.google.com")
    print("   - Custom Search: cse.google.com")
    
    print("\n💰 Cost Information:")
    print("   - 100 free queries per day")
    print("   - $5 per 1000 queries after that")

if __name__ == "__main__":
    print("Choose a search method:")
    print("1. Web Scraping (Free, Limited)")
    print("2. Google API (Paid, Reliable)")
    print("3. Open in Browser (Free)")
    print("4. Other Search Engines")
    print("5. Setup Instructions")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        google_search_web()
    elif choice == "2":
        google_search_api()
    elif choice == "3":
        open_google_search()
    elif choice == "4":
        search_other_engines()
    elif choice == "5":
        setup_instructions()
    else:
        print("❌ Invalid choice") 