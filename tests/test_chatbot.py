import json
from true_lies import validate_llm_candidates

# Facts that MUST be in the response
facts = {
    'policy_number': {'extractor': 'categorical', 'expected': 'POL-2024-001', 'patterns':{ 'POL-2024-001': ['POL-2024-001', 'POL-2024-002', 'POL-2024-003'] }},
    'amount': {'extractor': 'money', 'expected': '850'},
    'coverage_type': {'extractor': 'categorical',
    'expected': 'auto insurance',
    'patterns': {
        'auto insurance': [
            'auto insurance', 'car insurance', 'automobile', 'motor insurance', 'auto policy',
            'car policy', 'automobile policy',
            'motor policy', 'auto coverage', 'car coverage',
            'automobile coverage', 'vehicle'
        ]
    }}
}

# Reference text for semantic comparison
reference_text = "Your auto insurance policy #POL-2024-001 has a premium of $850"

# Create scenario (simplified structure for v0.8.0)
scenario = {
    "name": "What is the cover for my auto policy POL-2024-001?",
    "semantic_reference": reference_text,
    "facts": facts
}

# Load candidates from JSON file
with open('tests/data/chatbot_candidates.json', 'r') as f:
    data = json.load(f)
    candidates = data['candidates']

validation_result = validate_llm_candidates(
    scenario=scenario,
    candidates=candidates,
    threshold=0.5,
    generate_html_report=True,
    html_output_file="true_lies_reporting/performance_semana_1.html",
    html_title="Performance Tests - Week 1"
)