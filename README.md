# Chatbot Test Project 🤖

A Python chatbot project with natural language processing capabilities and automated response validation using **True Lies Validator**.

## 🚀 Initial Setup

### 1. Create and activate virtual environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
# Edit .env with your configurations
```

## 📁 Project Structure

```
chatbot-test/
├── .github/
│   └── workflows/          # GitHub Actions workflows
│       ├── test-and-report.yml
│       └── README.md
├── venv/                   # Virtual environment
├── tests/                  # True Lies tests
│   ├── test_chatbot.py
│   └── test_clinic.py
├── true_lies_reporting/    # Reports and historical data
│   └── validation_history.json
├── *.html                  # Generated HTML reports
├── requirements.txt        # Dependencies
├── .gitignore             # Files to ignore
└── README.md              # This file
```

## 🛠️ Development

### Run tests locally

```bash
# Run all tests
pytest tests/ -v

# Run a specific test
pytest tests/test_clinic.py -v
```

Tests will automatically generate HTML reports in the root directory and in `true_lies_reporting/`.

### 🎭 Validation with True Lies

This project uses **True Lies Validator** to validate chatbot responses. Tests evaluate:

- ✅ **Semantic similarity**: Does the response convey the same meaning?
- ✅ **Factual accuracy**: Are the extracted data points correct?
- ✅ **Polarity analysis**: Is the tone appropriate?

#### View reports locally

After running tests, open any `.html` file in your browser:

```bash
# On macOS
open clinic_semana_1.html

# On Linux
xdg-open clinic_semana_1.html

# On Windows
start clinic_semana_1.html
```

### 📊 GitHub Actions - Continuous Integration

The project includes a GitHub Actions workflow that:

1. ✅ Automatically runs tests on every push/PR
2. 📊 Generates HTML reports with True Lies
3. 📈 Preserves validation history for trends
4. 🌐 Publishes reports to GitHub Pages
5. 💬 Comments on PRs with result summaries

#### View reports on GitHub Pages

Reports are published at: **https://thefreerangetester.github.io/demo_truelies/**

- Direct browser access
- Automatically updated with every push to main
- Includes historical trend charts
- No need to download files

📖 For more details, see [`.github/workflows/README.md`](.github/workflows/README.md)

### Format code

```bash
black tests/
```

### Check code style

```bash
flake8 tests/
```

## 🛠️ Technologies

- **Python 3.13** - Programming language
- **True Lies Validator** - LLM response validation
- **pytest** - Testing framework
- **GitHub Actions** - Continuous integration and automated reporting

## 📝 Notes

- This project uses True Lies for automated chatbot response validation
- HTML reports include detailed metrics and interactive visualizations
- Validation history enables metric tracking over time
- GitHub Actions runs tests automatically and preserves history

## 🤝 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request