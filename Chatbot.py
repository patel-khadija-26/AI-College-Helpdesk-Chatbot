from flask import Flask, request, jsonify

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Chatbot</title>
</head>
<body style="font-family: Arial; text-align:center;">

<h2>College Chatbot 🤖</h2>

<div id="chatbox" style="border:1px solid black; height:300px; width:300px; margin:auto; overflow:auto;"></div>

<input type="text" id="userInput">
<button onclick="sendMessage()">Send</button>

<script>
function sendMessage() {
    let input = document.getElementById("userInput").value;

    document.getElementById("chatbox").innerHTML += "<p><b>You:</b> " + input + "</p>";

    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: input})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("chatbox").innerHTML += "<p><b>Bot:</b> " + data.reply + "</p>";
    });

    document.getElementById("userInput").value = "";
}
</script>

</body>
</html>
"""

def get_response(msg):
    msg = msg.lower()

    if "admission" in msg or "apply" in msg:
        return "Admissions start from June. You can apply online."

    elif "exam" in msg:
        return "Exams are conducted in December and May."

    elif "fees" in msg:
        return "Total fees is approximately ₹80,000 per year."

    elif "hostel" in msg:
        return "Hostel fees is around ₹30,000 per year."

    elif "placement" in msg:
        return "Top companies like TCS and Infosys visit our college."

    elif "faculty" in msg:
        return "Our faculty is highly experienced."

    elif "complaint" in msg:
        return "You can submit complaints in the admin office."

    else:
        return "I didn't understand."

@app.route("/")
def home():
    return html_page

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    return jsonify({"reply": get_response(user_input)})

# FIXED PART
if __name__ == "__main__":
    app.run(debug=True)


