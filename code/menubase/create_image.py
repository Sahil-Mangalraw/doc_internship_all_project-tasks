from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random
import math
import os

def create_basic_image():
    """Create a basic colored image"""
    print("=" * 50)
    print("🎨 BASIC IMAGE CREATOR")
    print("=" * 50)
    
    try:
        width = int(input("📏 Enter width (pixels): "))
        height = int(input("📏 Enter height (pixels): "))
        color = input("🎨 Enter color (red/green/blue/white/black): ").lower()
        
        # Color mapping
        colors = {
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'white': (255, 255, 255),
            'black': (0, 0, 0)
        }
        
        rgb_color = colors.get(color, (255, 255, 255))
        
        # Create image
        image = Image.new('RGB', (width, height), rgb_color)
        
        # Save image
        filename = f"basic_image_{color}_{width}x{height}.png"
        image.save(filename)
        
        print(f"✅ Image created: {filename}")
        print(f"📊 Size: {width}x{height} pixels")
        print(f"🎨 Color: {color}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def create_gradient_image():
    """Create a gradient image"""
    print("\n" + "=" * 50)
    print("🌈 GRADIENT IMAGE CREATOR")
    print("=" * 50)
    
    try:
        width = int(input("📏 Enter width (pixels): "))
        height = int(input("📏 Enter height (pixels): "))
        
        print("Choose gradient type:")
        print("1. Linear (horizontal)")
        print("2. Linear (vertical)")
        print("3. Radial")
        print("4. Diagonal")
        
        choice = input("Enter choice (1-4): ")
        
        # Create gradient
        if choice == "1":  # Horizontal
            image = Image.new('RGB', (width, height))
            draw = ImageDraw.Draw(image)
            
            for x in range(width):
                r = int(255 * x / width)
                g = int(128 * x / width)
                b = int(255 * (width - x) / width)
                draw.line([(x, 0), (x, height)], fill=(r, g, b))
                
        elif choice == "2":  # Vertical
            image = Image.new('RGB', (width, height))
            draw = ImageDraw.Draw(image)
            
            for y in range(height):
                r = int(255 * y / height)
                g = int(128 * y / height)
                b = int(255 * (height - y) / height)
                draw.line([(0, y), (width, y)], fill=(r, g, b))
                
        elif choice == "3":  # Radial
            image = Image.new('RGB', (width, height))
            center_x, center_y = width // 2, height // 2
            max_distance = math.sqrt(center_x**2 + center_y**2)
            
            for y in range(height):
                for x in range(width):
                    distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
                    intensity = int(255 * (1 - distance / max_distance))
                    image.putpixel((x, y), (intensity, intensity//2, 255-intensity))
                    
        elif choice == "4":  # Diagonal
            image = Image.new('RGB', (width, height))
            draw = ImageDraw.Draw(image)
            
            for i in range(width + height):
                r = int(255 * i / (width + height))
                g = int(128 * i / (width + height))
                b = int(255 * ((width + height) - i) / (width + height))
                draw.line([(i, 0), (0, i)], fill=(r, g, b))
        else:
            print("❌ Invalid choice")
            return
        
        # Save image
        filename = f"gradient_{choice}_{width}x{height}.png"
        image.save(filename)
        
        print(f"✅ Gradient created: {filename}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def create_pattern_image():
    """Create a pattern image"""
    print("\n" + "=" * 50)
    print("🔲 PATTERN IMAGE CREATOR")
    print("=" * 50)
    
    try:
        width = int(input("📏 Enter width (pixels): "))
        height = int(input("📏 Enter height (pixels): "))
        
        print("Choose pattern type:")
        print("1. Checkerboard")
        print("2. Stripes")
        print("3. Dots")
        print("4. Waves")
        
        choice = input("Enter choice (1-4): ")
        
        image = Image.new('RGB', (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        
        if choice == "1":  # Checkerboard
            square_size = 20
            for y in range(0, height, square_size):
                for x in range(0, width, square_size):
                    if (x // square_size + y // square_size) % 2 == 0:
                        draw.rectangle([x, y, x + square_size, y + square_size], 
                                     fill=(0, 0, 0))
                        
        elif choice == "2":  # Stripes
            stripe_width = 20
            for x in range(0, width, stripe_width * 2):
                draw.rectangle([x, 0, x + stripe_width, height], 
                             fill=(255, 0, 0))
                
        elif choice == "3":  # Dots
            dot_size = 10
            spacing = 30
            for y in range(spacing, height, spacing):
                for x in range(spacing, width, spacing):
                    draw.ellipse([x - dot_size, y - dot_size, 
                                x + dot_size, y + dot_size], 
                               fill=(0, 0, 255))
                    
        elif choice == "4":  # Waves
            for x in range(width):
                for y in range(height):
                    wave = math.sin(x * 0.1) * 20 + math.cos(y * 0.1) * 20
                    intensity = int(128 + 127 * math.sin(wave))
                    image.putpixel((x, y), (intensity, intensity//2, 255-intensity))
        else:
            print("❌ Invalid choice")
            return
        
        # Save image
        filename = f"pattern_{choice}_{width}x{height}.png"
        image.save(filename)
        
        print(f"✅ Pattern created: {filename}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def create_text_image():
    """Create an image with text"""
    print("\n" + "=" * 50)
    print("📝 TEXT IMAGE CREATOR")
    print("=" * 50)
    
    try:
        width = int(input("📏 Enter width (pixels): "))
        height = int(input("📏 Enter height (pixels): "))
        text = input("📝 Enter text: ")
        font_size = int(input("🔤 Enter font size: "))
        
        # Create image
        image = Image.new('RGB', (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        
        # Try to use a default font
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
            except:
                font = ImageFont.load_default()
        
        # Calculate text position (center)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (width - text_width) // 2
        y = (height - text_height) // 2
        
        # Draw text
        draw.text((x, y), text, fill=(0, 0, 0), font=font)
        
        # Save image
        filename = f"text_image_{len(text)}.png"
        image.save(filename)
        
        print(f"✅ Text image created: {filename}")
        print(f"📝 Text: '{text}'")
        print(f"🔤 Font size: {font_size}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def create_artistic_image():
    """Create an artistic image"""
    print("\n" + "=" * 50)
    print("🎭 ARTISTIC IMAGE CREATOR")
    print("=" * 50)
    
    try:
        width = int(input("📏 Enter width (pixels): "))
        height = int(input("📏 Enter height (pixels): "))
        
        print("Choose artistic style:")
        print("1. Abstract")
        print("2. Fractal")
        print("3. Noise")
        print("4. Spiral")
        
        choice = input("Enter choice (1-4): ")
        
        image = Image.new('RGB', (width, height))
        
        if choice == "1":  # Abstract
            for y in range(height):
                for x in range(width):
                    r = (x * y) % 256
                    g = (x + y) % 256
                    b = (x ^ y) % 256
                    image.putpixel((x, y), (r, g, b))
                    
        elif choice == "2":  # Fractal
            for y in range(height):
                for x in range(width):
                    # Simple Mandelbrot-like pattern
                    cx = (x - width/2) / (width/4)
                    cy = (y - height/2) / (height/4)
                    
                    zx, zy = 0, 0
                    iteration = 0
                    max_iteration = 100
                    
                    while zx*zx + zy*zy < 4 and iteration < max_iteration:
                        zx, zy = zx*zx - zy*zy + cx, 2*zx*zy + cy
                        iteration += 1
                    
                    if iteration == max_iteration:
                        color = (0, 0, 0)
                    else:
                        color = (iteration * 25 % 256, iteration * 50 % 256, iteration * 75 % 256)
                    
                    image.putpixel((x, y), color)
                    
        elif choice == "3":  # Noise
            for y in range(height):
                for x in range(width):
                    noise = random.randint(0, 255)
                    image.putpixel((x, y), (noise, noise, noise))
                    
        elif choice == "4":  # Spiral
            center_x, center_y = width // 2, height // 2
            for angle in range(0, 3600, 5):
                radius = angle / 10
                x = int(center_x + radius * math.cos(math.radians(angle)))
                y = int(center_y + radius * math.sin(math.radians(angle)))
                
                if 0 <= x < width and 0 <= y < height:
                    color = (angle % 256, (angle * 2) % 256, (angle * 3) % 256)
                    image.putpixel((x, y), color)
        else:
            print("❌ Invalid choice")
            return
        
        # Save image
        filename = f"artistic_{choice}_{width}x{height}.png"
        image.save(filename)
        
        print(f"✅ Artistic image created: {filename}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def create_photo_effect():
    """Apply effects to an existing image"""
    print("\n" + "=" * 50)
    print("📸 PHOTO EFFECT APPLIER")
    print("=" * 50)
    
    try:
        image_path = input("📁 Enter image path: ")
        
        if not os.path.exists(image_path):
            print("❌ Image file not found!")
            return
        
        print("Choose effect:")
        print("1. Grayscale")
        print("2. Invert colors")
        print("3. Blur")
        print("4. Brightness adjustment")
        
        choice = input("Enter choice (1-4): ")
        
        # Open image
        image = Image.open(image_path)
        
        if choice == "1":  # Grayscale
            image = image.convert('L').convert('RGB')
            
        elif choice == "2":  # Invert
            image = Image.eval(image, lambda x: 255 - x)
            
        elif choice == "3":  # Blur
            from PIL import ImageFilter
            image = image.filter(ImageFilter.BLUR)
            
        elif choice == "4":  # Brightness
            factor = float(input("Enter brightness factor (0.5-2.0): "))
            image = Image.eval(image, lambda x: min(255, int(x * factor)))
            
        else:
            print("❌ Invalid choice")
            return
        
        # Save image
        base_name = os.path.splitext(image_path)[0]
        filename = f"{base_name}_effect_{choice}.png"
        image.save(filename)
        
        print(f"✅ Effect applied: {filename}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def batch_create_images():
    """Create multiple images in batch"""
    print("\n" + "=" * 50)
    print("📦 BATCH IMAGE CREATOR")
    print("=" * 50)
    
    try:
        count = int(input("📊 Number of images to create: "))
        width = int(input("📏 Width (pixels): "))
        height = int(input("📏 Height (pixels): "))
        
        print("Choose type:")
        print("1. Random colors")
        print("2. Random patterns")
        print("3. Numbered images")
        
        choice = input("Enter choice (1-3): ")
        
        for i in range(count):
            if choice == "1":  # Random colors
                color = (random.randint(0, 255), 
                        random.randint(0, 255), 
                        random.randint(0, 255))
                image = Image.new('RGB', (width, height), color)
                
            elif choice == "2":  # Random patterns
                image = Image.new('RGB', (width, height), (255, 255, 255))
                draw = ImageDraw.Draw(image)
                
                # Draw random shapes
                for _ in range(10):
                    x1 = random.randint(0, width)
                    y1 = random.randint(0, height)
                    x2 = random.randint(0, width)
                    y2 = random.randint(0, height)
                    color = (random.randint(0, 255), 
                            random.randint(0, 255), 
                            random.randint(0, 255))
                    draw.rectangle([x1, y1, x2, y2], fill=color)
                    
            elif choice == "3":  # Numbered images
                image = Image.new('RGB', (width, height), (255, 255, 255))
                draw = ImageDraw.Draw(image)
                
                try:
                    font = ImageFont.truetype("arial.ttf", 50)
                except:
                    font = ImageFont.load_default()
                
                text = str(i + 1)
                bbox = draw.textbbox((0, 0), text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                
                x = (width - text_width) // 2
                y = (height - text_height) // 2
                
                draw.text((x, y), text, fill=(0, 0, 0), font=font)
            else:
                print("❌ Invalid choice")
                return
            
            filename = f"batch_image_{i+1:03d}.png"
            image.save(filename)
            print(f"✅ Created: {filename}")
        
        print(f"\n📦 Batch complete! Created {count} images.")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("Choose an image creation option:")
    print("1. Basic Image")
    print("2. Gradient Image")
    print("3. Pattern Image")
    print("4. Text Image")
    print("5. Artistic Image")
    print("6. Photo Effect")
    print("7. Batch Create")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == "1":
        create_basic_image()
    elif choice == "2":
        create_gradient_image()
    elif choice == "3":
        create_pattern_image()
    elif choice == "4":
        create_text_image()
    elif choice == "5":
        create_artistic_image()
    elif choice == "6":
        create_photo_effect()
    elif choice == "7":
        batch_create_images()
    else:
        print("❌ Invalid choice") 