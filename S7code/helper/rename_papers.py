#!/usr/bin/env python3
"""Rename papers from arxiv ID to slug format."""
from pathlib import Path

PAPERS = [
    ("2306.05685", "judging-llm-as-judge-mtbench"),
    ("2310.08491", "prometheus"),
    ("2405.01535", "prometheus-2"),
    ("2309.00267", "rlaif"),
    ("2302.04023", "helm"),
    ("2311.12983", "gpqa"),
    ("2305.20050", "pandalm"),
    ("2210.09261", "bigbench-hard"),
    ("2310.05029", "llm-cannot-self-correct"),
    ("2406.04770", "chatbot-arena"),
    ("2203.02155", "instructgpt"),
    ("2204.05862", "helpful-harmless-rlhf"),
    ("2212.08073", "constitutional-ai"),
    ("2305.18290", "dpo"),
    ("2009.01325", "learning-summarize-rlhf"),
    ("2112.00114", "webgpt"),
    ("2305.11206", "lima"),
    ("2212.10560", "self-instruct"),
    ("2009.03300", "mmlu"),
    ("2107.03374", "codex-humaneval"),
    ("2303.08774", "gpt4-technical-report"),
    ("2206.04615", "bigbench"),
    ("2312.11805", "gemini"),
    ("2310.06825", "mistral-7b"),
    ("2404.14219", "phi-3"),
    ("2407.21783", "llama-3-herd"),
    ("2201.11903", "chain-of-thought-prompting"),
    ("2203.11171", "self-consistency"),
    ("2205.01068", "zero-shot-reasoners"),
    ("2210.11610", "react"),
    ("2205.10625", "least-to-most-prompting"),
    ("2305.10601", "tree-of-thoughts"),
    ("2303.12528", "sparks-of-agi"),
    ("2206.07682", "emergent-abilities"),
    ("2001.08361", "scaling-laws"),
    ("2203.15556", "chinchilla"),
    ("2005.14165", "gpt-3"),
    ("2302.13971", "llama-1"),
    ("2307.09288", "llama-2"),
    ("2210.06726", "flan-t5"),
    ("1706.03762", "attention-is-all-you-need"),
    ("2402.09171", "gemma"),
    ("2404.07143", "arena-hard-auto"),
    ("2308.07902", "wizardlm"),
    ("2303.17580", "hugginggpt"),
    ("2306.09212", "llm-vs-human-evaluations"),
    ("2308.12966", "code-llama"),
    ("2401.04088", "mixtral-of-experts"),
    ("2406.11697", "judging-the-judges"),
    ("2402.01720", "mixtral-8x22b"),
]

if __name__ == "__main__":
    d = Path(__file__).parent / "sandbox" / "my-papers"
    count = 0
    for arxiv_id, slug in PAPERS:
        old = d / f"{arxiv_id}.md"
        new = d / f"{slug}.md"
        if old.exists():
            old.rename(new)
            count += 1
            print(f"  {arxiv_id}.md -> {slug}.md")
    print(f"\nRenamed {count} files")
