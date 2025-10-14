#!/usr/bin/env python3
"""
Check Links Script - Validate Demo Video Links

Validates that all demo_link URLs in prompt files are accessible and working.
Helps maintain repository quality by identifying broken or inaccessible videos.

Usage:
    python scripts/check_links.py                    # Check all prompts
    python scripts/check_links.py prompts/category/  # Check specific category
    python scripts/check_links.py prompt.yaml        # Check single file

Features:
    - Validates HTTP/HTTPS accessibility
    - Checks for common video hosting platforms
    - Reports broken links with details
    - Exit code 1 if any links are broken (for CI)

Requirements:
    - requests library (included in requirements.txt)
"""

import yaml
import sys
import requests
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from urllib.parse import urlparse
from dataclasses import dataclass

# Timeout for HTTP requests (seconds)
REQUEST_TIMEOUT = 10

# Supported video hosting platforms
SUPPORTED_PLATFORMS = [
    'youtube.com',
    'youtu.be',
    'vimeo.com',
    'dailymotion.com',
    'streamable.com',
    'twitch.tv',
]


@dataclass
class LinkCheckResult:
    """Result of checking a single link."""
    file_path: Path
    prompt_title: str
    demo_link: str
    accessible: bool
    status_code: Optional[int]
    error_message: Optional[str]
    platform: Optional[str]


def load_prompt(file_path: Path) -> Optional[Dict]:
    """Load and parse a YAML prompt file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"⚠️  Error loading {file_path}: {e}", file=sys.stderr)
        return None


def extract_platform(url: str) -> Optional[str]:
    """Extract platform name from URL."""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()

        # Remove 'www.' prefix if present
        if domain.startswith('www.'):
            domain = domain[4:]

        # Check against supported platforms
        for platform in SUPPORTED_PLATFORMS:
            if platform in domain:
                return platform

        return domain  # Return full domain if not in supported list
    except Exception:
        return None


def check_link(url: str, timeout: int = REQUEST_TIMEOUT) -> Tuple[bool, Optional[int], Optional[str]]:
    """
    Check if a URL is accessible.

    Returns:
        Tuple of (accessible, status_code, error_message)
    """
    try:
        # Use HEAD request first (faster, less bandwidth)
        response = requests.head(url, timeout=timeout, allow_redirects=True)

        # If HEAD fails, try GET (some servers don't support HEAD)
        if response.status_code >= 400:
            response = requests.get(url, timeout=timeout, allow_redirects=True, stream=True)

        # Consider 2xx and 3xx as successful
        accessible = response.status_code < 400
        return accessible, response.status_code, None

    except requests.exceptions.Timeout:
        return False, None, f"Timeout after {timeout}s"
    except requests.exceptions.ConnectionError:
        return False, None, "Connection error - host unreachable"
    except requests.exceptions.TooManyRedirects:
        return False, None, "Too many redirects"
    except requests.exceptions.RequestException as e:
        return False, None, str(e)
    except Exception as e:
        return False, None, f"Unexpected error: {str(e)}"


def check_prompt_link(file_path: Path) -> Optional[LinkCheckResult]:
    """Check the demo link in a prompt file."""
    prompt_data = load_prompt(file_path)
    if not prompt_data:
        return None

    # Extract demo link
    demo_link = prompt_data.get('demo_link')
    if not demo_link:
        # No demo link to check (might be optional in some cases)
        return None

    # Check link accessibility
    accessible, status_code, error_message = check_link(demo_link)

    # Extract platform
    platform = extract_platform(demo_link)

    return LinkCheckResult(
        file_path=file_path,
        prompt_title=prompt_data.get('title', 'Untitled'),
        demo_link=demo_link,
        accessible=accessible,
        status_code=status_code,
        error_message=error_message,
        platform=platform
    )


def find_prompt_files(path: Path) -> List[Path]:
    """Find all YAML prompt files in the given path."""
    if path.is_file():
        return [path] if path.suffix == '.yaml' else []
    elif path.is_dir():
        return list(path.glob('**/*.yaml'))
    else:
        return []


def format_result(result: LinkCheckResult) -> str:
    """Format a link check result for display."""
    status_icon = "✅" if result.accessible else "❌"

    lines = [
        f"{status_icon} {result.prompt_title}",
        f"   File: {result.file_path.relative_to(result.file_path.parents[2])}",
        f"   Link: {result.demo_link}",
    ]

    if result.platform:
        lines.append(f"   Platform: {result.platform}")

    if result.accessible:
        lines.append(f"   Status: {result.status_code} (Accessible)")
    else:
        lines.append(f"   Status: BROKEN")
        if result.status_code:
            lines.append(f"   HTTP Code: {result.status_code}")
        if result.error_message:
            lines.append(f"   Error: {result.error_message}")

    return "\n".join(lines)


def generate_summary(results: List[LinkCheckResult]) -> str:
    """Generate summary report of link checks."""
    total = len(results)
    accessible = sum(1 for r in results if r.accessible)
    broken = total - accessible

    lines = [
        "=" * 80,
        "LINK CHECK SUMMARY",
        "=" * 80,
        f"Total Links Checked: {total}",
        f"✅ Accessible: {accessible}",
        f"❌ Broken: {broken}",
    ]

    if broken > 0:
        lines.append("")
        lines.append("BROKEN LINKS:")
        lines.append("-" * 80)
        for result in results:
            if not result.accessible:
                lines.append("")
                lines.append(format_result(result))

    # Platform breakdown
    if results:
        lines.append("")
        lines.append("PLATFORMS:")
        lines.append("-" * 80)
        platforms = {}
        for result in results:
            if result.platform:
                platforms[result.platform] = platforms.get(result.platform, 0) + 1

        for platform, count in sorted(platforms.items(), key=lambda x: x[1], reverse=True):
            lines.append(f"  {platform}: {count}")

    return "\n".join(lines)


def main():
    """Main execution function."""
    print("🔗 Checking demo video links...\n")

    # Determine path to check
    if len(sys.argv) > 1:
        check_path = Path(sys.argv[1])
    else:
        # Default to prompts directory
        script_dir = Path(__file__).parent
        check_path = script_dir.parent / "prompts"

    if not check_path.exists():
        print(f"❌ Path not found: {check_path}", file=sys.stderr)
        sys.exit(1)

    # Find all prompt files
    prompt_files = find_prompt_files(check_path)

    if not prompt_files:
        print(f"⚠️  No YAML files found in: {check_path}")
        sys.exit(0)

    print(f"Found {len(prompt_files)} prompt files\n")

    # Check each prompt's demo link
    results = []
    for i, prompt_file in enumerate(prompt_files, 1):
        # Show progress
        print(f"[{i}/{len(prompt_files)}] Checking {prompt_file.name}...", end=" ")
        sys.stdout.flush()

        result = check_prompt_link(prompt_file)
        if result:
            results.append(result)
            status = "✅" if result.accessible else "❌"
            print(status)
        else:
            print("⏭️  (no demo link)")

    # Generate and display summary
    print()
    print(generate_summary(results))

    # Exit with error code if any links are broken
    broken_count = sum(1 for r in results if not r.accessible)
    if broken_count > 0:
        print(f"\n❌ {broken_count} broken link(s) found", file=sys.stderr)
        sys.exit(1)
    else:
        print("\n✨ All demo links are accessible!")
        sys.exit(0)


if __name__ == "__main__":
    main()
