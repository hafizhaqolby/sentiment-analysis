from youtube_comment_downloader import *
import pandas as pd

# ID video YouTube (ambil dari URL)
video_id = "-WLpXmnBmxo"

downloader = YoutubeCommentDownloader()
comments = []

print("🔍 Mulai ambil komentar...")

for comment in downloader.get_comments_from_url(f"https://www.youtube.com/watch?v={video_id}", sort_by=SORT_BY_POPULAR):
    comments.append(comment["text"])

print(f"✅ Total komentar diambil: {len(comments)}")

# Simpan ke CSV
df = pd.DataFrame(comments, columns=["comment"])
df.to_csv("presidenprabowomenjawab_youtube_comments.csv", index=False, encoding="utf-8")
print("📁 Komentar berhasil disimpan ke 'presidenprabowomenjawab_youtube_comments.csv'")