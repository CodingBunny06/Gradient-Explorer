# Contributing to Gradient Explorer

Thank you for your interest in improving Gradient Explorer. This is an individual academic project maintained by its owner; contributions and well-written issue reports are welcome, but please discuss substantial changes before investing time in them.

## Before you start

- Read the [README](README.md) to understand the application and supported equation syntax.
- Check existing issues and pull requests to avoid duplicating work.
- For security concerns, follow [SECURITY.md](SECURITY.md) instead of opening a public issue.

## Development setup

The CI workflow uses Python 3.12.

```bash
git clone https://github.com/CodingBunny06/Gradient-Explorer.git
cd Gradient-Explorer
python3.12 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate       # Windows
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Make and test changes

1. Create a focused branch from `main`.
2. Keep changes small and explain the reasoning behind non-obvious decisions.
3. Preserve the equation parser's allowlist and resource limits. Do not introduce arbitrary `eval` or `exec` execution.
4. Add or update tests for behavior changes, especially mathematical edge cases and invalid input.
5. Run the full test suite:

   ```bash
   python -m pytest -v
   ```

6. Update documentation when user-visible behavior, supported syntax, setup, or architecture changes.

## Pull requests

- Use a descriptive title and complete the pull request template.
- Explain the problem, implementation, and how the change was tested.
- Include screenshots for meaningful UI changes when practical.
- Disclose dependency changes and any security implications.
- Do not include credentials, API keys, personal data, virtual environments, or generated caches.

All contributions are subject to maintainer review. Opening a pull request does not guarantee acceptance or a particular review timeline.
