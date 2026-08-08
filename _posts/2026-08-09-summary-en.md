---
layout: default
title: "AI Daily: 2026-08-09 (EN)"
date: 2026-08-09
lang: en
---

> From 73 items, 3 important content pieces were selected

---

1. [SGLang v0.5.17 Adds Day-0 Support for Kimi K3 2.8T MoE](#item-1) ⭐️ 8.0/10
2. [DeepMind&\#x27;s WeatherNext Achieves Breakthrough in Cyclone Forecasting](#item-2) ⭐️ 8.0/10
3. [Timeline of the OpenAI accidental attack against Hugging Face](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.17 Adds Day-0 Support for Kimi K3 2.8T MoE](https://github.com/sgl-project/sglang/releases/tag/v0.5.17) ⭐️ 8.0/10

SGLang v0.5.17 was released with 582 PRs from 194 contributors, featuring day-0 support for the Kimi K3, a 2.8T-parameter multimodal LatentMoE model with a 1M-token context window, as well as day-0 support for MiniMax&\#x27;s H3 video-and-audio generation model across the SGLang-Diffusion stack. Day-0 support for a 2.8T-parameter frontier MoE model positions SGLang as the first inference engine able to serve Kimi K3, reinforcing its role as a leading open-source serving framework backed by LMSYS and used by major AI labs. The breadth of optimizations—DSpark speculative decoding, MXFP4 quantization, Rust frontend migration, and DWDP for MoE prefill—signals ongoing performance leadership over alternatives like vLLM. Kimi K3 uses a LatentMoE architecture with 896 experts \(top-16, routed in a 3584-dim latent space\) interleaving 69 KDA linear-attention layers with 24 MLA layers at a roughly 3:1 ratio, paired with a MoonViT3d vision tower and shipped as a native MXFP4 checkpoint. DWDP for MoE prefill achieves 1.92x over DEP4 at 32K context and 506K vs 329K tok/s at saturation on 4x B200 with gpt-oss-120b, while verification was performed on NVIDIA GB300 and AMD MI35x hardware.

github · Fridge003 · Aug 8, 00:19

**Background**: SGLang is an open-source high-performance serving framework for LLMs and multimodal models, developed at UC Berkeley and hosted by LMSYS, known for its RadixAttention technique for KV-cache reuse. Moonshot AI&\#x27;s Kimi K3 is a frontier-scale 2.8T-parameter model built on the Kimi Linear hybrid attention architecture, which interleaves Kimi Delta Attention \(KDA\), a hardware-optimized linear attention module, with Multi-Head Latent Attention \(MLA\) full-attention layers to reduce KV-cache usage while preserving recall. LatentMoE is a routing-efficient MoE variant that performs expert selection in a lower-dimensional latent space rather than directly over token embeddings.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/sgl-project/sglang">GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub</a></li>
<li><a href="https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html">Kimi K3 Architecture Notes | Sebastian Raschka, PhD</a></li>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention ... GitHub - Dev-X25874/Kimi-Linear-Attention: Hybrid KDA+MLA ... Kimi-Linear-Attention/README.md at main · Dev-X25874/Kimi ... KDA (Kimi Delta Attention) | fla-org/flash-linear-attention ... Kimi Linear: Hybrid Linear Attention - emergentmind.com</a></li>

</ul>
</details>

**Tags**: `#sglang`, `#kimi-k3`, `#moe`, `#inference-engine`, `#release`

---

<a id="item-2"></a>
## [DeepMind&\#x27;s WeatherNext Achieves Breakthrough in Cyclone Forecasting](https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/) ⭐️ 8.0/10

Google DeepMind announced that its WeatherNext model achieved breakthrough accuracy in cyclone forecasting, providing an extra day of warning compared to traditional methods. The organization is open-sourcing the model to enable broader adoption. This demonstrates the real-world impact of domain-specific AI models in critical applications like disaster preparedness, potentially saving lives through earlier evacuation warnings. It highlights a meaningful shift beyond LLMs toward specialized AI systems that deliver tangible benefits in science and public safety. The model is based on hierarchical Graph Neural Network \(GNN\) architecture, which processes atmospheric data as interconnected graph structures rather than grid-based methods. This approach is orders of magnitude more efficient at inference than classic Numerical Weather Prediction \(NWP\) models while achieving superior accuracy.

hackernews · bhavansig · Aug 8, 09:18 · [Discussion](https://news.ycombinator.com/item?id=49220126)

**Background**: Traditional weather forecasting relies on Numerical Weather Prediction \(NWP\) models, which solve complex physics equations on supercomputers and can be computationally expensive and slow. GraphCast, introduced by DeepMind in 2023, pioneered the use of Graph Neural Networks for weather prediction by representing the Earth&\#x27;s atmosphere as an irregular graph of nodes \(grid points\) connected by edges, allowing the model to learn spatial relationships more naturally. Recent successors like WeatherNext 2 \(released November 2025\) introduced a Functional Generative Network architecture that uses a 32-dimensional Gaussian noise vector to generate ensemble forecasts, further improving probabilistic prediction capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/google-deepmind/weathernext/blob/main/README.md">weathernext /README.md at main · google- deepmind / weathernext</a></li>
<li><a href="https://dataconomy.com/2025/11/18/google-launches-weathernext-2-with-fgn-architecture/">Google Launches WeatherNext 2 With FGN Architecture - Dataconomy</a></li>
<li><a href="https://medium.com/stanford-cs224w/revolutionizing-weather-forecasting-with-graph-neural-networks-dcc2d06a4d52">Revolutionizing Weather Forecasting with Graph Neural Networks | by climatecast | Stanford CS224W: Machine Learning with Graphs | Medium</a></li>

</ul>
</details>

**Discussion**: The community response was overwhelmingly positive, with commenters expressing enthusiasm for domain-specific AI models that produce real-world impact rather than chasing LLM trends. Multiple users highlighted the value of Graph Neural Network architectures, recommended the original GraphCast paper, and noted practical tools like zoom.earth for tracking cyclones. One commenter humorously suggested that DeepMind&\#x27;s weather breakthroughs may be more strategically valuable than competing in the general LLM space.

**Tags**: `#AI`, `#weather-forecasting`, `#deepmind`, `#graph-neural-networks`, `#climate-science`

---

<a id="item-3"></a>
## [Timeline of the OpenAI accidental attack against Hugging Face](https://simonwillison.net/2026/Aug/7/openai-timeline/) ⭐️ 8.0/10

Simon Willison provides a detailed timeline of an incident where OpenAI&\#x27;s automated systems accidentally attacked Hugging Face, raising questions about AI safety practices and competitive behaviors.

hackernews · 882542F3884314B · Aug 8, 10:57 · [Discussion](https://news.ycombinator.com/item?id=49220609)

**Tags**: `#ai-safety`, `#openai`, `#hugging-face`, `#incident-analysis`, `#automated-systems`

---