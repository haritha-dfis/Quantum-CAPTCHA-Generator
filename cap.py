# captcha_with_verification.py
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string
import numpy as np
import secrets

# --- Random string generator ---
def random_string(length=6):
    charset = string.ascii_letters + string.digits
    return ''.join(secrets.choice(charset) for _ in range(length))

# --- CAPTCHA generator ---
def generate_captcha(text=None, width=280, height=110):
    if text is None:
        text = random_string(6)

    bg_color = tuple(np.random.randint(200, 255, size=3))
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)

    fonts = ["arial.ttf", "times.ttf", "calibri.ttf"]
    try:
        font = ImageFont.truetype(random.choice(fonts), 42)
    except:
        font = ImageFont.load_default()

    # Random lines
    for _ in range(random.randint(8, 15)):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        line_color = tuple(np.random.randint(100, 180, size=3))
        draw.line(((x1, y1), (x2, y2)), fill=line_color, width=random.randint(1, 3))

    # Draw characters
    x_offset = 20
    for ch in text:
        y_pos = random.randint(20, 45)
        text_color = tuple(np.random.randint(0, 100, size=3))
        draw.text((x_offset, y_pos), ch, font=font, fill=text_color)
        x_offset += random.randint(35, 45)

    # Slight rotation and blur
    image = image.rotate(random.uniform(-3, 3), expand=0, fillcolor=bg_color)
    image = image.filter(ImageFilter.GaussianBlur(random.uniform(0.3, 1.0)))

    filename = f"captcha_{secrets.randbelow(10000)}.png"
    image.save(filename)
    print(f"✅ CAPTCHA Generated: {text}")
    print(f"🖼️ Saved as '{filename}'")
    image.show()

    return text

# --- CAPTCHA verification ---
def verify_captcha():
    captcha_text = generate_captcha()
    user_input = input("Enter the CAPTCHA text you see: ")
    if user_input.strip() == captcha_text:
        print("✅ Verification successful! You typed it correctly.")
    else:
        print(f"❌ Verification failed! Correct text was: {captcha_text}")

# --- Run ---
if __name__ == "__main__":
    verify_captcha()
