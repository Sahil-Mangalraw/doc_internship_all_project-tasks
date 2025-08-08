import tweepy
import requests
import json
import webbrowser
from datetime import datetime

def post_to_twitter():
    """Post to Twitter using Twitter API"""
    print("=" * 50)
    print("🐦 TWITTER POSTER")
    print("=" * 50)
    
    try:
        # Twitter API credentials
        api_key = input("🔑 Enter Twitter API Key: ")
        api_secret = input("🔑 Enter Twitter API Secret: ")
        access_token = input("🔑 Enter Access Token: ")
        access_token_secret = input("🔑 Enter Access Token Secret: ")
        
        # Authenticate
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        
        # Get tweet content
        tweet_text = input("💬 Enter your tweet (max 280 characters): ")
        
        if len(tweet_text) > 280:
            print("❌ Tweet is too long! Maximum 280 characters.")
            return
        
        # Post tweet
        print(f"\n🐦 Posting tweet: '{tweet_text}'")
        status = api.update_status(tweet_text)
        
        print("✅ Tweet posted successfully!")
        print(f"📋 Tweet ID: {status.id}")
        print(f"🔗 Tweet URL: https://twitter.com/user/status/{status.id}")
        
    except tweepy.TweepError as e:
        print(f"❌ Twitter API Error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

def post_to_facebook():
    """Post to Facebook using Facebook Graph API"""
    print("\n" + "=" * 50)
    print("📘 FACEBOOK POSTER")
    print("=" * 50)
    
    try:
        # Facebook Graph API credentials
        access_token = input("🔑 Enter Facebook Access Token: ")
        page_id = input("📄 Enter Page ID (optional, press Enter to skip): ")
        
        # Get post content
        message = input("💬 Enter your post message: ")
        
        # Facebook Graph API endpoint
        if page_id:
            url = f"https://graph.facebook.com/v18.0/{page_id}/feed"
        else:
            url = "https://graph.facebook.com/v18.0/me/feed"
        
        data = {
            'message': message,
            'access_token': access_token
        }
        
        print(f"\n📘 Posting to Facebook: '{message}'")
        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Facebook post created successfully!")
            print(f"📋 Post ID: {result.get('id', 'N/A')}")
        else:
            print(f"❌ Failed to post: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def post_to_instagram():
    """Post to Instagram using Instagram Basic Display API"""
    print("\n" + "=" * 50)
    print("📷 INSTAGRAM POSTER")
    print("=" * 50)
    
    print("⚠️  Instagram API requires:")
    print("   - Instagram Basic Display API setup")
    print("   - User authorization")
    print("   - Business/Creator account")
    
    try:
        access_token = input("🔑 Enter Instagram Access Token: ")
        user_id = input("👤 Enter Instagram User ID: ")
        
        # Get post content
        caption = input("💬 Enter your caption: ")
        image_url = input("🖼️ Enter image URL: ")
        
        # Instagram Basic Display API endpoint
        url = f"https://graph.instagram.com/v18.0/{user_id}/media"
        
        data = {
            'image_url': image_url,
            'caption': caption,
            'access_token': access_token
        }
        
        print(f"\n📷 Creating Instagram post...")
        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Instagram post created successfully!")
            print(f"📋 Media ID: {result.get('id', 'N/A')}")
        else:
            print(f"❌ Failed to create post: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def post_to_linkedin():
    """Post to LinkedIn using LinkedIn API"""
    print("\n" + "=" * 50)
    print("💼 LINKEDIN POSTER")
    print("=" * 50)
    
    try:
        access_token = input("🔑 Enter LinkedIn Access Token: ")
        
        # Get post content
        text = input("💬 Enter your post text: ")
        
        # LinkedIn API endpoint
        url = "https://api.linkedin.com/v2/ugcPosts"
        
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'X-Restli-Protocol-Version': '2.0.0'
        }
        
        data = {
            "author": "urn:li:person:{YOUR_PERSON_ID}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": text
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        
        print(f"\n💼 Posting to LinkedIn: '{text}'")
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 201:
            print("✅ LinkedIn post created successfully!")
        else:
            print(f"❌ Failed to post: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def open_social_media():
    """Open social media platforms in browser"""
    print("\n" + "=" * 50)
    print("🌐 OPEN SOCIAL MEDIA IN BROWSER")
    print("=" * 50)
    
    print("📡 Available Platforms:")
    print("   1. Twitter")
    print("   2. Facebook")
    print("   3. Instagram")
    print("   4. LinkedIn")
    print("   5. YouTube")
    print("   6. TikTok")
    
    try:
        choice = input("\nChoose platform (1-6): ")
        
        urls = {
            "1": "https://twitter.com/compose/tweet",
            "2": "https://www.facebook.com/",
            "3": "https://www.instagram.com/",
            "4": "https://www.linkedin.com/feed/update/",
            "5": "https://studio.youtube.com/",
            "6": "https://www.tiktok.com/upload"
        }
        
        if choice in urls:
            url = urls[choice]
            print(f"\n🔗 Opening: {url}")
            webbrowser.open(url)
            print("✅ Platform opened in browser!")
        else:
            print("❌ Invalid choice")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def setup_instructions():
    """Show setup instructions for social media APIs"""
    print("\n" + "=" * 50)
    print("📋 SOCIAL MEDIA API SETUP")
    print("=" * 50)
    
    print("🔧 Twitter Setup:")
    print("   1. Go to developer.twitter.com")
    print("   2. Create a new app")
    print("   3. Get API keys and tokens")
    print("   4. Enable OAuth 1.0a")
    
    print("\n🔧 Facebook Setup:")
    print("   1. Go to developers.facebook.com")
    print("   2. Create a new app")
    print("   3. Add Facebook Login product")
    print("   4. Get access token")
    
    print("\n🔧 Instagram Setup:")
    print("   1. Go to developers.facebook.com")
    print("   2. Create Instagram Basic Display app")
    print("   3. Configure OAuth redirect")
    print("   4. Get user authorization")
    
    print("\n🔧 LinkedIn Setup:")
    print("   1. Go to developer.linkedin.com")
    print("   2. Create a new app")
    print("   3. Request API access")
    print("   4. Get OAuth 2.0 credentials")
    
    print("\n🔗 Developer Links:")
    print("   - Twitter: developer.twitter.com")
    print("   - Facebook: developers.facebook.com")
    print("   - Instagram: developers.facebook.com")
    print("   - LinkedIn: developer.linkedin.com")

if __name__ == "__main__":
    print("Choose a social media platform:")
    print("1. Twitter")
    print("2. Facebook")
    print("3. Instagram")
    print("4. LinkedIn")
    print("5. Open in Browser")
    print("6. Setup Instructions")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        post_to_twitter()
    elif choice == "2":
        post_to_facebook()
    elif choice == "3":
        post_to_instagram()
    elif choice == "4":
        post_to_linkedin()
    elif choice == "5":
        open_social_media()
    elif choice == "6":
        setup_instructions()
    else:
        print("❌ Invalid choice") 