from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
      <head><title>pppeeekkkk</title></head>
      <body>
        <h1>Ujian BNSP</h1>
        <p>Nama: Luluk Dwi Kuncoro</p>
        <p>Layanan ini dideploy di VPS dengan Docker + CI/CD + Monitoring (Prometheus & Grafana).</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
