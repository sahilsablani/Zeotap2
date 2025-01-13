from flask import Flask, request, jsonify
from scraper.segment_scraper import fetch_segment_docs
from scraper.mparticle_scraper import fetch_mparticle_docs
from scraper.lytics_scraper import fetch_lytics_docs
from scraper.zeotap_scraper import fetch_zeotap_docs
from indexer.content_indexer import search_docs

app = Flask(__name__)

# Map CDP names to their respective scraper functions
SCRAPERS = {
    "segment": fetch_segment_docs,
    "mparticle": fetch_mparticle_docs,
    "lytics": fetch_lytics_docs,
    "zeotap": fetch_zeotap_docs,
}

@app.route('/')
def index():
    return "Welcome to the CDP Chatbot! Ask how-to questions about Segment, mParticle, Lytics, or Zeotap."

@app.route('/query', methods=['POST'])
def query():
    user_question = request.json.get('question', '')
    cdp_name = request.json.get('cdp', '').lower()

    if not user_question or not cdp_name:
        return jsonify({"error": "Please provide both a question and a CDP name."}), 400

    # Get the scraper for the requested CDP
    scraper_function = SCRAPERS.get(cdp_name)
    if not scraper_function:
        return jsonify({"error": f"Invalid CDP name '{cdp_name}'. Supported CDPs: {', '.join(SCRAPERS.keys())}"}), 400

    # Fetch and index the CDP documentation
    try:
        documentation = scraper_function()
        response = search_docs(documentation, user_question)
        return jsonify({"answer": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
