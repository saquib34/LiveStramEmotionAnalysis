from flask import Flask, request, Response
import requests
from urllib.parse import urljoin, urlparse, quote

app = Flask(__name__)

def resolve_url(base, path):
    """Resolve relative URLs properly"""
    if path.startswith('http'):
        return path
    return urljoin(base, path)

@app.route('/proxy')
def hls_proxy():
    original_url = request.args.get('url')
    if not original_url:
        return 'Missing URL parameter', 400

    try:
        parsed = urlparse(original_url)
        base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path.rsplit('/', 1)[0]}/"
        
        resp = requests.get(original_url, stream=True, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        return f'Proxy error: {str(e)}', 500

    content_type = resp.headers.get('Content-Type', '')

    if 'mpegurl' in content_type or original_url.endswith(('.m3u8', '.m3u')):
        modified_content = []
        parent_url = original_url.rsplit('/', 1)[0] + '/'
        
        for line in resp.text.split('\n'):
            line = line.strip()
            if line.startswith('#EXT-X-STREAM-INF') or line.startswith('#EXT-X-MEDIA'):
                modified_content.append(line)
            elif line.startswith('#'):
                modified_content.append(line)
            elif line:
                # Resolve relative paths properly
                absolute_url = resolve_url(parent_url, line)
                proxy_url = f"{request.host_url}proxy?url={quote(absolute_url)}"
                modified_content.append(proxy_url)
            else:
                modified_content.append('')
        
        response = Response('\n'.join(modified_content), content_type=content_type)
    else:
        response = Response(resp.iter_content(chunk_size=1024*1024), content_type=content_type)

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

if __name__ == '__main__':
    app.run(port=5000, threaded=True)