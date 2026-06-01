### Query A. Shannon Wikipedia (artifact attach, carryover)

Fetch https://en.wikipedia.org/wiki/Claude_Shannon and tell me his birth date, death date, and three key contributions to information theory.

### Query B. Tokyo activities and weather (multi-goal, memory carryover, carryover)

Find 3 family-friendly things to do in Tokyo this weekend.
Check Saturday's weather forecast there and tell me which one
is most appropriate.

### Query C. Mom's birthday (durable memory across runs, carryover)

Run 1: My mom's birthday is 15 May 2026. Remember that and create reminders for two weeks before and on the day.
Run 2: When is mom's birthday?

### Query D. Asyncio research (multi-source synthesis, carryover)

Search for "Python asyncio best practices", read the top 3 results, and give me a short numbered list of the advice they agree on.

### Query E. Single-document index and extract
Index the file papers/attention.md and tell me what the three key contributions of the Transformer architecture are according to this paper.

### Query F. Cross-run document recall (FAISS persistence)

Run 1: Index every .md file under papers/. Confirm how many chunks were indexed in total.
Run 2 (fresh process, persisted state): Across the papers I have indexed, what do they say about chain-of-thought reasoning?

### Query G. Synonym recall (vector beats keyword)

Across these papers, how do they handle the credit assignment
problem?

### Query H. Cross-document synthesis

Compare how the ReAct paper and the Chain-of-Thought paper differ in their treatment of intermediate reasoning.

---

## Assignment Queries (Index-Required Evaluation Set)

The following five queries are designed to test the FAISS vector index capabilities of agent7.py. Each query requires the index to answer correctly and would fail without it. Queries marked with [SEMANTIC] require semantic recall where query words do not appear in the answer chunks.

### Query I. [SEMANTIC] Reducing labeling costs in alignment

What techniques do the indexed papers propose for reducing human annotation costs when aligning language models with preferences?

*Rationale: The query uses "labeling costs" and "annotation costs" which may not appear verbatim. The answer requires finding papers discussing DPO (eliminates reward model training), RLAIF (uses AI feedback instead of human labels), Self-Instruct (bootstraps training data from model generations), and Constitutional AI (uses AI self-critique). Without the index, keyword search for "annotation costs" would fail.*

### Query J. [SEMANTIC] Making smaller models outperform larger ones

According to the indexed papers, what strategies allow smaller parameter models to outperform much larger ones?

*Rationale: The query asks about "smaller models outperforming larger ones" but papers discuss this as "1.3B InstructGPT preferred over 175B GPT-3" (InstructGPT) and "70B Chinchilla outperforms 280B Gopher" (Chinchilla). Semantic similarity is needed to match these concepts since exact phrase won't match.*

### Query K. Cross-document synthesis on reasoning enhancements

Across the indexed papers, what are the different prompting strategies proposed to enhance reasoning capabilities in large language models, and how do they differ in their approach?

*Rationale: Requires synthesizing information from Chain-of-Thought (intermediate reasoning steps), Tree-of-Thoughts (branching exploration with backtracking), Self-Consistency (sampling multiple paths and voting), Least-to-Most (decomposition into subproblems), and Zero-Shot Reasoners ("Let's think step by step"). Without the index, cannot retrieve all relevant chunks.*

### Query L. Emergent capabilities and scaling relationships

What do the indexed papers reveal about the relationship between model scale and capability emergence, and what are the implications for compute budget allocation?

*Rationale: Requires cross-referencing Emergent Abilities (unpredictable capabilities appearing at scale), Scaling Laws (power-law relationships), and Chinchilla (compute-optimal training). The connection between emergence and optimal scaling requires semantic understanding across multiple documents.*

### Query M. [SEMANTIC] Automated supervision approaches

What methods do the papers describe for training models to be helpful and harmless without requiring humans to manually label each problematic output?

*Rationale: Uses "automated supervision" and "problematic output" while papers discuss this as "RLAIF" (AI feedback), "Constitutional AI" (self-critique and revision), "self-improvement" without external inputs. Requires semantic matching since the query phrasing differs from paper terminology.*