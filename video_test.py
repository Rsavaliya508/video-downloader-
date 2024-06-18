import asyncio
import subprocess

# List of video URLs
video_urls = [
    "your_video_url_1",
    "your_video_url_2",
    "etc.."
]


# Referer URL
# referer_url = "your_referal_url_if_any"
# Directory to save videos
save_directory = "your_save_dir"
semaphore = asyncio.Semaphore(10)

async def download_video(url):
    async with semaphore:
        # command = ["yt-dlp", "--referer", referer_url, url, "-P", save_directory]
        command = ["yt-dlp", url, "-P", save_directory]
        process = await asyncio.create_subprocess_exec(
            *command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if process.returncode == 0:
            print(f"Downloaded {url} successfully.")
        else:
            print(f"Failed to download {url}. Error: {stderr.decode()}")

async def main():
    tasks = [download_video(url) for url in video_urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())