"""
Few-shot prompting: one short example (user + assistant) before the real task.
"""
from granite_prompt_utils import EXAMPLE_JAVA, chat_generate, load_tokenizer_and_model

GEN_KW = dict(max_new_tokens=512, temperature=0.5, top_p=0.8, do_sample=True)


def build_messages():
    return [
        {
            "role": "system",
            "content": "You explain Java code briefly: variables, control flow, and printed output.",
        },
        {
            "role": "user",
            "content": "Explain this code:\n<source_code>\nint x = 2 + 3;\nSystem.out.println(x);\n</source_code>",
        },
        {
            "role": "assistant",
            "content": (
                "The code computes 2+3 (5), stores it in x, then prints 5 to standard output."
            ),
        },
        {
            "role": "user",
            "content": f"Explain this code the same way:\n<source_code>\n{EXAMPLE_JAVA}\n</source_code>",
        },
    ]


if __name__ == "__main__":
    tokenizer, model = load_tokenizer_and_model()
    print("Generating (few-shot)...\n")
    print("--- Model Output ---")
    print(chat_generate(model, tokenizer, build_messages(), **GEN_KW))
