from yt_dlp import YoutubeDL

class Downloader():
  def __init__(self, resolution: int = 1080, output_dir: str = '/tmp'):
    self.options = {
      'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
      'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
      'merge_output_format': 'mp4',
      'progress_hooks': [self._on_progress],
    }

  def download_video(self, url):
    try:
      with YoutubeDL(self.options) as ydl:
        info = ydl.extract_info(url)
        return {
          'status': 'success',
          'title': info.get('title'),
          'path': f"{self.options['outtmpl']}",
        }
    except Exception as e
      print(f"Download failed: {str(e)}")
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
