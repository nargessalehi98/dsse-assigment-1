"""
Chain-of-thought style: ask for explicit reasoning steps, then a short summary.
"""
from granite_prompt_utils import EXAMPLE_JAVA, chat_generate, load_tokenizer_and_model

GEN_KW = dict(max_new_tokens=768, temperature=0.4, top_p=0.85, do_sample=True)


def build_messages():
    return [
        {
            "role": "system",
            "content": "You are a careful code analyst. Follow the user's format exactly.",
        },
        {
            "role": "user",
            "content": f"""Analyze the code using this structure:

1. Reasoning: Walk through the code step by step (variables, loops, expressions).
2. Summary: In 2-4 sentences, state what the program does overall.

<source_code>
{EXAMPLE_JAVA}
</source_code>
""",
        },
    ]


if __name__ == "__main__":
    tokenizer, model = load_tokenizer_and_model()
    print("Generating (chain-of-thought style)...\n")
    print("--- Model Output ---")
    print(chat_generate(model, tokenizer, build_messages(), **GEN_KW))
