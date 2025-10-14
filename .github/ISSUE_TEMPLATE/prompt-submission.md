---
name: 🎬 Prompt Submission
about: Submit a new Sora 2 prompt to the repository
title: '[PROMPT] '
labels: ['prompt-submission', 'needs-review']
assignees: ''
---

## Prompt Submission

### Basic Information

**Prompt Title:**
<!-- Clear, descriptive title for your prompt -->

**Category:**
<!-- Select one: cinematic, hyperrealism, animation, or experimental -->

**Demo Video Link:**
<!-- YouTube, Vimeo, or other video hosting URL -->
<!-- REQUIRED: Must show actual Sora 2 output -->

### Prompt Details

**Complete Prompt Text:**
<!-- Paste your full Sora 2 prompt here -->

```yaml
# Your prompt YAML file content
# Include all Five-Pillar sections
```

### Five-Pillar Framework Completeness

Confirm you've included all pillars:

- [ ] **Pillar 1: Subject/Character** - Who or what is the focus
- [ ] **Pillar 2: Action/Motion** - What movement occurs
- [ ] **Pillar 3: Environment/Setting** - Where and when it happens
- [ ] **Pillar 4: Cinematic Framing** - Camera work and composition
- [ ] **Pillar 5: Aesthetic/Style** - Visual treatment and mood

### Camera Specifications

- [ ] Lens type specified (e.g., 35mm, 100mm macro, wide-angle)
- [ ] Camera movement specified (e.g., tracking shot, static, dolly)
- [ ] Framing specified (e.g., close-up, wide shot, extreme close-up)

### Metadata

**Tags:**
<!-- List relevant tags, comma-separated -->
<!-- Examples: noir, rain, slow-motion, macro, glitch, cyberpunk -->

**Attribution:**
- [ ] This is my original prompt
- [ ] This prompt is from another source (provide link in `source` field)

**Source URL** (if applicable):
<!-- If prompt is from another creator, provide original URL -->

### Performance Metrics (Optional)

If you've tested this prompt and have performance data:

**3-Second Retention Rate:** <!-- % of viewers who watched 3+ seconds -->
**5-Second Retention Rate:** <!-- % of viewers who watched 5+ seconds -->
**Completion Rate:** <!-- % of viewers who watched to end -->
**Replays:** <!-- Number of times viewers replayed -->

### Validation Checklist

Before submitting, confirm:

- [ ] I have generated this video using Sora 2
- [ ] Demo video link is working and publicly accessible
- [ ] Prompt follows Five-Pillar Framework structure
- [ ] All required camera specifications are included
- [ ] I have run `python scripts/validate_prompts.py` locally and it passes
- [ ] YAML file uses correct schema structure (see `templates/PROMPT_TEMPLATE.yaml`)
- [ ] Tags are relevant and descriptive
- [ ] Attribution is correct (original or sourced)

### Additional Context

<!--
Add any additional information that might be helpful:
- Inspiration or creative process
- Technical challenges or learnings
- Iteration notes or version history
- Suggestions for remix or variations
-->

---

**Submission Workflow:**

1. Fork the repository
2. Create your prompt YAML file in the appropriate category directory
3. Run validation: `python scripts/validate_prompts.py prompts/category/your-prompt.yaml`
4. Submit pull request referencing this issue
5. Await maintainer review

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for detailed workflow.

**Questions?** Check the [FAQ](../../README.md#faq) or ask in Discussions.
