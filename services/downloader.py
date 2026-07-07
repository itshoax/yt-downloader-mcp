from yt_dlp import YoutubeDL
from typing import cast, Any
import logging

class Downloader():
  def __init__(self, resolution: int = 1080, output_dir: str = '/tmp'):
    self.options = {
      'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
      'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
      'merge_output_format': 'mp4',
      'progress_hooks': [self._on_progress],
    }
    self.logger = logging.getLogger(self.__class__.__name__)

  def download_video(self, url):
    try:
      with YoutubeDL(cast(Any, self.options)) as ydl:
        info = ydl.extract_info(url)
        return {
          'status': 'success',
          'title': info.get('title'),
          'path': f"{self.options['outtmpl']}",
        }
    except Exception as e:
      self.logger.error(f'Download failed: {e}')
      return {
        'status': 'failed',
        'error': str(e),
      }

  def _on_progress(self, d):
    if d['status'] == 'finished':
      return print("Download complete, merging audio and video...")

    if d['status'] == 'downloading':
      percent = d.get('_percent_str', '0%').strip()
      speed = d.get('_speed_str', '').strip()
      eta = d.get('_eta_str', '').strip()
      return print(f"Downloading: {percent} | Speed: {speed} | ETA: {eta}")

    if d['status'] == 'error':
      return print(f'Download error: {d.get("error")}')

  def download_playlist(self, url):
    try:
      results = []
      with YoutubeDL(cast(Any, self.options)) as ydl:
        info = ydl.extract_info(url)
        entries = info.get('entries', [])
        for entry in entries:
          results.append({
            'title': entry.get('title'),
            'path': f"{self.options['outtmpl']}",
          })
      return {
        'status': 'success',
        'playlist_title': info.get('title'),
        'videos': results,
        'total_videos': len(results),
      }
    except Exception as e:
      self.logger.error(f'Playlist download failed: {e}')
      return {
        'status': 'failed',
        'error': str(e),
      }
