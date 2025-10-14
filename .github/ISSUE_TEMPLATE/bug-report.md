---
name: 🐛 Bug Report
about: Report a bug or issue with the repository
title: '[BUG] '
labels: ['bug', 'needs-triage']
assignees: ''
---

## Bug Report

### Description

**Brief Summary:**
<!-- Clear, concise description of the bug -->

**What Happened:**
<!-- Describe the actual behavior -->

**What You Expected:**
<!-- Describe what should have happened instead -->

### Steps to Reproduce

1. <!-- First step -->
2. <!-- Second step -->
3. <!-- Third step -->
<!-- Add more steps as needed -->

**Reproducible:** <!-- Always / Sometimes / Once -->

### Environment

**Operating System:**
<!-- e.g., macOS 14.2, Ubuntu 22.04, Windows 11 -->

**Python Version:**
<!-- Run: python --version -->

**Dependencies:**
<!-- Run: pip list | grep -E "(jsonschema|PyYAML)" -->

**Repository Version:**
<!-- Latest commit hash or release tag -->

### Validation Output

**If this is a validation error, paste the full output:**

```bash
# Run: python scripts/validate_prompts.py prompts/category/your-prompt.yaml

<!-- Paste validation output here -->
```

### Schema Validation Errors

**If you're getting schema validation errors:**

```json
<!-- Paste the JSON Schema error output here -->
```

**Your YAML file structure:**
```yaml
<!-- Paste relevant sections of your YAML file -->
```

### Category-Specific Issues

**Which category does this affect?**
- [ ] Cinematic
- [ ] Hyperrealism
- [ ] Animation
- [ ] Experimental
- [ ] All categories
- [ ] Repository infrastructure (scripts, CI, documentation)

### Attempted Solutions

**What have you tried so far?**
<!-- List any troubleshooting steps you've already attempted -->

### Additional Context

**Screenshots:**
<!-- If applicable, add screenshots to help explain the problem -->

**Relevant Files:**
<!-- List any relevant prompt files, scripts, or configuration -->

**Error Logs:**
<!-- Paste any relevant error logs or tracebacks -->

**Related Issues:**
<!-- Link to any related issues if applicable -->

---

## Common Issues Quick Reference

Before submitting, check if your issue matches these common problems:

### Validation Failures

**Missing Required Fields:**
- Ensure all required schema fields are present: `title`, `category`, `prompt`, `camera`, `demo_link`, `tags`
- Check field spelling and structure

**Invalid YAML Syntax:**
- Validate YAML at: https://www.yamllint.com/
- Check for proper indentation (use spaces, not tabs)
- Ensure strings with special characters are quoted

**Camera Specification Errors:**
- Must include: `lens`, `movement`, `framing`
- Check for typos in camera field names

**Demo Link Issues:**
- Link must be publicly accessible
- Supported platforms: YouTube, Vimeo, or direct video URLs
- Test link in incognito/private browser window

### Script Issues

**Import Errors:**
- Install dependencies: `pip install -r scripts/requirements.txt`
- Verify Python version: 3.11+

**File Not Found:**
- Use correct relative paths from project root
- Check file names (case-sensitive on Linux/macOS)

**Permission Errors:**
- Ensure read/write permissions on files
- Check directory permissions

### CI Failures

**GitHub Actions Failing:**
- Check Actions tab for detailed error logs
- Ensure all required files are committed
- Verify YAML files pass local validation first

---

**Need Help?**

- 📖 **Documentation**: [CONTRIBUTING.md](../../CONTRIBUTING.md)
- 💬 **Discussions**: Ask questions in GitHub Discussions
- 🔍 **Search**: Check [existing issues](../../issues) for similar problems
- 📧 **Support**: For complex issues, provide maximum detail above

---

**For Maintainers:**

<!-- Triage checklist (maintainers only) -->
- [ ] Reproduced locally
- [ ] Severity assessed (critical/high/medium/low)
- [ ] Root cause identified
- [ ] Fix implemented or workaround provided
- [ ] Documentation updated if needed
