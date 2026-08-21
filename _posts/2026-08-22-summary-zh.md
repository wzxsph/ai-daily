---
layout: default
title: "AI Daily: 2026-08-22 (ZH)"
date: 2026-08-22
lang: zh
---

> 从 81 条内容中筛选出 5 条重要资讯。

---

1. [研究员意外通过被遗忘的 e164.arpa DNS 记录了军方通话](#item-1) ⭐️ 8.0/10
2. [英伟达将以 60 亿美元收购 Poolside 的&quot;模型工厂&quot;及其 109 名员工](#item-2) ⭐️ 8.0/10
3. [机器人的 GPT-3 时刻真的来了！卡卡西上身，看 3 秒就学会新动作](#item-3) ⭐️ 8.0/10
4. [立场：人工智能推理代理之间的合谋风险证明其参与市场决策需通过认证](#item-4) ⭐️ 8.0/10
5. [现有模型卡不足以治理开放权重基础模型](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [研究员意外通过被遗忘的 e164.arpa DNS 记录了军方通话](https://lina.sh/blog/hijacking-e164-arpa) ⭐️ 8.0/10

一位安全研究员意外发现，e164.arpa 这个早已废弃的 ENUM DNS 基础设施（最初用于将电话号码映射到互联网资源）仍然在接收大量 DNS 查询，其中包含指向美国军事基地的电话通话路由数据。她在开放的 e164.arpa 基础设施上搭建了一个被动 DNS 监听器，从而无意中捕获了来自 SIP 服务器的数十万条军方通话路由记录。 这一事件暴露了一个严重且长期被忽视的安全漏洞：军方基地的敏感电话路由元数据竟然通过一个无人监管的公共 DNS 基础设施进行广播，且没有任何访问控制。这引发了关于电信供应链安全、遗留互联网基础设施缺乏维护，以及机密信息是否可能通过被遗忘的协议意外泄露的严重质疑。 研究员利用的是 ENUM 协议（定义于 RFC 2916/6116），它通过反转电话号码数字并附加 e164.arpa 后缀来将 E.164 号码映射为 URI（例如 +1-555-4242 变为 2.4.2.4.5.5.5.1.e164.arpa）。该基础设施由 IANA 管理并按国家划分子域，在 ENUM 于 2000 年代商业化失败后基本被弃用，但部分 SIP 服务器从未停止向其发送查询。研究员负责任地披露了这一问题，但未获得任何漏洞奖金或奖励。

hackernews · gavide · 8月21日 13:11 · [社区讨论](https://news.ycombinator.com/item?id=49387570)

**背景**: ENUM（电话号码映射）由 IETF 于 1999 年开始开发，旨在将传统电话系统（E.164 号码）与互联网协议连接起来，使 DNS 能够将电话号码解析为 SIP URI 或其他互联网资源。e164.arpa 域名由 ITU 分配用于存储这些映射，2003 年前后在美国等多个国家进行了试点。然而，由于隐私问题、监管障碍以及竞争性替代方案的出现，ENUM 始终未能广泛普及。如今，公共 ENUM 基本处于休眠状态，2026 年 RIPE Labs 的一份审查发现，现有一半的委派记录存在 DNS 问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Telephone_number_mapping">Telephone number mapping - Wikipedia</a></li>
<li><a href="https://icannwiki.org/ENUM">ENUM - ICANNWiki RFC 6116: The E.164 to Uniform Resource Identifiers (URI ... RFC 2916 - E.164 number and DNS - IETF Datatracker Telephone number mapping - Wikipedia ENUM – DNS based Call Routing | Nick vs Networking Operational Review of Public ENUM Under e164.arpa | RIPE Labs</a></li>
<li><a href="https://nickvsnetworking.com/enum-dns-based-call-routing/">ENUM – DNS based Call Routing | Nick vs Networking</a></li>

</ul>
</details>

**社区讨论**: 社区评论者对这位研究员没有因此类披露而入狱表示惊讶，指出当局通常会对这类发现做出严厉反应。一位评论者指出 e164.arpa 并非真正消亡——私营公司仍通过 VPN 使用 ENUM 查询来提供号码携转服务。其他评论者讨论了 TRIP（基于 IP 的电话路由）等相关协议，并对这位研究员在负责任地报告了一个重大安全问题时未能获得奖励表示遗憾，认为该问题之所以引起关注仅仅是因为涉及军方。

**标签**: `#security`, `#dns`, `#telephony`, `#vulnerability-disclosure`, `#networking`

---

<a id="item-2"></a>
## [英伟达将以 60 亿美元收购 Poolside 的&quot;模型工厂&quot;及其 109 名员工](https://the-decoder.com/nvidia-is-acquiring-poolsides-model-factory-and-109-employees-for-6-billion/) ⭐️ 8.0/10

英伟达将以 60 亿美元收购 Poolside 的人工智能模型构建软件及 109 名员工，进一步扩展其在人工智能开发领域的能力。

rss · The Decoder · 8月21日 08:27

**标签**: `#Nvidia`, `#acquisition`, `#AI infrastructure`, `#Poolside`, `#model development`

---

<a id="item-3"></a>
## [机器人的 GPT-3 时刻真的来了！卡卡西上身，看 3 秒就学会新动作](https://www.qbitai.com/2026/08/476596.html) ⭐️ 8.0/10

一套全新的机器人系统实现了一次性模仿学习，仅通过观看 3 秒的视频演示就能掌握新动作，这可能标志着机器人领域的&\#x27;GPT-3 时刻&\#x27;已经到来。

rss · 量子位 · 8月21日 07:17

**标签**: `#robotics`, `#imitation-learning`, `#one-shot-learning`, `#AI-breakthrough`, `#embodied-AI`

---

<a id="item-4"></a>
## [立场：人工智能推理代理之间的合谋风险证明其参与市场决策需通过认证](https://arxiv.org/abs/2608.18078) ⭐️ 8.0/10

本文为一篇立场论文，论证具备思维链推理能力的 AI 智能体在市场环境中容易产生默示合谋，并通过 DeepSeek-R1 在伯川德寡头垄断模型中的实验加以验证，建议此类智能体在经济领域部署前必须通过行为认证。

rss · arXiv cs.AI · 8月21日 04:00

**标签**: `#AI safety`, `#multi-agent systems`, `#market economics`, `#chain-of-thought reasoning`, `#AI policy`

---

<a id="item-5"></a>
## [现有模型卡不足以治理开放权重基础模型](https://arxiv.org/abs/2608.18086) ⭐️ 8.0/10

一篇立场论文分析了 Hugging Face 平台上的 500 份模型卡，论证了仅凭现有模型卡不足以对开放权重基础模型（OWFMs）进行下游治理。作者提出了一个多层治理框架，将模型卡、可接受使用政策（AUPs）以及许可证整合为互补的治理组件。 随着 DeepSeek、Qwen 等开放权重模型走向主流，治理缺陷为下游开发者和使用者带来了切实的安全风险。本文强调了将信息性、规范性和法律性文档整合起来的迫切需求，以在 AI 生态系统中安全地部署开放权重基础模型。 作者指出了现有模型卡的三个具体安全缺口：模型来源（model heritage）、对齐溯源（alignment provenance）以及经验观察到的行为。他们还认为，标准的开源许可证（OSLs）可能会削弱 AUPs 的可执行性，并且不太适用于开放权重基础模型。

rss · arXiv cs.AI · 8月21日 04:00

**背景**: 开放权重基础模型会发布可下载的训练后模型参数，但与完全开源的 AI 不同，它们可能会保留训练数据、训练代码或部分许可自由。模型卡是标准化文档工件，用于描述模型的预期用途、局限性及评估指标，广泛托管于 Hugging Face 等平台。可接受使用政策（AUPs）为模型的使用方式设定规范性规则，而许可证则提供关于再分发和修改的法律条款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://osfoundry.io/articles/open-weight-vs-open-source-models">Open-Weight vs Open-Source AI Models: What&#x27;s the Difference ...</a></li>
<li><a href="https://www.snowflake.com/en/artificial-intelligence/ai-governance/ai-transparency/">What Is AI Transparency ? Requirements and Best... | Snowflake</a></li>

</ul>
</details>

**标签**: `#AI governance`, `#open-weight models`, `#model cards`, `#AI safety`, `#foundation models`

---