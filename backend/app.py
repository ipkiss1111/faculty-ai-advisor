from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)  # Разрешаем запросы от Vue.js

QUESTIONS = [
    {
        "id": 0,
        "text": "Какой предмет вам нравится больше всего?",
        "options": ["Математика", "Литература", "Биология", "Физика"]
    },
    # ... остальные вопросы
]

@app.route("/api/questions", methods=["GET"])
def get_questions():
    return jsonify(QUESTIONS)

@app.route("/api/analyze", methods=["POST"])
def analyze_answers():
    answers = request.json.get("answers")
    
    prompt = f"""
    Проанализируй ответы абитуриента и порекомендуй факультеты:
    1. Любимый предмет: {answers[0]}
    2. Деятельность: {answers[1]}
    3. Рабочая среда: {answers[2]}
    
    Дай развернутые рекомендации с объяснениями.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500
    )
    
    return jsonify({"result": response.choices[0].message['content']})

if __name__ == "__main__":
    app.run(port=5000)