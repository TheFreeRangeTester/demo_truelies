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

candidates = [
"Let me help you, Sophia Lopez! Your next appointment is with Dr. Sarah Green, specialist in Ophthalmology, on 2025-10-09 at 4:30 PM at Southview Medical.",
"Hi Sophia! You’re scheduled to see Dr. Sarah Green for Ophthalmology on October 9th, 2025 at 4:30 PM in Southview Medical Clinic.",
"Sophia Lopez, your upcoming Ophthalmology appointment with Dr. Sarah Green is set for 4:30 PM on October 9, 2025 at Southview Medical.",
"Sure thing, Sophia! You’ll be meeting Dr. Sarah Green from Ophthalmology on the 9th of October at 4:30 PM at our Southview Medical branch.",
"Certainly, Ms. Lopez. Your next Ophthalmology appointment with Dr. Sarah Green is on October 9, 2025 at 4:30 PM at Southview Medical.",
"Let me help you, Sophia Lopez! Your next appointment with Dr. Sarah Green in Ophthalmology is on 2025-10-09 at 4:30 PM.",
"Let me help you, Sophia Lopez! Your next appointment with Dr. Sarah Green is on 2025-10-09 at 3:30 PM at Southview Medical.",
"Let me help you, Sophia Lopez! Your next appointment with Dr. Sarah Green is on 2025-10-10 at 4:30 PM at Southview Medical.",
"Let me help you, Sophia Lopez! Your next appointment is with Dr. Emily Smith from Ophthalmology on 2025-10-09 at 4:30 PM at Southview Medical.",
"Let me help you, Sophia Lopez! Your next appointment is with Dr. Sarah Green, specialist in Cardiology, on 2025-10-09 at 4:30 PM at Southview Medical.",
"Let me help you, Sophia Lopez! Your next appointment is with Dr. Sarah Green on 2025-10-09 at 4:30 PM at Downtown Clinic.",
"Sophia, your next appointment is on 2025-10-09 at 4:30 PM at Southview Medical.",
"Hey Sophia! You’re booked with Dr. Sarah Green (Ophthalmology) on October 9th at 4:30 PM — Southview Medical.",
"Let me check that for you, Sophia Lopez. According to our system, your next medical visit is scheduled with Dr. Sarah Green, Ophthalmology specialist, on Thursday, October 9th 2025 at 4:30 PM, Southview Medical Center.",
"Let me help you, Sophia Lopez! Your next appointment at 4:30 PM on 2025-10-09 is with Dr. Sarah Green, Ophthalmology specialist, located in Southview Medical.",
]

validation_result = validate_llm_candidates(
    scenario=scenario,
    candidates=candidates,
    threshold=0.5,
    generate_html_report=True,
    html_output_file="true_lies_reporting/clinic_semana_1.html",
    html_title="Clinic Tests - Week 1"
)