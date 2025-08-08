import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email():
    """Send email using SMTP"""
    print("=" * 50)
    print("📧 EMAIL SENDER")
    print("=" * 50)
    
    try:
        # Email configuration
        sender_email = input("📧 Enter your email: ")
        sender_password = input("🔐 Enter your password (or app password): ")
        receiver_email = input("📧 Enter recipient email: ")
        subject = input("📝 Enter subject: ")
        message_body = input("💬 Enter message: ")
        
        # Create message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        
        # Add body to email
        message.attach(MIMEText(message_body, "plain"))
        
        # Ask for attachment
        attach_file = input("📎 Do you want to attach a file? (y/n): ").lower()
        if attach_file == 'y':
            file_path = input("📁 Enter file path: ")
            if os.path.exists(file_path):
                with open(file_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {os.path.basename(file_path)}"
                )
                message.attach(part)
                print("✅ File attached successfully!")
            else:
                print("❌ File not found!")
        
        # Create SMTP session
        print("\n🔗 Connecting to SMTP server...")
        
        # Try different SMTP servers based on email provider
        smtp_servers = {
            "gmail.com": ("smtp.gmail.com", 587),
            "outlook.com": ("smtp-mail.outlook.com", 587),
            "yahoo.com": ("smtp.mail.yahoo.com", 587),
            "hotmail.com": ("smtp-mail.outlook.com", 587)
        }
        
        email_domain = sender_email.split('@')[1].lower()
        smtp_server, port = smtp_servers.get(email_domain, ("smtp.gmail.com", 587))
        
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        
        # Login
        print("🔐 Logging in...")
        server.login(sender_email, sender_password)
        
        # Send email
        print("📤 Sending email...")
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        
        print("✅ Email sent successfully!")
        
        # Close connection
        server.quit()
        
    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed!")
        print("💡 For Gmail, use App Password instead of regular password")
        print("💡 Enable 2-factor authentication and generate app password")
    except smtplib.SMTPRecipientsRefused:
        print("❌ Invalid recipient email address!")
    except smtplib.SMTPServerDisconnected:
        print("❌ Server connection lost!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

def send_bulk_email():
    """Send email to multiple recipients"""
    print("\n" + "=" * 50)
    print("📧 BULK EMAIL SENDER")
    print("=" * 50)
    
    try:
        sender_email = input("📧 Enter your email: ")
        sender_password = input("🔐 Enter your password: ")
        
        # Get recipient emails
        recipients = []
        print("📧 Enter recipient emails (press Enter twice when done):")
        while True:
            email = input("📧 Email: ")
            if email == "":
                break
            recipients.append(email)
        
        if not recipients:
            print("❌ No recipients specified!")
            return
        
        subject = input("📝 Enter subject: ")
        message_body = input("💬 Enter message: ")
        
        # SMTP setup
        smtp_server, port = "smtp.gmail.com", 587
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Send to each recipient
        for recipient in recipients:
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient
            message["Subject"] = subject
            message.attach(MIMEText(message_body, "plain"))
            
            text = message.as_string()
            server.sendmail(sender_email, recipient, text)
            print(f"✅ Sent to: {recipient}")
        
        server.quit()
        print(f"\n✅ Bulk email sent to {len(recipients)} recipients!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Send single email")
    print("2. Send bulk email")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        send_email()
    elif choice == "2":
        send_bulk_email()
    else:
        print("❌ Invalid choice") 