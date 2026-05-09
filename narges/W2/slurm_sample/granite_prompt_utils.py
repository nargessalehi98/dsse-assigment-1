"""Shared Granite load + chat generate for prompting technique scripts."""
import os

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "ibm-granite/granite-34b-code-instruct-8k"

EXAMPLE_JAVA = r"""
public class Task2 {
    public static void main(String[] args) {
        String id1   = "AMQ-2104";
        double files = 8.0;
        String id2   = "AMQ-317";
        double dmm   = 0.45;

        int n = Integer.parseInt(id1.split("-")[1])
            + Integer.parseInt(id2.split("-")[1]);

        int digits = 0;
        while (n > 0) {
            n = n / 10;
            digits++;
        }

        int impact = (int) (files * dmm);

        System.out.println("Combined digits: " + digits);
        System.out.println("Impact: " + impact);
    }
}
""".strip()


def load_tokenizer_and_model(model_name: str = MODEL_NAME):
    hf_token = os.environ.get("HF_TOKEN")
    if not hf_token:
        print("WARNING: HF_TOKEN not found. Proceeding with open-weights model download.")

    print(f"Loading Tokenizer for {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        token=hf_token,
        trust_remote_code=True,
    )
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"

    print("Loading Model (device_map=auto)...")
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        token=hf_token,
        trust_remote_code=True,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )
    return tokenizer, model


def chat_generate(
    model,
    tokenizer,
    messages: list[dict],
    *,
    max_new_tokens: int = 512,
    temperature: float = 0.5,
    top_p: float = 0.8,
    do_sample: bool = True,
) -> str:
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_dict=True,
        return_tensors="pt",
    ).to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_p=top_p,
        do_sample=do_sample,
        pad_token_id=tokenizer.eos_token_id,
    )
    input_len = inputs["input_ids"].shape[1]
    return tokenizer.decode(outputs[0][input_len:], skip_special_tokens=True)
