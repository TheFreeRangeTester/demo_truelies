import json
from true_lies import validate_llm_candidates

facts = {
    'FullName': {
        'extractor': 'categorical',
        'expected': 'Sophia Lopez',
        'patterns': {
            'Sophia Lopez': ['Sophia Lopez', 'Sofia Lopez', 'S. Lopez', 'Sophia', 'Ms. Lopez', 'Ms Lopez']
        }
    },
    'DoctorName': {
        'extractor': 'categorical',
        'expected': 'Dr. Sarah Green',
        'patterns': {
            'Dr. Sarah Green': ['Dr. Sarah Green', 'Doctor Sarah Green', 'Sarah Green', 'Dr Green']
        }
    },
    'Specialty': {
        'extractor': 'categorical',
        'expected': 'Ophthalmology',
        'patterns': {
            'Ophthalmology': ['Ophthalmology', 'ophthalmology', 'eye specialist', 'eye doctor']
        }
    },
    'AppointmentDate': {
        'extractor': 'categorical',
        'expected': '2025-10-09',
        'patterns': {
            '2025-10-09': ['2025-10-09', '10-09-2025', '09-10-2025', '09/10/2025', '09/10/25', 'October 9th, 2025', 'October 9, 2025', '9th of October', 'October 9th', 'Oct 9, 2025']
        }
    },
    'AppointmentTime': {
        'extractor': 'categorical',
        'expected': '4:30 PM',
        'patterns': {
            '4:30 PM': ['4:30 PM', '4:30 pm', '4:30PM', '16:30', '4.30 PM']
        }
    },
    'ClinicLocation': {
        'extractor': 'categorical',
        'expected': 'Southview Medical',
        'patterns': {
            'Southview Medical': ['Southview Medical', 'Southview', 'Southview Clinic', 'Southview Medical Clinic', 'Southview Medical Center', 'Southview Medical branch']
        }
    },
}

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
    html_output_file="true_lies_reporting/clinic_semana_1.html",
    html_title="Clinic Tests"
)