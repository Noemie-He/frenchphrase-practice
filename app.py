from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_phrases():
    with open('phrases.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    data = load_phrases()
    return render_template('index.html', scenes=data['scenes'])

@app.route('/scene/<scene_id>')
def scene(scene_id):
    data = load_phrases()
    scene_data = next((s for s in data['scenes'] if s['id'] == scene_id), None)
    return render_template('scene.html', scene=scene_data)

@app.route('/phrase/<int:phrase_id>')
def phrase(phrase_id):
    data = load_phrases()
    for scene in data['scenes']:
        for p in scene['phrases']:
            if p['id'] == phrase_id:
                return render_template('phrase.html', phrase=p, scene=scene)
    return "Phrase not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
