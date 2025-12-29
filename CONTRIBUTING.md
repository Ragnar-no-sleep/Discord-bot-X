# Contributing to ASDF X Post Generator

Thank you for your interest in contributing!

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ragnar-no-sleep/Discord-bot-X.git
   cd Discord-bot-X
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install ruff pytest  # Dev dependencies
   ```

4. **Set up environment**
   ```bash
   cp .env.example .env
   # Edit .env with your Discord bot token
   ```

## Code Standards

### Linting

We use [Ruff](https://github.com/astral-sh/ruff) for linting. Before committing:

```bash
ruff check .
```

### Testing

Run tests before submitting changes:

```bash
pytest tests/ -v
```

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `chore:` Maintenance tasks
- `test:` Adding/updating tests
- `ci:` CI/CD changes

Example:
```
feat: add new raid template for product launch
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/amazing-feature`)
3. Make your changes
4. Run linting and tests
5. Commit with a clear message
6. Push to your fork
7. Open a Pull Request

## Security

- **Never commit secrets** (tokens, API keys, etc.)
- Report security vulnerabilities privately (see [SECURITY.md](SECURITY.md))
- Use environment variables for sensitive configuration

## Adding New Templates

### Raid Template
Edit `config.py` and add to `RAID_TEMPLATES`:

```python
"new_style": {
    "template": """Your template here...""",
    "products": ["holdex", "ignition"],
    "style": "your_style"
}
```

### Thread Template
Add to `THREAD_TEMPLATES`:

```python
"new_thread": [
    "Tweet 1...",
    "Tweet 2...",
    # ...
]
```

### FUD Response
Add to `FUD_RESPONSES`:

```python
"new_fud_type": [
    "Response 1...",
    "Response 2...",
]
```

## Questions?

Open an issue or reach out to the maintainers.
