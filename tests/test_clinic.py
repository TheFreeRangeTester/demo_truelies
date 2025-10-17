import json
from true_lies import validate_llm_candidates

# Load facts from JSON file
with open('tests/data/clinic_facts.json', 'r') as f:
    data = json.load(f)
    facts = data['facts']

reference_text = "Your appointment with Dr. Garcia is confirmed for October 10th at 2:30 PM at Green Valley Clinic."

scenario = {
    "name": "What is the next appointment for Sophia Lopez?",
    "semantic_reference": reference_text,
    "facts": facts
}

# Load candidates from JSON file
with open('tests/data/clinic_candidates.json', 'r') as f:
    data = json.load(f)
    candidates = data['candidates']

validation_result = validate_llm_candidates(
    scenario=scenario,
    candidates=candidates,
    threshold=0.5,
    generate_html_report=False,
    html_output_file="true_lies_reporting/daily_clinic_model_performance.html",
    html_title="Clinic Tests"
)