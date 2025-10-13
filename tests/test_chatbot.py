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

# Validate responses
candidates = [
    "Policy POL-2024-001 does not cover your automobile with monthly payments of $850",
    "Your car insurance policy POL-2024-001 costs $850 monthly",
    "Your auto insurance policy POL-2024-001 provides coverage up to $850.",
    "I can confirm that policy POL-2024-001 for your vehicle is active with $850 in coverage.",
    "Great news! Your car insurance policy POL-2024-001 remains valid and offers $850 in protection.",
    "Policy POL-2024-001 is an auto insurance plan with a coverage amount of $850.",
    "Just a reminder: your auto policy POL-2024-001 currently covers you for $850.",
    "Auto coverage details: Policy POL-2024-001, insured amount $850.",
    "Your vehicle is insured under policy POL-2024-001, which includes $850 of coverage.",
    "I've verified that your auto policy POL-2024-001 offers $850 in benefits.",
    "Everything is set—your auto insurance, policy POL-2024-001, protects you up to $850.",
    "Summary: Auto insurance policy POL-2024-001 with a coverage limit of $850 is active and in good standing."
]

validation_result = validate_llm_candidates(
    scenario=scenario,
    candidates=candidates,
    threshold=0.5,
    generate_html_report=True,
    html_output_file="true_lies_reporting/performance_semana_1.html",
    html_title="Performance Tests - Week 1"
)