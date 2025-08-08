import streamlit as st
import subprocess
import os
import sys
import tempfile

# Set page config
st.set_page_config(
    page_title="Python Automation Dashboard",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    .input-section {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🐍 Python Automation Dashboard</h1>', unsafe_allow_html=True)

# Automatically find all .py scripts except app.py
script_files = [f for f in os.listdir() if f.endswith('.py') and f != 'app.py']

# Create a comprehensive mapping for display names
display_names = {
    "ram_check.py": "💾 Check RAM Usage",
    "whatsapp_message.py": "📱 Send WhatsApp Message",
    "send_email.py": "📧 Send Email",
    "whatsapp_anonymous.py": "👻 Send Anonymous WhatsApp",
    "send_sms.py": "💬 Send SMS",
    "make_call.py": "📞 Make Phone Call",
    "google_search.py": "🔍 Google Search",
    "social_media_post.py": "📢 Post on Social Media",
    "web_scraper.py": "🌐 Web Scraping",
    "anonymous_email.py": "🕵️ Send Anonymous Email",
    "tuple_vs_list.py": "📚 Tuple vs List Comparison",
    "create_image.py": "🎨 Create Digital Image",
    "face_swap.py": "🔄 Face Swap Tool"
}

# Build menu options
menu_options = [display_names.get(f, f) for f in script_files]

# Sidebar for navigation
st.sidebar.markdown("## 🎯 Select Feature")
selected = st.sidebar.selectbox("Choose a feature to run", menu_options)

# Map selection back to filename
selected_file = None
for fname, dname in display_names.items():
    if dname == selected:
        selected_file = fname
        break
if not selected_file:
    # fallback if not in display_names
    selected_file = selected

# Main content area
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown(f'<div class="feature-card"><h3>{selected}</h3></div>', unsafe_allow_html=True)
    
    # Input section based on selected script
    st.markdown('<div class="input-section">', unsafe_allow_html=True)
    st.subheader("📝 Input Parameters")
    
    # Create input fields based on the selected script
    inputs = {}
    
    if selected_file == "whatsapp_message.py":
        inputs['phone_number'] = st.text_input("📞 Phone Number (with country code)", placeholder="+1234567890")
        inputs['message'] = st.text_area("💬 Message", placeholder="Enter your WhatsApp message")
        inputs['choice'] = st.selectbox("📱 Message Type", ["1", "2"], format_func=lambda x: "Text Message" if x == "1" else "Image Message")
        if inputs['choice'] == "2":
            inputs['image_path'] = st.text_input("🖼️ Image Path", placeholder="path/to/image.jpg")
            inputs['caption'] = st.text_input("💬 Caption (optional)")
            
    elif selected_file == "send_email.py":
        inputs['sender_email'] = st.text_input("📧 Your Email", placeholder="your.email@gmail.com")
        inputs['sender_password'] = st.text_input("🔐 Password/App Password", type="password")
        inputs['receiver_email'] = st.text_input("📧 Recipient Email", placeholder="recipient@example.com")
        inputs['subject'] = st.text_input("📝 Subject", placeholder="Email subject")
        inputs['message_body'] = st.text_area("💬 Message", placeholder="Enter your email message")
        inputs['choice'] = st.selectbox("📧 Email Type", ["1", "2"], format_func=lambda x: "Single Email" if x == "1" else "Bulk Email")
        if inputs['choice'] == "2":
            inputs['recipients'] = st.text_area("📧 Recipient Emails (one per line)", placeholder="email1@example.com\nemail2@example.com")
            
    elif selected_file == "send_sms.py":
        inputs['service'] = st.selectbox("📡 SMS Service", ["1", "2", "3", "4"], 
                                       format_func=lambda x: ["Twilio", "TextBelt", "Free Services", "Setup Instructions"][int(x)-1])
        if inputs['service'] == "1":  # Twilio
            inputs['account_sid'] = st.text_input("🔑 Twilio Account SID")
            inputs['auth_token'] = st.text_input("🔑 Twilio Auth Token", type="password")
            inputs['twilio_number'] = st.text_input("📞 Twilio Phone Number", placeholder="+1234567890")
        elif inputs['service'] == "2":  # TextBelt
            inputs['api_key'] = st.text_input("🔑 TextBelt API Key", type="password")
        if inputs['service'] in ["1", "2", "3"]:
            inputs['phone_number'] = st.text_input("📞 Recipient Phone Number", placeholder="+1234567890")
            inputs['message'] = st.text_area("💬 SMS Message", placeholder="Enter your SMS message")
            
    elif selected_file == "make_call.py":
        inputs['method'] = st.selectbox("📞 Calling Method", ["1", "2", "3", "4"], 
                                      format_func=lambda x: ["Twilio API", "Web Services", "VoIP Services", "Emergency Info"][int(x)-1])
        if inputs['method'] == "1":  # Twilio
            inputs['account_sid'] = st.text_input("🔑 Twilio Account SID")
            inputs['auth_token'] = st.text_input("🔑 Twilio Auth Token", type="password")
            inputs['twilio_number'] = st.text_input("📞 Twilio Phone Number", placeholder="+1234567890")
        if inputs['method'] in ["1", "2"]:
            inputs['phone_number'] = st.text_input("📞 Recipient Phone Number", placeholder="+1234567890")
            
    elif selected_file == "google_search.py":
        inputs['method'] = st.selectbox("🔍 Search Method", ["1", "2", "3", "4", "5"], 
                                      format_func=lambda x: ["Web Scraping", "Google API", "Open in Browser", "Other Engines", "Setup Instructions"][int(x)-1])
        if inputs['method'] in ["1", "2", "3", "4"]:
            inputs['query'] = st.text_input("🔍 Search Query", placeholder="Enter your search term")
        if inputs['method'] in ["1", "2"]:
            inputs['num_results'] = st.slider("📊 Number of Results", 1, 10, 5)
        if inputs['method'] == "2":  # Google API
            inputs['api_key'] = st.text_input("🔑 Google API Key")
            inputs['search_engine_id'] = st.text_input("🔑 Search Engine ID")
        if inputs['method'] == "4":  # Other engines
            inputs['engine'] = st.selectbox("🔍 Search Engine", ["1", "2", "3", "4", "5"], 
                                          format_func=lambda x: ["Bing", "DuckDuckGo", "Yahoo", "Wikipedia", "YouTube"][int(x)-1])
            
    elif selected_file == "social_media_post.py":
        inputs['platform'] = st.selectbox("📢 Social Media Platform", ["1", "2", "3", "4", "5", "6"], 
                                         format_func=lambda x: ["Twitter", "Facebook", "Instagram", "LinkedIn", "Open in Browser", "Setup Instructions"][int(x)-1])
        if inputs['platform'] in ["1", "2", "3", "4"]:
            inputs['content'] = st.text_area("💬 Post Content", placeholder="Enter your post content")
        if inputs['platform'] == "1":  # Twitter
            inputs['api_key'] = st.text_input("🔑 Twitter API Key")
            inputs['api_secret'] = st.text_input("🔑 Twitter API Secret", type="password")
            inputs['access_token'] = st.text_input("🔑 Access Token")
            inputs['access_token_secret'] = st.text_input("🔑 Access Token Secret", type="password")
        elif inputs['platform'] == "2":  # Facebook
            inputs['access_token'] = st.text_input("🔑 Facebook Access Token")
            inputs['page_id'] = st.text_input("📄 Page ID (optional)")
        elif inputs['platform'] == "3":  # Instagram
            inputs['access_token'] = st.text_input("🔑 Instagram Access Token")
            inputs['user_id'] = st.text_input("👤 Instagram User ID")
            inputs['image_url'] = st.text_input("🖼️ Image URL")
        elif inputs['platform'] == "4":  # LinkedIn
            inputs['access_token'] = st.text_input("🔑 LinkedIn Access Token")
            
    elif selected_file == "web_scraper.py":
        inputs['option'] = st.selectbox("🌐 Scraping Option", ["1", "2", "3", "4"], 
                                       format_func=lambda x: ["Scrape Website Data", "Download Files", "Multi-Page Scraper", "Open Website"][int(x)-1])
        if inputs['option'] in ["1", "2", "3"]:
            inputs['url'] = st.text_input("🔗 Website URL", placeholder="https://example.com")
        if inputs['option'] == "1":  # Scrape data
            inputs['output_format'] = st.selectbox("📄 Output Format", ["json", "csv", "txt"])
        elif inputs['option'] == "2":  # Download files
            inputs['file_types'] = st.text_input("📁 File Types", placeholder="pdf,jpg,png", value="pdf,jpg,png")
        elif inputs['option'] == "3":  # Multi-page
            inputs['max_pages'] = st.slider("📄 Maximum Pages", 1, 20, 5)
        elif inputs['option'] == "4":  # Open website
            inputs['url'] = st.text_input("🔗 Website URL", placeholder="example.com")
            
    elif selected_file == "anonymous_email.py":
        inputs['method'] = st.selectbox("🕵️ Anonymous Email Method", ["1", "2", "3", "4", "5"], 
                                       format_func=lambda x: ["SMTP Method", "Web Services", "Create Temporary Email", "API Services", "Privacy Tips"][int(x)-1])
        if inputs['method'] == "1":  # SMTP
            inputs['fake_sender'] = st.text_input("📧 Fake Sender Email", placeholder="fake@example.com")
            inputs['receiver_email'] = st.text_input("📧 Recipient Email", placeholder="recipient@example.com")
            inputs['subject'] = st.text_input("📝 Subject", placeholder="Email subject")
            inputs['message_body'] = st.text_area("💬 Message", placeholder="Enter your message")
            inputs['smtp_server'] = st.text_input("🔗 SMTP Server", placeholder="smtp.gmail.com")
            inputs['smtp_port'] = st.number_input("🔗 SMTP Port", value=587, min_value=1, max_value=65535)
        elif inputs['method'] == "2":  # Web services
            inputs['service'] = st.selectbox("📡 Service", ["1", "2", "3", "4", "5"], 
                                           format_func=lambda x: ["10minutemail.com", "temp-mail.org", "guerrillamail.com", "mailinator.com", "yopmail.com"][int(x)-1])
            
    elif selected_file == "create_image.py":
        inputs['option'] = st.selectbox("🎨 Image Creation Option", ["1", "2", "3", "4", "5", "6", "7"], 
                                       format_func=lambda x: ["Basic Image", "Gradient Image", "Pattern Image", "Text Image", "Artistic Image", "Photo Effect", "Batch Create"][int(x)-1])
        if inputs['option'] in ["1", "2", "3", "4", "5", "7"]:
            inputs['width'] = st.number_input("📏 Width (pixels)", value=400, min_value=1, max_value=2000)
            inputs['height'] = st.number_input("📏 Height (pixels)", value=300, min_value=1, max_value=2000)
        if inputs['option'] == "1":  # Basic image
            inputs['color'] = st.selectbox("🎨 Color", ["red", "green", "blue", "white", "black"])
        elif inputs['option'] == "2":  # Gradient
            inputs['gradient_type'] = st.selectbox("🌈 Gradient Type", ["1", "2", "3", "4"], 
                                                 format_func=lambda x: ["Horizontal", "Vertical", "Radial", "Diagonal"][int(x)-1])
        elif inputs['option'] == "3":  # Pattern
            inputs['pattern_type'] = st.selectbox("🔲 Pattern Type", ["1", "2", "3", "4"], 
                                                format_func=lambda x: ["Checkerboard", "Stripes", "Dots", "Waves"][int(x)-1])
        elif inputs['option'] == "4":  # Text image
            inputs['text'] = st.text_input("📝 Text", placeholder="Enter text to display")
            inputs['font_size'] = st.number_input("🔤 Font Size", value=50, min_value=10, max_value=200)
        elif inputs['option'] == "5":  # Artistic
            inputs['artistic_type'] = st.selectbox("🎭 Artistic Style", ["1", "2", "3", "4"], 
                                                 format_func=lambda x: ["Abstract", "Fractal", "Noise", "Spiral"][int(x)-1])
        elif inputs['option'] == "6":  # Photo effect
            inputs['image_path'] = st.text_input("📁 Image Path", placeholder="path/to/image.jpg")
            inputs['effect'] = st.selectbox("📸 Effect", ["1", "2", "3", "4"], 
                                          format_func=lambda x: ["Grayscale", "Invert Colors", "Blur", "Brightness"][int(x)-1])
            if inputs['effect'] == "4":
                inputs['brightness_factor'] = st.slider("💡 Brightness Factor", 0.5, 2.0, 1.0, 0.1)
        elif inputs['option'] == "7":  # Batch create
            inputs['count'] = st.number_input("📊 Number of Images", value=5, min_value=1, max_value=50)
            inputs['batch_type'] = st.selectbox("📦 Batch Type", ["1", "2", "3"], 
                                              format_func=lambda x: ["Random Colors", "Random Patterns", "Numbered Images"][int(x)-1])
            
    elif selected_file == "face_swap.py":
        inputs['option'] = st.selectbox("🔄 Face Swap Option", ["1", "2", "3", "4", "5", "6"], 
                                       format_func=lambda x: ["Basic Face Swap", "Advanced Face Swap", "Face Detection Demo", "Create Sample Images", "Tutorial", "Download Model"][int(x)-1])
        if inputs['option'] in ["1", "2", "3"]:
            inputs['source_path'] = st.text_input("📸 Source Image Path", placeholder="path/to/source.jpg")
            inputs['target_path'] = st.text_input("📸 Target Image Path", placeholder="path/to/target.jpg")
            
    elif selected_file == "whatsapp_anonymous.py":
        inputs['option'] = st.selectbox("👻 Anonymous Option", ["1", "2", "3"], 
                                       format_func=lambda x: ["Anonymous WhatsApp", "Anonymous SMS", "Anonymous Email"][int(x)-1])
        if inputs['option'] in ["1", "2"]:
            inputs['phone_number'] = st.text_input("📞 Phone Number", placeholder="+1234567890")
            inputs['message'] = st.text_area("💬 Message", placeholder="Enter your message")
            
    else:
        # For scripts that don't need specific inputs (like ram_check.py, tuple_vs_list.py)
        st.info("ℹ️ This feature doesn't require additional input parameters.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Run the selected script with inputs
    if st.button(f"🚀 Run {selected}", type="primary", use_container_width=True):
        try:
            with st.spinner(f"Running {selected}..."):
                # Create a temporary input file with the inputs
                input_data = "\n".join([f"{k}={v}" for k, v in inputs.items() if v])
                
                # For scripts that need input, we'll need to modify them to read from environment variables
                # For now, we'll run them normally and they'll prompt for input
                result = subprocess.run([sys.executable, selected_file], 
                                      capture_output=True, text=True, timeout=30,
                                      input=input_data if input_data else None)
                
                if result.stdout:
                    st.success("✅ Execution completed successfully!")
                    st.subheader("📤 Output:")
                    st.code(result.stdout, language="text")
                
                if result.stderr:
                    st.warning("⚠️ Warnings/Errors:")
                    st.code(result.stderr, language="text")
                    
        except subprocess.TimeoutExpired:
            st.error("⏰ Execution timed out after 30 seconds")
        except FileNotFoundError:
            st.error(f"❌ Script file '{selected_file}' not found")
        except Exception as e:
            st.error(f"❌ Error running {selected_file}: {str(e)}")

# Information section
st.markdown("---")
st.markdown("## 📋 Available Features")

# Create a grid layout for features
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **System & Communication:**
    - 💾 RAM Usage Check
    - 📱 WhatsApp Messaging
    - 📧 Email Sending
    - 💬 SMS Sending
    - 📞 Phone Calls
    """)

with col2:
    st.markdown("""
    **Web & Search:**
    - 🔍 Google Search
    - 🌐 Web Scraping
    - 📢 Social Media Posts
    - 🕵️ Anonymous Email
    - 👻 Anonymous WhatsApp
    """)

with col3:
    st.markdown("""
    **Creative & Learning:**
    - 🎨 Digital Image Creation
    - 🔄 Face Swap Tool
    - 📚 Tuple vs List Comparison
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>🐍 Built with Python & Streamlit | 🚀 Automation Dashboard</p>
</div>
""", unsafe_allow_html=True) 