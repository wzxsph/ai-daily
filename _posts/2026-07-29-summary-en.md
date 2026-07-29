---
layout: default
title: "AI Daily: 2026-07-29 (EN)"
date: 2026-07-29
lang: en
---

> From 80 items, 8 important content pieces were selected

---

1. [Anthropic says its Mythos model found vulnerabilities in cryptographic algorithms that secure the internet](#item-1) ⭐️ 9.0/10
2. [modelcontextprotocol/python-sdk released v2.0.0](#item-2) ⭐️ 8.0/10
3. [Kimi K3 Architecture: Eliminating RoPE in Favor of NoPE](#item-3) ⭐️ 8.0/10
4. [Deep Dive into Zig&\#x27;s Incremental Compilation Internals](#item-4) ⭐️ 8.0/10
5. [Kimi Linear: An Expressive, Efficient Attention Architecture](#item-5) ⭐️ 8.0/10
6. [Scientific computing in the age of agentic AI](#item-6) ⭐️ 8.0/10
7. [Nvidia invests in Ilya Sutskever&\#x27;s AI lab, shifting SSI away from Google chips](#item-7) ⭐️ 8.0/10
8. [PNAS Study: Over 51% of Academic Papers Show LLM Influence](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic says its Mythos model found vulnerabilities in cryptographic algorithms that secure the internet](https://the-decoder.com/anthropic-says-its-mythos-model-found-vulnerabilities-in-cryptographic-algorithms-that-secure-the-internet/) ⭐️ 9.0/10

Anthropic claims its Claude Mythos model discovered vulnerabilities in cryptographic algorithms, including a post-quantum signature scheme \(HAWK\), that human experts had missed for over two years.

rss · The Decoder · Jul 28, 19:12

**Tags**: `#AI`, `#cryptography`, `#cybersecurity`, `#Anthropic`, `#post-quantum`

---

<a id="item-2"></a>
## [modelcontextprotocol/python-sdk released v2.0.0](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0) ⭐️ 8.0/10

MCP Python SDK v2.0.0 stable release introduces the 2026-07-28 protocol revision with documentation rewrite, migration guide, and places v1 in maintenance mode.

github · maxisbey · Jul 28, 13:41

**Tags**: `#MCP`, `#Python-SDK`, `#Model-Context-Protocol`, `#release`, `#developer-tools`

---

<a id="item-3"></a>
## [Kimi K3 Architecture: Eliminating RoPE in Favor of NoPE](https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html) ⭐️ 8.0/10

Sebastian Raschka published a detailed architectural analysis of Moonshot AI&\#x27;s Kimi K3, revealing that the model entirely eliminates Rotary Position Embeddings \(RoPE\) in favor of NoPE \(No Positional Embeddings\) throughout the architecture. The analysis highlights several novel design choices that distinguish Kimi K3 from typical Western frontier model architectures. The complete abandonment of RoPE is a radical departure from a near-universal convention in modern LLMs, challenging the assumption that explicit positional encoding is necessary for transformer-based language models. This positions Kimi K3 as a genuinely innovative model rather than a derivative of Western counterparts, with implications for the broader research community rethinking positional encoding design. The most striking technical detail is the use of NoPE everywhere, removing all RoPE layers from the model. Other architectural innovations are discussed in Raschka&\#x27;s full blog post, which provides the level of detail typically expected from peer-reviewed architecture reports rather than informal technical write-ups.

hackernews · ModelForge · Jul 28, 15:48 · [Discussion](https://news.ycombinator.com/item?id=49085698)

**Background**: Large language models \(LLMs\) built on the Transformer architecture need some way to understand the order of tokens in a sequence, since the self-attention mechanism is inherently permutation-invariant. RoPE \(Rotary Position Embedding\), introduced in the RoFormer paper \(2021\), has become the dominant solution, encoding position by rotating query and key vectors. NoPE \(No Positional Embeddings\) is a more radical alternative that removes explicit positional encoding entirely, relying instead on the causal attention mask and the model&\#x27;s learned representations to implicitly capture token order. Prior work such as SmolLM3 has shown NoPE can work in selective parts of the architecture, but applying it universally — as Kimi K3 reportedly does — is unusual.

<details><summary>References</summary>
<ul>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/nope/">No Positional Embeddings (NoPE) | Sebastian Raschka, PhD</a></li>
<li><a href="https://arxiv.org/abs/2104.09864">RoFormer: Enhanced Transformer with Rotary Position Embedding</a></li>
<li><a href="https://newsletter.theaiedge.io/p/all-about-the-modern-positional-encodings">All About The Modern Positional Encodings In LLMs</a></li>

</ul>
</details>

**Discussion**: Community sentiment is strongly positive and impressed by Kimi K3. Users debated the counter-intuitive nature of NoPE, with one commenter expressing astonishment that a model can function without any explicit position information. Others raised concerns about the reproducibility of Chinese model architectures, comparing published specs to formats like PDF/DWG/PSD where crucial implementation details remain undocumented. One user reported switching to Kimi K3 as their daily driver, finding it comparable to Claude Opus 4.7/4.8, while another noted that Kimi&\#x27;s novel approaches contradict Western lab narratives that dismiss it as merely a product of distillation attacks.

**Tags**: `#kimik3`, `#llm-architecture`, `#moonshot-ai`, `#machine-learning`, `#research-analysis`

---

<a id="item-4"></a>
## [Deep Dive into Zig&\#x27;s Incremental Compilation Internals](https://mlugg.co.uk/posts/incremental-compilation-internals/) ⭐️ 8.0/10

A detailed blog post by mlugg explores how Zig&\#x27;s compiler implements incremental compilation, focusing on how it caches ZIR \(Zig Intermediate Representation\) per source file and only re-analyzes changed units. The article compares Zig&\#x27;s design trade-offs with Rust&\#x27;s incremental compilation approach. Incremental compilation is critical for developer productivity, especially in large codebases where full rebuilds can take minutes. Zig&\#x27;s design choices — making semantic analysis straightforward to cache — offer valuable lessons for other language implementers and highlight why Rust&\#x27;s complex type system makes incremental compilation significantly harder. Zig tracks four key per-declaration properties — layout, type, value, and body — which make dependency tracking much simpler than Rust&\#x27;s trait-based dependency graph. The article notes that incremental compilation for non-binary outputs \(e.g., \`zig build check\`\) was merged in August 2024 via \`--watch -fincremental\`, but full binary-level incremental linking support is still evolving.

hackernews · garyhtou · Jul 28, 15:46 · [Discussion](https://news.ycombinator.com/item?id=49085666)

**Background**: Incremental compilation is a technique where a compiler reuses analysis results from previous compilations, only redoing work for portions of code that have changed. Semantic analysis is the phase where the compiler checks types, scopes, and meaning of the program after parsing. Zig is a systems programming language designed for fast compilation, with a build system and C/C++ compiler \(\`zig cc\`\) bundled in its toolchain. Rust, by contrast, has a more sophisticated but slower incremental compilation system due to its complex type system involving traits, lifetimes, and monomorphization.

<details><summary>References</summary>
<ul>
<li><a href="https://mlugg.co.uk/posts/incremental-compilation-internals/">Inside Zig&#x27;s Incremental Compilation | mlugg.co.uk</a></li>
<li><a href="https://deepwiki.com/ziglang/zig/3.3-incremental-compilation">Incremental Compilation | ziglang/zig | DeepWiki</a></li>
<li><a href="https://www.reddit.com/r/Zig/comments/1ev8mvs/incremental_compilation_merged/">r/Zig on Reddit: Incremental compilation merged</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely positive and technical. steveklabnik praised Zig&\#x27;s toolchain work while noting reservations about memory safety. afdbcreid, a rust-analyzer team member, attributed Rust&\#x27;s slower compilation primarily to language design rather than compiler implementation. thefaux questioned why Zig produces a single large debug binary instead of many smaller shared libraries, and patrec raised a sharp question about how the model handles dependencies on the body of runtime functions in the context of comptime evaluation.

**Tags**: `#zig`, `#compilers`, `#incremental-compilation`, `#programming-languages`, `#systems-programming`

---

<a id="item-5"></a>
## [Kimi Linear: An Expressive, Efficient Attention Architecture](https://arxiv.org/abs/2510.26692) ⭐️ 8.0/10

Moonshot AI has introduced Kimi Linear, a new attention architecture featuring Kimi Delta Attention \(KDA\), which refines the gated delta rule with fine-grained gating. The team pretrained a 3B-activated/48B-total parameter model using a layerwise hybrid of KDA and Multi-Head Latent Attention \(MLA\) in a 3:1 ratio, and open-sourced the KDA kernel, vLLM implementations, and pretrained checkpoints. Kimi Linear reduces KV cache usage by up to 75% and achieves up to 6× decoding throughput at 1M context length, all while outperforming full MLA across evaluated tasks with identical training recipes. This makes it a practical drop-in replacement for full attention, potentially reshaping how large language models handle long-context inference efficiently. The architecture uses a 3:1 KDA-to-MLA layer ratio, meaning every fourth layer uses full MLA while the other three use the more efficient KDA. This hybrid design balances memory efficiency with the global context modeling capability that pure linear attention tends to lose. The open-source release includes both the low-level kernel and a vLLM integration for easy deployment.

hackernews · ronfriedhaber · Jul 28, 10:52 · [Discussion](https://news.ycombinator.com/item?id=49082022)

**Background**: Standard transformer attention scales quadratically with sequence length and requires storing a KV cache that grows linearly with context, creating major bottlenecks for long-context inference. Linear attention mechanisms address this by computing attention in a recurrent or kernel-based fashion, achieving O\(N\) complexity, but they historically sacrifice expressiveness compared to softmax attention. Hybrid architectures like Kimi Linear attempt to combine the efficiency of linear attention for most layers with the expressiveness of full attention on a subset of layers. MLA \(Multi-Head Latent Attention\), introduced with DeepSeek-V2, compresses the KV cache into a low-rank latent space and has become a popular efficiency technique in recent open-weight models.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://github.com/MoonshotAI/Kimi-Linear">GitHub - MoonshotAI/Kimi-Linear · GitHub</a></li>
<li><a href="https://vizuara.substack.com/p/kimi-linear-an-expressive-efficient">Kimi-Linear : An Expressive, Efficient Attention Architecture</a></li>

</ul>
</details>

**Discussion**: Commenters highlight that Kimi Linear serves as the foundation for the larger Kimi K3 model, which scales it up further and adds native vision and RL improvements. One user noted that Gated DeltaNet 2 appears to be a natural evolution of KDA with even better expressiveness in their internal testing. The open-source release of kernels and checkpoints was widely praised, and some skeptics were reminded that Kimi&\#x27;s strong results are genuine rather than the product of distillation attacks.

**Tags**: `#attention-mechanisms`, `#LLM-architecture`, `#Kimi`, `#efficient-inference`, `#open-source`

---

<a id="item-6"></a>
## [Scientific computing in the age of agentic AI](https://openai.com/index/scientific-computing-agentic-ai) ⭐️ 8.0/10

OpenAI&\#x27;s field report describes how scientists are using AI coding agents to modernize scientific computing and accelerate discovery in fields like genomics.

rss · OpenAI News · Jul 28, 17:00

**Tags**: `#agentic AI`, `#scientific computing`, `#coding agents`, `#AI for science`, `#OpenAI`

---

<a id="item-7"></a>
## [Nvidia invests in Ilya Sutskever&\#x27;s AI lab, shifting SSI away from Google chips](https://the-decoder.com/nvidia-invests-in-ilya-sutskevers-ai-lab-shifting-ssi-away-from-google-chips/) ⭐️ 8.0/10

Nvidia makes a &\#x27;substantial&\#x27; investment in Ilya Sutskever&\#x27;s Safe Superintelligence \(SSI\), with the AI lab shifting its chip strategy away from Google TPUs toward Nvidia hardware.

rss · The Decoder · Jul 28, 13:06

**Tags**: `#Nvidia`, `#Safe Superintelligence`, `#Ilya Sutskever`, `#AI Infrastructure`, `#GPU/TPU Competition`

---

<a id="item-8"></a>
## [PNAS Study: Over 51% of Academic Papers Show LLM Influence](https://www.reddit.com/r/MachineLearning/comments/1v93q78/pnas_over_half_of_all_academic_articles_now_show/) ⭐️ 8.0/10

A PNAS study analyzed 7.3 million academic articles and found that by 2025, over 51% of published papers show some degree of LLM influence, detected through characteristic word patterns associated with LLM-generated writing. The study reveals that LLM adoption skews toward lower-prestige and non-English-speaking institutions. This is the largest empirical study on LLM penetration in academic publishing to date, providing the most authoritative quantitative benchmark of how LLMs have reshaped scientific writing. The inequality dimension raises significant policy concerns, as unequal adoption across institutions could exacerbate existing disparities in global research output. The detection method relies on identifying specific words and phrases that are statistically overrepresented in LLM-generated text. The study found that LLM edits tend to shift writing away from first-person narratives toward more impersonal, academic styles, with this effect being more pronounced when the LLM is prompted to complete or polish existing text.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Jul 28, 16:38

**Background**: LLMs like GPT-4 have become widely accessible tools that can generate, edit, and refine text, including academic prose. Since their popularization in late 2022, researchers have debated the extent to which these tools influence scholarly publishing, with concerns about homogenization of writing styles and the integrity of the scientific record. PNAS \(Proceedings of the National Academy of Sciences\) is one of the most prestigious multidisciplinary scientific journals, with an impact factor exceeding 100, making it a high-credibility venue for publishing studies with broad implications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/muhammed-erkan-karabekmez-3948041a_the-diffusion-of-large-language-models-in-activity-7467652152929247232-mRqf">PNAS Study: LLM Influence on Academic Writing by 2025 | LinkedIn</a></li>
<li><a href="https://abdulhaim.github.io/documents/LLM_Homogenization_Project.pdf">How LLMs Distort Our Written Language</a></li>
<li><a href="https://www.pnas.org/">pnas .org</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#academic-publishing`, `#research-policy`, `#AI-adoption`, `#PNAS`

---