import json
from true_lies import validate_llm_candidates

# Load facts from JSON file
with open('tests/data/clinic_facts.json', 'r') as f:
    data = json.load(f)
    facts = data['facts']

reference_text = "Let me help you, Sophia Lopez! Your next appointment is with Dr. Sarah Green, specialist in Ophthalmology, on 2025-10-09 at 4:30 PM at Southview Medical."

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
    generate_html_report=True,
    html_output_file="true_lies_reporting/daily_clinic_model_performance.html",
    html_title="Clinic Tests"
)