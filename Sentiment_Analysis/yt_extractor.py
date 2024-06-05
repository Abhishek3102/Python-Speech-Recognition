import yt_dlp as youtube_dl

ydl = youtube_dl.YoutubeDL()

def get_video_info(url):
    with ydl:
        result = ydl.extract_info(
            url,
            download=False
        )
    if "entries" in result:
        return result["entries"][0]
    return result

def get_audio_url(video_info):
    print(video_info)

if __name__ == "__main__":
    video_info = get_video_info("https://youtu.be/MD0k7aWS5Fc?si=VW1dm4s8A4sWU9yN")
    audio_url = get_audio_url(video_info)
    print(audio_url)
