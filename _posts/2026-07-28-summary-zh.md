---
layout: default
title: "AI Daily: 2026-07-28 (ZH)"
date: 2026-07-28
lang: zh
---

> 从 74 条内容中筛选出 7 条重要资讯。

---

1. [vLLM v0.26.0 发布：新增 Inkling 模型支持与 DeepSeek-V4 性能优化](#item-1) ⭐️ 8.0/10
2. [Anthropic 对开源权重模型立场声明](#item-2) ⭐️ 8.0/10
3. [Bun Rust 重写进展：已在 Claude Code 中上线，v1.4 延期发布](#item-3) ⭐️ 8.0/10
4. [Moonshot AI 在 HuggingFace 发布 2.8 万亿参数 Kimi K3 开放权重](#item-4) ⭐️ 8.0/10
5. [NVIDIA Cosmos-H-Dreams：为手术机器人带来实时生成式仿真](#item-5) ⭐️ 8.0/10
6. [Claude 共享聊天通过谷歌搜索被意外曝光](#item-6) ⭐️ 8.0/10
7. [德里高等法院驳回印度主要新闻机构的版权禁令，OpenAI 胜诉](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 发布：新增 Inkling 模型支持与 DeepSeek-V4 性能优化](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 版本发布，包含 212 位贡献者的 411 次提交，首次引入对 Thinking Machines Lab 新 Inkling 模型家族的完整支持栈，包括基础建模、分段 CUDA graph、Hopper FA4 相对注意力、MTP=1 投机解码、LoRA 以及 ModelOpt NVFP4 量化。该版本还针对 DeepSeek-V4 在 NVIDIA、AMD 和 Intel XPU 上带来了显著的性能优化，新增通过 head\_dtype 参数支持 fp32 lm\_head，并支持按 KV-cache 组选择不同的注意力后端。 此次发布确保了在最主流的开源推理引擎上对一个超大规模开源多模态 MoE 模型（Inkling，总参 975B / 激活 41B，上下文 1M）实现 Day-0 支持，使其可立即供社区部署。针对 DeepSeek-V4 的跨厂商优化以及更成熟的 KV-cache 分层机制，显著改善了异构硬件下高吞吐量、长上下文场景的服务经济性。 针对 DeepSeek-V4，新增的专用 routing kernel 带来 2.94% 的端到端 TPOT 提升，fused\_topk\_bias 实现 1.5–2x 的 kernel 加速；新增的 fp32 lm\_head（通过 head\_dtype）已扩展到 LoRA 路径，并在 ROCm 上通过 torch.mm 获得快速路径。注意力后端现在可以按 KV-cache 组粒度选择，滑动窗口（sliding-window）作为显式后端能力暴露出来，便于混合模型的支持。KV offloading 引入了带 workload identity 的对象存储二级层以及 DP-replica-aware 分层机制。

github · khluu · 7月27日 01:06

**背景**: vLLM 是一个高吞吐量的开源大语言模型服务/推理引擎，最初由 UC Berkeley 开发，凭借其 PagedAttention 内存管理和连续批处理（continuous batching）已成为大模型部署事实上的标准。DeepSeek-V4 是近期发布的大规模 MoE 模型，其服务效率高度依赖于 routing 优化、fused topk\_bias 以及冗余 copy 消除等 kernel。NVFP4 是 NVIDIA Blackwell GPU 引入的一种 4 位浮点格式，采用共享指数和紧凑尾数以保留浮点语义，从而相比 INT4 具有更高的动态范围和更稳定的精度。FlashAttention 4（FA4）是面向 Blackwell 硬件重新设计的注意力实现，使用 TCGEN05 张量核指令和张量显存，取代了 Hopper 上 FA3 所使用的 WGMMA 路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://recipes.vllm.ai/thinkingmachines/Inkling">thinkingmachines/Inkling | vLLM Recipes</a></li>
<li><a href="https://vllm.ai/blog/2026-07-15-inkling">TML Inkling on vLLM: Day-0 Support with Optimized Performance | vLLM Blog</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#deepseek`, `#cuda-optimization`, `#model-serving`

---

<a id="item-2"></a>
## [Anthropic 对开源权重模型立场声明](https://www.anthropic.com/news/position-open-weights-models) ⭐️ 8.0/10

Anthropic 发布了一份官方政策立场，声称所有能力足够的 AI 模型——无论是开源还是闭源——都应通过强制性安全测试，同时表示该公司并不主张完全禁止开源权重的发布。 这份来自头部 AI 实验室的政策声明可能影响未来的 AI 监管方向和政府处理开源模型发布的方式，潜在地为独立研究人员和小型竞争者制造壁垒，同时巩固资金充裕的前沿实验室的既有地位。 该政策要求在发布前进行强制性安全测试，原则上反对禁令但支持限制向中国出口芯片，并提出加强出口管制——批评者认为这些措施实质上构成了监管俘获，保护了在位企业的利益同时限制了开源竞争。

hackernews · surprisetalk · 7月27日 22:03 · [社区讨论](https://news.ycombinator.com/item?id=49076057)

**背景**: 开源权重 AI 模型是指公开发布其训练参数的人工智能模型，任何人都可以下载、检查并在本地运行——这种做法由 Meta（推出 Llama）等公司大力倡导，OpenAI 也在近年加入这一行列。Anthropic 以其闭源、仅通过 API 提供模型（Claude）的策略及其负责任扩展政策（RSP）而闻名，该政策是一个用于管理灾难性 AI 风险的自愿性框架。围绕开源权重的争论核心在于普及强大 AI 与防止滥用之间的张力，前沿实验室经常以安全担忧为由，主张对模型分发施加更严格的控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/responsible-scaling-policy">Anthropic’s Responsible Scaling Policy \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/news/responsible-scaling-policy-v3">Responsible Scaling Policy Version 3.0 \ Anthropic</a></li>
<li><a href="https://allthings.how/what-is-an-open-weight-ai-model-and-how-to-use-one/">What is an Open Weight AI Model and How to Use One</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍持怀疑和批评态度，许多人认为强制性安全测试通过制造高昂的合规成本，实际上等同于禁止开源权重模型。多位用户指出了 Anthropic 立场中的矛盾——一方面声称禁令无效，另一方面却支持对华芯片出口限制——并指责该公司以安全为幌子进行道德表演和牟取商业利益。讨论还关注了对监管俘获的担忧、由谁来执行这些测试，以及对其 CEO 突然关心 AI 滥用问题的质疑。

**标签**: `#AI policy`, `#open-source`, `#Anthropic`, `#AI safety`, `#regulation`

---

<a id="item-3"></a>
## [Bun Rust 重写进展：已在 Claude Code 中上线，v1.4 延期发布](https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html) ⭐️ 8.0/10

Bun 创建者 Jarred Sumner 确认 Bun 的 Rust 重写版本一个多月前已在 Anthropic 的 Claude Code 中上线且未出现重大问题，并宣布 Bun v1.4 的发布将推迟，直至承诺的新增通过的 Node.js 兼容性测试数量达标。 这证明了 Bun 的 Rust 重写版本在一个高知名度应用中获得了重要的真实生产环境验证，而 v1.4 延期发布则表明团队将 Node.js 兼容性正确性置于发布速度之上——这对考虑在生产环境中使用 Bun 的开发者来说是一个关键信号。 为达到承诺的测试数量所需的兼容性相关 PR 已提交但尚未合并，Bun 1.4 版本暂定于下周二发布。此次重写已将 Bun 的内部实现从最初的 Zig 迁移到 Rust。

hackernews · tomlockwood · 7月27日 11:12 · [社区讨论](https://news.ycombinator.com/item?id=49067854)

**背景**: Bun 是由 Jarred Sumner 创建的 JavaScript 运行时、包管理器和测试运行器，旨在作为 Node.js 的即插即用替代品，最初使用苹果的 JavaScriptCore 引擎以获得高性能。Claude Code 是 Anthropic 开发的智能体 AI 编程工具，可在终端中运行，理解代码库并自主执行开发任务。Bun 项目一直在进行从最初的 Zig 代码库到 Rust 的重大重写，这一过渡引发了关于开发节奏以及使用 LLM 辅助代码翻译工具的讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_%28software%29">Bun (software) - Wikipedia</a></li>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>
<li><a href="https://github.com/anthropics/claude-code">GitHub - anthropics/claude-code: Claude Code is an agentic ...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪保持谨慎乐观。像 SquareWheel 这样的评论者警告不应通过提交数量来评判重大重构期间的开发速度，指出团队仍在学习 Rust，且可能专注于移除 unsafe 代码。用户 benjiro29 认为 LLM 翻译的代码或许能产出可运行的产品，但在集成、修复 bug 和 UI 打磨等更深层的工作上存在不足。Bendmorris 提到了一个并行的基于 Zig 的项目 buz，声称通过修复原始代码库中的问题就实现了 Bun 最初的目标，暗示此次重写或许并非必要。

**标签**: `#bun`, `#rust`, `#javascript-runtime`, `#llm-assisted-development`, `#software-rewrite`

---

<a id="item-4"></a>
## [Moonshot AI 在 HuggingFace 发布 2.8 万亿参数 Kimi K3 开放权重](https://huggingface.co/moonshotai/Kimi-K3) ⭐️ 8.0/10

Moonshot AI 在 HuggingFace 上以 Modified MIT 许可证发布了 Kimi K3 的完整开放权重,这是一个拥有 2.8 万亿参数的混合专家\(MoE\)语言模型。该模型支持原生 MXFP4 量化、100 万 token 上下文窗口、原生图像输入,架构中包含 Kimi Delta Attention、Attention Residuals 和 Stable LatentMoE 等组件。 这是迄今为止发布的最大开放权重模型,让创业公司可以基于自有数据微调前沿级别的权重并保持 IP 主权。然而,极低的运行门槛\(原生 MXFP4 下约需 1.5TB VRAM,实际部署通常需要 16 张 B200 级显卡\)意味着大多数个人用户只能通过第三方 API 使用,而无法自行托管。 原生 MXFP4 量化使得推理需要约 1.5TB VRAM,刚好处于 8 张 B200 配置的极限,但实际部署为了上下文长度和吞吐量优化仍需要 16 张显卡。Modified MIT 许可证中包含一项 Model-as-a-Service 条款:任何在连续 12 个月内收入超过 2000 万美元的许可方,在将模型用于商业用途之前必须与 Moonshot AI 另行签订商业协议。

hackernews · nateb2022 · 7月27日 06:18 · [社区讨论](https://news.ycombinator.com/item?id=49065752)

**背景**: 开放权重模型在许可证下发布训练好的模型参数,允许外部使用和微调,但通常不公开训练数据和代码,这与完全开源的软件有所区别。混合专家\(MoE\)架构在每个 token 上只激活部分参数,从而在总参数量极大的同时保持相对较低的推理计算成本。MXFP4 是 NVIDIA 设计的 4 位微缩放浮点格式,用于压缩模型权重和激活值,相比 FP8 大约可减少一半内存占用,同时精度损失极小。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.visionstory.ai/models/kimi-k3">Kimi K3 Model: Architecture, Context Window and Capabilities</a></li>
<li><a href="https://graphify.net/ai-coding/llms/kimi-k3/">Kimi K3: Architecture, Benchmarks, Pricing, and Open Weights</a></li>

</ul>
</details>

**社区讨论**: 评论者分为几个阵营。关注价格的用户热切期待 3T 级别模型的第三方每百万 token 定价,Fireworks 已将其列为未缓存输入 3.00 美元/百万 token、输出 15.00 美元/百万 token。支持定制的用户认为,微调和 IP 主权才是对创业公司真正的价值。硬件爱好者则感叹缺少功耗在 180-250W、显存 128-256GB 的消费级 GPU;许可证分析师则指出,2000 万美元营收门槛会迫使大型 MaaS 服务商重新回到谈判桌前。

**标签**: `#Kimi-K3`, `#open-source-llm`, `#large-language-models`, `#Moonshot-AI`, `#model-release`

---

<a id="item-5"></a>
## [NVIDIA Cosmos-H-Dreams：为手术机器人带来实时生成式仿真](https://huggingface.co/blog/nvidia/cosmos-h-dreams) ⭐️ 8.0/10

NVIDIA 推出了 Cosmos-H-Dreams，这是 Cosmos 平台上的一个新框架，专为手术机器人提供实时、照片级逼真的生成式仿真。该系统可创建用于手术机器人系统训练与评估的交互式虚拟环境。 此次发布将快速发展的生成式世界模型与高风险的应用领域（手术机器人）相结合，而基于仿真的训练对于该领域的安全性与技能培养至关重要。这标志着 NVIDIA 战略上将 Physical AI 技术栈从自动驾驶和工业机器人拓展至医疗健康领域，有望加速医疗机器人的 sim-to-real 迁移。 Cosmos-H-Dreams 利用 NVIDIA 的 Cosmos 世界基础模型（WFMs），该模型可作为环境动力学的内部仿真器，支持前向推演与反事实回滚以辅助决策。该框架面向需要感知、行动并预测行为如何重塑未来世界状态的具身智能体——在手术场景中，组织形变与器械交互高度动态，这一要求尤为严苛。

rss · Hugging Face · 7月27日 09:32

**背景**: 世界模型是一类学习物理环境动力学的生成式 AI 系统，使机器人和智能体能够在真实世界中行动之前模拟「假设」场景。NVIDIA Cosmos 是专为 Physical AI 打造的平台，提供世界基础模型、分词器、安全护栏以及加速的数据处理流水线，用于支持自动驾驶、机器人和 AI 智能体的开发。在手术机器人领域，高保真仿真长期以来被用于培训外科医生和验证机器人系统，避免患者风险，但传统仿真依赖手工构建的图形，而非能够对新型操作动态响应的生成式模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/ai/cosmos/">Physical AI with World Foundation Models | NVIDIA Cosmos</a></li>
<li><a href="https://docs.nvidia.com/cosmos/index.html">NVIDIA Cosmos - NVIDIA Docs</a></li>
<li><a href="https://arxiv.org/abs/2510.16732">[2510.16732] A Comprehensive Survey on World Models for ... Top Stories News about Robotics, Robot, Data collection News about Robotics, Awe, Embodied cognition Also in the news Embodied AI 2026: From Robot Foundation Models to Industrial ... Frontiers | A review of embodied intelligence systems: a ... A Survey of Embodied World Models A Comprehensive Survey on World Models for Embodied AI A Comprehensive Survey on World Models for Embodied AI</a></li>

</ul>
</details>

**标签**: `#nvidia`, `#surgical-robotics`, `#generative-simulation`, `#world-models`, `#embodied-ai`

---

<a id="item-6"></a>
## [Claude 共享聊天通过谷歌搜索被意外曝光](https://techcrunch.com/2026/07/27/psa-your-claude-shared-chats-and-artifacts-may-have-ended-up-on-google/) ⭐️ 8.0/10

Claude 的「分享聊天」功能似乎导致共享的对话和 Artifacts 被谷歌搜索引擎收录，使私有用户数据可能被任意在线搜索的人发现。 这是一起影响 Claude 用户的重要隐私事件——这些用户原本以为共享链接只对持有 URL 的人可见，但现在这些内容可能被广泛搜索到。它凸显了 AI 平台在处理可分享链接和搜索引擎收录方面持续存在的风险。 此次泄露似乎专门与「分享聊天」功能相关，该功能会为对话和 Artifacts 生成可访问的 URL，而谷歌爬虫抓取了这些 HTML 链接，尽管用户并未明确同意被收录。Claude 的 Artifacts 功能覆盖 Free、Pro、Max、Team 和 Enterprise 各层级，扩大了受影响用户的范围。

rss · TechCrunch AI · 7月27日 20:19

**背景**: Claude 的「分享聊天」功能允许用户生成可分享的 URL，以便他人直接查看对话或 Artifact。Artifact 是 Claude 的一项功能，可以将聊天回复转化为独立的应用程序、文档或可视化内容，供用户查看和交互。谷歌的搜索爬虫（Googlebot）会追踪网络上的 HTML 链接，并将发现的页面加入搜索索引，这意味着任何面向公众的 URL 都可能被纳入搜索，除非网站所有者添加 noindex 等保护性标签。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them">What are artifacts and how do I use them? - Anthropic</a></li>
<li><a href="https://developers.google.com/search/docs/crawling-indexing/links-crawlable">SEO Link Best Practices for Google | Google Search Central | Documentation | Google for Developers</a></li>

</ul>
</details>

**标签**: `#privacy`, `#security`, `#claude`, `#anthropic`, `#data-exposure`

---

<a id="item-7"></a>
## [德里高等法院驳回印度主要新闻机构的版权禁令，OpenAI 胜诉](https://the-decoder.com/delhi-high-court-hands-openai-a-win-by-rejecting-major-indian-news-agencys-copyright-injunction/) ⭐️ 8.0/10

德里高等法院驳回了 ANI 对 OpenAI 的版权禁令申请，这是法院首次将 AI 训练归类为私人使用，但主要诉讼仍在进行中。

rss · The Decoder · 7月27日 17:55

**标签**: `#AI`, `#copyright`, `#OpenAI`, `#legal`, `#India`

---