## Prompt Submission

**Category**: <!-- cinematic / hyperrealism / animation / experimental -->

**Prompt Title**: <!-- Your prompt's title -->

**Demo Video**: <!-- Required: YouTube/Vimeo link or direct URL -->

---

## Checklist

Please confirm you have completed the following (check all that apply):

### Required ✅
- [ ] Read [CONTRIBUTING.md](../CONTRIBUTING.md) and [Five-Pillar Framework Guide](../guides/five-pillars.md)
- [ ] Prompt follows Five-Pillar structure (Subject, Action, Environment, Framing, Style)
- [ ] All required YAML fields are filled (title, category, tags, summary, prompt, camera, author, created, sora_version)
- [ ] Camera object includes `lens`, `movement`, and `framing`
- [ ] Generated actual Sora 2 video from this prompt
- [ ] Included working `demo_link` to video output
- [ ] Validated locally with `python scripts/validate_prompts.py prompts/your-file.yaml`
- [ ] CI validation passes (GitHub Actions check must be green)

### Hyperrealism Only
- [ ] If category is `hyperrealism`, included `physics` field with `materials` and `forces`

### Attribution
- [ ] If original work: Set `source: "original"`
- [ ] If derived/inspired: Provided source URL and attribution

### Optional Enhancements
- [ ] Added `audio_notes` for synchronized audio guidance
- [ ] Added `expected_duration` estimate
- [ ] Included `physics` hints (even if not hyperrealism)

---

## Description

**What makes this prompt interesting?**
<!-- Describe what's unique or valuable about this contribution -->


**Techniques or approaches used:**
<!-- Any specific techniques worth highlighting -->


**Challenges overcome:**
<!-- Any difficulties you worked through -->


---

## Demo Video Details

**Link**: <!-- Same as above, for reference -->

**Actual output duration**: <!-- e.g., "7 seconds" -->

**Notes on result**:
<!-- How well did Sora 2 match your prompt? Any surprises? -->


---

## Additional Context

<!-- Any other information that would help reviewers understand your contribution -->


---

## For Maintainers

**Validation status**: <!-- Will be automatically checked by CI -->
- Validation: ![Validation](https://github.com/ai-video-factory/awesome-sora2-prompts/actions/workflows/validate.yml/badge.svg)

**Review notes**:
<!-- Maintainer use only -->
