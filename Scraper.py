import yt_dlp
import os

def download_data(url):
    print(f"Downloading {url}...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio_%(id)s.%(ext)s',
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['fa', 'fa-AF', 'prs'],
        'subtitlesformat': 'vtt',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Done downloading!")

if __name__ == "__main__":
    video_url = os.environ.get('VIDEO_URL')
    if video_url:
        download_data(video_url)
    else:
        print("No URL provided!")
