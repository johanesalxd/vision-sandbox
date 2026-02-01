import os
import sys
import argparse
import base64
from pathlib import Path
from google import genai
from google.genai import types

def run_vision_sandbox(image_path, prompt, model_id="gemini-3-flash-preview"):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    # Load image
    with open(image_path, "rb") as f:
        image_data = f.read()
    
    image_part = types.Part.from_bytes(
        data=image_data,
        mime_type="image/jpeg" if image_path.endswith((".jpg", ".jpeg")) else "image/png"
    )

    # Configure model with code execution
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution())],
        temperature=0.0, # Keep it deterministic for grounding
    )

    print(f"--- Sending request to {model_id} with Code Execution ---")
    
    response = client.models.generate_content(
        model=model_id,
        contents=[prompt, image_part],
        config=config
    )

    # Process response parts
    for part in response.candidates[0].content.parts:
        if part.executable_code:
            print("\n--- SANDBOX CODE ---")
            print(f"```python\n{part.executable_code.code}\n```")
        
        if part.code_execution_result:
            print("\n--- SANDBOX OUTPUT ---")
            print(f"```\n{part.code_execution_result.output}\n```")
            
        if part.text:
            print("\n--- MODEL RESPONSE ---")
            print(part.text)

    # Note: If the sandbox generated images, they would be in candidate.content.parts as well.
    # We could extract them and save to disk with a MEDIA: line.
    for i, candidate in enumerate(response.candidates):
        for j, part in enumerate(candidate.content.parts):
            if hasattr(part, 'inline_data') and part.inline_data:
                out_path = f"sandbox_output_{i}_{j}.png"
                with open(out_path, "wb") as f:
                    f.write(part.inline_data.data)
                print(f"\nMEDIA: {os.path.abspath(out_path)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vader Vision Sandbox Executor")
    parser.add_argument("-i", "--image", required=True, help="Path to input image")
    parser.add_argument("-p", "--prompt", required=True, help="Instruction for the model")
    parser.add_argument("-m", "--model", default="google/gemini-3-flash-preview", help="Model ID")

    args = parser.parse_args()
    run_vision_sandbox(args.image, args.prompt, args.model)
