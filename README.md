# Awesome Sora 2 Prompts

A structured collection of prompts for OpenAI's Sora 2 video generation model, organized using the Five-Pillar Framework.

## Status

| Metric | Value |
|--------|-------|
| Total prompts | 12 |
| Categories | 4 (cinematic, hyperrealism, animation, experimental) |
| Prompt format | YAML with JSON Schema validation |
| CI validation | GitHub Actions on every PR |
| License | MIT |

## What This Contains

Each prompt is a YAML file with:

- A tested prompt string for Sora 2
- Camera specifications (lens, movement, framing)
- Category and tag metadata
- Optional performance metrics (retention, completion rate)
- Demo video link (where available)

Prompts follow the Five-Pillar Framework: Subject, Action, Environment, Cinematic Framing, Aesthetic/Style.

## Categories

| Category | Path | Count | Focus |
|----------|------|-------|-------|
| Cinematic | [`prompts/cinematic/`](prompts/cinematic/) | 3 | Narrative-driven scenes, dramatic lighting |
| Hyperrealism | [`prompts/hyperrealism/`](prompts/hyperrealism/) | 3 | Photorealistic simulation, physics accuracy |
| Animation | [`prompts/animation/`](prompts/animation/) | 3 | Stylized aesthetics, non-realistic techniques |
| Experimental | [`prompts/experimental/`](prompts/experimental/) | 3 | Boundary-testing, avant-garde concepts |

## Usage

1. Browse a category directory
2. Open any `.yaml` file
3. Copy the `prompt` field
4. Paste into Sora 2

Example prompt file: [`prompts/cinematic/noir-detective.yaml`](prompts/cinematic/noir-detective.yaml)

## Five-Pillar Framework

| Pillar | Question |
|--------|----------|
| 1. Subject/Character | Who or what is the focus? |
| 2. Action/Motion | What movement occurs? |
| 3. Environment/Setting | Where and when does it happen? |
| 4. Cinematic Framing | Camera work and composition? |
| 5. Aesthetic/Style | Visual treatment and mood? |

Details: [guides/five-pillars.md](guides/five-pillars.md)

## Validation

Every prompt must pass:
- JSON Schema validation ([`prompt.schema.json`](prompt.schema.json))
- Five-Pillar structure check
- Camera specification requirement

```bash
pip install -r scripts/requirements.txt
python scripts/validate_prompts.py prompts/
```

CI runs validation on all pull requests automatically.

## Performance Tracking

Prompts can include optional performance data:

```yaml
performance:
  retention_3s: 85.5    # % viewers at 3 seconds
  retention_5s: 72.3    # % viewers at 5 seconds
  completion_rate: 68.9  # % viewers who finished
  replays: 12
```

Run `python scripts/identify_top_performers.py` to rank prompts by weighted score.

## Repository Structure

```
prompts/              # YAML prompts by category
  cinematic/
  hyperrealism/
  animation/
  experimental/
guides/               # Framework documentation
  five-pillars.md
templates/            # Submission template
scripts/              # Validation and analysis tools
prompt.schema.json    # JSON Schema Draft 7
```

## Limitations

- Requires Sora 2 access to generate videos from these prompts.
- Demo video links may become unavailable as Sora 2 evolves.
- Performance metrics are self-reported and limited in sample size.
- The Five-Pillar Framework is opinionated; other prompt structures can also produce good results.

## Contributing

Requirements:
1. Follow the Five-Pillar Framework
2. Provide a working Sora 2 demo video link
3. Pass schema validation

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow.

## License

MIT -- see [LICENSE](LICENSE).

Individual prompts may have additional attribution requirements specified in their `source` field.
