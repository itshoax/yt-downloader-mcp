from services.downloader import Downloader
from fastmcp import FastMCP
from services.video_info import VideoInfo
from validations.video_validator import validate_youtube_url, validate_resolution, validate_output_path
import logging

DOWNLOAD_PATH = '/tmp'


mcp = FastMCP('yt-downloader')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

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
def download_video(url: str, resolution: int = 1080, download_path: str = DOWNLOAD_PATH):
  """
  Downloads a YouTube video at specified resolution.
  Blocks until download is complete. Progress shown in real time.

  Args:
    url: Full YouTube video URL.
    resolution: Video height in pixels. Choose from 360, 480, 720, 1080, 1440, 2160. Default 1080.
    download_path: Directory to save the downloaded video. Default '/tmp'.

  Returns:
    dict with status, title, and file path on success. Error message on failure.
  """
  if not validate_youtube_url(url):
    return { 'error': 'Invalid YouTube URL' }
  if not validate_resolution(resolution):
    return { 'error': 'Invalid resolution' }
  if not validate_output_path(download_path):
    return {
      'status': 'failed',
      'error': f'Path {download_path} does not exist or is not writable'
    }
  return Downloader(resolution, download_path).download_video(url)

@mcp.tool()
def download_playlist(url: str, resolution: int = 1080, download_path: str = DOWNLOAD_PATH) -> dict:
  """
  Downloads all videos in a YouTube playlist.
  Args:
    url: YouTube playlist URL
    resolution: Video height in pixels. Default 1080.
    output_path: Directory to save videos.
  """

  if not validate_youtube_url(url):
    return { 'error': 'Invalid YouTube URL' }
  if not validate_resolution(resolution):
    return { 'error': 'Invalid resolution' }
  if not validate_output_path(download_path):
    return {
      'status': 'failed',
      'error': f'Path {download_path} does not exist or is not writable'
    }
  return Downloader(resolution, download_path).download_playlist(url)

if __name__ == '__main__':
  mcp.run()
