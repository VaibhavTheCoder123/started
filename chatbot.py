from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(_name_)

chatbot = ChatBot("StockBot")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = chatbot.get_response(user_message)
    return jsonify({"response": str(response)})

if _name_ == "_main_":
    app.run(debug=True)
