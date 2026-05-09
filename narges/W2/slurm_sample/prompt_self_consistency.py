"""
Self-consistency: same prompt, several stochastic samples; print all for comparison.
"""
from granite_prompt_utils import EXAMPLE_JAVA, chat_generate, load_tokenizer_and_model

NUM_SAMPLES = 3

GEN_KW = dict(max_new_tokens=512, temperature=0.8, top_p=0.9, do_sample=True)


def build_messages():
    return [
        {
            "role": "system",
            "content": "You are a helpful software assistant. Explain code clearly and accurately.",
        },
        {
            "role": "user",
            "content": f"Explain what this program does:\n<source_code>\n{EXAMPLE_JAVA}\n</source_code>",
        },
    ]


def run(model, tokenizer, num_samples: int = NUM_SAMPLES, *, echo: bool = True) -> str:
    messages = build_messages()
    if echo:
        print(f"Generating {num_samples} samples (self-consistency)...\n")
    blocks = []
    for i in range(num_samples):
        out = chat_generate(model, tokenizer, messages, **GEN_KW)
        block = f"--- Sample {i + 1} ---\n{out}\n"
        blocks.append(block)
        if echo:
            print(block)
    return "\n".join(blocks)


if __name__ == "__main__":
    tokenizer, model = load_tokenizer_and_model()
    run(model, tokenizer, echo=True)
