# Scripts Directory

Automation and validation scripts for the Sora 2 Prompts repository.

## Overview

This directory contains Python scripts that maintain repository quality and provide useful utilities for contributors.

## Scripts

### 🔍 `validate_prompts.py`

**Purpose**: Validates YAML prompt files against the JSON Schema

**Usage**:
```bash
# Validate all prompts
python scripts/validate_prompts.py prompts/

# Validate specific category
python scripts/validate_prompts.py prompts/cinematic/

# Validate single file
python scripts/validate_prompts.py prompts/cinematic/noir-detective.yaml
```

**Features**:
- Validates against `prompt.schema.json`
- Provides detailed error messages with constitution references
- Progress indicators for large directories
- CI/CD integration (exit code 1 on errors)

**Exit Codes**:
- `0` - All prompts valid
- `1` - Validation errors found

---

### 🔗 `check_links.py`

**Purpose**: Validates that demo video links are accessible

**Usage**:
```bash
# Check all prompt links
python scripts/check_links.py

# Check specific category
python scripts/check_links.py prompts/cinematic/

# Check single file
python scripts/check_links.py prompts/cinematic/noir-detective.yaml
```

**Features**:
- HTTP/HTTPS accessibility checks
- Platform detection (YouTube, Vimeo, etc.)
- Timeout handling (10 seconds default)
- Broken link reporting

**Exit Codes**:
- `0` - All links accessible
- `1` - Broken links found

---

### 🔨 `build_index.py`

**Purpose**: Automatically generates category README files from prompt YAMLs

**Usage**:
```bash
python scripts/build_index.py
```

**Features**:
- Scans all prompt YAML files
- Generates/updates category READMEs
- Sorts prompts by creation date (newest first)
- Includes performance badges (🔥 ⭐)
- Consistent formatting across categories

**Output**: Updates `prompts/*/README.md` files

---

### 🏆 `identify_top_performers.py`

**Purpose**: Analyzes performance data to identify top-performing prompts

**Usage**:
```bash
python scripts/identify_top_performers.py
```

**Features**:
- Weighted performance scoring
- Category breakdown analysis
- README-ready formatted output
- Saves results to `featured_prompts.md`

**Scoring Formula**:
```
weighted_score = retention_3s × 0.4 + retention_5s × 0.3 + completion_rate × 0.3
```

**Output**:
- Console report with rankings
- `featured_prompts.md` for README inclusion

---

### 🛠️ `utils.py`

**Purpose**: Shared utility functions to reduce code duplication

**Functions**:
- `load_yaml_file()` - Consistent YAML loading with error handling
- `find_project_root()` - Locate project root directory
- `get_relative_path()` - Clean relative paths for display

**Usage** (import in other scripts):
```python
from utils import load_yaml_file, find_project_root

data = load_yaml_file(Path("prompt.yaml"))
project_root = find_project_root()
```

---

## Installation

Install dependencies from the repository root:

```bash
pip install -r scripts/requirements.txt
```

**Requirements**:
- Python 3.11+
- jsonschema 4.19.2
- PyYAML 6.0.1
- requests 2.31.0

## Development

### Type Hints

All scripts use comprehensive type hints for better IDE support and static analysis:

```python
from typing import Dict, List, Optional, Any

def process_prompt(data: Dict[str, Any]) -> Optional[str]:
    """Process prompt data and return result."""
    pass
```

### Error Handling

Scripts follow consistent error handling patterns:

1. **File Operations**: Use try/except with specific error messages
2. **Network Operations**: Handle timeouts and connection errors
3. **User Feedback**: Clear progress indicators and error messages
4. **Exit Codes**: 0 for success, 1 for errors (CI-friendly)

### Testing Locally

Before submitting a PR, run all validation scripts:

```bash
# Validate prompts
python scripts/validate_prompts.py prompts/

# Check links (optional - can be slow)
python scripts/check_links.py prompts/

# Build indexes
python scripts/build_index.py

# Check for top performers
python scripts/identify_top_performers.py
```

## CI/CD Integration

These scripts are used in GitHub Actions workflows:

- **`.github/workflows/validate.yml`** - Runs `validate_prompts.py` on PRs
- **`.github/workflows/check-links.yml`** - Runs `check_links.py` weekly

See workflow files for specific configurations.

## Adding New Scripts

When adding a new script to this directory:

1. ✅ Add comprehensive docstrings (module, functions, classes)
2. ✅ Use type hints for all function signatures
3. ✅ Import shared utilities from `utils.py` when applicable
4. ✅ Follow consistent error handling patterns
5. ✅ Add progress indicators for long-running operations
6. ✅ Update this README with script documentation
7. ✅ Add any new dependencies to `requirements.txt`

## Support

For issues or questions about scripts:

1. Check script docstrings (`python script.py --help` or read source)
2. Review error messages (they include specific guidance)
3. Open an issue on GitHub with the `scripts` label

---

**Maintained by**: AI Video Factory Community
**Last Updated**: 2025-01-XX
