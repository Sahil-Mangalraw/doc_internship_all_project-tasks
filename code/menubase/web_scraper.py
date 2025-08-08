import requests
from bs4 import BeautifulSoup
import os
import json
import csv
import time
from urllib.parse import urljoin, urlparse
import webbrowser

def scrape_website():
    """Scrape a website and extract data"""
    print("=" * 50)
    print("🌐 WEB SCRAPER")
    print("=" * 50)
    
    try:
        url = input("🔗 Enter website URL: ")
        output_format = input("📄 Output format (json/csv/txt): ").lower()
        
        if output_format not in ['json', 'csv', 'txt']:
            output_format = 'txt'
        
        print(f"\n🔍 Scraping: {url}")
        print(f"📄 Output format: {output_format}")
        
        # Headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Make the request
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract data
            data = {
                'url': url,
                'title': soup.title.string if soup.title else 'No title',
                'headings': [],
                'links': [],
                'text_content': '',
                'images': []
            }
            
            # Extract headings
            for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                data['headings'].append({
                    'tag': heading.name,
                    'text': heading.get_text().strip()
                })
            
            # Extract links
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                text = link.get_text().strip()
                if href and text:
                    data['links'].append({
                        'url': urljoin(url, href),
                        'text': text
                    })
            
            # Extract text content
            for paragraph in soup.find_all('p'):
                text = paragraph.get_text().strip()
                if text:
                    data['text_content'] += text + '\n\n'
            
            # Extract images
            for img in soup.find_all('img', src=True):
                src = img.get('src')
                alt = img.get('alt', 'No alt text')
                if src:
                    data['images'].append({
                        'url': urljoin(url, src),
                        'alt': alt
                    })
            
            # Save data
            filename = f"scraped_data_{int(time.time())}.{output_format}"
            
            if output_format == 'json':
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            elif output_format == 'csv':
                with open(filename, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Type', 'Content'])
                    writer.writerow(['Title', data['title']])
                    for heading in data['headings']:
                        writer.writerow([f"Heading ({heading['tag']})", heading['text']])
                    for link in data['links']:
                        writer.writerow(['Link', f"{link['text']} - {link['url']}"])
            else:  # txt
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"URL: {data['url']}\n")
                    f.write(f"Title: {data['title']}\n")
                    f.write("\n" + "="*50 + "\n")
                    f.write("HEADINGS:\n")
                    for heading in data['headings']:
                        f.write(f"{heading['tag'].upper()}: {heading['text']}\n")
                    f.write("\n" + "="*50 + "\n")
                    f.write("LINKS:\n")
                    for link in data['links']:
                        f.write(f"{link['text']} - {link['url']}\n")
                    f.write("\n" + "="*50 + "\n")
                    f.write("TEXT CONTENT:\n")
                    f.write(data['text_content'])
            
            print(f"✅ Data saved to: {filename}")
            print(f"📊 Extracted:")
            print(f"   - {len(data['headings'])} headings")
            print(f"   - {len(data['links'])} links")
            print(f"   - {len(data['images'])} images")
            print(f"   - {len(data['text_content'])} characters of text")
            
        else:
            print(f"❌ Failed to access website: HTTP {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def download_files():
    """Download files from a website"""
    print("\n" + "=" * 50)
    print("📥 FILE DOWNLOADER")
    print("=" * 50)
    
    try:
        url = input("🔗 Enter website URL: ")
        file_types = input("📁 File types to download (e.g., pdf,jpg,png): ").split(',')
        
        print(f"\n🔍 Scanning: {url}")
        print(f"📁 Looking for: {', '.join(file_types)}")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Create downloads directory
            download_dir = f"downloads_{int(time.time())}"
            os.makedirs(download_dir, exist_ok=True)
            
            downloaded_files = []
            
            # Find all links
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                if href:
                    full_url = urljoin(url, href)
                    file_extension = os.path.splitext(full_url)[1].lower()
                    
                    if any(ext in file_extension for ext in file_types):
                        try:
                            filename = os.path.basename(urlparse(full_url).path)
                            if not filename:
                                filename = f"file_{len(downloaded_files)}{file_extension}"
                            
                            filepath = os.path.join(download_dir, filename)
                            
                            print(f"📥 Downloading: {filename}")
                            file_response = requests.get(full_url, headers=headers, timeout=30)
                            
                            if file_response.status_code == 200:
                                with open(filepath, 'wb') as f:
                                    f.write(file_response.content)
                                downloaded_files.append(filename)
                                print(f"✅ Downloaded: {filename}")
                            else:
                                print(f"❌ Failed to download: {filename}")
                                
                        except Exception as e:
                            print(f"❌ Error downloading {filename}: {e}")
            
            print(f"\n📊 Download Summary:")
            print(f"   - Directory: {download_dir}")
            print(f"   - Files downloaded: {len(downloaded_files)}")
            
            if downloaded_files:
                print(f"   - Files: {', '.join(downloaded_files)}")
            else:
                print("   - No files found matching the specified types")
                
        else:
            print(f"❌ Failed to access website: HTTP {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def scrape_multiple_pages():
    """Scrape multiple pages from a website"""
    print("\n" + "=" * 50)
    print("📄 MULTI-PAGE SCRAPER")
    print("=" * 50)
    
    try:
        base_url = input("🔗 Enter base URL: ")
        max_pages = int(input("📄 Maximum number of pages to scrape: "))
        
        if max_pages < 1:
            max_pages = 5
        
        print(f"\n🔍 Scraping up to {max_pages} pages from: {base_url}")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        all_data = []
        visited_urls = set()
        
        # Start with the base URL
        urls_to_visit = [base_url]
        
        while urls_to_visit and len(all_data) < max_pages:
            current_url = urls_to_visit.pop(0)
            
            if current_url in visited_urls:
                continue
                
            visited_urls.add(current_url)
            
            try:
                print(f"🔍 Scraping: {current_url}")
                response = requests.get(current_url, headers=headers, timeout=10)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    page_data = {
                        'url': current_url,
                        'title': soup.title.string if soup.title else 'No title',
                        'content': soup.get_text()[:1000] + '...' if len(soup.get_text()) > 1000 else soup.get_text()
                    }
                    
                    all_data.append(page_data)
                    
                    # Find more links to visit
                    if len(all_data) < max_pages:
                        for link in soup.find_all('a', href=True):
                            href = link.get('href')
                            full_url = urljoin(current_url, href)
                            
                            # Only visit URLs from the same domain
                            if urlparse(full_url).netloc == urlparse(base_url).netloc:
                                if full_url not in visited_urls and full_url not in urls_to_visit:
                                    urls_to_visit.append(full_url)
                    
                    time.sleep(1)  # Be respectful to the server
                    
                else:
                    print(f"❌ Failed to access: {current_url}")
                    
            except Exception as e:
                print(f"❌ Error scraping {current_url}: {e}")
        
        # Save all data
        filename = f"multi_page_data_{int(time.time())}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Scraped {len(all_data)} pages")
        print(f"📄 Data saved to: {filename}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def open_website():
    """Open a website in browser"""
    print("\n" + "=" * 50)
    print("🌐 OPEN WEBSITE IN BROWSER")
    print("=" * 50)
    
    try:
        url = input("🔗 Enter website URL: ")
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        print(f"\n🔗 Opening: {url}")
        webbrowser.open(url)
        print("✅ Website opened in browser!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("Choose a web scraping option:")
    print("1. Scrape Website Data")
    print("2. Download Files")
    print("3. Multi-Page Scraper")
    print("4. Open Website in Browser")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        scrape_website()
    elif choice == "2":
        download_files()
    elif choice == "3":
        scrape_multiple_pages()
    elif choice == "4":
        open_website()
    else:
        print("❌ Invalid choice") 