from yt_dlp import YoutubeDL

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

  def _format_qualities(self, qualities: list) -> list:
    for format in qualities:
      if format.get('resolution') and format.get('resolution') != 'audio only':
        qualities.add(format.get('resolution'))

    sorted_qualities = sorted(
      qualities,
      key=lambda s: [int(x) for x in s.split('x')]
    )
    return sorted_qualities

  def get_info(self, url):
    try:
      with YoutubeDL(self.options) as ydl:
        info = ydl.extract_info(url, download=False)

        return {
          'title': info.get('title'),
          'duration': info.get('duration'),
          'qualities': self._format_qualities(info.get('formats', []))
        }
    except Exception as e:
      print(f"Info fetching failed: {str(e)}")
      return { 'error': str(e) }
