---
layout: default
title: "AI Daily: 2026-07-27 (EN)"
date: 2026-07-27
lang: en
---

> From 39 items, 2 important content pieces were selected

---

1. [vLLM v0.26.0 Released: DeepSeek-V4 Optimization and Inkling Model Support](#item-1) ⭐️ 8.0/10
2. [Claude Opus 5 Nearly Quadruples Record on ARC-AGI-3 Benchmark](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 Released: DeepSeek-V4 Optimization and Inkling Model Support](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 has been released with 411 commits from 212 contributors \(61 new\), introducing support for the new Inkling model family \(including CUDA graph, speculative decoding, LoRA, and NVFP4 quantization\) and substantial DeepSeek-V4 performance optimizations across CUDA, ROCm, and XPU platforms, yielding 1.8–2.94% end-to-end TPOT improvements and up to 2x kernel speedups. 作为最广泛采用的开源大语言模型推理引擎之一，vLLM 的性能提升直接转化为生产部署中更低的推理成本和更高的吞吐量，尤其是对越来越流行的 DeepSeek 风格 MoE 模型而言。本次跨厂商（NVIDIA、AMD、Intel）的优化对异构 GPU 环境具有重要意义。 Notable features include a new \`head\_dtype\` parameter enabling fp32 \`lm\_head\` for generation models \(improving numerical accuracy\), per-KV-cache-group attention backend selection for hybrid models, and matured KV offloading with tiered secondary storage. The Rust frontend also gains native multimodal video/audio support and a \`vllm-bench\` port.

github · khluu · Jul 27, 01:06

**Background**: vLLM is a high-throughput, memory-efficient inference and serving engine for Large Language Models, originally developed at UC Berkeley and now one of the most active open-source projects in the LLM serving ecosystem. Speculative decoding \(including MTP, or Multi-Token Prediction\) is a technique where a smaller draft model predicts multiple tokens that the larger target model verifies in parallel, effectively boosting tokens-per-second. NVFP4 is a 4-bit floating-point quantization format introduced with NVIDIA&\#x27;s Blackwell GPU architecture that reduces memory footprint while maintaining accuracy. DeepSeek-V4-style MoE \(Mixture of Experts\) models route each token to a subset of experts, requiring specialized kernels for efficient routing.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm">vllm -project/ vllm : A high - throughput and memory-efficient inference ...</a></li>
<li><a href="https://docs.vllm.ai/projects/llm-compressor/en/latest/examples/quantization_w4a4_fp4/">fp4 Quantization with NVFP4 - LLM Compressor Docs</a></li>
<li><a href="https://localllm.in/blog/mtp-lm-studio">Multi-Token Prediction ( MTP ) LM Studio Tutorial - Boost... | LocalLLM.in</a></li>

</ul>
</details>

**Tags**: `#vllm`, `#LLM-inference`, `#DeepSeek`, `#model-serving`, `#release-notes`

---

<a id="item-2"></a>
## [Claude Opus 5 Nearly Quadruples Record on ARC-AGI-3 Benchmark](https://the-decoder.com/anthropics-opus-5-blows-past-fable-5-and-gpt-5-6-sol-on-the-benchmark-designed-to-measure-real-intelligence/) ⭐️ 8.0/10

Anthropic&\#x27;s Claude Opus 5 scored 30.2% on the ARC-AGI-3 benchmark, nearly four times the previous record of 7.8% held by GPT-5.6 Sol, with the benchmark&\#x27;s developers reporting that the model independently formulated reflection equations—a self-reflective reasoning behavior not previously observed in other models. ARC-AGI-3 is designed to measure interactive agentic reasoning in novel environments where humans score 100% while AI systems have historically scored below 1%. A nearly 4x jump on such a challenging benchmark signals a significant leap in frontier model reasoning capabilities and could accelerate progress toward more general-purpose AI agents. The benchmark&\#x27;s creators specifically attributed Opus 5&\#x27;s gains to stronger logical reasoning, noting the unprecedented emergence of self-formulated reflection equations. The jump from 7.8% to 30.2% is striking, though even at this level the model remains far below human performance \(100%\), underscoring that substantial headroom remains.

rss · The Decoder · Jul 26, 09:43

**Background**: ARC-AGI-3, introduced in April 2026, is the first interactive reasoning benchmark for AI agents, featuring novel abstract turn-based environments where agents must explore, infer goals, and build internal models of dynamics. Earlier AI models had scored under 1% on this benchmark while humans solve it at 100%, making it one of the hardest measures of general intelligence. ARC-AGI is developed by the Arc Prize organization, which has historically focused on creating benchmarks that resist simple pattern-matching and require genuine abstraction and planning.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://arxiv.org/abs/2603.24621">[2603.24621] ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-arc-agi-3-interactive-benchmark">What Is ARC AGI 3? The Interactive AI Benchmark Humans Solve at 100% | MindStudio</a></li>

</ul>
</details>

**Tags**: `#AI`, `#benchmarks`, `#Claude`, `#ARC-AGI`, `#reasoning`

---