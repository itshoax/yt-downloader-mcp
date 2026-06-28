from services.downloader import Downloader
from fastmcp import FastMCP
from services.video_info import VideoInfo

mcp = FastMCP('yt-downloader')

@mcp.tool()
def get_video_info(url: str) -> dict:
  return VideoInfo().get_info(url)

@mcp.tool()
def download_video(url: str, resolution: int = 1080):
  return Downloader(resolution).download_video(url)

if __name__ == '__main__':
  mcp.run()
