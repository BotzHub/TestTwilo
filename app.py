from flask import Flask, request

app = Flask(__name__)

@app.route("/sms-handler", methods=["POST"])
def sms_receive():
    from_number = request.form.get("From")
    message = request.form.get("Body")
    print(f"SMS from {from_number}: {message}")
    return "OK", 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
