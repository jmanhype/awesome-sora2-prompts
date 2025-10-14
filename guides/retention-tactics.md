# Retention Tactics: Hook-First Video Prompt Design

Master the art of capturing attention in the first 1-3 seconds with strategic prompt engineering.

---

## Table of Contents

1. [The Hook-First Principle](#the-hook-first-principle)
2. [Psychology of Attention](#psychology-of-attention)
3. [Opening Frame Design](#opening-frame-design)
4. [Motion as Hook](#motion-as-hook)
5. [Visual Contrast](#visual-contrast)
6. [Curiosity Gaps](#curiosity-gaps)
7. [Pattern Interruption](#pattern-interruption)
8. [Category-Specific Hooks](#category-specific-hooks)
9. [Anti-Patterns](#anti-patterns)
10. [Testing & Iteration](#testing--iteration)

---

## The Hook-First Principle

**Core Truth**: Users decide to keep watching within 1-3 seconds. Your prompt must prioritize the opening moment above all else.

### The 3-Second Rule

- **0-1 sec**: Establish immediate visual interest
- **1-2 sec**: Introduce motion or change
- **2-3 sec**: Reveal enough to create curiosity

**Prompt Structure Priority**:
1. **Opening frame** (what viewer sees first)
2. **Initial motion** (first movement)
3. **Progressive reveal** (what unfolds next)
4. **Sustained interest** (why they keep watching)

---

## Psychology of Attention

### What Captures Human Attention

**Evolutionary Triggers**:
- **Movement**: Sudden or unexpected motion
- **Faces**: Human faces, especially eyes
- **Contrast**: High-contrast elements
- **Novelty**: Unusual or unexpected elements
- **Threat/Safety**: Dangerous situations or narrow escapes
- **Mystery**: Incomplete information creating curiosity

### Attention Retention Strategies

1. **Visual Complexity**: Balance between interesting and overwhelming
2. **Predictable Unpredictability**: Pattern with variation
3. **Emotional Resonance**: Mood that connects with viewer
4. **Technical Excellence**: Quality that signals professionalism

---

## Opening Frame Design

The first frame is your billboard. Design it intentionally.

### Strong Opening Frames

✅ **Immediate Visual Interest**:
```yaml
Subject/Character:
OPENING FRAME: Extreme close-up of coffee pouring into cup, stream of liquid
frozen mid-air in first frame, droplets suspended, then motion begins.
```

✅ **High Contrast**:
```yaml
Subject/Character:
OPENING FRAME: Silhouette of lone figure against brilliant orange sunset,
dark foreground with explosive color in sky, figure begins walking.
```

✅ **Unexpected Scale**:
```yaml
Subject/Character:
OPENING FRAME: Macro view of water droplet, world reflected in curved surface,
then pull back reveals it's on leaf edge about to fall.
```

### Weak Opening Frames

❌ **Slow Build-Up**:
```yaml
Subject/Character:
Empty street gradually becomes visible as sun rises, then eventually
someone walks into frame after 8 seconds.
```

❌ **Generic Establishing Shot**:
```yaml
Subject/Character:
Wide shot of city skyline, camera slowly panning across buildings,
no immediate focal point or action.
```

### Hook-First Prompt Pattern

```yaml
Action/Motion:
[HOOK: Immediate attention-grabber in first 1-2 seconds]
[DEVELOPMENT: What happens next, building on hook]
[PAYOFF: Satisfying conclusion or loop point]

# Example:
Action/Motion:
Glass shatters in extreme slow motion revealing face behind it [HOOK],
fragments floating past camera in detailed trajectories [DEVELOPMENT],
time returns to normal as pieces hit ground [PAYOFF].
```

---

## Motion as Hook

Motion captures attention more effectively than static beauty.

### High-Impact Opening Motions

**Towards Camera**:
```
Motorcycle bursts from alley directly toward camera, headlight flaring,
immediate sense of speed and danger
```

**Sudden Action**:
```
Blade slicing through water balloon, frame opens mid-slice as water
explodes outward in all directions
```

**Scale Reveal**:
```
Opens tight on texture of object, immediate pull back reveals it's
massive structure, sudden scale recontextualization
```

**Collision**:
```
Two objects meeting at impact point, frame opens at moment of contact,
energy dispersing in all directions from collision
```

### Motion Timing

**Fast Start** (0-1 second):
```yaml
Action/Motion:
[Immediate explosive motion] → [Sustained development] → [Resolution]

Example: Firework explodes filling frame with light, sparks cascade down,
gentle float to ground with smoke trails
```

**Slow Build** (1-3 seconds):
```yaml
Action/Motion:
[Compelling static frame] → [Motion begins] → [Momentum builds]

Example: Perfect droplet hangs from faucet tip, slight tremor, surface
tension breaks, accelerating fall toward pool below
```

---

## Visual Contrast

Contrast creates instant visual hierarchy and captures attention.

### Contrast Dimensions

**Luminance Contrast**:
```
Pure white figure against midnight black background, no mid-tones,
graphic stark separation
```

**Color Contrast**:
```
Single vibrant red umbrella in completely desaturated rainy scene,
only element with color draws eye immediately
```

**Motion Contrast**:
```
Everything frozen in time except single element moving normally,
juxtaposition of static and dynamic
```

**Scale Contrast**:
```
Tiny figure in vast empty space, emphasizing isolation and scale through
negative space around subject
```

**Texture Contrast**:
```
Smooth polished metal surface reflecting rough organic tree bark,
material opposition creating interest
```

### Contrast Prompt Pattern

```yaml
Environment/Setting:
[Establish baseline visual state] then [introduce contrasting element]

# Example:
Environment/Setting:
Monochromatic grey industrial space, concrete walls, steel beams, no color,
then single shaft of warm golden sunlight cuts through dusty air, highlighting
floating particles
```

---

## Curiosity Gaps

Create questions in viewer's mind that can only be answered by continuing to watch.

### Types of Curiosity Gaps

**Partial Reveal**:
```yaml
Subject/Character:
OPENING: Only lower half of figure visible, unusual costume elements
suggesting something unexpected, slow tilt up reveals full character
```

**Context Mystery**:
```yaml
Environment/Setting:
OPENING: Extreme close-up of unfamiliar texture/surface, unclear what
object is, pull back gradually reveals unexpected context
```

**Outcome Uncertainty**:
```yaml
Action/Motion:
OPENING: Object teetering on edge, physics suggesting imminent fall,
tension builds, then surprising resolution
```

**Process Fascination**:
```yaml
Action/Motion:
OPENING: Complex mechanism in motion, unclear purpose, watching to
understand how parts interact and what end result will be
```

### Curiosity Prompt Pattern

```yaml
prompt: |
  OPENING QUESTION: [What is this? / What will happen? / How does this work?]
  GRADUAL REVEAL: [Partial information that increases curiosity]
  ANSWER: [Satisfying reveal or loop that prompts re-watch]
```

---

## Pattern Interruption

Break expectations to capture attention.

### Expectation vs. Reality

**Normal Setup, Unexpected Twist**:
```yaml
Action/Motion:
Person reaches for ordinary door handle, hand passes through it like
hologram, revealing digital glitch world beyond
```

**Impossible Physics**:
```yaml
Action/Motion:
Water pours from bottle upward instead of down, defying gravity naturally,
no explanation, just acceptance of impossible
```

**Scale Subversion**:
```yaml
Subject/Character:
Opens on what appears to be massive mountain landscape, reveal that
it's actually macro shot of sand pile, complete perspective shift
```

**Time Manipulation**:
```yaml
Action/Motion:
Left half of frame in real-time, right half in extreme slow motion,
same event occurring at different temporal speeds simultaneously
```

### Pattern Interrupt Techniques

1. **Reverse Expectations**: Set up obvious direction, then go opposite
2. **Break Physics**: Violate natural laws in visually interesting ways
3. **Genre Mix**: Combine incompatible visual styles or contexts
4. **Temporal Anomaly**: Time behaves unexpectedly or inconsistently
5. **Scale Shift**: Macro becomes massive or vice versa

---

## Category-Specific Hooks

### Cinematic Hooks

**Character Introduction**:
```yaml
OPENING: Dramatic reveal of character through silhouette, lighting,
or environmental context before showing face clearly

Example: Shadow on wall shows character with weapon, tension builds
before character steps into light
```

**In Media Res**:
```yaml
OPENING: Start in middle of action scene, no explanation, immediately
engaging situation

Example: Car chase already at high speed, no setup of why or how,
pure kinetic energy from frame one
```

### Hyperrealism Hooks

**Impossible Detail**:
```yaml
OPENING: Macro detail so precise it seems impossible, challenge viewer's
perception of reality

Example: Individual coffee bubbles on surface, each with its own reflection,
physics of foam structure visible
```

**Unexpected Physics**:
```yaml
OPENING: Physics event captured at scale or speed impossible to see naturally

Example: Bullet impact on water surface, shockwave cavity formation
visible in extreme slow motion
```

### Animation Hooks

**Style Impact**:
```yaml
OPENING: Immediately establish unique artistic style that differentiates
from everything else

Example: Cel-shaded character with bold outlines springs into frame,
graphic style unmistakable from first instant
```

**Impossible Motion**:
```yaml
OPENING: Animation-only movement that exploits lack of physical constraints

Example: Character stretches and snaps back like rubber, cartoon physics
establishing tone immediately
```

### Experimental Hooks

**Visual Paradox**:
```yaml
OPENING: Present visual impossibility that challenges perception

Example: M.C. Escher staircase, camera movement reveals contradiction
in first 2 seconds
```

**Digital Corruption**:
```yaml
OPENING: Normal scene immediately glitching or corrupting in unexpected ways

Example: Person's face splits into RGB channels that separate and drift,
digital breakdown as hook
```

---

## Anti-Patterns

### What NOT to Do

❌ **Slow Fade-In**:
```yaml
Action/Motion:
Scene fades in from black over 4 seconds, gradual reveal of environment,
then action eventually begins
```
**Problem**: Attention lost before anything interesting happens

✅ **Fix**:
```yaml
Action/Motion:
Scene opens mid-action, full brightness and motion from frame one
```

---

❌ **Generic Establishing Shot**:
```yaml
Cinematic Framing:
Wide shot of location, slow pan across environment, establishing geography
before introducing subject
```
**Problem**: No focal point, attention diffuses

✅ **Fix**:
```yaml
Cinematic Framing:
Opens tight on interesting detail, then reveals it's part of larger scene
```

---

❌ **Unclear Subject**:
```yaml
Subject/Character:
Something in the distance, not clearly visible yet, slowly approaching camera
```
**Problem**: Can't identify what to focus on

✅ **Fix**:
```yaml
Subject/Character:
Opens on dramatic silhouette or partial reveal that's visually interesting
even without full detail
```

---

❌ **Delayed Payoff**:
```yaml
Action/Motion:
Long setup of atmosphere and mood, interesting event occurs at 10-second mark
```
**Problem**: Hook comes too late

✅ **Fix**:
```yaml
Action/Motion:
Open with interesting event, then provide context and development
```

---

## Testing & Iteration

### Measuring Hook Effectiveness

**Mental 3-Second Test**:
1. Imagine only seeing first 3 seconds
2. Would you want to see more?
3. Can you identify a clear visual hook?

**Components Checklist**:
- [ ] Immediate visual interest in opening frame
- [ ] Motion or change within first 2 seconds
- [ ] Clear focal point (not diffuse attention)
- [ ] Contrast that creates hierarchy
- [ ] Curiosity gap or question posed
- [ ] Unexpected element or pattern interrupt

### Iteration Process

1. **Draft Prompt**: Write initial version
2. **Hook Audit**: Identify first 3 seconds explicitly
3. **Strengthen Hook**: Add specificity to opening moment
4. **Validate**: Does opening frame work as standalone image?
5. **Refine**: Adjust timing and motion for maximum impact

### Example Iteration

**Draft 1** (Weak Hook):
```yaml
Action/Motion:
Person walks down street at night, lights reflecting on wet pavement,
eventually something interesting happens
```

**Draft 2** (Stronger Hook):
```yaml
Action/Motion:
OPENING: Extreme close-up of shoe splashing into puddle, water explodes
upward in slow motion, pull back reveals noir detective walking through
rain-soaked street at night, neon reflections in ripples
```

---

## Practical Examples

### Example 1: Strong Hook (Hyperrealism)

```yaml
title: "Bullet Through Apple"

Action/Motion:
HOOK (0-1 sec): Bullet pierces apple skin, entry point visible with shock
wave radiating through flesh, apple skin splits in star pattern
DEVELOPMENT (1-3 sec): Bullet continues through core, apple flesh exploding
outward in chunks, internal structure visible in slow motion
PAYOFF (3-5 sec): Bullet exits far side, apple fragments dispersing in
perfect radial pattern, seeds floating in suspension
```

**Why It Works**:
- Immediate action in first frame
- Violent motion captures attention
- Slow motion reveals detail impossible to see naturally
- Physics demonstration satisfies curiosity

### Example 2: Strong Hook (Experimental)

```yaml
title: "Reality Glitch"

Action/Motion:
HOOK (0-1 sec): Person's face suddenly splits into RGB color channels,
red/green/blue versions offset by 2 inches, digital corruption visible
DEVELOPMENT (1-3 sec): Split channels drift further apart, pixel sorting
creates vertical streaks, figure fragmenting into data
PAYOFF (3-5 sec): Complete dissolution into abstract digital patterns,
then sudden snap back to normal like nothing happened
```

**Why It Works**:
- Unexpected visual breaks pattern
- Immediate recognizable glitch effect
- Curiosity about what will happen next
- Satisfying loop point for re-watch

---

## Key Takeaways

1. **Front-Load Interest**: Best content in first 1-3 seconds
2. **Motion Beats Beauty**: Movement captures attention more than static perfection
3. **Create Questions**: Curiosity gaps keep viewers engaged
4. **Break Patterns**: Unexpected elements interrupt scroll behavior
5. **Test Ruthlessly**: If first 3 seconds don't hook you, they won't hook others

---

**Related Guides**:
- [Prompt Engineering Guide](prompt-engineering.md) - Technical prompt construction
- [Contributing Guidelines](../CONTRIBUTING.md) - How to submit prompts

← [Back to Main README](../README.md)
