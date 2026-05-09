"""
Structured output: request JSON only (easier to parse downstream).
"""
from granite_prompt_utils import EXAMPLE_JAVA, chat_generate, load_tokenizer_and_model

if __name__ == "__main__":
    tokenizer, model = load_tokenizer_and_model()

    messages = [
        {
            "role": "system",
            "content": "You output only valid JSON. No markdown fences, no commentary.",
        },
        {
            "role": "user",
            "content": f"""Return ONLY a JSON object with these keys:
"summary" (string),
"variables" (array of objects with "name" and "role"),
"control_flow" (array of short strings),
"outputs" (array of strings describing what is printed).

<source_code>
{EXAMPLE_JAVA}
</source_code>
""",
        },
    ]

    print("Generating (structured JSON)...\n")
    print("--- Model Output ---")
    print(
        chat_generate(
            model,
            tokenizer,
            messages,
            max_new_tokens=768,
            temperature=0.2,
            top_p=0.9,
            do_sample=True,
        )
    )
