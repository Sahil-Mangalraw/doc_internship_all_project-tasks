import requests
import json
import time

def send_sms_twilio():
    """Send SMS using Twilio API"""
    print("=" * 50)
    print("💬 SMS SENDER (Twilio)")
    print("=" * 50)
    
    try:
        # Twilio credentials (you need to sign up at twilio.com)
        account_sid = input("")
        auth_token = input(" ")
        twilio_number = input("")
        
        # Message details
        to_number = input("📞 Enter recipient phone number (with country code): ")
        message = input("💬 Enter your message: ")
        
        # Validate phone numbers
        if not to_number.startswith('+'):
            print("❌ Recipient number must include country code with +")
            return
        
        if not twilio_number.startswith('+'):
            print("❌ Twilio number must include country code with +")
            return
        
        print(f"\n📱 Sending SMS...")
        print(f"   From: {twilio_number}")
        print(f"   To: {to_number}")
        print(f"   Message: {message}")
        
        # Twilio API endpoint
        url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"
        
        # Request data
        data = {
            'From': twilio_number,
            'To': to_number,
            'Body': message
        }
        
        # Send request
        response = requests.post(url, data=data, auth=(account_sid, auth_token))
        
        if response.status_code == 201:
            result = response.json()
            print(f"\n✅ SMS sent successfully!")
            print(f"📋 Message SID: {result['sid']}")
            print(f"💰 Cost: {result.get('price', 'N/A')}")
        else:
            print(f"❌ Failed to send SMS: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def send_sms_textbelt():
    """Send SMS using TextBelt API"""
    print("\n" + "=" * 50)
    print("💬 SMS SENDER (TextBelt)")
    print("=" * 50)
    
    try:
        # TextBelt API key (get from textbelt.com)
        api_key = input("🔑 Enter TextBelt API key: ")
        phone_number = input("📞 Enter recipient phone number (with country code): ")
        message = input("💬 Enter your message: ")
        
        if not phone_number.startswith('+'):
            print("❌ Phone number must include country code with +")
            return
        
        print(f"\n📱 Sending SMS via TextBelt...")
        print(f"   To: {phone_number}")
        print(f"   Message: {message}")
        
        # TextBelt API endpoint
        url = "https://textbelt.com/text"
        
        data = {
            'phone': phone_number,
            'message': message,
            'key': api_key
        }
        
        response = requests.post(url, data=data)
        result = response.json()
        
        if result['success']:
            print(f"\n✅ SMS sent successfully!")
            print(f"📋 Text ID: {result.get('textId', 'N/A')}")
            print(f"💰 Credits used: {result.get('creditsUsed', 'N/A')}")
        else:
            print(f"❌ Failed to send SMS: {result.get('error', 'Unknown error')}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def send_sms_free_service():
    """Send SMS using free online services"""
    print("\n" + "=" * 50)
    print("💬 SMS SENDER (Free Services)")
    print("=" * 50)
    
    print("⚠️  WARNING: Free SMS services are often unreliable!")
    print("⚠️  They may not work or may be blocked by carriers!")
    print()
    
    try:
        phone_number = input("📞 Enter recipient phone number (with country code): ")
        message = input("💬 Enter your message: ")
        
        if not phone_number.startswith('+'):
            print("❌ Phone number must include country code with +")
            return
        
        print(f"\n📱 Target: {phone_number}")
        print(f"💬 Message: {message}")
        
        # List of free SMS services
        print("\n📡 Available Free SMS Services:")
        print("   1. TextNow (requires registration)")
        print("   2. Google Voice (US only)")
        print("   3. Various online SMS websites")
        
        print("\n💡 Instructions:")
        print("   1. Visit a free SMS service website")
        print("   2. Enter the phone number and message")
        print("   3. Complete any verification required")
        print("   4. Send the message")
        
        print("\n🔗 Popular Free SMS Websites:")
        print("   - textnow.com")
        print("   - textfree.us")
        print("   - sms4free.com")
        print("   - receivesmsonline.net")
        
        print("\n⚠️  Important Notes:")
        print("   - Most free services require registration")
        print("   - Some may send ads with your message")
        print("   - Delivery is not guaranteed")
        print("   - Use at your own risk")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def setup_instructions():
    """Show setup instructions for SMS services"""
    print("\n" + "=" * 50)
    print("📋 SMS SERVICE SETUP INSTRUCTIONS")
    print("=" * 50)
    
    print("\n🔧 Twilio Setup:")
    print("   1. Sign up at twilio.com")
    print("   2. Get Account SID and Auth Token")
    print("   3. Buy a phone number")
    print("   4. Use the credentials in this script")
    
    print("\n🔧 TextBelt Setup:")
    print("   1. Visit textbelt.com")
    print("   2. Get an API key")
    print("   3. Use the API key in this script")
    
    print("\n💰 Cost Information:")
    print("   - Twilio: ~$0.0075 per SMS")
    print("   - TextBelt: ~$0.01 per SMS")
    print("   - Free services: Usually free but unreliable")

if __name__ == "__main__":
    print("Choose an SMS service:")
    print("1. Twilio (Paid, Reliable)")
    print("2. TextBelt (Paid, Reliable)")
    print("3. Free Services (Unreliable)")
    print("4. Setup Instructions")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        send_sms_twilio()
    elif choice == "2":
        send_sms_textbelt()
    elif choice == "3":
        send_sms_free_service()
    elif choice == "4":
        setup_instructions()
    else:
        print("❌ Invalid choice") 