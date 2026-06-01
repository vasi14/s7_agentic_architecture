# S7 Agentic Architecture

This workspace has two main parts:

- [llm_gatewayV7/README.md](llm_gatewayV7/README.md): an LLM gateway that exposes chat and embedding endpoints, handles provider routing and failover, and keeps the agent-facing API stable while adding V7 embedding support.
- [S7code/](S7code): the agent runtime that coordinates perception, decision, action, memory, MCP tools, vector indexing, persisted state, and logged evaluation runs.

## Folder Overview

### llm_gatewayV7

The [llm_gatewayV7](llm_gatewayV7) folder contains the standalone gateway service used by the agent. It wraps multiple model providers behind a single API, adds routing and fallback behavior, and exposes embedding support used for FAISS-backed retrieval workflows.

### S7code

The [S7code](S7code) folder contains the core agent implementation. It includes the agent loop, tool server integration, memory and artifact handling, vector search, evaluation helpers, and saved outputs from running the assignment-style queries.

## Query Set Overview

The full prompt set is documented in [S7code/helper/queries.md](S7code/helper/queries.md). It mixes web retrieval, multi-step planning, durable memory, reminder creation, document indexing, semantic retrieval, and cross-document synthesis so the agent can be evaluated on both tool use and retrieval quality.

## Query Result Logs

The [S7code/results](S7code/results) folder contains execution logs for each query in the evaluation set.

- [query_A.log](S7code/results/query_A.log): fetches Claude Shannon's page and extracts birth date, death date, and three core information-theory contributions.
- [query_B.log](S7code/results/query_B.log): combines Tokyo activity search with Saturday weather to recommend the best family-friendly outing.
- [query_C.log](S7code/results/query_C.log): stores a birthday in memory, creates reminder artifacts, and verifies the remembered date in a follow-up query.
- [query_D.log](S7code/results/query_D.log): searches top asyncio best-practice sources and synthesizes their shared advice into a short list.
- [query_E.log](S7code/results/query_E.log): indexes a single paper and summarizes the Transformer's key contributions from that document.
- [query_F.log](S7code/results/query_F.log): indexes the full `papers/` set, confirms chunk counts, and then answers a follow-up retrieval question about chain-of-thought reasoning.
- [query_G.log](S7code/results/query_G.log): tests semantic recall by asking about the credit assignment problem across indexed papers and records the system's limitation on that topic.
- [query_H.log](S7code/results/query_H.log): compares ReAct with Chain-of-Thought and explains how each treats intermediate reasoning.
- [query_I.log](S7code/results/query_I.log): probes whether the indexed corpus supports claims about reducing human annotation costs in alignment workflows.
- [query_J.log](S7code/results/query_J.log): summarizes strategies the retrieved papers associate with smaller models outperforming larger ones.
- [query_K.log](S7code/results/query_K.log): synthesizes prompting strategies for stronger reasoning, including CoT, standard few-shot prompting, and interactive agentic reasoning.
- [query_L.log](S7code/results/query_L.log): summarizes what the indexed papers say about scale, emergent capabilities, and compute budget allocation.
- [query_M.log](S7code/results/query_M.log): checks the corpus for methods that reduce manual labeling in helpful-and-harmless training and records the current retrieval gap.

## Additional Notes

- [S7code/results.md](S7code/results.md) is a separate transcript-style summary of several manual runs.
- [S7code/helper/indexing_results.md](S7code/helper/indexing_results.md) captures extra indexing experiments over the larger `my-papers/` collection.

## My-Papers Corpus

The [S7code/sandbox/my-papers](S7code/sandbox/my-papers) folder is a larger research-paper corpus used for broader retrieval and synthesis tests. It mainly contains four kinds of documents:

- architecture and model-family papers, such as Transformer, GPT, LLaMA, Gemma, Gemini, Mistral, Mixtral, Phi-3, and Code Llama;
- reasoning and prompting papers, such as Chain-of-Thought, Tree-of-Thoughts, Self-Consistency, Least-to-Most, ReAct, and Zero-Shot Reasoners;
- alignment and instruction-tuning papers, such as InstructGPT, DPO, RLAIF, Constitutional AI, Self-Instruct, LIMA, WizardLM, and helpful-harmless RLHF;
- evaluation, scaling, and capability-analysis papers, such as MMLU, GPQA, BIG-Bench, HELM, Arena-Hard, Prometheus, Scaling Laws, Emergent Abilities, and LLM-as-a-judge studies.

The indexing workflow and retrieval experiments for this larger corpus are documented in [S7code/helper/indexing_results.md](S7code/helper/indexing_results.md), which serves as the companion log for indexing `my-papers/` and querying the resulting vector store.
