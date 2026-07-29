---
layout: default
title: "AI Daily: 2026-07-29 (ZH)"
date: 2026-07-29
lang: zh
---

> 从 80 条内容中筛选出 8 条重要资讯。

---

1. [Anthropic 表示其 Mythos 模型发现了保护互联网安全的加密算法中的漏洞](#item-1) ⭐️ 9.0/10
2. [modelcontextprotocol/python-sdk 发布 v2.0.0](#item-2) ⭐️ 8.0/10
3. [Kimi K3 架构：完全弃用 RoPE，转向 NoPE](#item-3) ⭐️ 8.0/10
4. [深入剖析 Zig 的增量编译内部机制](#item-4) ⭐️ 8.0/10
5. [Kimi Linear：一种高效且富有表达力的注意力架构](#item-5) ⭐️ 8.0/10
6. [智能体 AI 时代的科学计算](#item-6) ⭐️ 8.0/10
7. [英伟达投资伊利亚·苏茨克维尔的 AI 实验室，SSI 转向使用英伟达芯片，放弃谷歌芯片](#item-7) ⭐️ 8.0/10
8. [PNAS 研究：超过 51%的学术论文已显现 LLM 影响](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 表示其 Mythos 模型发现了保护互联网安全的加密算法中的漏洞](https://the-decoder.com/anthropic-says-its-mythos-model-found-vulnerabilities-in-cryptographic-algorithms-that-secure-the-internet/) ⭐️ 9.0/10

Anthropic 声称其 Claude Mythos 模型发现了加密算法中的漏洞，包括一个后量子签名方案（HAWK），这些漏洞被人类专家遗漏了两年多。

rss · The Decoder · 7月28日 19:12

**标签**: `#AI`, `#cryptography`, `#cybersecurity`, `#Anthropic`, `#post-quantum`

---

<a id="item-2"></a>
## [modelcontextprotocol/python-sdk 发布 v2.0.0](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0) ⭐️ 8.0/10

MCP Python SDK v2.0.0 稳定版正式发布,引入 2026-07-28 协议修订版本,包含文档重写、迁移指南,并将 v1 版本转入维护模式。

github · maxisbey · 7月28日 13:41

**标签**: `#MCP`, `#Python-SDK`, `#Model-Context-Protocol`, `#release`, `#developer-tools`

---

<a id="item-3"></a>
## [Kimi K3 架构：完全弃用 RoPE，转向 NoPE](https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html) ⭐️ 8.0/10

Sebastian Raschka 发布了关于月之暗面 Kimi K3 的详细架构分析，揭示该模型在整个架构中完全摒弃了旋转位置编码（RoPE），转而采用 NoPE（无位置编码）。该分析指出了若干使 Kimi K3 区别于典型西方前沿模型架构的新颖设计选择。 彻底放弃 RoPE 是对现代大语言模型中近乎通用惯例的重大突破，挑战了显式位置编码对基于 Transformer 的语言模型不可或缺的假设。这使得 Kimi K3 成为一款真正具有创新性的模型，而非西方同行的衍生品，对整个研究社区重新思考位置编码设计具有深远影响。 最引人注目的技术细节是在整个模型中全面采用 NoPE，移除了所有的 RoPE 层。Raschka 的完整博客文章中还讨论了其他架构创新，这些细节的详尽程度通常见于同行评审的架构报告，而非非正式的技术文章。

hackernews · ModelForge · 7月28日 15:48 · [社区讨论](https://news.ycombinator.com/item?id=49085698)

**背景**: 基于 Transformer 架构的大语言模型（LLM）需要某种方式来理解序列中标记（token）的顺序，因为自注意力机制本质上对排列是不变的。RoPE（旋转位置编码）在 2021 年的 RoFormer 论文中被提出，已成为一种主流解决方案，它通过旋转查询向量和键向量来编码位置信息。NoPE（无位置编码）是一种更为激进的选择，它完全移除显式的位置编码，转而依赖因果注意力掩码和模型学到的表示来隐式地捕捉标记顺序。此前的工作（如 SmolLM3）已表明 NoPE 可以在架构的某些部分选择性使用，但像 Kimi K3 这样在整个模型中全面采用 NoPE 则非常罕见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/nope/">No Positional Embeddings (NoPE) | Sebastian Raschka, PhD</a></li>
<li><a href="https://arxiv.org/abs/2104.09864">RoFormer: Enhanced Transformer with Rotary Position Embedding</a></li>
<li><a href="https://newsletter.theaiedge.io/p/all-about-the-modern-positional-encodings">All About The Modern Positional Encodings In LLMs</a></li>

</ul>
</details>

**社区讨论**: 社区整体情绪非常积极，对 Kimi K3 印象深刻。用户们就 NoPE 反直觉的特性展开了讨论，一位评论者对模型在没有显式位置信息的情况下仍能正常运作表示惊叹。其他人则对中国模型的架构可复现性表示担忧，将已发布的规范比作 PDF/DWG/PSD 等格式，认为其中关键实现细节并未公开。一位用户表示已将 Kimi K3 切换为日常使用工具，认为其表现可与 Claude Opus 4.7/4.8 媲美；另一位用户则指出，Kimi 的新颖设计方法与西方实验室将其贬低为仅仅是蒸馏攻击产物的说法形成了鲜明对比。

**标签**: `#kimik3`, `#llm-architecture`, `#moonshot-ai`, `#machine-learning`, `#research-analysis`

---

<a id="item-4"></a>
## [深入剖析 Zig 的增量编译内部机制](https://mlugg.co.uk/posts/incremental-compilation-internals/) ⭐️ 8.0/10

mlugg 发表了一篇详细的博客文章，深入探讨 Zig 编译器如何实现增量编译，重点介绍了它如何按源文件缓存 ZIR（Zig 中间表示）并仅重新分析发生变化的单元。该文章还将 Zig 的设计权衡与 Rust 的增量编译方案进行了比较。 增量编译对开发者生产力至关重要，特别是在完整重建可能耗时数分钟的大型代码库中。Zig 的设计选择——让语义分析易于缓存——为其他语言的实现者提供了宝贵的经验，也说明了为什么 Rust 复杂的类型系统会让增量编译困难得多。 Zig 为每个声明追踪四个关键属性——layout、type、value 和 body——这使得依赖追踪比 Rust 基于 trait 的依赖图简单得多。文章指出，针对非二进制输出（例如 \`zig build check\`）的增量编译已于 2024 年 8 月通过 \`--watch -fincremental\` 合并，但完整的二进制级增量链接支持仍在发展中。

hackernews · garyhtou · 7月28日 15:46 · [社区讨论](https://news.ycombinator.com/item?id=49085666)

**背景**: 增量编译是一种编译器技术，它复用先前编译的分析结果，仅对代码中发生变化的部分重新执行工作。语义分析是编译器在解析之后检查程序类型、作用域和语义的阶段。Zig 是一门为快速编译而设计的系统编程语言，其工具链捆绑了构建系统和 C/C++ 编译器（\`zig cc\`）。相比之下，由于 Rust 涉及 trait、生命周期和单态化等复杂的类型系统，其增量编译系统虽然更复杂但速度较慢。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mlugg.co.uk/posts/incremental-compilation-internals/">Inside Zig&#x27;s Incremental Compilation | mlugg.co.uk</a></li>
<li><a href="https://deepwiki.com/ziglang/zig/3.3-incremental-compilation">Incremental Compilation | ziglang/zig | DeepWiki</a></li>
<li><a href="https://www.reddit.com/r/Zig/comments/1ev8mvs/incremental_compilation_merged/">r/Zig on Reddit: Incremental compilation merged</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极且具有技术深度。steveklabnik 称赞了 Zig 的工具链工作，同时表达了对内存安全性的保留意见。rust-analyzer 团队成员 afdbcreid 认为 Rust 编译较慢主要归因于语言设计而非编译器实现。thefaux 质疑为什么 Zig 为调试构建生成单个大型二进制文件而非许多较小的共享库，patrec 则提出了一个尖锐的问题：在 comptime 求值的背景下，该模型如何处理对运行时函数体的依赖。

**标签**: `#zig`, `#compilers`, `#incremental-compilation`, `#programming-languages`, `#systems-programming`

---

<a id="item-5"></a>
## [Kimi Linear：一种高效且富有表达力的注意力架构](https://arxiv.org/abs/2510.26692) ⭐️ 8.0/10

Moonshot AI 发布了 Kimi Linear，这是一种采用 Kimi Delta Attention（KDA）的新型注意力架构，通过细粒度门控机制对门控 Delta 规则进行了改进。团队基于 KDA 与多头潜在注意力（MLA）以 3:1 的层级混合方式，训练了一个激活参数 3B、总参数 48B 的模型，并开源了 KDA 算子、vLLM 实现以及预训练模型权重。 Kimi Linear 在 1M 上下文长度下将 KV 缓存使用量减少高达 75%，并将解码吞吐量提升至最高 6 倍，同时在相同训练方案下各项评估任务的表现均优于完整 MLA。这使其成为完整注意力的实用替代方案，有望改变大语言模型处理长上下文推理的效率范式。 该架构采用 3:1 的 KDA 与 MLA 层比例，即每四层中有一层使用完整的 MLA，另外三层使用更高效的 KDA。这种混合设计在内存效率与全局上下文建模能力之间取得了平衡，而后者正是纯线性注意力往往欠缺的部分。此次开源既包含底层算子实现，也包含 vLLM 集成，便于部署使用。

hackernews · ronfriedhaber · 7月28日 10:52 · [社区讨论](https://news.ycombinator.com/item?id=49082022)

**背景**: 标准 Transformer 注意力的计算复杂度随序列长度呈二次方增长，同时需要存储随上下文长度线性增长的 KV 缓存，这给长上下文推理带来了严重的瓶颈。线性注意力机制通过循环计算或核函数方法实现 O\(N\) 复杂度来解决这一问题，但在表达力上通常弱于 softmax 注意力。Kimi Linear 这类混合架构尝试在大多数层使用高效的线性注意力，同时在部分层保留完整的注意力以兼顾表达力。MLA（多头潜在注意力）随 DeepSeek-V2 一起提出，它将 KV 缓存压缩到低秩潜在空间中，已成为近期开源模型中流行的效率优化手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://github.com/MoonshotAI/Kimi-Linear">GitHub - MoonshotAI/Kimi-Linear · GitHub</a></li>
<li><a href="https://vizuara.substack.com/p/kimi-linear-an-expressive-efficient">Kimi-Linear : An Expressive, Efficient Attention Architecture</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 Kimi Linear 是更大的 Kimi K3 模型的基础，后者在此基础上进一步扩展规模，并加入了原生视觉和强化学习的改进。一位用户提到，Gated DeltaNet 2 在其内部测试中是 KDA 的自然演进版本，表达力更强。此次开源的算子和模型权重获得了广泛好评，也有怀疑者被提醒 Kimi 的强劲表现是真实成果，而非知识蒸馏攻击的结果。

**标签**: `#attention-mechanisms`, `#LLM-architecture`, `#Kimi`, `#efficient-inference`, `#open-source`

---

<a id="item-6"></a>
## [智能体 AI 时代的科学计算](https://openai.com/index/scientific-computing-agentic-ai) ⭐️ 8.0/10

OpenAI 的实地报告描述了科学家如何利用 AI 编程智能体来推动科学计算的现代化,并加速基因组学等领域的发现。

rss · OpenAI News · 7月28日 17:00

**标签**: `#agentic AI`, `#scientific computing`, `#coding agents`, `#AI for science`, `#OpenAI`

---

<a id="item-7"></a>
## [英伟达投资伊利亚·苏茨克维尔的 AI 实验室，SSI 转向使用英伟达芯片，放弃谷歌芯片](https://the-decoder.com/nvidia-invests-in-ilya-sutskevers-ai-lab-shifting-ssi-away-from-google-chips/) ⭐️ 8.0/10

英伟达对伊利亚·苏茨克维尔的 Safe Superintelligence（SSI）进行了一笔“巨额”投资，这家 AI 实验室将其芯片战略从谷歌 TPU 转向英伟达硬件。

rss · The Decoder · 7月28日 13:06

**标签**: `#Nvidia`, `#Safe Superintelligence`, `#Ilya Sutskever`, `#AI Infrastructure`, `#GPU/TPU Competition`

---

<a id="item-8"></a>
## [PNAS 研究：超过 51%的学术论文已显现 LLM 影响](https://www.reddit.com/r/MachineLearning/comments/1v93q78/pnas_over_half_of_all_academic_articles_now_show/) ⭐️ 8.0/10

一项发表于 PNAS 的研究分析了 730 万篇学术论文，发现到 2025 年，超过 51%的已发表论文呈现出不同程度的 LLM 影响，这一结论基于与 LLM 生成文本相关的特征词汇模式。研究还发现，LLM 的采用偏向于声望较低的机构以及非英语国家的机构。 这是迄今为止关于 LLM 渗透学术出版领域规模最大的实证研究，为衡量 LLM 如何重塑科学写作提供了最具权威性的量化基准。研究揭示的不平等现象引发了重要的政策担忧——机构间不均衡的 LLM 采用可能加剧全球科研成果产出中已有的差距。 该研究采用的检测方法依赖于识别在 LLM 生成文本中统计上出现频率过高的特定词汇和短语。研究发现，LLM 编辑倾向于将写作从第一人称叙事转变为更加非个人化的学术风格，而当 LLM 被用于补全或润色已有文本时，这种转变更为明显。

reddit · r/MachineLearning · /u/Justgototheeffinmoon · 7月28日 16:38

**背景**: 像 GPT-4 这样的 LLM 已成为广泛使用的工具，能够生成、编辑和润色文本，包括学术论文。自 2022 年末 LLM 普及以来，研究人员一直在争论这些工具对学术出版的影响程度，关注点包括写作风格的趋同化以及科学记录的完整性问题。PNAS（美国国家科学院院刊）是声誉最高的多学科科学期刊之一，影响因子超过 100，因此是发表具有广泛影响研究的权威平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/muhammed-erkan-karabekmez-3948041a_the-diffusion-of-large-language-models-in-activity-7467652152929247232-mRqf">PNAS Study: LLM Influence on Academic Writing by 2025 | LinkedIn</a></li>
<li><a href="https://abdulhaim.github.io/documents/LLM_Homogenization_Project.pdf">How LLMs Distort Our Written Language</a></li>
<li><a href="https://www.pnas.org/">pnas .org</a></li>

</ul>
</details>

**标签**: `#LLM`, `#academic-publishing`, `#research-policy`, `#AI-adoption`, `#PNAS`

---