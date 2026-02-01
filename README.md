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
   uv run vision-sandbox --image "my_screenshot.png" --prompt "Find the 'Login' button."
   ```

## Local Development

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
