# Contributing to Awesome Sora 2 Prompts

Thank you for your interest in contributing! This repository follows the **AI Video Factory Constitution** to ensure high-quality, well-structured prompts that advance the community's understanding of Sora 2.

## Quick Start

1. **Fork the repository** and clone your fork
2. **Create a new prompt** using the template in `templates/PROMPT_TEMPLATE.yaml`
3. **Test locally** with `python scripts/validate_prompts.py prompts/your-file.yaml`
4. **Generate actual Sora 2 video** from your prompt
5. **Create pull request** with demo link

**📚 New to prompt writing?** Read [guides/five-pillars.md](guides/five-pillars.md) first!

## The Five-Pillar Framework

Every prompt must follow this structure (per Constitution Principle III):

1. **Subject/Character** - Who or what is the focus
2. **Action/Motion** - What movement occurs
3. **Environment/Setting** - Where and when it happens
4. **Cinematic Framing** - Camera work and composition
5. **Aesthetic/Style** - Visual treatment and mood

See existing prompts in `prompts/` for examples.

## Contribution Workflow

### 1. Choose a Category

Place your prompt in the appropriate directory:

- **`prompts/cinematic/`** - Narrative-driven, story-focused videos
- **`prompts/hyperrealism/`** - Photorealistic simulations
- **`prompts/animation/`** - Stylized, non-realistic aesthetics
- **`prompts/experimental/`** - Avant-garde, boundary-pushing work

### 2. Create Your YAML File

```bash
cp templates/PROMPT_TEMPLATE.yaml prompts/category/your-prompt-name.yaml
```

**Naming convention**: Use lowercase-with-hyphens (e.g., `noir-detective.yaml`)

### 3. Fill Out Required Fields

Your YAML file must include:

- ✅ `title` - Descriptive title (5-100 chars)
- ✅ `category` - One of: cinematic, hyperrealism, animation, experimental
- ✅ `tags` - 1-12 searchable tags (lowercase-with-hyphens)
- ✅ `summary` - Brief description (20-280 chars)
- ✅ `prompt` - Full prompt following Five-Pillar framework (≥50 chars)
- ✅ `camera` - Must include `lens`, `movement`, `framing`
- ✅ `author` - Your GitHub username
- ✅ `created` - Date in YYYY-MM-DD format
- ✅ `sora_version` - Must start with "2." (e.g., "2.0")
- ✅ `demo_link` - **Required for PR merge** (see below)

**Hyperrealism category** also requires `physics` field with `materials` and `forces`.

### 4. Validate Locally

```bash
# Install dependencies (first time only)
pip install -r scripts/requirements.txt

# Validate your prompt
python scripts/validate_prompts.py prompts/category/your-prompt-name.yaml
```

Fix any validation errors before submitting PR.

### 5. Generate Demo Video (Required)

**Per Constitution Principle VI: Test-First Contribution**

You must generate actual Sora 2 output from your prompt and provide a demo link. This ensures the prompt actually works.

**Demo hosting options:**
- YouTube Unlisted link
- Vimeo link
- Direct file URL (if hosting elsewhere)

Add the demo link to your YAML file:
```yaml
demo_link: "https://youtube.com/watch?v=your-video-id"
```

**Why required?** This validates:
- The prompt actually produces the intended result
- The schema correctly captures working patterns
- The community can see real outputs

### 6. Submit Pull Request

```bash
git checkout -b add-your-prompt-name
git add prompts/category/your-prompt-name.yaml
git commit -m "Add [category]: your prompt title"
git push origin add-your-prompt-name
```

Open a PR using the pull request template. Include:
- Category and prompt title
- Link to demo video
- Brief description of what makes this prompt interesting

## Validation Rules

### Automatic Validation

CI will check:
- ✅ YAML syntax is valid
- ✅ All required fields present
- ✅ Field values match constraints (length, format, enums)
- ✅ Camera object has `lens`, `movement`, `framing`
- ✅ Hyperrealism prompts include `physics`
- ✅ Tags use lowercase-with-hyphens format
- ✅ `demo_link` is valid HTTPS URL

### Human Review

Maintainers will verify:
- ✅ Demo video matches prompt description
- ✅ Five-Pillar framework properly applied
- ✅ Prompt is original or properly attributed
- ✅ No NSFW content (unless pre-approved)
- ✅ Quality meets community standards

## Writing Great Prompts

### Do's ✅

- **Be specific**: "trench-coated detective" > "person"
- **Specify camera work**: Include lens, movement, framing
- **Add physics hints** (hyperrealism): Materials and forces
- **Use vivid language**: "rain-slicked streets with neon reflections"
- **Structure clearly**: Follow Five-Pillar framework explicitly
- **Test thoroughly**: Generate video before submitting
- **Cite sources**: If derived from existing work, provide attribution

### Don'ts ❌

- **Vague descriptions**: "cool scene with stuff"
- **Missing camera specs**: Required per constitution
- **Untested prompts**: Must include working demo
- **Plagiarism**: Always attribute sources
- **NSFW without approval**: Requires maintainer pre-approval

## Examples by Category

### Cinematic
See: `prompts/cinematic/noir-detective.yaml`
- Story-driven scenes
- Character focus
- Dramatic camera work
- Mood and atmosphere

### Hyperrealism
See: `prompts/hyperrealism/morning-coffee.yaml`
- Photorealistic detail
- Physics accuracy
- Material properties
- Natural lighting

### Animation
See: `prompts/animation/paper-cutout-forest.yaml`
- Stylized aesthetics
- Non-realistic rendering
- Creative techniques
- Artistic interpretation

### Experimental
See: `prompts/experimental/data-dissolution.yaml`
- Boundary-pushing concepts
- Surreal visuals
- Technical innovation
- Artistic expression

## Optional Fields

Enhance your prompt with:

- `physics.materials` - Materials in scene (recommended for hyperrealism)
- `physics.forces` - Physical forces at play
- `audio_notes` - Audio cues for synchronized sound (10-500 chars)
- `expected_duration` - Typical output length (e.g., "6-8 seconds")
- `performance` - Metrics for data-driven iteration
- `source` - Attribution if not original

## NSFW Content

NSFW prompts require:
1. Explicit `nsfw: true` flag
2. Pre-approval from maintainers (open issue first)
3. Clear content warnings
4. Legitimate artistic/educational purpose

## Attribution & Ethics

Per Constitution principles:

- **Original work**: Set `source: "original"`
- **Derived work**: Provide source URL and describe inspiration
- **Respect copyright**: Don't replicate copyrighted content
- **Credit properly**: When building on others' work

## Edge Cases & Troubleshooting

### Common Validation Errors

**Error: "Missing required field: camera.lens"**
- **Cause**: Camera object incomplete
- **Fix**: Ensure camera section includes all three fields:
```yaml
camera:
  lens: "35mm"
  movement: "tracking shot"
  framing: "medium close-up"
```

**Error: "Invalid tag format"**
- **Cause**: Tags contain uppercase, underscores, or spaces
- **Fix**: Use lowercase-with-hyphens only:
  - ✅ `slow-motion`, `film-noir`, `4k`
  - ❌ `Slow Motion`, `film_noir`, `4K Quality`

**Error: "demo_link must be valid HTTPS URL"**
- **Cause**: HTTP instead of HTTPS, or malformed URL
- **Fix**: Use full HTTPS URL: `https://youtube.com/watch?v=...`

**Error: "Expected type string, got null"**
- **Cause**: Empty or missing value
- **Fix**: Provide value for all required fields, use quotes if needed:
```yaml
summary: "Detective walks through rain-slicked noir streets"
```

### Advanced Scenarios

#### Multi-Character Prompts

When including multiple characters, structure your subject section clearly:

```yaml
subject_character: |
  PRIMARY: Trench-coated detective, weathered face, fedora pulled low
  SECONDARY: Femme fatale in red dress, standing in doorway
  BACKGROUND: Street musicians, pedestrians with umbrellas
```

#### Complex Camera Movements

For multi-phase camera work, describe sequence in action section:

```yaml
action_motion: |
  PHASE 1 (0-3s): Slow push-in from wide establishing shot
  PHASE 2 (3-6s): Tracking alongside moving subject
  PHASE 3 (6-8s): Crane up revealing full environment
```

#### Physics-Heavy Simulations (Hyperrealism)

Specify materials and forces explicitly:

```yaml
physics:
  materials:
    - "ceramic mug with matte glaze"
    - "hot coffee with visible steam"
    - "wooden table with natural grain"
  forces:
    - "gravity on liquid pour"
    - "surface tension forming meniscus"
    - "heat convection creating steam patterns"
```

#### Iterative Prompt Development

When submitting improved versions:

1. Keep original filename, update version in metadata
2. Add iteration notes:
```yaml
iteration_notes: |
  V1.0 (2025-01-15): Initial version, retention_3s: 68%
  V1.1 (2025-01-20): Improved hook, retention_3s: 82%
  V1.2 (2025-01-25): Refined camera movement, retention_3s: 87%
```
3. Update performance metrics with each iteration
4. Document what changed and why

#### Style Mixing (Experimental)

For hybrid aesthetics, be explicit about style ratios:

```yaml
aesthetic_style: |
  PRIMARY (70%): Vaporwave aesthetic - pink/cyan color grading
  SECONDARY (30%): Glitch art - digital distortion effects
  TECHNIQUE: Smooth blend, not jarring cuts between styles
```

### File Organization Edge Cases

**Q: Can I submit multiple related prompts?**
A: Yes! Use descriptive filenames:
- `noir-detective-rain-v1.yaml`
- `noir-detective-rain-v2.yaml`
- `noir-detective-fog.yaml`

**Q: What if my prompt fits multiple categories?**
A: Choose the PRIMARY category based on dominant technique:
- If photorealistic with slight stylization → Hyperrealism
- If narrative-focused with stylized rendering → Cinematic
- If pushing technical boundaries → Experimental

**Q: Can I include platform-specific parameters?**
A: Yes, in optional `notes` section:
```yaml
notes: |
  Tested on Sora 2.1 with extended context window.
  Works best with "cinematic" preset enabled.
  Requires high-fidelity mode for material detail.
```

### Performance Tracking Edge Cases

**Partial Metrics:**
If you only have some performance data, include what you have:
```yaml
performance:
  retention_3s: 85.5  # Have this
  # retention_5s: Not tracked
  # completion_rate: Not tracked
```

**A/B Testing:**
When comparing hook variants, document in notes:
```yaml
notes: |
  A/B Test Results:
  - Wide shot opening: retention_3s 64%
  - Macro detail opening: retention_3s 79% (selected)
```

### Demo Link Edge Cases

**Video Not Yet Public:**
- Mark PR as draft
- Add demo link when ready
- Convert to ready for review

**Multiple Angles/Versions:**
- Link to primary version in `demo_link`
- Add alternatives in `notes`:
```yaml
demo_link: "https://youtube.com/watch?v=main-version"
notes: |
  Alternative angles:
  - Close-up variant: https://youtube.com/watch?v=closeup
  - Wide variant: https://youtube.com/watch?v=wide
```

**Platform Restrictions:**
- If region-locked, note in PR description
- Consider alternative hosting (Vimeo, direct link)

### Validation Script Edge Cases

**Running on Specific Files:**
```bash
# Validate single file
python scripts/validate_prompts.py prompts/cinematic/prompt.yaml

# Validate entire category
python scripts/validate_prompts.py prompts/cinematic/

# Validate all prompts
python scripts/validate_prompts.py prompts/
```

**Custom Schema Testing:**
If you're developing schema extensions, test locally:
```bash
# Point to custom schema
SCHEMA_FILE=custom-schema.json python scripts/validate_prompts.py prompt.yaml
```

**Debugging Validation:**
For detailed error output, check the script logs:
```bash
python scripts/validate_prompts.py prompt.yaml 2>&1 | tee validation.log
```

### Schema Extension Proposals

If you want to propose new fields:

1. Open GitHub Issue titled "Schema Extension: [field name]"
2. Provide use case and examples
3. Show how it fits Five-Pillar framework
4. Demonstrate value with real prompts
5. Maintainers will discuss and potentially add to schema

### Contribution Quality Guidelines

**Minimum Bar for Acceptance:**
- Follows Five-Pillar framework structure
- Passes schema validation
- Includes working demo video
- Properly attributed

**High-Quality Contributions:**
- Detailed camera specifications
- Performance metrics included
- Clear iteration notes
- Novel techniques or patterns
- Educational value for community

### Getting Help

- **Questions?** Open a [GitHub Issue](../../issues)
- **Need examples?** Check `prompts/` directory
- **Learn the framework**: Read [guides/five-pillars.md](guides/five-pillars.md)
- **Technical issues**: See validation error messages for guidance
- **Edge cases**: Re-read this section for advanced scenarios

## Recognition

Contributors who submit quality prompts will be:
- Listed in repository credits
- Recognized in community highlights
- Building the definitive Sora 2 prompt library

## Code of Conduct

- Be respectful and constructive
- Help others learn and improve
- Focus on quality over quantity
- Share knowledge generously
- Build community value

---

**Ready to contribute?** Start with the [Quick Start](#quick-start) guide above!

For technical details, see:
- [Five-Pillar Framework Guide](guides/five-pillars.md)
- [Schema Requirements Contract](contracts/prompt-schema-requirements.md)
- [CI Workflow Contract](contracts/ci-workflow-requirements.md)
