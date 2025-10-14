# Maintainer Review Checklist

Use this checklist when reviewing prompt submissions or changes. Copy into PR comment.

## Schema Validation

- [ ] All YAML files pass `python scripts/validate_prompts.py prompts/`
- [ ] Required fields present: title, category, tags, summary, prompt, camera, author, created, sora_version
- [ ] Tags follow pattern `^[a-z0-9-]+$` (lowercase, numbers, hyphens only)
- [ ] Category matches one of: cinematic, hyperrealism, animation, experimental

## Prompt Quality (Five-Pillar Framework)

- [ ] **Subject/Character**: Clear, specific description of main subject
- [ ] **Action/Motion**: Detailed movement and behavior description
- [ ] **Environment/Setting**: Complete scene context and atmosphere
- [ ] **Cinematic Framing**: Camera details (lens, movement, framing)
- [ ] **Aesthetic/Style**: Consistent visual style and artistic direction

## Content Standards

- [ ] Prompt is clear and actionable (not vague or ambiguous)
- [ ] Language is professional and appropriate
- [ ] No copyrighted character names or brand references without fair use justification
- [ ] NSFW flag set correctly (`true` for mature content, `false` for safe content)
- [ ] Demo link is valid YouTube URL or placeholder format

## Technical Details

- [ ] Camera specifications are realistic (valid lens focal lengths, achievable movements)
- [ ] Physics section (if present) lists appropriate materials and forces
- [ ] Expected duration is reasonable (typically 4-15 seconds)
- [ ] Audio notes (if present) enhance understanding of intended result

## Documentation

- [ ] Prompt added to appropriate category README (`prompts/{category}/README.md`)
- [ ] Category README entry follows established format:
  - Title as heading
  - Summary section
  - Tags with inline code formatting
  - Camera details
  - Demo link
  - File link
  - Horizontal rule separator

## Categorization

- [ ] **Cinematic**: Story-driven with narrative elements → Place in `prompts/cinematic/`
- [ ] **Hyperrealism**: Photorealistic with physics accuracy → Place in `prompts/hyperrealism/`
- [ ] **Animation**: Stylized, non-realistic aesthetics → Place in `prompts/animation/`
- [ ] **Experimental**: Avant-garde, boundary-pushing → Place in `prompts/experimental/`

## Diversity & Balance

- [ ] New prompt adds variety to category (different subject matter, style, or technique)
- [ ] Prompt demonstrates unique capability or approach
- [ ] Category maintains balanced representation across prompt types

## Final Check

- [ ] All files committed with clear, descriptive commit message
- [ ] No merge conflicts with main branch
- [ ] CI/CD validation workflow passes (if configured)

---

## Rejection Criteria (must reject if any apply)

- ❌ Prompt fails schema validation
- ❌ Contains illegal content or hate speech
- ❌ Plagiarizes existing prompts without attribution
- ❌ Is duplicate or near-duplicate of existing prompt
- ❌ Documentation not updated (missing category README entry)
- ❌ NSFW content without proper flag
- ❌ Spam or low-effort submission

---

## Feedback Templates

### Request Changes
```
Thank you for your submission! Before we can merge, please address:

- [ ] [Specific issue 1]
- [ ] [Specific issue 2]

Please update your PR and I'll review again.
```

### Approve
```
✅ Excellent prompt! This demonstrates [specific strength].

Merging now. Thank you for contributing to awesome-sora2-prompts!
```

### Reject
```
Thank you for your interest in contributing. Unfortunately, this submission [specific reason for rejection].

We encourage you to [suggestion for improvement or alternative approach].
```
