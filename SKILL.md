---
name: Vision Sandbox
slug: vision-sandbox
version: 1.0.0
description: Agentic Vision via Gemini's native Code Execution sandbox. Use for spatial grounding, visual math, and UI auditing.
metadata:
  openclaw:
    emoji: "🔭"
    requires:
      bins: ["uv"]
      env: ["GEMINI_API_KEY"]
---

# Vision Sandbox 🔭

Leverage Gemini's native code execution to analyze images with high precision. The model writes and runs Python code in a Google-hosted sandbox to verify visual data, perfect for UI auditing, spatial grounding, and visual reasoning.

## Installation

```bash
clawhub install vision-sandbox
```

## Usage

```bash
uv run vision-sandbox --image "path/to/image.png" --prompt "Identify all buttons and provide [x, y] coordinates."
```

## Pattern Library

### 📍 Spatial Grounding
Ask the model to find specific items and return coordinates.
* **Prompt:** "Locate the 'Submit' button in this screenshot. Use code execution to verify its center point and return the [x, y] coordinates in a [0, 1000] scale."

### 🧮 Visual Math
Ask the model to count or calculate based on the image.
* **Prompt:** "Count the number of items in the list. Use Python to sum their values if prices are visible."

### 🖥️ UI Audit
Check layout and readability.
* **Prompt:** "Check if the header text overlaps with any icons. Use the sandbox to calculate the bounding box intersections."

## Configuration
- **GEMINI_API_KEY**: Required environment variable.
- **Model**: Defaults to `gemini-2.0-flash-exp`.
