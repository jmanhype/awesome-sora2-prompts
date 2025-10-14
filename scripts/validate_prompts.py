#!/usr/bin/env python3
"""
Sora 2 Prompt Validation Script

Validates YAML prompt files against prompt.schema.json per the
AI Video Factory Constitution and prompt-schema-requirements.md contract.

Usage:
    python validate_prompts.py <directory_or_file>

Exit Codes:
    0 - All prompts valid
    1 - Validation errors found

Contract: contracts/prompt-schema-requirements.md v1.0.0
"""

import sys
import json
import yaml
from pathlib import Path
from typing import List, Dict, Tuple
import jsonschema
from jsonschema import Draft7Validator, ValidationError


class PromptValidator:
    """Validates Sora 2 prompt YAML files against JSON Schema."""

    def __init__(self, schema_path: Path):
        """Initialize validator with schema file."""
        with open(schema_path, 'r', encoding='utf-8') as f:
            self.schema = json.load(f)

        # Use Draft 7 validator for schema compliance
        self.validator = Draft7Validator(self.schema)

    def validate_file(self, file_path: Path) -> Tuple[bool, List[str]]:
        """
        Validate a single YAML file.

        Returns:
            (is_valid, error_messages)
        """
        errors = []

        try:
            # Load YAML file
            with open(file_path, 'r', encoding='utf-8') as f:
                prompt_data = yaml.safe_load(f)

            # Validate against schema
            validation_errors = list(self.validator.iter_errors(prompt_data))

            if validation_errors:
                for error in validation_errors:
                    error_msg = self._format_error(file_path, error, prompt_data)
                    errors.append(error_msg)
                return False, errors

            return True, []

        except yaml.YAMLError as e:
            errors.append(f"[ERROR] {file_path}\nYAML parsing error: {e}")
            return False, errors

        except FileNotFoundError:
            errors.append(f"[ERROR] File not found: {file_path}")
            return False, errors

        except Exception as e:
            errors.append(f"[ERROR] {file_path}\nUnexpected error: {e}")
            return False, errors

    def _format_error(self, file_path: Path, error: ValidationError, prompt_data: dict) -> str:
        """
        Format validation error with custom error messages from schema.

        Per contract: Use custom error_msg from schema if present,
        include constitution references.
        """
        # Build field path (e.g., "camera.lens" for nested fields)
        field_path = ".".join(str(p) for p in error.path) if error.path else "root"

        # Try to get custom error message from schema
        error_msg = error.message
        if error.schema and "error_msg" in error.schema:
            error_msg = error.schema["error_msg"]

        # Get constitution reference if present
        constitution_ref = ""
        if error.schema and "constitution_ref" in error.schema:
            constitution_ref = f"\nConstitution Reference: {error.schema['constitution_ref']}"

        # Format error per contract specification
        formatted = f"""[ERROR] {file_path}
Field: {field_path}
Issue: {error_msg}{constitution_ref}"""

        return formatted

    def validate_directory(self, directory: Path) -> Tuple[int, int, List[str]]:
        """
        Recursively validate all YAML files in directory.

        Returns:
            (valid_count, total_count, all_errors)
        """
        yaml_files = list(directory.rglob("*.yaml")) + list(directory.rglob("*.yml"))

        if not yaml_files:
            print(f"⚠️  No YAML files found in {directory}")
            return 0, 0, []

        valid_count = 0
        all_errors = []

        print(f"✓ Validating prompts in: {directory}\n")

        for file_path in sorted(yaml_files):
            is_valid, errors = self.validate_file(file_path)

            if is_valid:
                print(f"✓ {file_path.relative_to(directory.parent)} - VALID")
                valid_count += 1
            else:
                print(f"✗ {file_path.relative_to(directory.parent)} - INVALID")
                all_errors.extend(errors)

        return valid_count, len(yaml_files), all_errors


def main():
    """Main entry point for validation script."""
    if len(sys.argv) < 2:
        print("Usage: python validate_prompts.py <directory_or_file>")
        print("\nExamples:")
        print("  python validate_prompts.py prompts/")
        print("  python validate_prompts.py prompts/cinematic/noir-detective.yaml")
        sys.exit(1)

    target_path = Path(sys.argv[1])

    if not target_path.exists():
        print(f"❌ Error: Path does not exist: {target_path}")
        sys.exit(1)

    # Find schema file (look in current directory and parent)
    schema_path = Path("prompt.schema.json")
    if not schema_path.exists():
        schema_path = Path("../prompt.schema.json")

    if not schema_path.exists():
        print("❌ Error: prompt.schema.json not found")
        print("   Ensure schema file is in current directory or parent directory")
        sys.exit(1)

    try:
        validator = PromptValidator(schema_path)

        if target_path.is_file():
            # Validate single file
            is_valid, errors = validator.validate_file(target_path)

            if is_valid:
                print(f"✓ {target_path} - VALID")
                sys.exit(0)
            else:
                print(f"✗ {target_path} - INVALID\n")
                for error in errors:
                    print(error)
                    print()
                sys.exit(1)

        elif target_path.is_dir():
            # Validate directory
            valid_count, total_count, all_errors = validator.validate_directory(target_path)

            print()  # Blank line before summary

            if all_errors:
                # Print all errors
                for error in all_errors:
                    print(error)
                    print()  # Blank line between errors

                print(f"Summary: {valid_count}/{total_count} prompts valid ({len(all_errors)} errors)")
                sys.exit(1)
            else:
                print(f"Summary: {valid_count}/{total_count} prompts valid")
                sys.exit(0)

        else:
            print(f"❌ Error: {target_path} is neither a file nor directory")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
