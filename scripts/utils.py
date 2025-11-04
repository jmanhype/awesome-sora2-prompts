#!/usr/bin/env python3
"""
Shared Utility Functions for Sora 2 Prompt Scripts

Common functionality used across multiple scripts to reduce code duplication
and ensure consistency.
"""

import sys
import yaml
from pathlib import Path
from typing import Optional, Dict, Any


def load_yaml_file(file_path: Path) -> Optional[Dict[str, Any]]:
    """
    Load and parse a YAML file with consistent error handling.

    Args:
        file_path: Path to YAML file to load

    Returns:
        Parsed YAML content as dictionary, or None if loading fails

    Examples:
        >>> data = load_yaml_file(Path("prompts/cinematic/example.yaml"))
        >>> if data:
        ...     print(data['title'])
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}", file=sys.stderr)
        return None
    except yaml.YAMLError as e:
        print(f"❌ YAML parsing error in {file_path}: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"❌ Unexpected error loading {file_path}: {e}", file=sys.stderr)
        return None


def find_project_root(start_path: Optional[Path] = None) -> Path:
    """
    Find the project root directory by looking for marker files.

    Args:
        start_path: Starting path for search (defaults to current file's parent)

    Returns:
        Path to project root directory

    Raises:
        RuntimeError: If project root cannot be found
    """
    if start_path is None:
        start_path = Path(__file__).parent

    current = start_path.resolve()

    # Look for project markers (prompt.schema.json AND prompts/ directory together)
    # This ensures we find the actual project root, not a subdirectory
    required_markers = ['prompt.schema.json', 'prompts']

    # Search up to 5 levels
    for _ in range(5):
        # Check if ALL required markers exist at this level
        if all((current / marker).exists() for marker in required_markers):
            return current

        if current.parent == current:
            # Reached filesystem root
            break

        current = current.parent

    raise RuntimeError("Could not find project root directory. Expected to find both prompt.schema.json and prompts/ directory.")


def get_relative_path(file_path: Path, levels_up: int = 2) -> Path:
    """
    Get a clean relative path for display purposes.

    Args:
        file_path: Path to make relative
        levels_up: Number of parent levels to use as base (default 2)

    Returns:
        Relative path for display

    Examples:
        >>> path = Path("/project/prompts/cinematic/example.yaml")
        >>> get_relative_path(path)
        PosixPath('prompts/cinematic/example.yaml')
    """
    try:
        return file_path.relative_to(file_path.parents[levels_up])
    except (ValueError, IndexError):
        # If relative path fails, return the name
        return Path(file_path.name)
