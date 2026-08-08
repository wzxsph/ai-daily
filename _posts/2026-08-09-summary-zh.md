---
layout: default
title: "AI Daily: 2026-08-09 (ZH)"
date: 2026-08-09
lang: zh
---

> 从 73 条内容中筛选出 3 条重要资讯。

---

1. [SGLang v0.5.17 首发支持 Kimi K3 2.8 万亿参数 MoE 模型](#item-1) ⭐️ 8.0/10
2. [DeepMind 的 WeatherNext 在气旋预测方面取得突破性进展](#item-2) ⭐️ 8.0/10
3. [OpenAI 对 Hugging Face 意外攻击事件的时间线](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.17 首发支持 Kimi K3 2.8 万亿参数 MoE 模型](https://github.com/sgl-project/sglang/releases/tag/v0.5.17) ⭐️ 8.0/10

SGLang v0.5.17 正式发布，包含来自 194 位贡献者的 582 个 PR，亮点包括对 Kimi K3（2.8 万亿参数的多模态 LatentMoE 模型，上下文长度为 100 万 token）的首发支持，以及对 MiniMax H3 视频与音频生成模型在 SGLang-Diffusion 全任务模式下的首发支持。 对 2.8 万亿参数前沿 MoE 模型的首发支持，使 SGLang 成为首个可服务 Kimi K3 的推理引擎，进一步巩固了其作为 LMSYS 背书的领先开源推理框架的地位。该版本涵盖 DSpark 推测解码、MXFP4 量化、Rust 前端迁移以及 DWDP MoE 预填充等大量优化，表明其在性能上持续领先于 vLLM 等替代方案。 Kimi K3 采用 LatentMoE 架构（896 个专家，top-16 激活，在 3584 维潜空间中进行路由），以约 3:1 的比例将 69 层 KDA 线性注意力层与 24 层 MLA 层交错排列，搭配 MoonViT3d 视觉塔，并以原生 MXFP4 checkpoint 形式发布。DWDP MoE 预填充策略在 4x B200 + gpt-oss-120b 上 32K 上下文时达到 DEP4 的 1.92 倍，饱和吞吐下达到 506K 对比 329K tok/s（1.54 倍），并在 NVIDIA GB300 和 AMD MI35x 硬件上完成验证。

github · Fridge003 · 8月8日 00:19

**背景**: SGLang 是一个开源的高性能大语言模型与多模态模型推理框架，由 UC Berkeley 开发、LMSYS 托管，以 RadixAttention KV 缓存复用技术著称。月之暗面（Moonshot AI）的 Kimi K3 是一款前沿规模的 2.8 万亿参数模型，构建于 Kimi Linear 混合注意力架构之上，该架构将 Kimi Delta Attention（KDA，一种硬件优化的线性注意力模块）与 Multi-Head Latent Attention（MLA）全局注意力层交错排列，以在保留召回能力的同时降低 KV 缓存开销。LatentMoE 是一种路由高效的 MoE 变体，在低维潜空间而非直接对 token 嵌入进行专家选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sgl-project/sglang">GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub</a></li>
<li><a href="https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html">Kimi K3 Architecture Notes | Sebastian Raschka, PhD</a></li>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention ... GitHub - Dev-X25874/Kimi-Linear-Attention: Hybrid KDA+MLA ... Kimi-Linear-Attention/README.md at main · Dev-X25874/Kimi ... KDA (Kimi Delta Attention) | fla-org/flash-linear-attention ... Kimi Linear: Hybrid Linear Attention - emergentmind.com</a></li>

</ul>
</details>

**标签**: `#sglang`, `#kimi-k3`, `#moe`, `#inference-engine`, `#release`

---

<a id="item-2"></a>
## [DeepMind 的 WeatherNext 在气旋预测方面取得突破性进展](https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/) ⭐️ 8.0/10

这展示了领域专用 AI 模型在防灾减灾等关键应用中的实际价值，有望通过更早的疏散预警来挽救生命。它标志着 AI 领域正从大语言模型向具有实际科学和公共安全效益的专用系统转变。 该模型基于层次化图神经网络（GNN）架构，将大气数据作为相互连接的图结构来处理，而非传统的网格化方法。这种方法在推理效率上比经典数值天气预报（NWP）模型高出数个数量级，同时准确度更优。

hackernews · bhavansig · 8月8日 09:18 · [社区讨论](https://news.ycombinator.com/item?id=49220126)

**背景**: 传统天气预报依赖数值天气预报（NWP）模型，通过超级计算机求解复杂的物理方程，计算开销大且速度较慢。DeepMind 于 2023 年推出的 GraphCast 开创了将图神经网络用于天气预测的先河，将地球大气表示为以节点（网格点）和边连接的不规则图结构，使模型能够更自然地学习空间关系。2025 年 11 月发布的 WeatherNext 2 等后续模型引入了函数生成网络架构，利用 32 维高斯噪声向量生成集合预报，进一步提升了概率预测能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/google-deepmind/weathernext/blob/main/README.md">weathernext /README.md at main · google- deepmind / weathernext</a></li>
<li><a href="https://dataconomy.com/2025/11/18/google-launches-weathernext-2-with-fgn-architecture/">Google Launches WeatherNext 2 With FGN Architecture - Dataconomy</a></li>
<li><a href="https://medium.com/stanford-cs224w/revolutionizing-weather-forecasting-with-graph-neural-networks-dcc2d06a4d52">Revolutionizing Weather Forecasting with Graph Neural Networks | by climatecast | Stanford CS224W: Machine Learning with Graphs | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区反馈非常积极，评论者对能够产生实际影响的领域专用 AI 模型表示热烈欢迎，认为这比追逐大语言模型潮流更有价值。多位用户强调了图神经网络架构的价值，推荐了原始的 GraphCast 论文，并提到了 zoom.earth 等用于追踪气旋的实用工具。有一名评论者幽默地表示，DeepMind 在天气预测方面的突破在战略上可能比参与通用大语言模型竞争更有价值。

**标签**: `#AI`, `#weather-forecasting`, `#deepmind`, `#graph-neural-networks`, `#climate-science`

---

<a id="item-3"></a>
## [OpenAI 对 Hugging Face 意外攻击事件的时间线](https://simonwillison.net/2026/Aug/7/openai-timeline/) ⭐️ 8.0/10

Simon Willison 详细梳理了 OpenAI 自动化系统意外攻击 Hugging Face 的事件经过，这一事件引发了人们对 AI 安全实践和竞争行为的质疑。

hackernews · 882542F3884314B · 8月8日 10:57 · [社区讨论](https://news.ycombinator.com/item?id=49220609)

**标签**: `#ai-safety`, `#openai`, `#hugging-face`, `#incident-analysis`, `#automated-systems`

---