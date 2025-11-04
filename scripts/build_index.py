#!/usr/bin/env python3
"""
Build Index Script - Automated Category README Generation

Automatically generates category README files from YAML prompt files.
This ensures category READMEs stay in sync with prompt library.

Usage:
    python scripts/build_index.py

Features:
    - Scans all prompt YAML files in prompts/ directory
    - Generates/updates category README files
    - Maintains consistent formatting
    - Preserves category descriptions
    - Sorts prompts by creation date (newest first)
"""

import yaml
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime

# Category descriptions
CATEGORY_DESCRIPTIONS = {
    "cinematic": {
        "emoji": "🎬",
        "description": "Story-driven videos with traditional filmmaking techniques. Character-focused scenes with narrative elements and dramatic lighting."
    },
    "hyperrealism": {
        "emoji": "📸",
        "description": "Photorealistic simulations with material accuracy and physics. Natural lighting, real-world plausibility, physics-based rendering."
    },
    "animation": {
        "emoji": "🎨",
        "description": "Stylized, non-realistic aesthetics using creative animation techniques. Artistic stylization, handcrafted quality, emphasis on design."
    },
    "experimental": {
        "emoji": "🔬",
        "description": "Boundary-pushing, avant-garde work exploring Sora 2's capabilities. Innovative concepts, surreal visuals, unconventional approaches."
    }
}


def load_prompt(file_path: Path) -> Optional[Dict[str, Any]]:
    """Load and parse a YAML prompt file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error loading {file_path}: {e}", file=sys.stderr)
        return None


def format_camera_details(camera: Dict[str, Any]) -> str:
    """Format camera section as readable string."""
    parts = []
    if 'lens' in camera:
        parts.append(f"{camera['lens']} lens")
    if 'movement' in camera:
        parts.append(camera['movement'])
    if 'framing' in camera:
        parts.append(camera['framing'])
    return " | ".join(parts)


def format_tags(tags: List[str]) -> str:
    """Format tags as inline code elements."""
    return " ".join([f"`{tag}`" for tag in tags])


def get_performance_badge(prompt_data: Dict[str, Any]) -> str:
    """Determine performance badge based on metrics."""
    performance = prompt_data.get('performance', {})

    # 🔥 for retention_3s > 80 (high hook quality)
    if performance.get('retention_3s', 0) > 80:
        return "🔥 "

    # ⭐ for completion_rate > 60 (strong overall engagement)
    if performance.get('completion_rate', 0) > 60:
        return "⭐ "

    return ""


def generate_prompt_entry(prompt_data: Dict[str, Any], file_name: str) -> str:
    """Generate markdown entry for a single prompt."""
    entry_parts = []

    # Title with performance badge
    badge = get_performance_badge(prompt_data)
    entry_parts.append(f"### {badge}{prompt_data['title']}\n")

    # Summary
    if 'summary' in prompt_data:
        summary = prompt_data['summary'].strip()
        entry_parts.append(f"**Summary**: {summary}\n")

    # Tags
    if 'tags' in prompt_data:
        tags_str = format_tags(prompt_data['tags'])
        entry_parts.append(f"**Tags**: {tags_str}\n")

    # Camera
    if 'camera' in prompt_data:
        camera_str = format_camera_details(prompt_data['camera'])
        entry_parts.append(f"**Camera**: {camera_str}\n")

    # Performance metrics (if available)
    performance = prompt_data.get('performance', {})
    if performance:
        perf_parts = []
        if 'retention_3s' in performance:
            perf_parts.append(f"3s: {performance['retention_3s']:.1f}%")
        if 'retention_5s' in performance:
            perf_parts.append(f"5s: {performance['retention_5s']:.1f}%")
        if 'completion_rate' in performance:
            perf_parts.append(f"completion: {performance['completion_rate']:.1f}%")
        if perf_parts:
            entry_parts.append(f"**Performance**: {' | '.join(perf_parts)}\n")

    # Demo link
    if 'demo_link' in prompt_data:
        entry_parts.append(f"**Demo**: [Watch on YouTube]({prompt_data['demo_link']})\n")

    # File link
    entry_parts.append(f"**File**: [`{file_name}`]({file_name})\n")

    # Separator
    entry_parts.append("---\n")

    return "\n".join(entry_parts)


def generate_category_readme(category: str, prompts: List[Tuple[Dict[str, Any], str]]) -> Optional[str]:
    """Generate complete README content for a category."""
    if category not in CATEGORY_DESCRIPTIONS:
        print(f"⚠️  Unknown category: {category}", file=sys.stderr)
        return None

    cat_info = CATEGORY_DESCRIPTIONS[category]
    lines = []

    # Header
    lines.append(f"# {cat_info['emoji']} {category.title()} Prompts\n")
    lines.append(f"{cat_info['description']}\n")
    lines.append(f"**Total Prompts**: {len(prompts)}\n")
    lines.append("---\n")

    # Sort prompts by creation date (newest first)
    sorted_prompts = sorted(prompts, key=lambda x: x[0].get('created', ''), reverse=True)

    # Generate entries
    for prompt_data, file_name in sorted_prompts:
        entry = generate_prompt_entry(prompt_data, file_name)
        lines.append(entry)

    # Back link
    lines.append("\n---\n")
    lines.append("← [Back to Main README](../../README.md)\n")

    return "\n".join(lines)


def main() -> None:
    """Main execution function."""
    print("🔨 Building category indexes...\n")

    # Get project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    prompts_dir = project_root / "prompts"

    if not prompts_dir.exists():
        print(f"❌ Prompts directory not found: {prompts_dir}", file=sys.stderr)
        sys.exit(1)

    # Collect prompts by category
    prompts_by_category = {}

    for category_dir in prompts_dir.iterdir():
        if not category_dir.is_dir():
            continue

        category = category_dir.name
        prompts_by_category[category] = []

        # Find all YAML files
        for yaml_file in category_dir.glob("*.yaml"):
            if yaml_file.name == "README.md":
                continue

            prompt_data = load_prompt(yaml_file)
            if prompt_data:
                prompts_by_category[category].append((prompt_data, yaml_file.name))

    # Generate README for each category
    updated_count = 0
    for category, prompts in prompts_by_category.items():
        if not prompts:
            print(f"⚠️  No prompts found for category: {category}")
            continue

        readme_content = generate_category_readme(category, prompts)
        if not readme_content:
            continue

        readme_path = prompts_dir / category / "README.md"

        # Write README
        try:
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(readme_content)
            print(f"✅ Updated {category}/README.md ({len(prompts)} prompts)")
            updated_count += 1
        except Exception as e:
            print(f"❌ Error writing {readme_path}: {e}", file=sys.stderr)

    print(f"\n✨ Successfully updated {updated_count} category READMEs")


if __name__ == "__main__":
    main()
