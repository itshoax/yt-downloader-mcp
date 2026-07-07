from yt_dlp import YoutubeDL
from typing import cast, Any
import logging

class VideoInfo():
  def __init__(self):
    self.options = {
      'quiet': True,
      'no_warnings': True,
      'skip_download': True,
      'extract_flat': False,
      'writesubtitles': False,
      'writeautomaticsub': False,
      'writethumbnail': False,
      'no-playlist': True,
    }
    self.logger = logging.getLogger(self.__class__.__name__)

  def _format_qualities(self, qualities: list) -> list:
    sorted_qualities = set()
    for format in qualities:
      if format.get('resolution') and format.get('resolution') != 'audio only':
        sorted_qualities.add(format.get('resolution'))

    sorted_qualities = sorted(
      sorted_qualities,
      key=lambda s: [int(x) for x in s.split('x')]
    )
    return sorted_qualities

  def get_info(self, url):
    try:
      with YoutubeDL(cast(Any, self.options)) as ydl:
        info = ydl.extract_info(url, download=False)

        return {
          'title': info.get('title'),
          'duration': info.get('duration'),
          'qualities': self._format_qualities(info.get('formats') or [])
        }
    except Exception as e:
      self.logger.error(f'Download failed: {e}')
      return { 'error': str(e) }
