# {EMOJI} {Category Name} Prompts

{Category description - what makes this category unique, visual style, use cases}

**Total Prompts**: {X}

---

### {BADGE} Prompt Title

**Summary**: {One-sentence description of what the video shows}

**Tags**: `tag1` `tag2` `tag3` `tag4`

**Camera**: {lens type} | {camera movement} | {framing}

**Performance**: 3s: {X.X}% | 5s: {X.X}% | completion: {X.X}%

**Demo**: [Watch on YouTube]({demo_url})

**File**: [`prompt-filename.yaml`](prompt-filename.yaml)

---

### {BADGE} Another Prompt Title

**Summary**: {Another one-sentence description}

**Tags**: `tag1` `tag2` `tag3`

**Camera**: {lens} | {movement} | {framing}

**Performance**: 3s: {X.X}% | 5s: {X.X}% | completion: {X.X}%

**Demo**: [Watch on Vimeo]({demo_url})

**File**: [`another-prompt.yaml`](another-prompt.yaml)

---

<!-- TEMPLATE INSTRUCTIONS FOR MAINTAINERS -->

<!--
This template is used by scripts/build_index.py to generate category README files.

AUTOMATIC GENERATION:
- Run: python scripts/build_index.py
- This automatically scans all YAML files in the category
- Generates formatted entries for each prompt
- Updates category README with latest prompts
- Sorts by creation date (newest first)

MANUAL UPDATES:
If adding prompts manually, follow this structure:

1. TITLE SECTION:
   ### {BADGE} {Prompt Title}
   - Badge options:
     - 🔥 for retention_3s > 80% (high hook quality)
     - ⭐ for completion_rate > 60% (strong engagement)
     - (none) for standard prompts

2. SUMMARY:
   **Summary**: One clear sentence describing the video content

3. TAGS:
   **Tags**: `tag1` `tag2` `tag3` (use backticks for inline code style)

4. CAMERA:
   **Camera**: {lens type} | {camera movement} | {framing}
   Example: 35mm lens | tracking shot | medium close-up

5. PERFORMANCE (if available):
   **Performance**: 3s: 85.5% | 5s: 72.3% | completion: 68.9%

6. DEMO LINK:
   **Demo**: [Watch on {Platform}]({url})

7. FILE LINK:
   **File**: [`filename.yaml`](filename.yaml)

8. SEPARATOR:
   ---

CATEGORY DESCRIPTIONS:

Cinematic (🎬):
"Story-driven videos with traditional filmmaking techniques. Character-focused scenes with narrative elements and dramatic lighting."

Hyperrealism (📸):
"Photorealistic simulations with material accuracy and physics. Natural lighting, real-world plausibility, physics-based rendering."

Animation (🎨):
"Stylized, non-realistic aesthetics using creative animation techniques. Artistic stylization, handcrafted quality, emphasis on design."

Experimental (🔬):
"Boundary-pushing, avant-garde work exploring Sora 2's capabilities. Innovative concepts, surreal visuals, unconventional approaches."

AUTOMATION NOTES:
- build_index.py reads CATEGORY_DESCRIPTIONS from script
- Automatically formats camera section as readable string
- Adds performance badges based on metrics
- Sorts prompts by 'created' field (newest first)
- Maintains consistent formatting across all categories

FOOTER:
Always include:
---
← [Back to Main README](../../README.md)
-->

---

← [Back to Main README](../../README.md)
