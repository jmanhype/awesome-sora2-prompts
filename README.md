# Awesome Sora 2 Prompts 🎬

> A curated collection of high-quality prompts for OpenAI's Sora 2, structured using the Five-Pillar Framework

[![Validation](https://github.com/ai-video-factory/awesome-sora2-prompts/actions/workflows/validate.yml/badge.svg)](https://github.com/ai-video-factory/awesome-sora2-prompts/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## What is This?

This repository contains **battle-tested Sora 2 prompts** organized by the **Five-Pillar Framework** - a structured approach to prompt engineering that produces consistent, high-quality results.

Every prompt includes:
- ✅ **Working demo video** - Verified Sora 2 output
- ✅ **Structured framework** - Subject, Action, Environment, Framing, Style
- ✅ **Camera specifications** - Lens, movement, framing details
- ✅ **Complete metadata** - Tags, category, attribution

**No theory. No guesses. Only prompts that actually work.**

## Quick Start

### 🎯 Using Prompts

1. **Browse by category**:
   - [`prompts/cinematic/`](prompts/cinematic/) - Narrative-driven scenes
   - [`prompts/hyperrealism/`](prompts/hyperrealism/) - Photorealistic simulations
   - [`prompts/animation/`](prompts/animation/) - Stylized aesthetics
   - [`prompts/experimental/`](prompts/experimental/) - Boundary-pushing work

2. **Pick a prompt** (example: [`noir-detective.yaml`](prompts/cinematic/noir-detective.yaml))

3. **Copy the `prompt` field** and paste into Sora 2

4. **Generate!** 🎥

### 📚 Learning Prompt Engineering

**New to prompt writing?** Start here:
1. Read the [Five-Pillar Framework Guide](guides/five-pillars.md)
2. Study example prompts in each category
3. Practice with the framework structure
4. Generate your own videos

### 🔍 Search by Tags

Find prompts by searching tags in the repository:

```
tag:noir tag:rain          # Multiple tags
tag:hyperrealism tag:macro # Category + style
tag:stop-motion            # Animation technique
tag:glitch tag:experimental # Experimental effects
```

Or browse prompts directly in each category directory.

### 🤝 Contributing

We welcome high-quality prompts that advance the community's understanding!

**Requirements**:
- Follow the Five-Pillar Framework
- Generate actual Sora 2 video (demo link required)
- Pass schema validation

See [CONTRIBUTING.md](CONTRIBUTING.md) for complete workflow.

## The Five-Pillar Framework

Every prompt in this repository follows this structure:

```
🎭 Pillar 1: Subject/Character
   Who or what is the focus?

🎬 Pillar 2: Action/Motion
   What movement occurs?

🌍 Pillar 3: Environment/Setting
   Where and when does it happen?

📷 Pillar 4: Cinematic Framing
   Camera work and composition

🎨 Pillar 5: Aesthetic/Style
   Visual treatment and mood
```

**Why use this framework?**
- 🎯 Produces consistent results
- 📐 Reduces ambiguity
- 🔄 Enables effective iteration
- 🎓 Teachable and shareable

Learn more: [Five-Pillar Framework Guide](guides/five-pillars.md)

## Browse by Category

### 🎬 [Cinematic Prompts](prompts/cinematic/)
Story-driven videos with traditional filmmaking techniques. Character-focused scenes with narrative elements and dramatic lighting.

**Featured Prompts**:
- **[Noir Detective in Rain](prompts/cinematic/noir-detective.yaml)** - Trench-coated detective walking through rain-slicked streets, 35mm tracking shot, high-contrast noir lighting | [Demo →](https://youtube.com/watch?v=example-noir-detective)

[→ View all cinematic prompts](prompts/cinematic/)

---

### 📸 [Hyperrealism Prompts](prompts/hyperrealism/)
Photorealistic simulations with material accuracy and physics. Natural lighting, real-world plausibility, physics-based rendering.

**Featured Prompts**:
- **[Morning Coffee Pour](prompts/hyperrealism/morning-coffee.yaml)** - Extreme close-up of coffee pouring into ceramic mug, 100mm macro lens, physics-accurate liquid dynamics | [Demo →](https://youtube.com/watch?v=example-morning-coffee)

[→ View all hyperrealism prompts](prompts/hyperrealism/)

---

### 🎨 [Animation Prompts](prompts/animation/)
Stylized, non-realistic aesthetics using creative animation techniques. Artistic stylization, handcrafted quality, emphasis on design.

**Featured Prompts**:
- **[Paper Cutout Forest Journey](prompts/animation/paper-cutout-forest.yaml)** - Stylized paper cutout character walking through layered forest, stop-motion aesthetic, parallax scrolling | [Demo →](https://youtube.com/watch?v=example-paper-forest)

[→ View all animation prompts](prompts/animation/)

---

### 🔬 [Experimental Prompts](prompts/experimental/)
Boundary-pushing, avant-garde work exploring Sora 2's capabilities. Innovative concepts, surreal visuals, unconventional approaches.

**Featured Prompts**:
- **[Digital Data Dissolution](prompts/experimental/data-dissolution.yaml)** - 3D wireframe cityscape dissolving into data particles, glitch effects, vaporwave aesthetic | [Demo →](https://youtube.com/watch?v=example-data-dissolution)

[→ View all experimental prompts](prompts/experimental/)

## Repository Structure

```
awesome-sora2-prompts/
├── prompts/              # All prompts organized by category
│   ├── cinematic/        # Narrative-driven videos
│   ├── hyperrealism/     # Photorealistic simulations
│   ├── animation/        # Stylized aesthetics
│   └── experimental/     # Avant-garde work
├── guides/               # Educational resources
│   └── five-pillars.md   # Framework guide
├── templates/            # Prompt template
│   └── PROMPT_TEMPLATE.yaml
├── scripts/              # Validation tooling
│   ├── validate_prompts.py
│   └── requirements.txt
├── .github/
│   └── workflows/
│       └── validate.yml  # CI validation
├── prompt.schema.json    # JSON Schema for validation
├── CONTRIBUTING.md       # Contribution guide
└── README.md             # This file
```

## Validation & Quality

Every prompt must:
- ✅ Pass JSON Schema validation
- ✅ Follow Five-Pillar structure
- ✅ Include camera specifications
- ✅ Provide working demo video
- ✅ Be properly attributed

### Run Validation Locally

```bash
# Install dependencies
pip install -r scripts/requirements.txt

# Validate a prompt
python scripts/validate_prompts.py prompts/category/prompt-name.yaml

# Validate all prompts
python scripts/validate_prompts.py prompts/
```

### CI Validation

All pull requests automatically run validation via GitHub Actions. PRs with validation failures cannot be merged.

## Search by Tags

Find prompts by combining tags:

| Search | Results |
|--------|---------|
| `tag:noir tag:rain` | Film noir in rainy scenes |
| `tag:hyperrealism tag:macro` | Photorealistic close-ups |
| `tag:stop-motion tag:whimsical` | Handcrafted animation |
| `tag:glitch tag:cyberpunk` | Digital experimental |

**Tag search syntax**: Use GitHub's native search with `tag:tagname` format. Combine multiple tags to narrow results.

## Schema & Contracts

This repository uses formal specifications to ensure quality:

- **[prompt.schema.json](prompt.schema.json)** - JSON Schema Draft 7 validation
- **[contracts/prompt-schema-requirements.md](contracts/prompt-schema-requirements.md)** - Schema contract
- **[contracts/ci-workflow-requirements.md](contracts/ci-workflow-requirements.md)** - CI contract

These contracts define exact requirements and error messages.

## Constitution

This repository follows the **AI Video Factory Constitution**, which establishes:

- **Principle III**: Five-Pillar Framework structure
- **Principle VI**: Test-First Contribution (demo videos required)
- **Quality Standards**: Schema validation, attribution, ethics

See the constitution in the project documentation.

## Tools & Resources

### Validation
- Python 3.11+
- jsonschema 4.19.2
- PyYAML 6.0.1

### Sora 2 Access
This repository is for users with Sora 2 access. Prompts are designed for OpenAI's Sora 2 model.

### Additional Resources
- [Five-Pillar Framework Guide](guides/five-pillars.md)
- [Contribution Guidelines](CONTRIBUTING.md)
- [Pull Request Template](.github/pull_request_template.md)

## Community

### Get Involved

- 🐛 **Found an issue?** [Open an issue](../../issues)
- 💡 **Have an idea?** Start a discussion
- 🎬 **Created a great prompt?** Submit a PR
- 📚 **Want to learn?** Read the guides

### Recognition

Contributors who submit quality prompts are recognized in repository credits and community highlights.

## FAQ

**Q: Do I need Sora 2 access to contribute?**
A: Yes, you must be able to generate actual Sora 2 videos to include required demo links.

**Q: Can I submit prompts from other sources?**
A: Yes, but you must provide proper attribution. Set `source` field to the original URL.

**Q: What if my prompt fails validation?**
A: Read the error messages - they include specific guidance. See [CONTRIBUTING.md](CONTRIBUTING.md) for help.

**Q: Can I submit NSFW content?**
A: Only with maintainer pre-approval. Open an issue first to discuss.

**Q: How do I format camera specifications?**
A: See the [Five-Pillar Framework Guide](guides/five-pillars.md) for detailed camera guidance.

## License

MIT License - See [LICENSE](LICENSE) for details.

Prompts are contributed by the community. Individual prompts may have additional attribution requirements specified in their `source` field.

## Credits

Created by the AI Video Factory community.

**Core Contributors**:
- Repository structure and validation system
- Five-Pillar Framework design
- Initial seed prompts

**Community Contributors**:
- See [Contributors](../../graphs/contributors) page

## Support

- 📖 **Documentation**: [guides/](guides/)
- 💬 **Discussions**: GitHub Discussions
- 🐛 **Bug Reports**: [GitHub Issues](../../issues)
- 📧 **Contact**: [Open an issue](../../issues/new)

---

**Ready to create?** Start with the [Five-Pillar Framework Guide](guides/five-pillars.md)! 🎬
