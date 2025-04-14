import pandas as pd
import re
from langdetect import detect, LangDetectException
import emoji

# Load file hasil scraping
df = pd.read_csv("presidenprabowomenjawab_youtube_comments.csv")

print(f"📦 Total komentar mentah: {len(df)}")

# Fungsi cleaning
def clean_comment(text):
    if pd.isnull(text) or len(text.strip()) < 5:
        return None
    text = re.sub(r"http\S+", "", text)  # hapus link
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # hapus angka/simbol
    text = text.lower().strip()
    return text if len(text) >= 5 else None

# Bersihkan komentar
df["cleaned_comment"] = df["comment"].apply(clean_comment)
df = df.dropna(subset=["cleaned_comment"]).reset_index(drop=True)

# Hapus Emoji
def clean_comment(text):
    if pd.isnull(text) or len(text.strip()) < 5:
        return None
    text = re.sub(r"http\S+", "", text)
    text = emoji.replace_emoji(text, "")  # HAPUS EMOJI
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = text.lower().strip()
    return text if len(text) >= 5 else None

# Deteksi bahasa
def detect_lang(text):
    try:
        return detect(text)
    except LangDetectException:
        return "unknown"

print("🌍 Deteksi bahasa tiap komentar...")
df["lang"] = df["cleaned_comment"].apply(detect_lang)

# Filter hanya bahasa Indonesia
df_id = df[df["lang"] == "id"].reset_index(drop=True)

# Simpan hasilnya
df_id.to_csv("youtube_comments_cleaned.csv", index=False, encoding="utf-8")
print(f"✅ Komentar bahasa Indonesia: {len(df_id)}")
print("📁 Disimpan ke 'youtube_comments_cleaned.csv'")
