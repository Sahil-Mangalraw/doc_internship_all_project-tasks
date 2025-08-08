import cv2
import numpy as np
import dlib
import os
from PIL import Image
import requests

def face_swap_basic():
    """Basic face swap using OpenCV"""
    print("=" * 50)
    print("🔄 FACE SWAP TOOL")
    print("=" * 50)
    
    try:
        # Get image paths
        source_path = input("📸 Enter source image path: ")
        target_path = input("📸 Enter target image path: ")
        
        if not os.path.exists(source_path) or not os.path.exists(target_path):
            print("❌ One or both image files not found!")
            return
        
        print(f"\n🔄 Loading images...")
        print(f"   Source: {source_path}")
        print(f"   Target: {target_path}")
        
        # Load images
        source_img = cv2.imread(source_path)
        target_img = cv2.imread(target_path)
        
        if source_img is None or target_img is None:
            print("❌ Failed to load images!")
            return
        
        print(f"✅ Images loaded successfully!")
        print(f"   Source size: {source_img.shape}")
        print(f"   Target size: {target_img.shape}")
        
        # Convert to grayscale for face detection
        source_gray = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)
        target_gray = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)
        
        # Load face detection model
        print("\n🔍 Detecting faces...")
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Detect faces
        source_faces = face_cascade.detectMultiScale(source_gray, 1.1, 4)
        target_faces = face_cascade.detectMultiScale(target_gray, 1.1, 4)
        
        if len(source_faces) == 0:
            print("❌ No face detected in source image!")
            return
        
        if len(target_faces) == 0:
            print("❌ No face detected in target image!")
            return
        
        print(f"✅ Found {len(source_faces)} face(s) in source")
        print(f"✅ Found {len(target_faces)} face(s) in target")
        
        # Use the first face from each image
        source_face = source_faces[0]
        target_face = target_faces[0]
        
        # Extract face regions
        sx, sy, sw, sh = source_face
        tx, ty, tw, th = target_face
        
        source_face_region = source_img[sy:sy+sh, sx:sx+sw]
        target_face_region = target_img[ty:ty+th, tx:tx+tw]
        
        # Resize source face to match target face size
        source_face_resized = cv2.resize(source_face_region, (tw, th))
        
        # Simple face swap (just replace the region)
        result_img = target_img.copy()
        result_img[ty:ty+th, tx:tx+tw] = source_face_resized
        
        # Save result
        output_path = "face_swap_result.png"
        cv2.imwrite(output_path, result_img)
        
        print(f"\n✅ Face swap completed!")
        print(f"📁 Result saved as: {output_path}")
        
        # Show comparison
        print("\n📊 Face Swap Summary:")
        print(f"   Source face size: {sw}x{sh}")
        print(f"   Target face size: {tw}x{th}")
        print(f"   Result image size: {result_img.shape}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def face_swap_advanced():
    """Advanced face swap with facial landmarks"""
    print("\n" + "=" * 50)
    print("🔄 ADVANCED FACE SWAP")
    print("=" * 50)
    
    print("⚠️  This requires dlib and facial landmark model")
    print("💡 For best results, install dlib and download shape_predictor_68_face_landmarks.dat")
    
    try:
        # Check if dlib is available
        try:
            import dlib
            print("✅ dlib is available")
        except ImportError:
            print("❌ dlib not found. Installing...")
            import subprocess
            subprocess.check_call(["pip", "install", "dlib"])
            import dlib
        
        # Get image paths
        source_path = input("📸 Enter source image path: ")
        target_path = input("📸 Enter target image path: ")
        
        if not os.path.exists(source_path) or not os.path.exists(target_path):
            print("❌ One or both image files not found!")
            return
        
        # Load images
        source_img = cv2.imread(source_path)
        target_img = cv2.imread(target_path)
        
        # Convert to RGB for dlib
        source_rgb = cv2.cvtColor(source_img, cv2.COLOR_BGR2RGB)
        target_rgb = cv2.cvtColor(target_img, cv2.COLOR_BGR2RGB)
        
        # Initialize dlib face detector and landmark predictor
        detector = dlib.get_frontal_face_detector()
        
        # Try to load landmark predictor
        predictor_path = "shape_predictor_68_face_landmarks.dat"
        if not os.path.exists(predictor_path):
            print("❌ Facial landmark model not found!")
            print("💡 Download from: http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2")
            return
        
        predictor = dlib.shape_predictor(predictor_path)
        
        print("\n🔍 Detecting faces and landmarks...")
        
        # Detect faces
        source_faces = detector(source_rgb)
        target_faces = detector(target_rgb)
        
        if len(source_faces) == 0:
            print("❌ No face detected in source image!")
            return
        
        if len(target_faces) == 0:
            print("❌ No face detected in target image!")
            return
        
        print(f"✅ Found {len(source_faces)} face(s) in source")
        print(f"✅ Found {len(target_faces)} face(s) in target")
        
        # Get landmarks for first face in each image
        source_landmarks = predictor(source_rgb, source_faces[0])
        target_landmarks = predictor(target_rgb, target_faces[0])
        
        print(f"✅ Extracted {source_landmarks.num_parts} landmarks from each face")
        
        # Convert landmarks to numpy arrays
        source_points = np.array([[p.x, p.y] for p in source_landmarks.parts()])
        target_points = np.array([[p.x, p.y] for p in target_landmarks.parts()])
        
        # Calculate transformation matrix
        transformation_matrix = cv2.estimateAffinePartial2D(source_points, target_points)[0]
        
        # Apply transformation to source face
        source_face_warped = cv2.warpAffine(source_img, transformation_matrix, 
                                           (target_img.shape[1], target_img.shape[0]))
        
        # Create mask for face region
        hull = cv2.convexHull(target_points)
        mask = np.zeros(target_img.shape[:2], dtype=np.uint8)
        cv2.fillConvexPoly(mask, hull, 255)
        
        # Blend the faces
        mask_3d = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) / 255.0
        result_img = (source_face_warped * mask_3d + target_img * (1 - mask_3d)).astype(np.uint8)
        
        # Save result
        output_path = "advanced_face_swap_result.png"
        cv2.imwrite(output_path, result_img)
        
        print(f"\n✅ Advanced face swap completed!")
        print(f"📁 Result saved as: {output_path}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def face_detection_demo():
    """Demonstrate face detection"""
    print("\n" + "=" * 50)
    print("🔍 FACE DETECTION DEMO")
    print("=" * 50)
    
    try:
        image_path = input("📸 Enter image path: ")
        
        if not os.path.exists(image_path):
            print("❌ Image file not found!")
            return
        
        # Load image
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Load face detection model
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        print(f"🔍 Found {len(faces)} face(s)")
        
        # Draw rectangles around faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            print(f"   Face at ({x}, {y}) with size {w}x{h}")
        
        # Save result
        output_path = "face_detection_result.png"
        cv2.imwrite(output_path, img)
        
        print(f"✅ Face detection result saved as: {output_path}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def create_sample_images():
    """Create sample images for testing"""
    print("\n" + "=" * 50)
    print("📸 CREATE SAMPLE IMAGES")
    print("=" * 50)
    
    try:
        # Create two simple face-like images
        size = 200
        
        # Image 1 (face 1)
        img1 = np.ones((size, size, 3), dtype=np.uint8) * 255
        cv2.circle(img1, (size//2, size//3), 30, (0, 0, 0), -1)  # Head
        cv2.circle(img1, (size//2 - 20, size//2), 5, (0, 0, 0), -1)  # Left eye
        cv2.circle(img1, (size//2 + 20, size//2), 5, (0, 0, 0), -1)  # Right eye
        cv2.ellipse(img1, (size//2, size//2 + 20), (15, 10), 0, 0, 180, (0, 0, 0), 2)  # Mouth
        
        # Image 2 (face 2)
        img2 = np.ones((size, size, 3), dtype=np.uint8) * 200
        cv2.circle(img2, (size//2, size//3), 35, (100, 100, 100), -1)  # Head
        cv2.circle(img2, (size//2 - 25, size//2), 8, (100, 100, 100), -1)  # Left eye
        cv2.circle(img2, (size//2 + 25, size//2), 8, (100, 100, 100), -1)  # Right eye
        cv2.ellipse(img2, (size//2, size//2 + 25), (20, 15), 0, 0, 180, (100, 100, 100), 3)  # Mouth
        
        # Save images
        cv2.imwrite("sample_face1.png", img1)
        cv2.imwrite("sample_face2.png", img2)
        
        print("✅ Sample images created:")
        print("   - sample_face1.png")
        print("   - sample_face2.png")
        print("\n💡 You can use these for testing face swap!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def face_swap_tutorial():
    """Show face swap tutorial"""
    print("\n" + "=" * 50)
    print("📚 FACE SWAP TUTORIAL")
    print("=" * 50)
    
    print("🎯 How Face Swap Works:")
    print("   1. Detect faces in both images")
    print("   2. Extract facial landmarks")
    print("   3. Calculate transformation matrix")
    print("   4. Warp source face to match target")
    print("   5. Blend the faces together")
    print("   6. Apply color correction")
    
    print("\n🔧 Requirements:")
    print("   - OpenCV (cv2)")
    print("   - dlib (for advanced features)")
    print("   - numpy")
    print("   - Facial landmark model")
    
    print("\n📁 Required Files:")
    print("   - shape_predictor_68_face_landmarks.dat")
    print("   - Source and target images")
    
    print("\n💡 Tips for Better Results:")
    print("   - Use high-quality images")
    print("   - Ensure good lighting")
    print("   - Face should be clearly visible")
    print("   - Similar face angles work better")
    print("   - Avoid extreme expressions")
    
    print("\n⚠️  Limitations:")
    print("   - Works best with similar face shapes")
    print("   - Lighting differences can cause artifacts")
    print("   - Extreme angles may not work well")
    print("   - Requires good face detection")

def download_landmark_model():
    """Download facial landmark model"""
    print("\n" + "=" * 50)
    print("📥 DOWNLOAD LANDMARK MODEL")
    print("=" * 50)
    
    model_url = "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2"
    model_path = "shape_predictor_68_face_landmarks.dat"
    
    if os.path.exists(model_path):
        print("✅ Model already exists!")
        return
    
    try:
        print("📥 Downloading facial landmark model...")
        print("💡 This may take a few minutes...")
        
        response = requests.get(model_url, stream=True)
        response.raise_for_status()
        
        with open("shape_predictor_68_face_landmarks.dat.bz2", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print("✅ Download completed!")
        print("💡 Extract the .bz2 file to get the .dat file")
        
    except Exception as e:
        print(f"❌ Download failed: {e}")
        print("💡 You can manually download from:")
        print("   http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2")

if __name__ == "__main__":
    print("Choose a face swap option:")
    print("1. Basic Face Swap")
    print("2. Advanced Face Swap")
    print("3. Face Detection Demo")
    print("4. Create Sample Images")
    print("5. Tutorial")
    print("6. Download Model")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        face_swap_basic()
    elif choice == "2":
        face_swap_advanced()
    elif choice == "3":
        face_detection_demo()
    elif choice == "4":
        create_sample_images()
    elif choice == "5":
        face_swap_tutorial()
    elif choice == "6":
        download_landmark_model()
    else:
        print("❌ Invalid choice") 