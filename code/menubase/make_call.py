import requests
import json
import time
import webbrowser

def make_call_twilio():
    """Make phone call using Twilio API"""
    print("=" * 50)
    print("📞 PHONE CALL MAKER (Twilio)")
    print("=" * 50)
    
    try:
        # Twilio credentials
        account_sid = input("🔑 Enter Twilio Account SID: ")
        auth_token = input("🔑 Enter Twilio Auth Token: ")
        twilio_number = input("📞 Enter your Twilio phone number: ")
        
        # Call details
        to_number = input("📞 Enter recipient phone number (with country code): ")
        
        # Validate phone numbers
        if not to_number.startswith('+'):
            print("❌ Recipient number must include country code with +")
            return
        
        if not twilio_number.startswith('+'):
            print("❌ Twilio number must include country code with +")
            return
        
        print(f"\n📞 Making call...")
        print(f"   From: {twilio_number}")
        print(f"   To: {to_number}")
        
        # Twilio API endpoint for calls
        url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls.json"
        
        # Request data
        data = {
            'From': twilio_number,
            'To': to_number,
            'Url': 'http://demo.twilio.com/docs/voice.xml'  # Default TwiML
        }
        
        # Make the call
        response = requests.post(url, data=data, auth=(account_sid, auth_token))
        
        if response.status_code == 201:
            result = response.json()
            print(f"\n✅ Call initiated successfully!")
            print(f"📋 Call SID: {result['sid']}")
            print(f"📊 Status: {result['status']}")
            print(f"💰 Cost: {result.get('price', 'N/A')}")
        else:
            print(f"❌ Failed to make call: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def make_call_web_services():
    """Make calls using web-based services"""
    print("\n" + "=" * 50)
    print("📞 PHONE CALL MAKER (Web Services)")
    print("=" * 50)
    
    try:
        phone_number = input("📞 Enter recipient phone number (with country code): ")
        
        if not phone_number.startswith('+'):
            print("❌ Phone number must include country code with +")
            return
        
        print(f"\n📞 Target: {phone_number}")
        
        # List of web-based calling services
        print("\n📡 Available Web Calling Services:")
        print("   1. Google Voice (US only)")
        print("   2. Skype")
        print("   3. WhatsApp Call")
        print("   4. Facebook Messenger Call")
        print("   5. Various online calling websites")
        
        print("\n🔗 Direct Links:")
        
        # Google Voice
        google_voice_url = f"https://voice.google.com/calls"
        print(f"   Google Voice: {google_voice_url}")
        
        # Skype
        skype_url = f"skype:{phone_number}?call"
        print(f"   Skype: {skype_url}")
        
        # WhatsApp
        whatsapp_url = f"https://wa.me/{phone_number.replace('+', '')}"
        print(f"   WhatsApp: {whatsapp_url}")
        
        # Ask user which service to use
        print("\nChoose a service to open:")
        print("1. Google Voice")
        print("2. Skype")
        print("3. WhatsApp")
        print("4. None (manual)")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            webbrowser.open(google_voice_url)
            print("✅ Google Voice opened in browser!")
        elif choice == "2":
            webbrowser.open(skype_url)
            print("✅ Skype opened!")
        elif choice == "3":
            webbrowser.open(whatsapp_url)
            print("✅ WhatsApp Web opened!")
        elif choice == "4":
            print("💡 Manual instructions:")
            print("   1. Open your preferred calling service")
            print("   2. Enter the phone number")
            print("   3. Make the call")
        else:
            print("❌ Invalid choice")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def make_call_voip():
    """Make calls using VoIP services"""
    print("\n" + "=" * 50)
    print("📞 PHONE CALL MAKER (VoIP Services)")
    print("=" * 50)
    
    print("📡 Popular VoIP Services:")
    print("   1. Discord")
    print("   2. Zoom")
    print("   3. Microsoft Teams")
    print("   4. Slack")
    print("   5. Telegram")
    
    print("\n💡 Instructions:")
    print("   1. Install the VoIP application")
    print("   2. Create an account")
    print("   3. Add contacts or use phone numbers")
    print("   4. Make voice/video calls")
    
    print("\n🔗 Download Links:")
    print("   - Discord: discord.com")
    print("   - Zoom: zoom.us")
    print("   - Teams: teams.microsoft.com")
    print("   - Slack: slack.com")
    print("   - Telegram: telegram.org")

def emergency_call_info():
    """Show emergency calling information"""
    print("\n" + "=" * 50)
    print("🚨 EMERGENCY CALLING INFORMATION")
    print("=" * 50)
    
    print("⚠️  IMPORTANT:")
    print("   - For emergencies, always call 911 (US) or your local emergency number")
    print("   - Do not rely on internet-based calling for emergencies")
    print("   - Use a landline or mobile phone for emergency calls")
    
    print("\n📞 Emergency Numbers:")
    print("   - US/Canada: 911")
    print("   - UK: 999")
    print("   - EU: 112")
    print("   - Australia: 000")
    print("   - India: 100 (Police), 101 (Fire), 102 (Ambulance)")

if __name__ == "__main__":
    print("Choose a calling method:")
    print("1. Twilio API (Paid, Reliable)")
    print("2. Web Services (Free)")
    print("3. VoIP Services (Free)")
    print("4. Emergency Call Info")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        make_call_twilio()
    elif choice == "2":
        make_call_web_services()
    elif choice == "3":
        make_call_voip()
    elif choice == "4":
        emergency_call_info()
    else:
        print("❌ Invalid choice") 