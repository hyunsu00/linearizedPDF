#!/usr/bin/env python3

from flask import Flask, render_template, send_from_directory
import time

class SlowResponseMiddleware:
    def __init__(self, app, delay=1, chunk_size=1024):
        self.app = app
        self.delay = delay  # 각 청크 사이의 지연 시간(초)
        self.chunk_size = chunk_size  # 청크 크기(바이트)

    def __call__(self, environ, start_response):
        app_iter = self.app(environ, start_response)
        for chunk in self.chunked_response(app_iter):
            time.sleep(self.delay)  # 지연 시간 추가
            yield chunk

    def chunked_response(self, app_iter):
        for data in app_iter:
            for i in range(0, len(data), self.chunk_size):
                yield data[i:i+self.chunk_size]

app = Flask(__name__)

# 대역폭 제한 미들웨어 적용
# app.wsgi_app = SlowResponseMiddleware(app.wsgi_app, delay=0.5, chunk_size=1024 * 100)  # 예: 0.5초 지연, 100KB 청크

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pdf/<filename>')
def pdf_viewer(filename):
    return send_from_directory('static/pdfs', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)