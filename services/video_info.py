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

  def get_info(self, url):
    with YoutubeDL(self.options) as ydl:
      info = ydl.extract_info(url, download=False)
      qualities = set()
      for format in info.get('formats', []):
        if format.get('resolution') and format.get('resolution') != 'audio only':
          qualities.add(format.get('resolution'))

      sorted_qualities = sorted(
        qualities,
        key=lambda s: [int(x) for x in s.split('x')]
      )

      result = {
        'title': info.get('title'),
        'qualities': sorted_qualities
      }
      return result
