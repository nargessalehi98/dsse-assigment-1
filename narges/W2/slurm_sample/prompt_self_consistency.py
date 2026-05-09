"""
Self-consistency: same prompt, several stochastic samples; print all for comparison.
"""
from granite_prompt_utils import EXAMPLE_JAVA, chat_generate, load_tokenizer_and_model

NUM_SAMPLES = 3

if __name__ == "__main__":
    tokenizer, model = load_tokenizer_and_model()

    messages = [
        {
            "role": "system",
            "content": "You are a helpful software assistant. Explain code clearly and accurately.",
        },
        {
            "role": "user",
            "content": f"Explain what this program does:\n<source_code>\n{EXAMPLE_JAVA}\n</source_code>",
        },
    ]

    print(f"Generating {NUM_SAMPLES} samples (self-consistency)...\n")
    for i in range(NUM_SAMPLES):
        out = chat_generate(
            model,
            tokenizer,
            messages,
            max_new_tokens=512,
            temperature=0.8,
            top_p=0.9,
            do_sample=True,
        )
        print(f"--- Sample {i + 1} ---")
        print(out)
        print()
