from datetime import datetime
import time

from flask import Flask, Response, stream_with_context, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("sse.html")

@app.route("/stream-time")
def stream_time():
    def generate():
        while True:
            now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            # SSE-сообщение: только дата и время
            yield f"data: {now}\n\n"
            time.sleep(1)
    return Response(stream_with_context(generate()),
                    mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(threaded=True)
