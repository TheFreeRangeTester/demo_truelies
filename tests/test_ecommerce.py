import json
from true_lies import validate_llm_candidates

# Load facts from JSON file
with open('tests/data/ecommerce_facts.json', 'r') as f:
    data = json.load(f)
    facts = data['facts']

# Baseline: informal, geek-style response
reference_text = "Hey! The Game Boy Color is $100 USD with shipping in 10 business days. Ready to level up? 🎮"

scenario = {
    "name": "How much is the Game Boy Color and when does it ship?",
    "semantic_reference": reference_text,
    "facts": facts
}

# Load candidates from JSON file
with open('tests/data/ecommerce_candidates.json', 'r') as f:
    data = json.load(f)
    candidates = data['candidates']

validation_result = validate_llm_candidates(
    scenario=scenario,
    candidates=candidates,
    threshold=0.5,
    generate_html_report=True,
    html_output_file="true_lies_reporting/ecommerce_model_performance.html",
    html_title="Ecommerce - Digital Products Tests"
)
