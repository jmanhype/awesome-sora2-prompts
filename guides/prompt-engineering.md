# Advanced Prompt Engineering for Sora 2

Comprehensive guide to crafting high-quality video generation prompts using the Five-Pillar Framework.

---

## Table of Contents

1. [The Five-Pillar Framework](#the-five-pillar-framework)
2. [Pillar 1: Subject/Character](#pillar-1-subjectcharacter)
3. [Pillar 2: Action/Motion](#pillar-2-actionmotion)
4. [Pillar 3: Environment/Setting](#pillar-3-environmentsetting)
5. [Pillar 4: Cinematic Framing](#pillar-4-cinematic-framing)
6. [Pillar 5: Aesthetic/Style](#pillar-5-aestheticstyle)
7. [Camera Specifications](#camera-specifications)
8. [Physics Modeling](#physics-modeling)
9. [Common Pitfalls](#common-pitfalls)
10. [Category-Specific Techniques](#category-specific-techniques)

---

## The Five-Pillar Framework

The Five-Pillar Framework provides a systematic approach to video prompt engineering by ensuring comprehensive coverage of all critical elements:

1. **Subject/Character** - Who or what is the focus
2. **Action/Motion** - What is happening and how it moves
3. **Environment/Setting** - Where the action takes place
4. **Cinematic Framing** - How the camera captures the scene
5. **Aesthetic/Style** - Visual treatment and artistic direction

**Key Principle**: Each pillar should contain specific, actionable details. Avoid vague language like "beautiful" or "interesting" - instead describe *what makes it beautiful*.

---

## Pillar 1: Subject/Character

Define the primary focus of your video with concrete visual details.

### Best Practices

✅ **DO**: Be specific about appearance, materials, and distinguishing features
```yaml
Subject/Character:
Black-clad motorcycle rider on sleek red sport bike, visor reflecting neon signs,
chrome details catching colored light, futuristic helmet design.
```

❌ **DON'T**: Use vague or generic descriptions
```yaml
Subject/Character:
A cool person on a motorcycle riding through the city.
```

### Detail Hierarchy

1. **Primary Characteristics**: Core identity (person, object, creature)
2. **Physical Attributes**: Size, color, texture, material
3. **Distinctive Features**: Unique elements that set it apart
4. **Contextual Details**: Relationship to environment

### Examples by Category

**Cinematic** (Character-focused):
```
Elderly jazz musician in worn fedora, weathered hands on saxophone,
callused fingertips positioned on keys, silver instrument catching
stage spotlight, slight tremor in hands suggesting decades of performance.
```

**Hyperrealism** (Object-focused):
```
Clear glass coffee mug with visible thickness variation, handle showing
manufacturing seam, ceramic base with micro-scratches from daily use,
coffee inside showing surface tension meniscus at rim.
```

**Animation** (Stylized):
```
Simplified paper cutout character with flat color fills, bold black outline,
articulated joints visible as brass fasteners, slight texture suggesting
cardstock material, whimsical proportions with oversized head.
```

**Experimental** (Abstract):
```
Geometric wireframe humanoid form composed of cyan light particles,
vertices pulsing with different intensities, translucent mesh revealing
background through negative space, glitch distortions at edge vertices.
```

---

## Pillar 2: Action/Motion

Describe movement with precision, including speed, direction, and physics.

### Motion Vocabulary

- **Speed**: slow, deliberate, rapid, explosive, gradual, sudden
- **Direction**: forward, backward, upward, circular, spiraling, chaotic
- **Quality**: smooth, jerky, flowing, stuttering, graceful, aggressive
- **Physics**: momentum, inertia, gravity, wind resistance, friction

### Best Practices

✅ **DO**: Specify motion characteristics and transitions
```yaml
Action/Motion:
High-speed chase through crowded streets, sharp turns around corners,
bike leaning into curves at 45-degree angle, sparks flying from occasional
contact, weaving between traffic with 1-2 feet clearance, speed gradually
increasing from 40mph to 80mph.
```

❌ **DON'T**: Use single-word motion descriptions
```yaml
Action/Motion:
Fast motorcycle riding.
```

### Motion Complexity Levels

**Simple Motion** (Single action):
```
Slow forward walk at 2mph, arms swinging naturally, slight head bob
matching stride rhythm.
```

**Compound Motion** (Multiple simultaneous actions):
```
Walking forward while turning head to look left, right hand reaching
toward pocket, coat tails swaying from side-to-side motion, subtle
weight shift with each step.
```

**Dynamic Motion** (Action with transitions):
```
Starting from standstill, accelerating to sprint, sudden direction
change with sliding momentum, controlled deceleration to walking pace,
final stop with forward lean recovering to upright stance.
```

---

## Pillar 3: Environment/Setting

Create immersive worlds with atmospheric detail and spatial relationships.

### Environmental Layers

1. **Immediate Space**: 0-10 feet around subject
2. **Mid-ground**: 10-50 feet, supporting elements
3. **Background**: 50+ feet, context and atmosphere
4. **Atmospheric Effects**: Lighting, weather, particles

### Best Practices

✅ **DO**: Build environmental layers with specific details
```yaml
Environment/Setting:
Dystopian megacity at night [background], towering skyscrapers with holographic
ads [mid-ground], neon signs in Japanese and English at street level [immediate],
steam rising from sidewalk vents [atmospheric], rain-slicked streets reflecting
colored light [surface], crowds with umbrellas on sidewalks [context].
```

❌ **DON'T**: Generic location names without details
```yaml
Environment/Setting:
A city at night.
```

### Lighting Techniques

**Natural Lighting**:
- Golden hour: Warm, low-angle sunlight
- Overcast: Soft, diffused light without hard shadows
- Backlit: Subject silhouetted against bright background
- Dappled: Light filtering through foliage

**Artificial Lighting**:
- Neon: Vibrant colored light with bloom/glow
- Practical: Light sources visible in frame (lamps, signs)
- Motivated: Light matching logical sources (window, fireplace)
- Dramatic: High-contrast with intentional shadows

---

## Pillar 4: Cinematic Framing

Technical camera specifications that define how the scene is captured.

### Camera Movement Types

**Static**:
- Locked position: Camera doesn't move at all
- Tripod-mounted: Stable, professional aesthetic

**Dynamic**:
- Tracking: Camera follows subject's movement
- Dolly: Camera moves on rails parallel or perpendicular to action
- Crane: Vertical movement (high to low or vice versa)
- Handheld: Organic, documentary feel with subtle shake
- Steadicam: Smooth flowing movement through space

### Shot Framing

**Wide Shot (WS)**: Subject is small, environment dominates
```
wide shot, figure occupies lower third of frame, vast sky emphasized,
emphasizing scale relationship between human and landscape
```

**Medium Shot (MS)**: Subject from waist up, balanced composition
```
medium shot, center-frame composition, subject fills 40% of vertical frame,
environment visible but supporting
```

**Close-Up (CU)**: Subject fills frame, intimacy and detail
```
close-up on hands, fingers filling frame, shallow depth of field,
background completely blurred
```

**Extreme Close-Up (ECU)**: Macro detail of small element
```
extreme close-up of water droplet, surface tension visible,
reflections distorted in curved surface, 100mm macro lens
```

### Best Practices

✅ **DO**: Specify lens, movement, and framing together
```yaml
camera:
  lens: "35mm"
  movement: "slow dolly forward at 1 foot per second, low angle tracking"
  framing: "medium shot, rule of thirds composition, subject in right third"
```

❌ **DON'T**: Omit technical specifications
```yaml
camera:
  lens: "normal"
  movement: "moving"
  framing: "good angle"
```

---

## Pillar 5: Aesthetic/Style

Define the artistic vision and visual treatment.

### Style Dimensions

1. **Historical Period**: Modern, retro, futuristic, period-specific
2. **Artistic Movement**: Impressionism, surrealism, minimalism
3. **Media Influence**: Film noir, anime, documentary, music video
4. **Technical Approach**: Film grain, digital clean, painterly, cel-shaded
5. **Color Palette**: Monochrome, saturated, muted, neon, earth tones
6. **Mood**: Contemplative, energetic, melancholic, suspenseful

### Reference-Based Styling

**Cinematic References**:
```
Blade Runner-inspired cyberpunk aesthetic, Ridley Scott's use of atmospheric
fog and neon, high contrast lighting with deep shadows, lens flares from
practical light sources, desaturated colors except for vibrant neon accents.
```

**Artistic References**:
```
M.C. Escher lithograph aesthetic translated to 3D, impossible perspective
manipulation, mathematical precision in contradictory spatial relationships,
monochromatic palette emphasizing form and shadow.
```

### Best Practices

✅ **DO**: Specify multiple style dimensions consistently
```yaml
Aesthetic/Style:
Traditional watercolor animation technique, visible brush textures and paper grain,
transparent color overlays creating depth, wet-on-wet blending effects,
impressionistic rather than detailed, soft atmospheric lighting, palette of
blues, purples, and muted greens.
```

❌ **DON'T**: Single-word style descriptions
```yaml
Aesthetic/Style:
Cinematic and artistic.
```

---

## Camera Specifications

### Lens Focal Lengths

| Focal Length | Effect | Best For |
|--------------|--------|----------|
| 14-24mm | Extreme wide, distortion at edges | Architecture, vast landscapes |
| 24-35mm | Wide angle, natural perspective | Environmental storytelling |
| 35-50mm | Standard, human eye equivalent | Balanced shots, documentary |
| 50-85mm | Portrait, shallow DOF | Character focus, interviews |
| 85-135mm | Telephoto, compressed perspective | Isolation, emotional closeups |
| 100mm+ Macro | Extreme detail, shallow DOF | Product, nature, abstract |

### Depth of Field

**Shallow DOF** (f/1.4 - f/2.8):
```
Subject sharp, background blurred into smooth bokeh, creating subject
isolation and drawing eye to main element
```

**Medium DOF** (f/4 - f/8):
```
Subject and immediate environment in focus, gradual falloff to background,
balanced between isolation and context
```

**Deep DOF** (f/11 - f/22):
```
Everything from foreground to background sharp, emphasizing spatial
relationships and environmental detail
```

---

## Physics Modeling

For hyperrealistic prompts, physics specifications ensure believable material behavior.

### Material Properties

**Solid Materials**:
- Metals: Reflectivity, weight, rigidity
- Plastics: Flexibility, translucency, surface finish
- Fabrics: Drape, texture, response to motion
- Glass: Transparency, refraction, surface reflections

**Fluid Dynamics**:
- Water: Surface tension, viscosity, splashing behavior
- Smoke: Dispersion patterns, density variation, wind interaction
- Fire: Combustion dynamics, heat distortion, light emission

### Force Specifications

```yaml
physics:
  materials:
    - tempered glass panels
    - polished chrome steel
    - reflective coating
  forces:
    - natural daylight (5000K color temperature)
    - atmospheric refraction
    - mirror reflection (0.9 reflectivity coefficient)
    - surface tension on glass
```

---

## Common Pitfalls

### 1. Vague Language

❌ **Bad**: "A beautiful scene with amazing visuals"
✅ **Good**: "Golden hour lighting with 20-degree sun angle, warm orange tones (2500K), long shadows stretching across frame"

### 2. Conflicting Specifications

❌ **Bad**: "Intimate close-up with vast landscape visible in background"
✅ **Good**: "Extreme close-up with shallow depth of field, landscape implied through out-of-focus color suggestion"

### 3. Missing Technical Details

❌ **Bad**: "Camera moves around the subject"
✅ **Good**: "180-degree orbital dolly at 5-foot radius, maintaining eye-level framing, 2 revolutions per minute"

### 4. Overcomplicated Actions

❌ **Bad**: "Subject walks, runs, jumps, spins, dances, and flies simultaneously"
✅ **Good**: "Subject walks forward, then transitions to run with 3-step acceleration, culminating in single vertical jump"

### 5. Inconsistent Style

❌ **Bad**: "Hyperrealistic person in cartoon environment with abstract lighting"
✅ **Good**: Pick ONE style and commit: "Hyperrealistic person in photorealistic environment with natural lighting"

---

## Category-Specific Techniques

### Cinematic Prompts

**Focus**: Narrative and emotion
**Key Elements**:
- Character-driven action
- Motivated camera movement
- Dramatic lighting for mood
- 24fps motion cadence
- Film grain and color grading

**Template**:
```
Subject/Character: [Detailed character description]
Action/Motion: [Narrative action with emotional context]
Environment/Setting: [Scene that supports story]
Cinematic Framing: [Traditional filmmaking techniques]
Aesthetic/Style: [Film references, lighting mood, color palette]
```

### Hyperrealism Prompts

**Focus**: Physical accuracy and believability
**Key Elements**:
- Physics-based material behavior
- Natural lighting conditions
- Real-world plausibility
- Subtle imperfections
- Material-specific responses

**Template**:
```
Subject/Character: [Precise material descriptions]
Action/Motion: [Physics-accurate movement]
Environment/Setting: [Natural lighting and context]
Cinematic Framing: [Documentary-style capture]
Aesthetic/Style: [Natural color, minimal stylization]
physics:
  materials: [Specific materials list]
  forces: [Physical forces affecting materials]
```

### Animation Prompts

**Focus**: Artistic stylization and creative technique
**Key Elements**:
- Non-realistic aesthetics
- Exaggerated proportions or motion
- Handcrafted quality indicators
- Animation-specific techniques (cel-shading, stop-motion, etc.)
- Design emphasis over realism

**Template**:
```
Subject/Character: [Stylized character design]
Action/Motion: [Animation principles - squash, stretch, exaggeration]
Environment/Setting: [Artistic world design]
Cinematic Framing: [Animation composition rules]
Aesthetic/Style: [Animation technique, color theory, design philosophy]
```

### Experimental Prompts

**Focus**: Boundary-pushing innovation
**Key Elements**:
- Unconventional approaches
- Abstract concepts
- Technical rule-breaking
- Surreal or impossible scenarios
- Artistic exploration

**Template**:
```
Subject/Character: [Unconventional subject matter]
Action/Motion: [Physics-defying or abstract movement]
Environment/Setting: [Surreal or impossible spaces]
Cinematic Framing: [Experimental camera techniques]
Aesthetic/Style: [Avant-garde references, unique visual treatment]
```

---

## Next Steps

1. **Study Examples**: Review prompts in each category to understand patterns
2. **Start Simple**: Begin with basic prompts before adding complexity
3. **Iterate**: Test and refine based on results
4. **Build Library**: Create reusable components (lighting setups, camera moves)
5. **Contribute**: Share your successful prompts with the community

---

**Related Guides**:
- [Retention Tactics Guide](retention-tactics.md) - Hook-first prompt design
- [Contributing Guidelines](../CONTRIBUTING.md) - How to submit prompts

← [Back to Main README](../README.md)
