import yt_dlp
import os

def download_data(url):
    print(f"Downloading {url}...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio_%(id)s.%(ext)s', # Saves the audio file in the repo
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['fa', 'fa-AF', 'prs'],
        'subtitlesformat': 'vtt',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Done downloading!")

if __name__ == "__main__":
    # GitHub Actions will pass the URL as an environment variable
    video_url = os.environ.get('VIDEO_URL')
    if video_url:
        download_data(video_url)
    else:
        print("No URL provided!")
