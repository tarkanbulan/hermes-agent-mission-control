import http.server
import socketserver
import json
import os
import glob
from urllib.parse import urlparse, parse_qs
import dagit_ekip

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(DIRECTORY)

class MissionControlHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def _set_headers(self, content_type="application/json"):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def _send_json_error(self, message, status=400):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"error": message}).encode("utf-8"))

    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path.startswith("/api/"):
            if path == "/api/gorevler":
                self._handle_get_files(os.path.join(PROJECT_ROOT, "01_GOREV_MERKEZI"))
            elif path == "/api/loglar":
                self._handle_get_files(os.path.join(PROJECT_ROOT, "05_LOG_MERKEZI"))
            elif path == "/api/ruya":
                self._handle_get_files(os.path.join(PROJECT_ROOT, "04_RUYA_PROTOKOLU", "KARBON_HAVUZU"))
            else:
                self._send_json_error("Not Found", 404)
            return

        # Fallback to serving files from 06_DASHBOARD directory
        return super().do_GET()

    def _handle_get_files(self, dir_path):
        self._set_headers()
        files_data = []

        if os.path.exists(dir_path):
            md_files = glob.glob(os.path.join(dir_path, "*.md"))
            for md_file in md_files:
                try:
                    with open(md_file, "r", encoding="utf-8") as f:
                        content = f.read()
                    filename = os.path.basename(md_file)
                    files_data.append({"filename": filename, "content": content})
                except Exception as e:
                    print(f"Error reading {md_file}: {e}")

        self.wfile.write(json.dumps(files_data).encode("utf-8"))

    def do_POST(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path.startswith("/api/kopru/"):
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length == 0:
                self._send_json_error("Missing request body")
                return

            post_data = self.rfile.read(content_length).decode('utf-8')
            try:
                data = json.loads(post_data)
                rapor_yolu = data.get("rapor_yolu")
            except json.JSONDecodeError:
                self._send_json_error("Invalid JSON")
                return

            if not rapor_yolu:
                self._send_json_error("Missing 'rapor_yolu' in request body")
                return

            # Convert to absolute path or path relative to PROJECT_ROOT
            if not os.path.isabs(rapor_yolu):
                rapor_yolu = os.path.join(PROJECT_ROOT, rapor_yolu)

            hedef = path.split("/")[-1]
            success, message = False, ""

            if hedef == "spark":
                success, message = dagit_ekip.kopru_spark(rapor_yolu)
            elif hedef == "jules":
                success, message = dagit_ekip.kopru_jules(rapor_yolu)
            elif hedef == "agy":
                success, message = dagit_ekip.kopru_agy(rapor_yolu)
            elif hedef == "geri":
                success, message = dagit_ekip.kopru_geri(rapor_yolu)
            else:
                self._send_json_error("Bilinmeyen köprü hedefi", 404)
                return

            self._set_headers()
            self.wfile.write(json.dumps({"success": success, "message": message}).encode("utf-8"))
        else:
            self._send_json_error("Not Found", 404)


def run(server_class=http.server.HTTPServer, handler_class=MissionControlHandler, port=PORT):
    # Change current working directory to PROJECT_ROOT so that paths are relative to root if needed,
    # but handler is configured to serve from DIRECTORY. We serve from DIRECTORY so index.html works.
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    print(f"Mission Control Dashboard: http://127.0.0.1:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server stopped.")

if __name__ == "__main__":
    run()
