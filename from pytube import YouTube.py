from pytube import YouTube

def download_video(video_url, save_path):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()  # Get the highest resolution stream
        print(f"Downloading: {yt.title}")
        stream.download(output_path=save_path)
        print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the path to save the video: ")

    download_video(video_url, save_path)
