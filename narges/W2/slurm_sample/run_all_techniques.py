"""
Load Granite once, then run every prompting technique and save each output to disk.

Slurm: submit from the directory that contains this file (and granite_prompt_utils.py).
Outputs: results/job_<SLURM_JOB_ID>/<technique>.txt (also printed to stdout / .log).
"""
from __future__ import annotations

import os
from pathlib import Path

import prompt_chain_of_thought
import prompt_few_shot
import prompt_self_consistency
import prompt_structured_output
import prompt_zero_shot
from granite_prompt_utils import chat_generate, load_tokenizer_and_model

SIMPLE_TECHNIQUES = [
    ("zero_shot", prompt_zero_shot.build_messages, prompt_zero_shot.GEN_KW),
    ("few_shot", prompt_few_shot.build_messages, prompt_few_shot.GEN_KW),
    ("chain_of_thought", prompt_chain_of_thought.build_messages, prompt_chain_of_thought.GEN_KW),
    ("structured_output", prompt_structured_output.build_messages, prompt_structured_output.GEN_KW),
]


def results_dir() -> Path:
    submit = os.environ.get("SLURM_SUBMIT_DIR", "").strip() or os.getcwd()
    job_id = os.environ.get("SLURM_JOB_ID", "").strip() or "local"
    path = Path(submit) / "results" / f"job_{job_id}"
    path.mkdir(parents=True, exist_ok=True)
    return path


def main():
    out_dir = results_dir()
    print(f"Results directory: {out_dir}\n")

    tokenizer, model = load_tokenizer_and_model()

    for label, builder, gen_kw in SIMPLE_TECHNIQUES:
        print("\n" + "=" * 72)
        print(f"TECHNIQUE: {label}")
        print("=" * 72 + "\n")
        out = chat_generate(model, tokenizer, builder(), **gen_kw)
        print(out)
        (out_dir / f"{label}.txt").write_text(out.strip() + "\n", encoding="utf-8")

    print("\n" + "=" * 72)
    print("TECHNIQUE: self_consistency")
    print("=" * 72 + "\n")
    sc_text = prompt_self_consistency.run(model, tokenizer, echo=True)
    (out_dir / "self_consistency.txt").write_text(sc_text.strip() + "\n", encoding="utf-8")

    print(f"\nSaved all technique outputs under: {out_dir}")


if __name__ == "__main__":
    main()
