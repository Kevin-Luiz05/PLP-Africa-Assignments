#!/usr/bin/env python3
"""ubuntu_fetcher.py
Ubuntu-Inspired Image Fetcher
- Prompts the user for a URL containing an image
- Creates Fetched_Images directory (if missing)
- Downloads the image using requests (with proper error handling)
- Saves image with filename extracted from URL or generated safely
- Respects errors and prints friendly messages (Ubuntu spirit)

Usage:
    python ubuntu_fetcher.py
Then enter/paste an image URL when prompted.
"""

import os
import sys
import requests # type: ignore
from urllib.parse import urlparse, unquote
from datetime import datetime

FETCH_DIR = "Fetched_Images"

def make_fetch_dir(path=FETCH_DIR):
    """Create the fetch directory if it doesn't exist."""
    try:
        os.makedirs(path, exist_ok=True)
        return path
    except OSError as e:
        print(f"Error: Could not create directory '{path}': {e}")
        raise

def extract_filename_from_url(url: str) -> str:
    """Attempt to extract a sane filename from URL. If not available, generate one."""
    parsed = urlparse(url)
    # take the path portion and unquote percent encoding
    path = unquote(parsed.path)
    filename = os.path.basename(path)
    # Basic sanity checks: filename should have an extension indicating image
    if filename and any(filename.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp']):
        return filename
    # else try to use last part of query or netloc
    if parsed.query:
        # as fallback, generate name from domain + timestamp
        domain = parsed.netloc.replace(':', '_')
        ext = '.jpg'
        return f"{domain}_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}{ext}"
    # fallback generic name
    return f"image_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.jpg"

def safe_filename(directory: str, filename: str) -> str:
    """Ensure filename does not collide; if it does, append a counter."""
    base, ext = os.path.splitext(filename)
    candidate = filename
    counter = 1
    while os.path.exists(os.path.join(directory, candidate)):
        candidate = f"{base}_{counter}{ext}"
        counter += 1
    return candidate

def download_image(url: str, dest_dir: str = FETCH_DIR, timeout: int = 15) -> str:
    """Download image from URL and save it into dest_dir. Returns saved filepath."""
    # Create directory
    make_fetch_dir(dest_dir)

    # Basic URL check
    if not url or not url.strip():
        raise ValueError("Empty URL provided.")

    url = url.strip()

    # Add a simple user-agent to be a polite client
    headers = {
        'User-Agent': 'UbuntuImageFetcher/1.0 (+https://example.org/)'
    }

    try:
        with requests.get(url, headers=headers, stream=True, timeout=timeout) as r:
            r.raise_for_status()  # HTTP errors -> exceptions

            # Respect content-type; ensure it's an image
            content_type = r.headers.get('Content-Type', '').lower()
            if not content_type.startswith('image/'):
                raise ValueError(f"URL does not point to an image. Content-Type: {content_type}")

            # Extract filename and ensure safe unique name
            filename = extract_filename_from_url(url)
            filename = safe_filename(dest_dir, filename)
            target_path = os.path.join(dest_dir, filename)

            # Stream the content to file in binary mode
            total_bytes = 0
            max_bytes = 50 * 1024 * 1024  # 50 MB safety limit
            with open(target_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:  # filter out keep-alive chunks
                        total_bytes += len(chunk)
                        if total_bytes > max_bytes:
                            # If file too large, abort and remove partial file
                            f.close()
                            os.remove(target_path)
                            raise ValueError('Image exceeds maximum allowed size (50 MB).')
                        f.write(chunk)

    except requests.exceptions.Timeout:
        raise ConnectionError('Request timed out. Please try again later.')
    except requests.exceptions.TooManyRedirects:
        raise ConnectionError('Too many redirects. The URL may be malformed.')
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f'Network error occurred: {e}')
    # Return the path where image saved
    return target_path

def prompt_and_fetch():
    print("Ubuntu Image Fetcher — 'I am because we are'\nRespectfully fetch and organize shared images from the web.\n")
    url = input('Enter image URL (or paste and press Enter): ').strip()
    if not url:
        print('No URL entered. Exiting.')
        return

    try:
        saved = download_image(url)
        print(f'Success! Image saved to: {saved}')
    except ValueError as ve:
        print(f'Failed to fetch image: {ve}')
    except ConnectionError as ce:
        print(f'Network/connection issue: {ce}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

if __name__ == '__main__':
    # If a URL is provided as a command-line argument, use it (useful for scripts).
    if len(sys.argv) > 1:
        input_url = sys.argv[1]
        try:
            saved_path = download_image(input_url)
            print(f'Success! Image saved to: {saved_path}')
        except Exception as e:
            print(f'Error: {e}')
            sys.exit(1)
    else:
        prompt_and_fetch()
