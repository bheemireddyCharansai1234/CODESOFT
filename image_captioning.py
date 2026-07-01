import os
import sys
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

def find_image():
    # Look for any file starting with 'test' in the current directory
    valid_extensions = ['.jpg', '.jpeg', '.png', '.webp', '.bmp']
    for file in os.listdir('.'):
        name, ext = os.path.splitext(file.lower())
        if name == 'test' and ext in valid_extensions:
            return file
    return None

def generate_caption(image_path):
    print("🤖 Loading pre-trained AI Vision models (this may take a moment on first run)...")
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    
    try:
        raw_image = Image.open(image_path).convert('RGB')
    except Exception as e:
        print(f"❌ Error: Could not open the image file. Details: {e}")
        return None

    print("🔍 Analyzing image features and generating caption...")
    inputs = processor(raw_image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

def main():
    print("=" * 55)
    print("📸 AI IMAGE CAPTIONING UTILITY INITIALIZED 📸")
    print("=" * 55)
    
    # Automatically locate the image file in the directory
    image_path = find_image()
    
    if not image_path:
        print("❌ Error: Could not find any image named 'test' in C:\\Users\\bheem")
        print("Please ensure your image file is pasted inside the folder.")
        sys.exit()
        
    print(f"[+] Found image file: {image_path}")
    caption = generate_caption(image_path)
    
    if caption:
        print("\n" + "="*40)
        print(f"✅ SUCCESSFUL ANALYSIS")
        print(f"Target Image: {image_path}")
        print(f"Generated AI Caption: \"{caption.capitalize()}\"")
        print("="*40 + "\n")

if __name__ == "__main__":
    main()