"""
safe_code_resources.py
A lightweight, dependency-free Python module that centralizes the Top 20 GitHub repositories and resources for safe code practices.

This file was generated to implement the requested Safe Code Resources Module (DepredadorCloud Ultra).
"""

from typing import List, Dict, Optional

__version__ = "0.1.0"
__author__ = "Depredador-cloud"

# Curated list of ~20 safe-code resources. "stars" are approximate snapshots (strings).
_RESOURCES: List[Dict[str, str]] = [
    {
        "name": "OWASP Cheat Sheet Series",
        "description": "Comprehensive practical guides for mitigating common web application vulnerabilities.",
        "language": "All",
        "stars": "N/A",
        "link": "https://cheatsheetseries.owasp.org/"
    },
    {
        "name": "OWASP Top Ten",
        "description": "The canonical top 10 most critical web application security risks and guidance for mitigation.",
        "language": "All",
        "stars": "N/A",
        "link": "https://owasp.org/www-project-top-ten/"
    },
    {
        "name": "GitHub Code Scanning (CodeQL)",
        "description": "GitHub's code scanning powered by CodeQL for finding vulnerabilities via query-based analysis.",
        "language": "Multi",
        "stars": "N/A",
        "link": "https://securitylab.github.com/tools/codeql"
    },
    {
        "name": "Dependabot",
        "description": "Automated dependency updates to help keep projects up-to-date and reduce supply-chain risk.",
        "language": "Multi",
        "stars": "N/A",
        "link": "https://github.com/dependabot/dependabot-core"
    },
    {
        "name": "GitHub Secret Scanning",
        "description": "Detects and prevents secrets from being pushed to GitHub repositories; integrates with providers.",
        "language": "Multi",
        "stars": "N/A",
        "link": "https://docs.github.com/en/code-security/secret-scanning"
    },
    {
        "name": "Semgrep",
        "description": "Fast, open-source static analysis for many languages with an extensible ruleset and registry.",
        "language": "Multi",
        "stars": "~24k",
        "link": "https://github.com/returntocorp/semgrep"
    },
    {
        "name": "CodeQL CLI and Queries",
        "description": "Library of query packs and community queries for CodeQL to detect a wide range of vulnerabilities.",
        "language": "Multi",
        "stars": "N/A",
        "link": "https://github.com/github/codeql"
    },
    {
        "name": "SonarQube",
        "description": "Static analysis platform with quality and security rules across many languages (SonarSource).",
        "language": "Multi",
        "stars": "N/A",
        "link": "https://www.sonarqube.org/"
    },
    {
        "name": "OpenSSF Scorecard",
        "description": "Automated checks that score project security hygiene and provide actionable recommendations.",
        "language": "Multi",
        "stars": "~2.5k",
        "link": "https://github.com/ossf/scorecard"
    },
    {
        "name": "OpenSSF Best Practices",
        "description": "Best practices and a badge program to indicate security-conscious project practices.",
        "language": "Multi",
        "stars": "N/A",
        "link": "https://bestpractices.coreinfrastructure.org/"
    },
    {
        "name": "Bandit (Python)",
        "description": "Security-oriented static analyzer for Python code that finds common vulnerabilities.",
        "language": "Python",
        "stars": "~9k",
        "link": "https://github.com/PyCQA/bandit"
    },
    {
        "name": "gosec",
        "description": "Go security analyzer that scans for common programming mistakes and vulnerabilities.",
        "language": "Go",
        "stars": "~9k",
        "link": "https://github.com/securego/gosec"
    },
    {
        "name": "RustSec Advisory DB",
        "description": "A central database of security advisories for Rust crates and ecosystem tooling (cargo-audit).",
        "language": "Rust",
        "stars": "~3k",
        "link": "https://github.com/RustSec/advisory-db"
    },
    {
        "name": "cargo-audit",
        "description": "Tool that scans Rust projects for vulnerable dependencies using the RustSec advisory database.",
        "language": "Rust",
        "stars": "~4k",
        "link": "https://github.com/RustSec/cargo-audit"
    },
    {
        "name": "TensorFlow Security",
        "description": "Guidance and resources related to security considerations when using TensorFlow and ML models.",
        "language": "TensorFlow",
        "stars": "N/A",
        "link": "https://www.tensorflow.org/security"
    },
    {
        "name": "Snyk",
        "description": "Developer-first security tooling for dependency, container, and IaC scanning with remediation advice.",
        "language": "Multi",
        "stars": "~11k",
        "link": "https://snyk.io/"
    },
    {
        "name": "Trivy (Aqua Security)",
        "description": "A simple and comprehensive vulnerability scanner for containers, filesystems and Git repositories.",
        "language": "Multi",
        "stars": "~21k",
        "link": "https://github.com/aquasecurity/trivy"
    },
    {
        "name": "Dependabot Core (core engine)",
        "description": "The core library that powers Dependabot plumbing for updating dependencies across ecosystems.",
        "language": "Multi",
        "stars": "~3k",
        "link": "https://github.com/dependabot/dependabot-core"
    },
    {
        "name": "Zig (language & security guidance)",
        "description": "Zig language repo and community resources; review project policies and security considerations.",
        "language": "Zig",
        "stars": "~16k",
        "link": "https://github.com/ziglang/zig"
    },
    {
        "name": "Awesome Security (curated lists)",
        "description": "A curated list of security-related tools, papers, and resources useful for teams and researchers.",
        "language": "Multi",
        "stars": "~12k",
        "link": "https://github.com/sbilly/awesome-security"
    }
]


def list_resources() -> List[Dict[str, str]]:
    """Return the full list of curated resource dictionaries.

    This returns the live list object for simple read-only consumption. Callers may copy it if they
    intend to mutate it.
    """
    return _RESOURCES


def search_resources(keyword: str) -> List[Dict[str, str]]:
    """Case-insensitive search against `name` and `description` fields.

    Args:
        keyword: search term (will be lower-cased). Empty or whitespace-only keywords return an empty list.

    Returns:
        List of matching resource dictionaries (may be empty).
    """
    if not keyword or not keyword.strip():
        return []
    k = keyword.lower()
    results: List[Dict[str, str]] = []
    for r in _RESOURCES:
        if k in r.get("name", "").lower() or k in r.get("description", "").lower():
            results.append(r)
    return results


def get_resource(index: int) -> Optional[Dict[str, str]]:
    """Return resource at zero-based index or None if out of range.

    Args:
        index: zero-based index into the resources list.
    """
    try:
        return _RESOURCES[index]
    except Exception:
        return None


def _format_resource(r: Dict[str, str]) -> str:
    return (
        f"{r.get('name')}\n"
        f"  Description: {r.get('description')}\n"
        f"  Language: {r.get('language')}\n"
        f"  Stars: {r.get('stars')}\n"
        f"  Link: {r.get('link')}\n"
    )


if __name__ == "__main__":
    # Simple CLI-style printout
    import argparse

    parser = argparse.ArgumentParser(description="Print curated safe code resources.")
    parser.add_argument("--search", "-s", help="Search keyword to filter results.", default="")
    args = parser.parse_args()

    if args.search:
        hits = search_resources(args.search)
        if not hits:
            print(f"No resources matched: {args.search}")
        else:
            print(f"Found {len(hits)} resource(s) matching '{args.search}':\n")
            for h in hits:
                print(_format_resource(h))
    else:
        print(f"Safe Code Resources (Total: {len(_RESOURCES)})\n")
        for i, res in enumerate(_RESOURCES):
            print(f"[{i}] {res.get('name')} ({res.get('language')}) - {res.get('link')}")

# End of safe_code_resources.py
