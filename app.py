token = "YOUR API KEY HERE"

from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

openai.api_key = token
response = openai.FineTune.list()
for model in response['data']:
    print(model['training_files'][0]['filename'] + ": " + model['fine_tuned_model'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_description():
    prompt = request.json.get('prompt', '')
    response = openai.Completion.create(
      model="YOUR MODEL HERE", 
      prompt=prompt, 
      max_tokens=10
    )
    return jsonify({"description": response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
