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

## Featured Prompts

### Cinematic
**[Noir Detective in Rain](prompts/cinematic/noir-detective.yaml)**
- Trench-coated detective walking through rain-slicked streets
- 35mm tracking shot, high-contrast noir lighting
- Neon reflections, film grain aesthetic
- [Demo video →](https://youtube.com/watch?v=example-noir-detective)

### Hyperrealism
**[Morning Coffee Pour](prompts/hyperrealism/morning-coffee.yaml)**
- Extreme close-up of coffee pouring into ceramic mug
- 100mm macro lens, static shot
- Physics-accurate liquid dynamics, steam, light refraction
- [Demo video →](https://youtube.com/watch?v=example-morning-coffee)

### Animation
**[Paper Cutout Forest Journey](prompts/animation/paper-cutout-forest.yaml)**
- Stylized paper cutout character walking through layered forest
- Stop-motion aesthetic, parallax scrolling
- Handcrafted texture, vibrant colors
- [Demo video →](https://youtube.com/watch?v=example-paper-forest)

### Experimental
**[Digital Data Dissolution](prompts/experimental/data-dissolution.yaml)**
- 3D wireframe cityscape dissolving into data particles
- Glitch effects, vaporwave aesthetic
- Impossible physics, abstract visualization
- [Demo video →](https://youtube.com/watch?v=example-data-dissolution)

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

## Categories

### 🎬 Cinematic
Story-driven videos with traditional filmmaking techniques. Focus on character, narrative, and emotional impact.

**Characteristics**:
- Character-focused scenes
- Narrative elements
- Traditional cinematography
- Dramatic lighting and composition

### 📸 Hyperrealism
Photorealistic simulations emphasizing material accuracy and physics.

**Characteristics**:
- Photorealistic detail
- Physics accuracy (materials, forces)
- Natural lighting
- Real-world plausibility

**Requirements**: Must include `physics` field with materials and forces.

### 🎨 Animation
Stylized, non-realistic aesthetics using creative animation techniques.

**Characteristics**:
- Artistic stylization
- Non-realistic rendering
- Creative techniques (stop-motion, 2D, etc.)
- Emphasis on design and style

### 🔬 Experimental
Boundary-pushing, avant-garde work exploring Sora 2's capabilities.

**Characteristics**:
- Innovative concepts
- Surreal or abstract visuals
- Technical experimentation
- Unconventional approaches

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
