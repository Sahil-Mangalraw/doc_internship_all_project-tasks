import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import json
import webbrowser

def send_anonymous_email_smtp():
    """Send anonymous email using SMTP with fake sender"""
    print("=" * 50)
    print("🕵️ ANONYMOUS EMAIL SENDER (SMTP)")
    print("=" * 50)
    
    print("⚠️  WARNING: This is for educational purposes only!")
    print("⚠️  Use responsibly and ethically!")
    print("⚠️  Many email providers block fake sender addresses!")
    print()
    
    try:
        # Email configuration
        fake_sender = input("📧 Enter fake sender email: ")
        receiver_email = input("📧 Enter recipient email: ")
        subject = input("📝 Enter subject: ")
        message_body = input("💬 Enter message: ")
        
        # SMTP server (using a public SMTP server)
        smtp_server = input("🔗 Enter SMTP server (e.g., smtp.gmail.com): ")
        smtp_port = int(input("🔗 Enter SMTP port (e.g., 587): "))
        
        # Create message
        message = MIMEMultipart()
        message["From"] = fake_sender
        message["To"] = receiver_email
        message["Subject"] = subject
        
        # Add body to email
        message.attach(MIMEText(message_body, "plain"))
        
        print(f"\n📧 Sending anonymous email...")
        print(f"   From: {fake_sender}")
        print(f"   To: {receiver_email}")
        print(f"   Subject: {subject}")
        
        # Try to send (this will likely fail due to authentication)
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            
            # This will fail without proper authentication
            server.sendmail(fake_sender, receiver_email, message.as_string())
            server.quit()
            
            print("✅ Email sent successfully!")
            
        except smtplib.SMTPAuthenticationError:
            print("❌ Authentication failed!")
            print("💡 Most SMTP servers require authentication")
            print("💡 Fake sender addresses are usually blocked")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def send_anonymous_email_web_service():
    """Send anonymous email using web services"""
    print("\n" + "=" * 50)
    print("🕵️ ANONYMOUS EMAIL SENDER (Web Services)")
    print("=" * 50)
    
    print("📡 Available Anonymous Email Services:")
    print("   1. 10minutemail.com")
    print("   2. temp-mail.org")
    print("   3. guerrillamail.com")
    print("   4. mailinator.com")
    print("   5. yopmail.com")
    
    try:
        choice = input("\nChoose service (1-5): ")
        
        service_urls = {
            "1": "https://10minutemail.com",
            "2": "https://temp-mail.org",
            "3": "https://guerrillamail.com",
            "4": "https://mailinator.com",
            "5": "https://yopmail.com"
        }
        
        if choice in service_urls:
            url = service_urls[choice]
            print(f"\n🔗 Opening: {url}")
            webbrowser.open(url)
            print("✅ Service opened in browser!")
            print("\n💡 Instructions:")
            print("   1. Get a temporary email address")
            print("   2. Use it to send emails")
            print("   3. Check for responses")
            print("   4. Email expires after some time")
        else:
            print("❌ Invalid choice")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def create_temporary_email():
    """Create a temporary email address"""
    print("\n" + "=" * 50)
    print("📧 TEMPORARY EMAIL CREATOR")
    print("=" * 50)
    
    print("🔧 Steps to create temporary email:")
    print("   1. Visit a temporary email service")
    print("   2. Generate a temporary email address")
    print("   3. Use it for registration or testing")
    print("   4. Check for incoming emails")
    print("   5. Email expires automatically")
    
    print("\n📡 Popular Temporary Email Services:")
    print("   - 10minutemail.com (10 minutes)")
    print("   - temp-mail.org (24 hours)")
    print("   - guerrillamail.com (1 hour)")
    print("   - mailinator.com (no expiration)")
    print("   - yopmail.com (no expiration)")
    
    print("\n⚠️  Important Notes:")
    print("   - Temporary emails are often blocked by websites")
    print("   - Some services may be unreliable")
    print("   - Use for testing purposes only")
    print("   - Don't use for important communications")

def send_anonymous_email_api():
    """Send anonymous email using API services"""
    print("\n" + "=" * 50)
    print("🕵️ ANONYMOUS EMAIL SENDER (API)")
    print("=" * 50)
    
    print("📡 API Services for Anonymous Emails:")
    print("   1. SendGrid (requires setup)")
    print("   2. Mailgun (requires setup)")
    print("   3. Amazon SES (requires setup)")
    print("   4. Custom SMTP server")
    
    print("\n💡 Note: Most API services require:")
    print("   - Account registration")
    print("   - API key authentication")
    print("   - Domain verification")
    print("   - Sender address verification")
    
    print("\n🔗 API Service Links:")
    print("   - SendGrid: sendgrid.com")
    print("   - Mailgun: mailgun.com")
    print("   - Amazon SES: aws.amazon.com/ses")

def email_privacy_tips():
    """Show email privacy tips"""
    print("\n" + "=" * 50)
    print("🔒 EMAIL PRIVACY TIPS")
    print("=" * 50)
    
    print("🛡️  How to Protect Your Email Privacy:")
    print("   1. Use a VPN when sending emails")
    print("   2. Use encrypted email services (ProtonMail, Tutanota)")
    print("   3. Use temporary email for registrations")
    print("   4. Don't share your real email publicly")
    print("   5. Use email aliases")
    print("   6. Enable two-factor authentication")
    print("   7. Use strong, unique passwords")
    print("   8. Be careful with email attachments")
    print("   9. Don't click suspicious links")
    print("   10. Regularly check for suspicious activity")
    
    print("\n🔐 Encrypted Email Services:")
    print("   - ProtonMail (protonmail.com)")
    print("   - Tutanota (tutanota.com)")
    print("   - Hushmail (hushmail.com)")
    print("   - Mailfence (mailfence.com)")

if __name__ == "__main__":
    print("Choose an anonymous email option:")
    print("1. SMTP Method (Limited)")
    print("2. Web Services (Free)")
    print("3. Create Temporary Email")
    print("4. API Services (Paid)")
    print("5. Privacy Tips")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        send_anonymous_email_smtp()
    elif choice == "2":
        send_anonymous_email_web_service()
    elif choice == "3":
        create_temporary_email()
    elif choice == "4":
        send_anonymous_email_api()
    elif choice == "5":
        email_privacy_tips()
    else:
        print("❌ Invalid choice") 