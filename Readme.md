# YouTube Downloader MCP
Youtube Downloader MCP lets you download YouTube videos via MCP directly in your agent. No more finding any download links or using external tools.
Just provide the video URL and let the MCP do the rest.
### Usage
- Connect to your agent via stdio MCP
- Clone the repo create a virtual python environment.
```bash
  python -m venv venv
  source venv/bin/activate
```
- Install the dependencies using `pip install -r requirements.txt`.
- In any MCP client, the configuration remains most likely the same.
```bash
  "youtube-downloader-mcp": {
    "command": "/path/to/yt-downloader-mcp/.venv/bin/python",
    "args" : ["/path/to/yt-downloader-mcp/mcp_server.py"]
  }
```

- Then just say to download the video or playlist like `download <url> with quality <quality> in <directory>`
- If you don't specify a directory, the video will be downloaded to the `/tmp` directory.
- If you don't specify a quality, the video will be downloaded in 1080P.
