# optimize_images
# 画像最適化スクリプト（PNG・JPEG → WebP）

このスクリプトは、フォルダ内の **PNG・JPEG 画像を WebP に最適化** する Python プログラムです。

## 🚀 特徴
- **PNG** → 透過を維持しつつ、最大圧縮 (`lossless=True, method=6`)
- **JPEG** → 画質80% (`quality=80`) で軽量化
- **元のファイル名の大文字・小文字を維持**
- **フォルダ内の画像を一括変換**
