# Vision Sandbox 🔭

This OpenClaw skill enables **Agentic Vision** using Gemini's native Python code execution sandbox. 

Instead of just "guessing" what's in an image, the model can write and execute code to verify spatial relationships, count objects, or perform complex visual reasoning with pixel-level precision.

## Features
- **Spatial Grounding:** Get precise [x, y] coordinates for UI elements.
- **Visual Calculation:** Let the model use Python to calculate values from visual data.
- **UI Auditing:** Automatically check for overlaps, alignment, and accessibility.
- **Integrated with OpenClaw:** Designed to work seamlessly within the OpenClaw ecosystem.

## Prerequisites
- [uv](https://github.com/astral-sh/uv) (Python package manager)
- `GEMINI_API_KEY` set in your environment.

## Quick Start

1. **Install via ClawHub:**
   ```bash
   clawhub install vision-sandbox
   ```

2. **Run a task:**
   ```bash
   uv run vision-sandbox --image "sample/how-many-fingers.png" --prompt "Count the fingers."
   ```

## Visual Example: Counting Fingers

Using the included sample image, you can see the power of the sandbox. Instead of just identifying a hand, the model can logically isolate and count parts.

**Command:**
```bash
uv run vision-sandbox --image "sample/how-many-fingers.png" --prompt "Count the number of fingers on this hand. Use code execution to identify the bounding box for each finger and return the total count."
```

**Result:** The model will write Python code to define bounding boxes for each digit, ensuring an accurate count rather than a visual guess.

## Integration with OpenCode

Vision Sandbox is a powerful companion for OpenCode (the coding agent). You can use it to provide visual context for your development tasks.

### Workflow
1. **Visual UI Grounding:** If you are building a UI, take a screenshot and ask Vision Sandbox to get the exact coordinates of elements.
2. **Pass to OpenCode:** Feed those coordinates back into your OpenCode session to write precise CSS or layout logic.

**Example from OpenCode:**
> "Hey Vader, run `vision-sandbox` on this screenshot to find the exact padding of the login card, then update `styles.css` accordingly."

## Pattern Library

If you want to modify the skill:

1. Clone the repository.
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Run directly:
   ```bash
   uv run scripts/vision_executor.py --image test.png --prompt "Analyze this."
   ```

## License
MIT
