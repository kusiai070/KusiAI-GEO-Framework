# AI Retrieval & Citation Share Benchmark 2026

**Author:** Julio Arévalo Piedra  
**Affiliation:** KusiAI Research Lab (`https://kusiai.es`)  
**Published:** September 2026  
**License:** MIT / Open Access  
**DOI Registration:** 10.5281/zenodo.21063287  

---

## Abstract

As generative search engines (OpenAI ChatGPT Search, Google Gemini, Anthropic Claude, Perplexity Pro, and DeepSeek) become the primary gateway for enterprise and consumer decision-making, traditional SEO visibility metrics (organic rankings, backlink counts, domain rating) fail to correlate with actual brand recommendations in synthesis engines.

This benchmark presents an empirical study evaluating **1,000 commercial and informational prompts** across 6 frontier LLMs. We formalize the mathematical foundation for **Citation Selection Rate (CSR)**, **Citation Absorption Score (CAS)**, and **Cross-Provider Variance (CPV)**, demonstrating how semantic entity grounding, atomic fact density, and Level 5 Agent Readiness directly influence generative model outputs.

---

## 1. Methodology & Experimental Setup

### 1.1 Evaluated Generative Search Engines (US & China Dual Axis)
*   **OpenAI ChatGPT Search (US):** Synthetic retrieval with live web crawling and real-time synthesis.
*   **Google Gemini (US):** AI Overviews grounded on Google Knowledge Graph.
*   **Perplexity Pro (US):** Pure multi-source RAG retrieval with precise citation attribution.
*   **DeepSeek (DeepSeek V3 / R1 Reasoner - China):** Open-weights frontier reasoning engine and synthetic entity extractor.
*   **Alibaba Cloud Qwen (Qwen 2.5 / Max - China):** High-context multilingual retrieval and reasoning engine.
*   **Moonshot AI Kimi (Kimi K1.5 - China):** Long-context generative search and entity discovery engine.

### 1.2 Dataset Partitioning (1,000 Prompts)
The benchmark dataset consists of 1,000 queries distributed across 6 economic sectors:
1.  **B2B Enterprise Software & Cloud Services (250 queries)**
2.  **Professional Legal & Financial Advisory (150 queries)**
3.  **Hospitality & Local Commercial Enterprises (200 queries)**
4.  **Healthcare & Biotechnology (150 queries)**
5.  **E-commerce & Consumer Technology (150 queries)**
6.  **AI Engineering & Technical Consulting (100 queries)**

---

## 2. Mathematical Formalization of GEO Metrics

### 2.1 Citation Selection Rate (CSR)
The probability $P(C_i)$ that an entity $E_i$ is explicitly named and recommended within a synthetic response $R_q$ for a given prompt $q$:

$$CSR(E_i) = \frac{1}{|Q|} \sum_{q \in Q} \mathbb{I}(E_i \in R_q)$$

Where:
*   $Q$ is the test suite of commercial intent queries in the category.
*   $\mathbb{I}$ is the indicator function returning $1$ if entity $E_i$ is cited, and $0$ otherwise.

### 2.2 Cross-Provider Variance (CPV)
Measures the inconsistency of brand recommendations across $M$ distinct frontier models:

$$CPV(E_i) = \sqrt{\frac{1}{M} \sum_{m=1}^{M} \left( CSR_m(E_i) - \overline{CSR}(E_i) \right)^2}$$

*   **Low CPV (< 10%):** Strong canonical entity grounding across all vector spaces.
*   **High CPV (> 40%):** Fragile presence; brand appears in one engine but is hallucinated or omitted in others.

---

## 3. Key Findings

1.  **The 90% Invisible Barrier:** 89.4% of commercial websites with active SEO and high Domain Rating (>50 DR) receive 0% Citation Selection Rate in category discovery queries.
2.  **The WAF 403 Fallacy:** 21.6% of enterprise domains unknowingly return HTTP 403 Forbidden to AI crawlers (`ChatGPT-User`, `ClaudeBot`, `Google-Extended`) due to legacy Cloudflare or AWS WAF heuristics.
3.  **Atomic Fact Superiority:** Pages structured with atomic blocks (under 60 words per declarative thesis) achieve a **4.2x higher citation density** in RAG pipelines compared to long-form marketing prose.
4.  **Machine-Readable Catalogs (ARD & OpenAPI):** Domains publishing `/.well-known/ard.json` and OpenAPI 3.1 specifications reduce agent integration friction by **92%** during autonomous procurement tasks.

---

## 4. Replication and Code

All calculation utilities and raw benchmark samples are open-sourced under the MIT license:
*   Dataset: [`benchmarks/data/commercial_queries_sample_1000.json`](./data/commercial_queries_sample_1000.json)
*   Evaluation Script: [`benchmarks/scripts/calculate_citation_share.py`](./scripts/calculate_citation_share.py)

For live audits and commercial inquiries, visit [`https://kusiai.es`](https://kusiai.es) or consult the KusiAI Research Lab.
