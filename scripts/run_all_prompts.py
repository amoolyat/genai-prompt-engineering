import openai
import os
import json

# load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

with open("../prompts.json", "r") as f:
    all_prompts = json.load(f)

output_dir = "../raw_outputs/"
os.makedirs(output_dir, exist_ok=True)

def run_prompt(prompt_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt_text}],
            temperature=0.3
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"[ERROR] {e}"

for item in all_prompts:
    task = item["task_number"]
    strategy = item["strategy"]
    prompt = item["prompt"]
    filename = f"task{task:02d}_{strategy}_gpt-4.txt"
    output_path = os.path.join(output_dir, filename)

    #print(f"Running Task {task} - {strategy}...")

    output = run_prompt(prompt)

    with open(output_path, "w", encoding="utf-8") as out_file:
        out_file.write("Prompt:\n")
        out_file.write(prompt)
        out_file.write("\n\n---\n\n")
        out_file.write("Model Output:\n")
        out_file.write(output)
