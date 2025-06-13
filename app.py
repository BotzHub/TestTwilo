from flask import Flask, request

app = Flask(__name__)

@app.route("/sms-handler", methods=["POST"])
def sms_receive():
    from_number = request.form.get("From")
    body = request.form.get("Body")
    print(f"📩 SMS from {from_number}: {body}")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
