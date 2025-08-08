import requests
import json
import time

def send_anonymous_whatsapp():
    """Send anonymous WhatsApp message using web services"""
    print("=" * 50)
    print("👻 ANONYMOUS WHATSAPP SENDER")
    print("=" * 50)
    
    print("⚠️  WARNING: This is for educational purposes only!")
    print("⚠️  Respect privacy and use responsibly!")
    print()
    
    try:
        # Get user input
        phone_number = input("📞 Enter phone number (with country code, e.g., +1234567890): ")
        message = input("💬 Enter your message: ")
        
        # Validate phone number
        if not phone_number.startswith('+'):
            print("❌ Please include country code with + symbol")
            return
        
        # Remove + and any spaces
        clean_number = phone_number.replace('+', '').replace(' ', '')
        
        print(f"\n📱 Target: {phone_number}")
        print(f"💬 Message: {message}")
        print("\n🔗 Attempting to send message...")
        
        # Method 1: Using WhatsApp Web API (requires setup)
        print("📡 Method 1: WhatsApp Web API")
        print("💡 This requires WhatsApp Business API setup")
        print("💡 For testing, you can use WhatsApp Web manually")
        
        # Method 2: Using online services (demonstration)
        print("\n📡 Method 2: Online Services")
        print("💡 Note: Most online services require registration")
        print("💡 Some services may not work due to WhatsApp's security")
        
        # Create WhatsApp Web URL
        whatsapp_url = f"https://wa.me/{clean_number}?text={message.replace(' ', '%20')}"
        
        print(f"\n🔗 WhatsApp Web URL:")
        print(f"   {whatsapp_url}")
        print("\n💡 Instructions:")
        print("   1. Copy the URL above")
        print("   2. Open it in your browser")
        print("   3. Click 'Continue to Chat'")
        print("   4. Send the message manually")
        
        # Alternative method using Python webbrowser
        import webbrowser
        open_browser = input("\n🌐 Open in browser automatically? (y/n): ").lower()
        if open_browser == 'y':
            webbrowser.open(whatsapp_url)
            print("✅ Browser opened with WhatsApp Web!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def send_anonymous_sms():
    """Send anonymous SMS using online services"""
    print("\n" + "=" * 50)
    print("📱 ANONYMOUS SMS SENDER")
    print("=" * 50)
    
    print("⚠️  WARNING: This is for educational purposes only!")
    print("⚠️  Most free SMS services are unreliable!")
    print()
    
    try:
        phone_number = input("📞 Enter phone number (with country code): ")
        message = input("💬 Enter your message: ")
        
        if not phone_number.startswith('+'):
            print("❌ Please include country code with + symbol")
            return
        
        print(f"\n📱 Target: {phone_number}")
        print(f"💬 Message: {message}")
        
        # List of free SMS services (for educational purposes)
        print("\n📡 Available SMS Services:")
        print("   1. TextBelt (requires API key)")
        print("   2. Twilio (requires account)")
        print("   3. Online SMS websites")
        
        print("\n💡 Note: Most reliable services require:")
        print("   - Registration/API key")
        print("   - Payment for credits")
        print("   - Phone number verification")
        
        print("\n🔗 Alternative: Use your phone's SMS app")
        print("   - This is the most reliable method")
        print("   - No additional setup required")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def create_anonymous_email():
    """Create anonymous email using temporary email services"""
    print("\n" + "=" * 50)
    print("📧 ANONYMOUS EMAIL CREATOR")
    print("=" * 50)
    
    print("💡 Temporary Email Services:")
    print("   1. 10minutemail.com")
    print("   2. temp-mail.org")
    print("   3. guerrillamail.com")
    print("   4. mailinator.com")
    
    print("\n🔗 Steps to send anonymous email:")
    print("   1. Visit a temporary email service")
    print("   2. Get a temporary email address")
    print("   3. Use that email to send messages")
    print("   4. Email expires after some time")
    
    print("\n⚠️  Important:")
    print("   - Temporary emails are often blocked")
    print("   - Recipients may mark as spam")
    print("   - Use responsibly and ethically")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Send anonymous WhatsApp message")
    print("2. Send anonymous SMS")
    print("3. Create anonymous email")
    
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == "1":
        send_anonymous_whatsapp()
    elif choice == "2":
        send_anonymous_sms()
    elif choice == "3":
        create_anonymous_email()
    else:
        print("❌ Invalid choice") 