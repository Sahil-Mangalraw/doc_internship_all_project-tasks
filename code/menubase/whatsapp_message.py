import pywhatkit as pwk
import datetime
import time

def send_whatsapp_message():
    """Send WhatsApp message using pywhatkit"""
    print("=" * 50)
    print("📱 WHATSAPP MESSAGE SENDER")
    print("=" * 50)
    
    try:
        # Get user input
        phone_number = input("📞 Enter phone number (with country code, e.g., +1234567890): ")
        message = input("💬 Enter your message: ")
        
        # Validate phone number
        if not phone_number.startswith('+'):
            print("❌ Please include country code with + symbol")
            return
        
        # Get current time
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 1  # Send message 1 minute from now
        
        print(f"\n⏰ Sending message at {hour:02d}:{minute:02d}")
        print(f"📱 To: {phone_number}")
        print(f"💬 Message: {message}")
        
        # Send the message
        pwk.sendwhatmsg(phone_number, message, hour, minute)
        
        print("\n✅ Message sent successfully!")
        print("💡 Note: WhatsApp Web will open automatically")
        
    except ValueError as e:
        print(f"❌ Invalid input: {e}")
    except Exception as e:
        print(f"❌ Error sending message: {e}")
        print("💡 Make sure:")
        print("   - You have WhatsApp Web set up")
        print("   - Your phone is connected to internet")
        print("   - The phone number is correct")

def send_whatsapp_image():
    """Send WhatsApp image"""
    print("\n" + "=" * 50)
    print("🖼️ WHATSAPP IMAGE SENDER")
    print("=" * 50)
    
    try:
        phone_number = input("📞 Enter phone number (with country code): ")
        image_path = input("🖼️ Enter image path: ")
        caption = input("💬 Enter caption (optional): ")
        
        if not phone_number.startswith('+'):
            print("❌ Please include country code with + symbol")
            return
        
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 1
        
        print(f"\n⏰ Sending image at {hour:02d}:{minute:02d}")
        pwk.sendwhats_image(phone_number, image_path, caption, hour, minute)
        
        print("✅ Image sent successfully!")
        
    except Exception as e:
        print(f"❌ Error sending image: {e}")

if __name__ == "__main__":
    try:
        print("Choose an option:")
        print("1. Send text message")
        print("2. Send image")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            send_whatsapp_message()
        elif choice == "2":
            send_whatsapp_image()
        else:
            print("❌ Invalid choice")
            
    except ImportError:
        print("❌ pywhatkit module not found. Installing...")
        import subprocess
        subprocess.check_call(["pip", "install", "pywhatkit"])
        print("✅ pywhatkit installed successfully!")
        print("Please run the script again.")
    except Exception as e:
        print(f"❌ Error: {e}") 