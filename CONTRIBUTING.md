# Contributing to Safe Code Resources

Thanks for your interest in contributing! This module curates high-signal resources that help developers write secure code. Contributions that improve accuracy, coverage, and usability are welcome.

## Ways to contribute
- Propose new resources (must be widely adopted, actively maintained, and directly relevant to secure coding)
- Improve descriptions for clarity and precision
- Fix links or update star counts (approximate)
- Add examples or integration notes to the README

## Getting started
1. Fork the repository and create a feature branch:
   - `feat/resource-<name>` for new entries
   - `docs/update-readme` for documentation updates
2. Ensure your changes are limited to the scope of the PR.
3. Run a quick self-check:
   - Links resolve (HTTP 200)
   - No typos (use a spell checker if possible)
   - Python syntax is valid (`python -m py_compile safe_code_resources.py`)

## Adding a resource
- Edit `safe_code_resources.py` and append a dict to `SAFE_CODE_RESOURCES`:
  ```python
  {
      "name": "org/repo",
      "description": "What this resource provides and why it matters for secure code.",
      "language": "<language or N/A>",
      "stars": "~<approximate>",
      "link": "https://github.com/org/repo"
  }
  ```
- Keep descriptions concise (1–2 sentences), objective, and vendor-neutral where possible.
- Prefer canonical sources (official org repos) over third-party mirrors.

## Code style & docs
- This module is intentionally dependency-free and lightweight.
- Types are optional; keep function names stable: `list_resources`, `search_resources`, `get_resource`.
- Update `README_SAFE_CODE_RESOURCES.md` if behavior or schema changes.

## Pull requests
- Use clear, descriptive PR titles and bodies.
- Reference issues if applicable (e.g., `Fixes #123`).
- Keep diffs small and focused.
- Be responsive to review feedback; maintainers aim for fast, friendly reviews.

## Security
- Do not include secrets in commits.
- If a resource is discovered to be compromised or misleading, open an issue labeled `security` and propose removal/replacement.

## License
By contributing, you agree that your contributions will be licensed under the MIT License. See [LICENSE](LICENSE).