# 🎭 GitHub Actions - True Lies Testing

This workflow automatically runs your True Lies tests and publishes HTML reports to GitHub Pages.

## 🚀 Features

- ✅ Automatic execution on push and pull requests
- 📊 HTML report generation with True Lies Validator
- 📈 Validation history preservation between runs
- 🌐 GitHub Pages publication with direct URL access
- 💬 Automatic PR comments with test results

## 📋 When does it run?

The workflow executes automatically when:

- You push to `main`, `master`, or `develop` branches
- You create or update a Pull Request to these branches
- You manually trigger it from the Actions tab

## 🌐 Viewing reports

Reports are publicly available on GitHub Pages:

**URL:** https://thefreerangetester.github.io/demo_truelies/

Reports are automatically updated after each push to main and include:

- Detailed validation metrics
- Historical trend graphs
- Index page for easy navigation

## 📈 Validation history

The `validation_history.json` file is preserved between runs using GitHub Actions cache, allowing True Lies to generate trend graphs automatically showing:

- Success rate trends over time
- Semantic similarity evolution
- Factual accuracy changes
- Run-to-run comparisons

## ⚙️ Configuration

### Add more branches

To run the workflow on other branches, add them here:

```yaml
on:
  push:
    branches: [main, master, develop, your-branch-here]
```

### Install additional dependencies

Add extra packages in the "Install dependencies" step:

```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    pip install true-lies-validator>=0.8.0
    pip install your-additional-package
```

## 🐛 Troubleshooting

### Tests fail but I need the reports

The workflow uses `continue-on-error: true`, so reports are **always generated** even if tests fail.

### Reports not published to GitHub Pages

Verify that:

1. Your tests generate `.html` files
2. The `true_lies_reporting` directory exists
3. GitHub Pages is enabled: Settings → Pages → Source: "GitHub Actions"
4. The push was to `main` or `master` branch (only these publish to Pages)

## 📚 More information

- [True Lies Validator Documentation](https://pypi.org/project/true-lies-validator/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
