from urllib.parse import urlparse

VALID_RESOLUTIONS = [360, 480, 720, 1080, 1440, 2160]

def validate_youtube_url(url: str) -> bool:
    parsed = urlparse(url)
    return 'youtube.com' in parsed.netloc or 'youtu.be' in parsed.netloc

def validate_resolution(resolution: int) -> bool:
    return resolution in VALID_RESOLUTIONS
