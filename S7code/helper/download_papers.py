#!/usr/bin/env python3
"""
Bulk download 50 arXiv papers as markdown files into sandbox/my-papers/.
Topics: LLMs, LLM-as-Judge, RLHF, evaluation, reasoning, scaling.

Usage:
    python download_papers.py
"""

import asyncio
from pathlib import Path

# ---------------------------------------------------------------------------
# Curated list of 50 arXiv papers: (arxiv_id, slug)
# ---------------------------------------------------------------------------
PAPERS = [
    # ── LLM-as-Judge / Evaluation ────────────────────────────────────────
    ("2306.05685", "judging-llm-as-judge-mtbench"),          # MT-Bench / LLM-as-a-Judge
    ("2310.08491", "prometheus"),                             # Prometheus: Fine-grained Eval
    ("2405.01535", "prometheus-2"),                          # Prometheus 2
    ("2309.00267", "rlaif"),                                  # RLAIF: Scaling RLHF with AI Feedback
    ("2302.04023", "helm"),                                   # HELM: Holistic Evaluation of LMs
    ("2311.12983", "gpqa"),                                   # GPQA: Graduate-Level Q&A Benchmark
    ("2305.20050", "pandalm"),                                # PandaLM: Automatic Eval Benchmark
    ("2210.09261", "bigbench-hard"),                          # BIG-bench Hard
    ("2310.05029", "llm-cannot-self-correct"),                # LLMs Cannot Self-Correct Reasoning
    ("2406.04770", "chatbot-arena"),                          # Chatbot Arena (LMSYS)

    # ── RLHF / Alignment ─────────────────────────────────────────────────
    ("2203.02155", "instructgpt"),                            # InstructGPT
    ("2204.05862", "helpful-harmless-rlhf"),                  # Helpful, Harmless, Honest RLHF
    ("2212.08073", "constitutional-ai"),                      # Constitutional AI
    ("2305.18290", "dpo"),                                    # Direct Preference Optimization
    ("2009.01325", "learning-summarize-rlhf"),                # Learning to Summarize with RLHF
    ("2112.00114", "webgpt"),                                 # WebGPT
    ("2305.11206", "lima"),                                   # LIMA: Less Is More for Alignment
    ("2212.10560", "self-instruct"),                          # SELF-INSTRUCT

    # ── Benchmarks ───────────────────────────────────────────────────────
    ("2009.03300", "mmlu"),                                   # MMLU
    ("2107.03374", "codex-humaneval"),                        # Codex / HumanEval
    ("2303.08774", "gpt4-technical-report"),                  # GPT-4 Technical Report
    ("2206.04615", "bigbench"),                               # BIG-bench
    ("2312.11805", "gemini"),                                 # Gemini
    ("2310.06825", "mistral-7b"),                             # Mistral 7B
    ("2404.14219", "phi-3"),                                  # Phi-3 Technical Report
    ("2407.21783", "llama-3-herd"),                           # LLaMA 3 Herd of Models

    # ── Reasoning / Chain-of-Thought ─────────────────────────────────────
    ("2201.11903", "chain-of-thought-prompting"),             # Chain-of-Thought Prompting
    ("2203.11171", "self-consistency"),                       # Self-Consistency CoT
    ("2205.01068", "zero-shot-reasoners"),                    # Zero-Shot CoT (Let's Think Step by Step)
    ("2210.11610", "react"),                                  # ReAct: Synergizing Reasoning + Acting
    ("2205.10625", "least-to-most-prompting"),                # Least-to-Most Prompting
    ("2305.10601", "tree-of-thoughts"),                       # Tree of Thoughts
    ("2303.12528", "sparks-of-agi"),                          # Sparks of AGI: Early Experiments w/ GPT-4
    ("2206.07682", "emergent-abilities"),                     # Emergent Abilities of LLMs

    # ── Scaling / Foundation Models ──────────────────────────────────────
    ("2001.08361", "scaling-laws"),                           # Scaling Laws for Neural LMs
    ("2203.15556", "chinchilla"),                             # Chinchilla: Compute-Optimal Training
    ("2005.14165", "gpt-3"),                                  # GPT-3: Language Models are Few-Shot Learners
    ("2302.13971", "llama-1"),                                # LLaMA: Open & Efficient Foundation Models
    ("2307.09288", "llama-2"),                                # LLaMA 2
    ("2210.06726", "flan-t5"),                                # Scaling Instruction-Finetuned LMs (FLAN-T5)
    ("1706.03762", "attention-is-all-you-need"),              # Attention Is All You Need (Transformer)
    ("2402.09171", "gemma"),                                  # Gemma: Open Models Based on Gemini

    # ── Additional Models / Evaluation ───────────────────────────────────
    ("2404.07143", "arena-hard-auto"),                        # Arena-Hard Auto
    ("2308.07902", "wizardlm"),                               # WizardLM
    ("2303.17580", "hugginggpt"),                             # HuggingGPT
    ("2306.09212", "llm-vs-human-evaluations"),               # LLMs as Alternative to Human Evaluations
    ("2308.12966", "code-llama"),                             # Code Llama
    ("2401.04088", "mixtral-of-experts"),                     # Mixtral of Experts (MoE)
    ("2406.11697", "judging-the-judges"),                     # Judging the Judges
    ("2402.01720", "mixtral-8x22b"),                          # Mixtral 8x22B
]

OUTPUT_DIR = Path(__file__).parent / "sandbox" / "my-papers"
CONCURRENCY = 3       # simultaneous requests
DELAY_SECONDS = 1.5   # polite delay after each download (per semaphore slot)


async def _fetch_one(
    idx: int,
    total: int,
    arxiv_id: str,
    slug: str,
    crawler,
    semaphore: asyncio.Semaphore,
) -> tuple[str, bool, str]:
    """Fetch one arXiv abstract page as markdown. Returns (arxiv_id, success, message)."""
    out = OUTPUT_DIR / f"{arxiv_id}.md"
    if out.exists():
        print(f"[{idx:>2}/{total}] SKIP  {arxiv_id}  ({slug})")
        return arxiv_id, True, "skipped"

    url = f"https://arxiv.org/abs/{arxiv_id}"
    async with semaphore:
        print(f"[{idx:>2}/{total}] GET   {arxiv_id}  {slug}")
        try:
            r = await crawler.arun(url=url)

            # r.markdown is a StringCompatibleMarkdown whose Pydantic fields are
            # private — pull out the raw string with attribute fallbacks.
            md = r.markdown
            text = str(
                getattr(md, "raw_markdown", None)
                or getattr(md, "fit_markdown", None)
                or md
                or r.cleaned_html
                or r.html
                or ""
            ).strip()

            if not text:
                return arxiv_id, False, "empty content"

            out.write_text(text, encoding="utf-8")
            kb = len(text.encode()) / 1024
            print(f"[{idx:>2}/{total}] DONE  {arxiv_id}  {kb:.1f} KB  → {out.name}")
            await asyncio.sleep(DELAY_SECONDS)
            return arxiv_id, True, f"{kb:.1f} KB"

        except Exception as exc:
            print(f"[{idx:>2}/{total}] FAIL  {arxiv_id}  {exc}")
            return arxiv_id, False, str(exc)


async def main() -> None:
    from crawl4ai import AsyncWebCrawler

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    total = len(PAPERS)

    print(f"Target : {total} arXiv papers")
    print(f"Output : {OUTPUT_DIR}")
    print(f"Options: concurrency={CONCURRENCY}  delay={DELAY_SECONDS}s")
    print("-" * 60)

    semaphore = asyncio.Semaphore(CONCURRENCY)
    async with AsyncWebCrawler(verbose=False) as crawler:
        results = await asyncio.gather(*[
            _fetch_one(i + 1, total, arxiv_id, slug, crawler, semaphore)
            for i, (arxiv_id, slug) in enumerate(PAPERS)
        ])

    downloaded = [r for r in results if r[1] and r[2] != "skipped"]
    skipped    = [r for r in results if r[2] == "skipped"]
    failed     = [r for r in results if not r[1]]

    print("\n" + "=" * 60)
    print(f"Downloaded : {len(downloaded)}")
    print(f"Skipped    : {len(skipped)}  (already existed)")
    print(f"Failed     : {len(failed)}")
    if failed:
        print("\nFailed papers (check IDs or network):")
        for arxiv_id, _, msg in failed:
            print(f"  {arxiv_id}: {msg}")


if __name__ == "__main__":
    asyncio.run(main())
