---
layout: default
title: "AI Daily: 2026-07-28 (EN)"
date: 2026-07-28
lang: en
---

> From 74 items, 7 important content pieces were selected

---

1. [vLLM v0.26.0 Released: Inkling Model Support and DeepSeek-V4 Optimizations](#item-1) ⭐️ 8.0/10
2. [Anthropic&\#x27;s Position on Open-Weights AI Models](#item-2) ⭐️ 8.0/10
3. [Bun Rust Rewrite Update: Ships in Claude Code, v1.4 Delayed](#item-3) ⭐️ 8.0/10
4. [Moonshot AI Releases 2.8T-Parameter Kimi K3 Open Weights on HuggingFace](#item-4) ⭐️ 8.0/10
5. [NVIDIA Cosmos-H-Dreams: Real-Time Generative Simulation for Surgical Robotics](#item-5) ⭐️ 8.0/10
6. [Claude Shared Chats Exposed via Google Indexing](#item-6) ⭐️ 8.0/10
7. [Delhi High Court hands OpenAI a win by rejecting major Indian news agency&\#x27;s copyright injunction](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 Released: Inkling Model Support and DeepSeek-V4 Optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 was released with 411 commits from 212 contributors, introducing a full support stack for the new Inkling model family from Thinking Machines Lab—including base modeling, piecewise CUDA graphs, Hopper FA4 relative attention, MTP=1 speculative decoding, LoRA, and ModelOpt NVFP4 quantization. The release also brings significant DeepSeek-V4 performance optimizations across NVIDIA, AMD, and Intel XPU vendors, fp32 lm\_head support via a new head\_dtype parameter, and per-KV-cache-group attention backend selection. This release ensures Day-0 support for one of the largest open multimodal MoE models \(Inkling, 975B total / 41B active parameters with 1M context\) on the most widely adopted open-source inference engine, making it immediately deployable for the community. The multi-vendor DeepSeek-V4 optimizations and mature KV-cache tiering significantly improve serving economics for high-throughput, long-context workloads across heterogeneous hardware. The specialized routing kernel yields a 2.94% E2E TPOT improvement for DeepSeek-V4, while fused\_topk\_bias achieves a 1.5–2x kernel speedup; the new fp32 lm\_head via head\_dtype extends to LoRA and gets a ROCm torch.mm fast path. Attention backends can now be selected per KV-cache group, and sliding-window support is exposed as an explicit backend capability for hybrid models. KV offloading introduces object-store secondary tiers with workload identity and DP-replica-aware tiering.

github · khluu · Jul 27, 01:06

**Background**: vLLM is a high-throughput, open-source large language model serving/inference engine originally developed at UC Berkeley that has become the de facto standard for LLM deployment due to its PagedAttention memory management and continuous batching. DeepSeek-V4 is a recently released large MoE model where serving efficiency depends heavily on optimized routing, fused top-k bias, and copy elimination kernels. NVFP4 is a 4-bit floating-point format introduced with NVIDIA Blackwell GPUs that retains floating-point semantics with a shared exponent and compact mantissa, enabling higher dynamic range and more stable accuracy than INT4. FlashAttention 4 \(FA4\) is a recent attention implementation designed for Blackwell hardware using TCGEN05 tensor core instructions and tensor memory, replacing the older WGMMA path used by FA3 on Hopper.

<details><summary>References</summary>
<ul>
<li><a href="https://recipes.vllm.ai/thinkingmachines/Inkling">thinkingmachines/Inkling | vLLM Recipes</a></li>
<li><a href="https://vllm.ai/blog/2026-07-15-inkling">TML Inkling on vLLM: Day-0 Support with Optimized Performance | vLLM Blog</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>

</ul>
</details>

**Tags**: `#vllm`, `#llm-inference`, `#deepseek`, `#cuda-optimization`, `#model-serving`

---

<a id="item-2"></a>
## [Anthropic&\#x27;s Position on Open-Weights AI Models](https://www.anthropic.com/news/position-open-weights-models) ⭐️ 8.0/10

Anthropic published an official policy position stating that all sufficiently capable AI models—whether open or closed—should undergo mandatory safety testing, while claiming the company does not advocate for outright bans on open-weights releases. This policy statement from one of the leading AI labs could shape future AI regulation and influence how governments approach open model releases, potentially creating barriers that affect independent researchers and smaller competitors while reinforcing the position of well-funded frontier labs. The policy calls for mandatory safety testing prior to release, opposes bans in principle but supports restrictions on chip exports to China, and proposes enhanced export controls—measures critics argue amount to regulatory capture that protects incumbents while constraining open-source competition.

hackernews · surprisetalk · Jul 27, 22:03 · [Discussion](https://news.ycombinator.com/item?id=49076057)

**Background**: Open-weights AI models are those whose trained parameters are publicly released, allowing anyone to download, inspect, and run them locally—a practice championed by groups like Meta \(with Llama\) and increasingly OpenAI. Anthropic is known for its closed-weight, API-only model strategy \(Claude\) and for its Responsible Scaling Policy \(RSP\), a voluntary framework for managing catastrophic AI risks. The debate around open weights centers on tensions between democratizing access to powerful AI and preventing misuse, with frontier labs often arguing that safety concerns justify tighter controls on model distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/responsible-scaling-policy">Anthropic’s Responsible Scaling Policy \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/news/responsible-scaling-policy-v3">Responsible Scaling Policy Version 3.0 \ Anthropic</a></li>
<li><a href="https://allthings.how/what-is-an-open-weight-ai-model-and-how-to-use-one/">What is an Open Weight AI Model and How to Use One</a></li>

</ul>
</details>

**Discussion**: Commenters were overwhelmingly skeptical and critical, with many arguing that mandatory safety testing effectively functions as a ban on open-weights models by creating prohibitive compliance costs. Several users pointed out contradictions in Anthropic&\#x27;s position—claiming bans don&\#x27;t work while simultaneously supporting chip export restrictions to China—and accused the company of virtue signaling and protecting its commercial interests under the guise of safety. The discussion highlighted concerns about regulatory capture, who would administer such tests, and skepticism about a CEO&\#x27;s sudden concern about AI misuse.

**Tags**: `#AI policy`, `#open-source`, `#Anthropic`, `#AI safety`, `#regulation`

---

<a id="item-3"></a>
## [Bun Rust Rewrite Update: Ships in Claude Code, v1.4 Delayed](https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html) ⭐️ 8.0/10

Bun creator Jarred Sumner confirmed that the Rust rewrite of Bun has already shipped in Anthropic&\#x27;s Claude Code over a month ago without major incident, and announced that the Bun v1.4 release is delayed until a promised number of newly passing Node.js compatibility tests are achieved. This demonstrates a significant real-world production validation of Bun&\#x27;s Rust rewrite in a high-profile application, while the delayed v1.4 release signals that the team prioritizes Node.js compatibility correctness over shipping speed — a key concern for developers considering Bun for production use. The compatibility-related PRs to meet the promised test threshold are open but not yet merged, with a Bun 1.4 release tentatively planned for the following Tuesday. The rewrite has notably transitioned Bun&\#x27;s internals from the original Zig implementation to Rust.

hackernews · tomlockwood · Jul 27, 11:12 · [Discussion](https://news.ycombinator.com/item?id=49067854)

**Background**: Bun is a JavaScript runtime, package manager, and test runner designed as a drop-in replacement for Node.js, created by Jarred Sumner. It originally used Apple&\#x27;s JavaScriptCore engine for fast performance. Claude Code is Anthropic&\#x27;s agentic AI coding tool that runs in the terminal, understands codebases, and executes development tasks autonomously. The Bun project has been undergoing a major rewrite from its original Zig codebase to Rust, a transition that raised questions about development pace and the use of LLM-assisted code translation tools.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_%28software%29">Bun (software) - Wikipedia</a></li>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>
<li><a href="https://github.com/anthropics/claude-code">GitHub - anthropics/claude-code: Claude Code is an agentic ...</a></li>

</ul>
</details>

**Discussion**: Community sentiment is cautiously optimistic. Commenters like SquareWheel caution against judging development velocity by commit counts during a major refactor, noting the team is still learning Rust and likely focused on removing unsafe code. User benjiro29 argues that LLM-translated code may produce a working product but fails at the deeper work of integration, bug-fixing, and UI polish. Bendmorris pointed to a parallel Zig-based project \(buz\) that claims to achieve Bun&\#x27;s original goals by fixing issues in the original codebase, suggesting the rewrite may not have been necessary.

**Tags**: `#bun`, `#rust`, `#javascript-runtime`, `#llm-assisted-development`, `#software-rewrite`

---

<a id="item-4"></a>
## [Moonshot AI Releases 2.8T-Parameter Kimi K3 Open Weights on HuggingFace](https://huggingface.co/moonshotai/Kimi-K3) ⭐️ 8.0/10

Moonshot AI has released the full open weights for Kimi K3, a 2.8-trillion-parameter Mixture-of-Experts language model, on HuggingFace under a Modified MIT license. The model features native MXFP4 quantization, a one-million-token context window, native image input, and architecture components including Kimi Delta Attention, Attention Residuals, and Stable LatentMoE. This is the largest open-weight model released to date, opening the door for startups to fine-tune frontier-class weights on their own data and retain IP sovereignty. However, extreme hosting requirements \(roughly 1.5 TB of VRAM in MXFP4, with realistic deployments needing 16x B200-class cards\) mean most independent users will consume the model through third-party APIs rather than self-host. Native MXFP4 quantization puts inference at ~1.5 TB VRAM, just at the edge of 8x B200 setups but realistically requiring 16x cards for context and throughput optimization. The Modified MIT license includes a Model-as-a-Service clause: any licensee earning over $20M in a 12-month period must negotiate a separate commercial agreement with Moonshot AI before offering the model commercially.

hackernews · nateb2022 · Jul 27, 06:18 · [Discussion](https://news.ycombinator.com/item?id=49065752)

**Background**: Open-weight models release trained model parameters under a license, allowing external use and fine-tuning, but typically withhold training data and code, distinguishing them from fully open-source software. Mixture-of-Experts \(MoE\) architectures activate only a subset of parameters per token, enabling very large total parameter counts without proportional compute cost per inference. MXFP4 is a 4-bit micro-scaling floating-point format designed by NVIDIA to compress model weights and activations, roughly halving memory requirements versus FP8 with minimal accuracy loss.

<details><summary>References</summary>
<ul>
<li><a href="https://www.visionstory.ai/models/kimi-k3">Kimi K3 Model: Architecture, Context Window and Capabilities</a></li>
<li><a href="https://graphify.net/ai-coding/llms/kimi-k3/">Kimi K3: Architecture, Benchmarks, Pricing, and Open Weights</a></li>

</ul>
</details>

**Discussion**: Commenters split into several camps. Pricing-focused users eagerly await third-party $/MTok rates for 3T-class serving, with Fireworks already listing the model at $3.00/M uncached input and $15.00/M output. Customization advocates see fine-tuning and IP sovereignty as the real win for startups. Hardware enthusiasts lament the lack of prosumer GPUs in the 180-250W range with 128-256 GB VRAM, while licensing analysts flag the $20M revenue trigger that forces large Model-as-a-Service operators back to the negotiation table.

**Tags**: `#Kimi-K3`, `#open-source-llm`, `#large-language-models`, `#Moonshot-AI`, `#model-release`

---

<a id="item-5"></a>
## [NVIDIA Cosmos-H-Dreams: Real-Time Generative Simulation for Surgical Robotics](https://huggingface.co/blog/nvidia/cosmos-h-dreams) ⭐️ 8.0/10

NVIDIA has introduced Cosmos-H-Dreams, a new framework on the Cosmos platform that enables real-time, photorealistic generative simulation specifically designed for surgical robotics. The system creates interactive virtual environments that can be used for both training and evaluation of robotic surgical systems. This release bridges the rapidly advancing field of generative world models with a high-stakes application domain—surgical robotics—where simulation-based training is critical for safety and skill development. It signals NVIDIA&\#x27;s strategy to extend its Physical AI stack beyond autonomous vehicles and industrial robots into healthcare, potentially accelerating sim-to-real transfer for medical robots. Cosmos-H-Dreams leverages NVIDIA&\#x27;s Cosmos world foundation models \(WFMs\), which serve as internal simulators of environment dynamics and support forward and counterfactual rollouts for decision making. The framework targets embodied AI agents that must perceive, act, and anticipate how actions reshape future world states—a particularly demanding requirement in surgical contexts where tissue deformation and tool interaction are highly dynamic.

rss · Hugging Face · Jul 27, 09:32

**Background**: World models are generative AI systems that learn the dynamics of physical environments, allowing robots and AI agents to simulate &\#x27;what-if&\#x27; scenarios before acting in the real world. NVIDIA Cosmos is a platform purpose-built for Physical AI, offering world foundation models, tokenizers, guardrails, and accelerated data pipelines to support development of autonomous vehicles, robots, and AI agents. In surgical robotics specifically, high-fidelity simulation has long been used to train surgeons and validate robotic systems without risk to patients, but traditional simulators rely on hand-crafted graphics rather than generative models that can react dynamically to novel actions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/ai/cosmos/">Physical AI with World Foundation Models | NVIDIA Cosmos</a></li>
<li><a href="https://docs.nvidia.com/cosmos/index.html">NVIDIA Cosmos - NVIDIA Docs</a></li>
<li><a href="https://arxiv.org/abs/2510.16732">[2510.16732] A Comprehensive Survey on World Models for ... Top Stories News about Robotics, Robot, Data collection News about Robotics, Awe, Embodied cognition Also in the news Embodied AI 2026: From Robot Foundation Models to Industrial ... Frontiers | A review of embodied intelligence systems: a ... A Survey of Embodied World Models A Comprehensive Survey on World Models for Embodied AI A Comprehensive Survey on World Models for Embodied AI</a></li>

</ul>
</details>

**Tags**: `#nvidia`, `#surgical-robotics`, `#generative-simulation`, `#world-models`, `#embodied-ai`

---

<a id="item-6"></a>
## [Claude Shared Chats Exposed via Google Indexing](https://techcrunch.com/2026/07/27/psa-your-claude-shared-chats-and-artifacts-may-have-ended-up-on-google/) ⭐️ 8.0/10

Claude&\#x27;s &\#x27;share chat&\#x27; feature appears to have caused shared conversations and Artifacts to be indexed by Google Search, making private user data potentially discoverable to anyone searching online. This is a significant privacy incident affecting Claude users who believed their shared links were restricted to those with the URL, but which may now be broadly searchable. It highlights ongoing risks around how AI platforms handle shareable URLs and search engine indexing. The exposure appears tied specifically to the &\#x27;share chat&\#x27; feature that generates viewable URLs for conversations and Artifacts, with Google&\#x27;s crawler indexing these HTML links despite no explicit opt-in from users. Artifacts on Claude span Free, Pro, Max, Team, and Enterprise plans, broadening the affected user base.

rss · TechCrunch AI · Jul 27, 20:19

**Background**: Claude&\#x27;s &\#x27;share chat&\#x27; feature lets users generate shareable URLs so others can view a conversation or Artifact directly. Artifacts are a Claude feature that turns chat responses into standalone apps, documents, or visualizations that can be viewed and interacted with. Google&\#x27;s search crawler \(Googlebot\) follows HTML links across the web and adds the discovered pages to its search index, meaning any public-facing URL can become searchable unless site owners add protective headers like noindex tags.

<details><summary>References</summary>
<ul>
<li><a href="https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them">What are artifacts and how do I use them? - Anthropic</a></li>
<li><a href="https://developers.google.com/search/docs/crawling-indexing/links-crawlable">SEO Link Best Practices for Google | Google Search Central | Documentation | Google for Developers</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#security`, `#claude`, `#anthropic`, `#data-exposure`

---

<a id="item-7"></a>
## [Delhi High Court hands OpenAI a win by rejecting major Indian news agency&\#x27;s copyright injunction](https://the-decoder.com/delhi-high-court-hands-openai-a-win-by-rejecting-major-indian-news-agencys-copyright-injunction/) ⭐️ 8.0/10

The Delhi High Court rejected ANI&\#x27;s copyright injunction against OpenAI, marking the first time a court has classified AI training as private use, though the main trial is still pending.

rss · The Decoder · Jul 27, 17:55

**Tags**: `#AI`, `#copyright`, `#OpenAI`, `#legal`, `#India`

---