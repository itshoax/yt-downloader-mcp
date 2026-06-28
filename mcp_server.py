from services.downloader import Downloader
from fastmcp import FastMCP
from services.video_info import VideoInfo
from validations.video_validator import validate_youtube_url, validate_resolution

mcp = FastMCP('yt-downloader')

@mcp.tool()
def get_video_info(url: str) -> dict:
  """
  Fetches YouTube video metadata without downloading.

  Args:
    url: Full YouTube video or playlist URL.

  Returns:
    dict with title, thumbnail, duration, is_playlist, available formats/resolutions.
  """
  if not validate_youtube_url(url):
    return { 'error': 'Invalid YouTube URL' }
  return VideoInfo().get_info(url)

@mcp.tool()
def download_video(url: str, resolution: int = 1080):
  """
  Downloads a YouTube video at specified resolution.
  Blocks until download is complete. Progress shown in real time.

  Args:
    url: Full YouTube video URL.
    resolution: Video height in pixels. Choose from 360, 480, 720, 1080, 1440, 2160. Default 1080.

  Returns:
    dict with status, title, and file path on success. Error message on failure.
  """
  if not validate_youtube_url(url):
    return { 'error': 'Invalid YouTube URL' }
  if not validate_resolution(resolution):
    return { 'error': 'Invalid resolution' }
  return Downloader(resolution, '/tmp').download_video(url) # passing '/tmp' as the output directory later will replace it with user input

if __name__ == '__main__':
  mcp.run()
