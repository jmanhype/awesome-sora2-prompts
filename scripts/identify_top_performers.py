#!/usr/bin/env python3
"""
Identify Top Performers Script - Performance-Based Prompt Discovery

Analyzes prompts with performance data to identify top performers for featured placement.
Uses weighted scoring algorithm emphasizing early retention metrics.

Usage:
    python scripts/identify_top_performers.py

Output:
    - Ranked list of top performing prompts
    - Weighted performance scores
    - Category breakdown
    - Formatted output for README inclusion

Scoring Formula:
    weighted_score = retention_3s * 0.4 + retention_5s * 0.3 + completion_rate * 0.3

    Emphasizes 3-second retention (40% weight) as primary indicator of hook quality.
"""

import yaml
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class PromptPerformance:
    """Performance metrics for a single prompt."""
    file_path: Path
    title: str
    category: str
    retention_3s: Optional[float]
    retention_5s: Optional[float]
    completion_rate: Optional[float]
    replays: Optional[int]
    weighted_score: float
    created: str

    def __post_init__(self):
        """Calculate weighted score after initialization."""
        if self.retention_3s is not None and self.retention_5s is not None and self.completion_rate is not None:
            self.weighted_score = (
                self.retention_3s * 0.4 +
                self.retention_5s * 0.3 +
                self.completion_rate * 0.3
            )
        else:
            self.weighted_score = 0.0


def load_prompt(file_path: Path) -> Optional[Dict]:
    """Load and parse a YAML prompt file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"⚠️  Error loading {file_path}: {e}", file=sys.stderr)
        return None


def extract_performance(prompt_data: Dict, file_path: Path) -> Optional[PromptPerformance]:
    """Extract performance data from prompt and create PromptPerformance object."""
    if not prompt_data:
        return None

    # Check if performance data exists
    performance = prompt_data.get('performance', {})
    if not performance:
        return None

    # Extract performance metrics
    retention_3s = performance.get('retention_3s')
    retention_5s = performance.get('retention_5s')
    completion_rate = performance.get('completion_rate')
    replays = performance.get('replays')

    # Require at least retention_3s for meaningful scoring
    if retention_3s is None:
        return None

    return PromptPerformance(
        file_path=file_path,
        title=prompt_data.get('title', 'Untitled'),
        category=prompt_data.get('category', 'unknown'),
        retention_3s=retention_3s,
        retention_5s=retention_5s,
        completion_rate=completion_rate,
        replays=replays,
        weighted_score=0.0,  # Will be calculated in __post_init__
        created=prompt_data.get('created', '')
    )


def find_all_prompts(prompts_dir: Path) -> List[Path]:
    """Recursively find all YAML prompt files."""
    return list(prompts_dir.glob("**/*.yaml"))


def analyze_performance(prompts_dir: Path) -> List[PromptPerformance]:
    """Analyze all prompts with performance data."""
    prompt_files = find_all_prompts(prompts_dir)
    performances = []

    print(f"📊 Analyzing {len(prompt_files)} prompt files...\n")

    for prompt_file in prompt_files:
        # Skip README files
        if prompt_file.name == "README.md":
            continue

        prompt_data = load_prompt(prompt_file)
        if not prompt_data:
            continue

        perf = extract_performance(prompt_data, prompt_file)
        if perf:
            performances.append(perf)

    return performances


def calculate_top_performers(performances: List[PromptPerformance], top_percent: float = 0.10) -> List[PromptPerformance]:
    """Calculate top N% of performers based on weighted score."""
    if not performances:
        return []

    # Sort by weighted score (descending)
    sorted_performances = sorted(performances, key=lambda p: p.weighted_score, reverse=True)

    # Calculate number of top performers (minimum 1, maximum all)
    num_top = max(1, int(len(sorted_performances) * top_percent))

    return sorted_performances[:num_top]


def format_performance_report(performances: List[PromptPerformance]) -> str:
    """Format performance data as readable report."""
    if not performances:
        return "No prompts with performance data found."

    lines = []
    lines.append("=" * 80)
    lines.append("TOP PERFORMING PROMPTS")
    lines.append("=" * 80)
    lines.append("")

    for i, perf in enumerate(performances, 1):
        lines.append(f"#{i} - {perf.title}")
        lines.append(f"    Category: {perf.category}")
        lines.append(f"    File: {perf.file_path.relative_to(perf.file_path.parents[2])}")
        lines.append(f"    Weighted Score: {perf.weighted_score:.2f}")
        lines.append(f"    Metrics:")
        if perf.retention_3s is not None:
            lines.append(f"      - 3s Retention: {perf.retention_3s:.1f}%")
        if perf.retention_5s is not None:
            lines.append(f"      - 5s Retention: {perf.retention_5s:.1f}%")
        if perf.completion_rate is not None:
            lines.append(f"      - Completion Rate: {perf.completion_rate:.1f}%")
        if perf.replays is not None:
            lines.append(f"      - Replays: {perf.replays}")
        lines.append("")

    return "\n".join(lines)


def format_for_readme(performances: List[PromptPerformance]) -> str:
    """Format top performers for README inclusion."""
    if not performances:
        return "No featured prompts available yet."

    lines = []
    lines.append("## 🏆 Featured Prompts")
    lines.append("")
    lines.append("Top-performing prompts based on retention and engagement metrics.")
    lines.append("")

    for perf in performances:
        # Determine performance badge
        badge = ""
        if perf.retention_3s and perf.retention_3s >= 80:
            badge = "🔥 "
        elif perf.completion_rate and perf.completion_rate >= 60:
            badge = "⭐ "

        # Get relative file path
        relative_path = perf.file_path.relative_to(perf.file_path.parents[2])

        lines.append(f"- {badge}**[{perf.title}]({relative_path})** ({perf.category})")
        lines.append(f"  - 3s retention: {perf.retention_3s:.1f}% | Weighted score: {perf.weighted_score:.2f}")

    lines.append("")
    lines.append("*Scores based on: retention_3s × 0.4 + retention_5s × 0.3 + completion_rate × 0.3*")
    lines.append("")

    return "\n".join(lines)


def generate_category_breakdown(performances: List[PromptPerformance]) -> str:
    """Generate performance breakdown by category."""
    if not performances:
        return "No data available."

    # Group by category
    by_category = {}
    for perf in performances:
        if perf.category not in by_category:
            by_category[perf.category] = []
        by_category[perf.category].append(perf)

    lines = []
    lines.append("PERFORMANCE BY CATEGORY")
    lines.append("-" * 80)
    lines.append("")

    for category, perfs in sorted(by_category.items()):
        avg_score = sum(p.weighted_score for p in perfs) / len(perfs)
        lines.append(f"{category.upper()}: {len(perfs)} prompts | Avg Score: {avg_score:.2f}")

        # Top 3 in category
        top_3 = sorted(perfs, key=lambda p: p.weighted_score, reverse=True)[:3]
        for i, perf in enumerate(top_3, 1):
            lines.append(f"  {i}. {perf.title} (Score: {perf.weighted_score:.2f})")
        lines.append("")

    return "\n".join(lines)


def main():
    """Main execution function."""
    print("🔍 Identifying Top Performing Prompts...\n")

    # Get project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    prompts_dir = project_root / "prompts"

    if not prompts_dir.exists():
        print(f"❌ Prompts directory not found: {prompts_dir}", file=sys.stderr)
        sys.exit(1)

    # Analyze all prompts
    performances = analyze_performance(prompts_dir)

    if not performances:
        print("⚠️  No prompts with performance data found.")
        print("\nTo add performance data, include a 'performance' section in your YAML:")
        print("performance:")
        print("  retention_3s: 85.5")
        print("  retention_5s: 72.3")
        print("  completion_rate: 68.9")
        print("  replays: 12")
        return

    print(f"✅ Found {len(performances)} prompts with performance data\n")

    # Calculate top 10%
    top_performers = calculate_top_performers(performances, top_percent=0.10)

    # Generate reports
    print(format_performance_report(top_performers))
    print("\n")
    print(generate_category_breakdown(performances))
    print("\n")
    print("=" * 80)
    print("README FORMAT OUTPUT")
    print("=" * 80)
    print(format_for_readme(top_performers))

    # Save README format to file for easy inclusion
    readme_output_path = project_root / "featured_prompts.md"
    try:
        with open(readme_output_path, 'w', encoding='utf-8') as f:
            f.write(format_for_readme(top_performers))
        print(f"\n💾 Saved README format to: {readme_output_path}")
    except Exception as e:
        print(f"\n⚠️  Could not save README format: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
