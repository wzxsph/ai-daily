---
layout: default
title: "AI Daily: 2026-07-27 (ZH)"
date: 2026-07-27
lang: zh
---

> 从 39 条内容中筛选出 2 条重要资讯。

---

1. [vLLM v0.26.0 发布：DeepSeek-V4 性能优化与 Inkling 模型支持](#item-1) ⭐️ 8.0/10
2. [Claude Opus 5 在 ARC-AGI-3 基准测试中近乎四倍刷新纪录](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 发布：DeepSeek-V4 性能优化与 Inkling 模型支持](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 已发布，包含 212 位贡献者（其中 61 位新加入）的 411 次提交，新增了 Inkling 模型家族的完整支持栈（包括 CUDA 图、推测解码、LoRA 和 NVFP4 量化），并对 DeepSeek-V4 在 CUDA、ROCm 和 XPU 平台上进行了大幅性能优化，端到端 TPOT 提升 1.8–2.94%，内核速度提升最高达 2 倍。 vLLM 的性能改进直接降低生产部署的推理成本并提升吞吐量，尤其对日益流行的 DeepSeek 风格 MoE 模型影响显著。本次跨 NVIDIA、AMD 和 Intel 平台的优化对异构 GPU 部署环境意义重大。 重要特性包括：新增 \`head\_dtype\` 参数，支持生成模型的 fp32 \`lm\_head\`（提升数值精度）；支持按 KV-cache 组选择注意力后端，便于混合架构模型；KV 卸载与分层二级存储功能显著成熟。Rust 前端还新增了原生多模态视频/音频支持和原生 \`vllm-bench\` 移植版本。

github · khluu · 7月27日 01:06

**背景**: vLLM 是一个高吞吐量、内存高效的大语言模型推理与服务引擎，最初由 UC Berkeley 开发，现已成为大语言模型服务生态中最活跃的开源项目之一。推测解码（包括 MTP，即多 token 预测）是一种让较小的草稿模型预测多个 token，再由较大的目标模型并行验证的技术，能有效提升每秒 token 数。NVFP4 是 NVIDIA Blackwell GPU 架构引入的 4 位浮点量化格式，可在保持精度的同时减少内存占用。DeepSeek-V4 风格的 MoE（混合专家）模型将每个 token 路由到部分专家，需要专门的路由内核以保证效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm">vllm -project/ vllm : A high - throughput and memory-efficient inference ...</a></li>
<li><a href="https://docs.vllm.ai/projects/llm-compressor/en/latest/examples/quantization_w4a4_fp4/">fp4 Quantization with NVFP4 - LLM Compressor Docs</a></li>
<li><a href="https://localllm.in/blog/mtp-lm-studio">Multi-Token Prediction ( MTP ) LM Studio Tutorial - Boost... | LocalLLM.in</a></li>

</ul>
</details>

**标签**: `#vllm`, `#LLM-inference`, `#DeepSeek`, `#model-serving`, `#release-notes`

---

<a id="item-2"></a>
## [Claude Opus 5 在 ARC-AGI-3 基准测试中近乎四倍刷新纪录](https://the-decoder.com/anthropics-opus-5-blows-past-fable-5-and-gpt-5-6-sol-on-the-benchmark-designed-to-measure-real-intelligence/) ⭐️ 8.0/10

Anthropic 的 Claude Opus 5 在 ARC-AGI-3 基准测试中取得了 30.2% 的成绩，几乎是 GPT-5.6 Sol 此前 7.8% 纪录的四倍。基准测试的开发者指出，该模型独立构建了反思方程（reflection equations），展现出此前从未在其他模型中观察到的自我反思式推理行为。 ARC-AGI-3 旨在衡量 AI 在全新交互式环境中的智能体推理能力，而人类在此基准上可达 100%，AI 系统此前长期低于 1%。在如此具有挑战性的基准上取得近 4 倍的跃升，标志着前沿模型推理能力的重大突破，可能加速更通用 AI 智能体的发展进程。 基准测试的创建者将 Opus 5 的进步归因于更强的逻辑推理能力，并特别指出模型自发构建反思方程这一前所未有的现象。从 7.8% 到 30.2% 的跃升虽然惊人，但即便如此，模型表现仍远低于人类水平（100%），说明距离通用智能仍有巨大的提升空间。

rss · The Decoder · 7月26日 09:43

**背景**: ARC-AGI-3 于 2026 年 4 月发布，是首个面向 AI 智能体的交互式推理基准测试，包含全新且抽象的回合制环境，要求智能体在其中进行探索、推断目标并构建对环境动态的内部模型。此前 AI 模型在该基准上得分低于 1%，而人类可以 100% 解决，因此它被认为是衡量通用智能最难的指标之一。ARC-AGI 由 Arc Prize 组织开发，该组织长期致力于创建能够抵御简单模式匹配、需要真正抽象与规划能力的基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://arxiv.org/abs/2603.24621">[2603.24621] ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-arc-agi-3-interactive-benchmark">What Is ARC AGI 3? The Interactive AI Benchmark Humans Solve at 100% | MindStudio</a></li>

</ul>
</details>

**标签**: `#AI`, `#benchmarks`, `#Claude`, `#ARC-AGI`, `#reasoning`

---