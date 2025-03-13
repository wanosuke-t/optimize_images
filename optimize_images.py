from PIL import Image
import os

def optimize_image(input_path, output_path):
    """PNGは透過を保持して圧縮, JPEGは品質80で圧縮"""
    with Image.open(input_path) as img:
        ext = os.path.splitext(input_path)[1].lower()  # 拡張子だけ小文字に変換（ファイル名はそのまま）
        
        if ext == ".png":  # PNGなら透過保持＆method=6
            if img.mode != "RGBA":
                img = img.convert("RGBA")  # 透過対応

            # 圧縮率最大でWebP保存（透過保持）
            img.save(output_path, "WebP", lossless=True, method=6)
            print(f"✅ PNG圧縮: {input_path} → {output_path} (透過保持)")

        else:  # JPEGなら画質80%で圧縮
            if img.mode != "RGB":
                img = img.convert("RGB")  # JPEGはRGBに変換（透過なし）

            img.save(output_path, "WebP", lossless=False, quality=80)
            print(f"✅ JPEG圧縮: {input_path} → {output_path} (品質80)")

# 使い方
if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "output_images"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        ext = os.path.splitext(filename)[1].lower()  # 拡張子のみ小文字に変換（ファイル名は変更しない）
        
        if ext in (".png", ".jpg", ".jpeg"):  # 対象の拡張子
            input_path = os.path.join(input_folder, filename)

            # ファイル名の大文字・小文字はそのまま、拡張子のみ `.webp` に変更
            output_path = os.path.join(output_folder, filename.rsplit(".", 1)[0] + ".webp")

            optimize_image(input_path, output_path)
