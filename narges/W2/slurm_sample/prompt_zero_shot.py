"""
Zero-shot + role prompting: single instruction, no examples (baseline).
Same idea as sample.py; uses shared loader.
"""
from granite_prompt_utils import EXAMPLE_JAVA, chat_generate, load_tokenizer_and_model

if __name__ == "__main__":
    tokenizer, model = load_tokenizer_and_model()

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful software assistant. Explain the functionality "
                "of the provided code in simple terms."
            ),
        },
        {
            "role": "user",
            "content": f"Please analyze the following source code:\n\n<source_code>\n{EXAMPLE_JAVA}\n</source_code>",
        },
    ]

    print("Generating (zero-shot)...\n")
    print("--- Model Output ---")
    print(
        chat_generate(
            model,
            tokenizer,
            messages,
            max_new_tokens=512,
            temperature=0.5,
            top_p=0.8,
            do_sample=True,
        )
    )
