# The Five-Pillar Framework for Sora 2 Prompts

**Master the art of Sora 2 prompt engineering**

This guide teaches the Five-Pillar Framework, the foundational structure for creating effective Sora 2 prompts as defined in the AI Video Factory Constitution (Principle III).

## Why Five Pillars?

Sora 2 generates videos from text, but not all prompts are equal. The Five-Pillar Framework ensures your prompts:

✅ **Produce consistent results** - Structure reduces ambiguity
✅ **Capture all dimensions** - Nothing important is left to chance
✅ **Enable iteration** - Clear structure makes refinement easier
✅ **Share knowledge** - Others can learn from your approach

## The Five Pillars

### Pillar 1: Subject/Character

**What it is**: The primary focus of your video - the "who" or "what"

**Why it matters**: Sora needs to know what to center the video around

**What to include**:
- Physical description (appearance, clothing, features)
- Scale and proportion
- Key identifying characteristics
- Expression or demeanor (if character)

**Examples**:

```
❌ Weak: "A detective"

✅ Strong: "A trench-coated detective in a fedora, face half-lit by neon signs.
Weathered features, stubble, tired eyes scanning the street with world-weary vigilance.
Navy trench coat collar turned up against the rain."
```

**Tips**:
- Be specific about visual details
- Use vivid, sensory language
- Include clothing, props, or accessories
- Describe expression or attitude if relevant

---

### Pillar 2: Action/Motion

**What it is**: What movement occurs in the scene - the dynamics

**Why it matters**: Video is motion; static images aren't videos

**What to include**:
- Primary movement or action
- Speed and rhythm of motion
- Sequence of events (if applicable)
- Physical interactions with environment
- Secondary movements or reactions

**Examples**:

```
❌ Weak: "The detective walks"

✅ Strong: "The detective walks slowly through rain-slicked streets at night,
each footstep deliberate and measured. Puddles ripple as footsteps disturb the water.
Occasional head turn to check side alleys."
```

**Tips**:
- Describe the quality of movement (slow, abrupt, fluid)
- Include interactions (splashing, touching, displacing)
- Note timing and pacing
- Consider cause and effect

---

### Pillar 3: Environment/Setting

**What it is**: Where and when the scene takes place - the context

**Why it matters**: Setting creates atmosphere and grounds the action

**What to include**:
- Location type (indoor/outdoor, specific place)
- Time of day and lighting conditions
- Weather or atmospheric effects
- Background elements and details
- Spatial depth (foreground, middle, background)
- Color palette and mood

**Examples**:

```
❌ Weak: "City street at night"

✅ Strong: "City street at midnight. Heavy rain creating sheets of water.
Neon signs reflect in wet pavement - red, green, amber lights creating streaks of color.
Distant streetlights create pools of amber light. Steam rises from subway grates.
Mist hangs in the air. Depth: Detective in foreground, blurred city lights in
background fading into misty darkness."
```

**Tips**:
- Layer depth (foreground → background)
- Describe lighting sources and quality
- Include atmospheric effects (fog, rain, dust)
- Specify color palette
- Create spatial relationships

---

### Pillar 4: Cinematic Framing

**What it is**: Camera work, lens choice, and composition - the cinematography

**Why it matters**: This is what transforms description into cinematic language

**What to include**:
- **Lens**: Focal length (35mm, 85mm, wide-angle, etc.)
- **Movement**: Camera motion (tracking, dolly, static, handheld)
- **Framing**: Shot type (close-up, medium, wide, angle)
- Focal depth (shallow DOF with bokeh, deep focus)
- Camera position and angle

**Required subfields** (per schema):
- `camera.lens` - Lens specification
- `camera.movement` - Camera movement description
- `camera.framing` - Shot framing and composition

**Examples**:

```
❌ Weak: "Camera follows detective"

✅ Strong: "35mm lens. Medium shot from behind, third-person perspective,
camera positioned at shoulder height. Slow tracking movement follows detective
at consistent walking pace, maintaining 8-10 feet distance. Shallow depth of field
keeps focus on detective's silhouette, background softly blurred with bokeh effect
from neon lights."
```

**Common lens choices**:
- **Wide angle (24-35mm)**: Environmental context, space
- **Standard (40-50mm)**: Natural perspective
- **Portrait (85mm)**: Character focus, flattering
- **Macro (100mm+)**: Extreme detail
- **Telephoto**: Compression, isolation

**Movement types**:
- **Static**: Locked, no movement
- **Pan**: Horizontal rotation
- **Tilt**: Vertical rotation
- **Tracking/Dolly**: Camera moves with subject
- **Crane**: Vertical movement
- **Handheld**: Natural shake, documentary feel

**Framing types**:
- **Extreme close-up**: Facial details, objects
- **Close-up**: Face or object focus
- **Medium shot**: Waist up, interaction
- **Wide shot**: Full body, environment
- **Establishing shot**: Location context

**Tips**:
- Match lens to intent (wide for space, tight for emotion)
- Describe movement speed and smoothness
- Specify camera position (height, angle)
- Include depth of field effects
- Think like a cinematographer

---

### Pillar 5: Aesthetic/Style

**What it is**: Visual treatment, mood, and artistic interpretation

**Why it matters**: This transforms technical description into emotional experience

**What to include**:
- Lighting style (high contrast, soft, dramatic)
- Color grading and palette
- Film/texture treatment (grain, digital, pristine)
- Artistic references or styles
- Mood and emotional tone
- Visual effects or treatments

**Examples**:

```
❌ Weak: "Dark and moody"

✅ Strong: "High contrast noir lighting with deep blacks and bright highlights.
Film grain texture reminiscent of 1940s detective films. Color palette: deep blues
dominate shadows, amber streetlights, neon reds and greens punctuate the darkness.
Cinematic film stock aesthetic with slight vignette. Moody, atmospheric,
emphasizing isolation and mystery."
```

**Lighting styles**:
- **High key**: Bright, minimal shadows (comedy, upbeat)
- **Low key**: Dark, dramatic shadows (noir, thriller)
- **Natural**: Realistic light sources
- **High contrast**: Strong light/dark separation
- **Soft**: Diffused, gentle lighting

**Color approaches**:
- Specific palette (cyan and orange, teal and gold)
- Color temperature (warm/cool)
- Saturation level (vibrant, desaturated, monochrome)
- Color grading references (film stock, era)

**Tips**:
- Reference specific visual styles or eras
- Describe the emotional intent
- Include texture and treatment details
- Consider cultural or genre associations
- Use evocative language

---

## Putting It All Together

### Example Prompt Structure

```
[Subject/Character - Pillar 1]
A trench-coated detective in a fedora...
[Detailed description]

[Action/Motion - Pillar 2]
The detective walks slowly through rain-slicked streets...
[Motion description]

[Environment/Setting - Pillar 3]
City street at midnight. Heavy rain...
[Setting details]

[Cinematic Framing - Pillar 4]
35mm lens. Medium shot from behind...
[Camera specifications]

[Aesthetic/Style - Pillar 5]
High contrast noir lighting...
[Visual treatment]
```

### Complete Example: Noir Detective

See `prompts/cinematic/noir-detective.yaml` for the full implementation.

---

## Category-Specific Guidance

### Cinematic Prompts
- Focus on storytelling and character
- Use traditional cinematography
- Create emotional connection
- Reference film genres

### Hyperrealism Prompts
- Emphasize photorealistic detail
- Include physics hints (materials, forces)
- Specify realistic lighting
- Focus on material accuracy

### Animation Prompts
- Embrace stylization
- Reference animation techniques
- Allow for non-realistic physics
- Emphasize artistic vision

### Experimental Prompts
- Push boundaries creatively
- Explore impossible scenarios
- Mix styles and techniques
- Challenge conventions

---

## Advanced Techniques

### Layering Detail

Build complexity by layering details within each pillar:

**Environment example**:
```
Foreground: Dark green paper grass with hand-cut irregular edges
Middle ground: Tree trunks in brown and tan, simple cylindrical shapes
Background: Lighter green paper trees, progressively lighter colors for distance
```

### Physics Hints (Hyperrealism)

For photorealistic prompts, include physics information:

```yaml
physics:
  materials:
    - wet pavement
    - fabric trench coat
    - falling rain
  forces:
    - gravity on raindrops
    - coat fabric flow as detective walks
    - water ripples from footsteps
```

### Audio Sync Notes

Enhance with audio cues:

```yaml
audio_notes: "Steady rain pattering on pavement. Muffled footsteps splashing
through puddles. Distant jazz music from nearby club. Steam hissing from subway grate."
```

---

## Common Mistakes to Avoid

❌ **Vague subjects**: "A person" → "A weather-worn detective with stubble"
❌ **Static scenes**: "Detective stands" → "Detective walks, checking alleys"
❌ **No environment depth**: "Street" → "Multi-layered street with fog, neon, steam"
❌ **Missing camera specs**: Must include lens, movement, framing
❌ **Unclear aesthetic**: "Nice looking" → "High contrast noir with film grain"

---

## Practice Exercise

Try writing a Five-Pillar prompt for: **"Coffee being poured into a mug"**

**Challenge yourself**:
1. Make the subject specific (what kind of coffee? what mug?)
2. Describe the motion in detail (how does liquid behave?)
3. Set the environment (kitchen? time of day? lighting?)
4. Choose appropriate camera work (macro lens? static? angle?)
5. Define the aesthetic (photorealistic? stylized? mood?)

**Compare your result** to `prompts/hyperrealism/morning-coffee.yaml`

---

## Learning Resources

### Study Existing Prompts
- Browse `prompts/` directory by category
- Analyze structure and techniques
- Note effective language choices
- See how pillars interact

### Cinematography References
- Roger Deakins (cinematographer)
- Emmanuel Lubezki (cinematographer)
- Film analysis videos (Every Frame a Painting)
- Photography composition tutorials

### Iterate and Refine
1. Write prompt following Five Pillars
2. Generate video with Sora 2
3. Analyze what worked / what didn't
4. Refine specific pillars
5. Test again

---

## Quick Reference Checklist

Before submitting, ensure your prompt has:

- [ ] **Pillar 1**: Specific, detailed subject/character description
- [ ] **Pillar 2**: Clear action and motion with timing/quality
- [ ] **Pillar 3**: Rich environment with depth and atmosphere
- [ ] **Pillar 4**: Complete camera specs (lens + movement + framing)
- [ ] **Pillar 5**: Defined aesthetic, mood, and visual treatment
- [ ] **Physics** (if hyperrealism): Materials and forces listed
- [ ] **Validation**: Prompt passes schema validation
- [ ] **Demo**: Actual Sora 2 video generated and linked

---

## Questions?

- See example prompts in `prompts/` directory
- Review [CONTRIBUTING.md](../CONTRIBUTING.md) for workflow
- Open GitHub issue for help or clarification

**Now go create something amazing!** 🎬
