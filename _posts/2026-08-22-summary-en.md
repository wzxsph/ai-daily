---
layout: default
title: "AI Daily: 2026-08-22 (EN)"
date: 2026-08-22
lang: en
---

> From 81 items, 5 important content pieces were selected

---

1. [Researcher accidentally logs military phone calls via forgotten e164.arpa DNS](#item-1) ⭐️ 8.0/10
2. [Nvidia is acquiring Poolside&\#x27;s &quot;Model Factory&quot; and 109 employees for $6 billion](#item-2) ⭐️ 8.0/10
3. [机器人的GPT-3时刻真·来了！卡卡西上身，看3秒就学会新动作](#item-3) ⭐️ 8.0/10
4. [Position: Collusion Risks Among AI Reasoning Agents Justify Certification Requirements for Making Market Decisions](#item-4) ⭐️ 8.0/10
5. [Model Cards Insufficient for Governing Open-Weight Foundation Models](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Researcher accidentally logs military phone calls via forgotten e164.arpa DNS](https://lina.sh/blog/hijacking-e164-arpa) ⭐️ 8.0/10

A security researcher accidentally discovered that e164.arpa, a long-dormant ENUM DNS infrastructure originally designed to map phone numbers to internet resources, was still receiving large volumes of DNS queries containing routing data for phone calls to U.S. military bases. By setting up a passive DNS listener on the open e164.arpa infrastructure, she inadvertently captured hundreds of thousands of call routing records from SIP servers processing calls to military installations. This incident exposes a critical and long-overlooked security vulnerability: sensitive telephony routing metadata for military bases was being broadcast through a public, poorly-monitored DNS infrastructure with no access controls. It raises serious questions about telecommunications supply chain security, the lack of maintenance of legacy internet infrastructure, and whether classified information could be inadvertently exposed through forgotten protocols. The researcher used ENUM \(defined in RFC 2916/6116\), which maps E.164 phone numbers to URIs by reversing digits and appending e164.arpa \(e.g., +1-555-4242 becomes 2.4.2.4.5.5.5.1.e164.arpa\). The infrastructure, managed by IANA with country-specific subdomains, was largely abandoned after ENUM failed commercially in the 2000s, but some SIP servers never stopped sending queries to it. The researcher responsibly disclosed the issue but received no bounty or reward.

hackernews · gavide · Aug 21, 13:11 · [Discussion](https://news.ycombinator.com/item?id=49387570)

**Background**: ENUM \(Telephone Number Mapping\) was developed by the IETF starting in 1999 as a way to bridge traditional telephony \(E.164 numbers\) with internet protocols, allowing DNS to resolve phone numbers into SIP URIs or other internet resources. The e164.arpa domain was assigned by the ITU to store these mappings, and trials ran in multiple countries including the US starting around 2003. However, ENUM never achieved widespread adoption due to privacy concerns, regulatory hurdles, and competing alternatives. Today, public ENUM is largely dormant, with a 2026 RIPE Labs review finding that half of the existing delegations have DNS problems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Telephone_number_mapping">Telephone number mapping - Wikipedia</a></li>
<li><a href="https://icannwiki.org/ENUM">ENUM - ICANNWiki RFC 6116: The E.164 to Uniform Resource Identifiers (URI ... RFC 2916 - E.164 number and DNS - IETF Datatracker Telephone number mapping - Wikipedia ENUM – DNS based Call Routing | Nick vs Networking Operational Review of Public ENUM Under e164.arpa | RIPE Labs</a></li>
<li><a href="https://nickvsnetworking.com/enum-dns-based-call-routing/">ENUM – DNS based Call Routing | Nick vs Networking</a></li>

</ul>
</details>

**Discussion**: Community commenters expressed amazement that the researcher wasn&\#x27;t jailed for this kind of disclosure, noting that authorities often react harshly to such discoveries. One commenter pointed out that e164.arpa isn&\#x27;t truly dead—private companies still use ENUM queries via VPNs for number porting services. Others discussed related protocols like TRIP \(Telephony Routing over IP\) and lamented that the researcher wasn&\#x27;t rewarded for responsibly reporting a significant security issue that only got attention because of the military connection.

**Tags**: `#security`, `#dns`, `#telephony`, `#vulnerability-disclosure`, `#networking`

---

<a id="item-2"></a>
## [Nvidia is acquiring Poolside&\#x27;s &quot;Model Factory&quot; and 109 employees for $6 billion](https://the-decoder.com/nvidia-is-acquiring-poolsides-model-factory-and-109-employees-for-6-billion/) ⭐️ 8.0/10

Nvidia is acquiring Poolside&\#x27;s AI model-building software and 109 employees for $6 billion, expanding its AI development capabilities.

rss · The Decoder · Aug 21, 08:27

**Tags**: `#Nvidia`, `#acquisition`, `#AI infrastructure`, `#Poolside`, `#model development`

---

<a id="item-3"></a>
## [机器人的GPT-3时刻真·来了！卡卡西上身，看3秒就学会新动作](https://www.qbitai.com/2026/08/476596.html) ⭐️ 8.0/10

A new robotics system achieves one-shot imitation learning, mastering new actions from just 3 seconds of video demonstration, potentially marking a &\#x27;GPT-3 moment&\#x27; for the robotics field.

rss · 量子位 · Aug 21, 07:17

**Tags**: `#robotics`, `#imitation-learning`, `#one-shot-learning`, `#AI-breakthrough`, `#embodied-AI`

---

<a id="item-4"></a>
## [Position: Collusion Risks Among AI Reasoning Agents Justify Certification Requirements for Making Market Decisions](https://arxiv.org/abs/2608.18078) ⭐️ 8.0/10

A position paper arguing that AI agents with chain-of-thought reasoning are prone to tacit collusion in market settings, demonstrated via DeepSeek-R1 experiments in Bertrand oligopolies, with the recommendation that such agents require behavioral certification before economic deployment.

rss · arXiv cs.AI · Aug 21, 04:00

**Tags**: `#AI safety`, `#multi-agent systems`, `#market economics`, `#chain-of-thought reasoning`, `#AI policy`

---

<a id="item-5"></a>
## [Model Cards Insufficient for Governing Open-Weight Foundation Models](https://arxiv.org/abs/2608.18086) ⭐️ 8.0/10

A position paper analyzes 500 Hugging Face model cards and argues that current model cards alone are insufficient for downstream governance of open-weight foundation models \(OWFMs\). The authors propose a multi-layered governance framework integrating model cards, acceptable use policies \(AUPs\), and licenses as complementary components. As open-weight models like DeepSeek and Qwen become mainstream, governance gaps pose real safety risks for downstream developers and users. This paper highlights an urgent need for integrated informational, normative, and legal artifacts to safely deploy OWFMs across the AI ecosystem. The authors identify three specific safety gaps in current model cards: model heritage, alignment provenance, and empirically observed behaviors. They also argue that standard open-source licenses \(OSLs\) may weaken the enforceability of AUPs and are poorly suited for OWFMs.

rss · arXiv cs.AI · Aug 21, 04:00

**Background**: Open-weight foundation models release trained model parameters for download, but unlike fully open-source AI, they may withhold training data, training code, or full license freedoms. Model cards are standardized documentation artifacts that describe a model&\#x27;s intended use, limitations, and evaluation metrics, and are widely hosted on platforms like Hugging Face. Acceptable Use Policies \(AUPs\) set normative rules for how a model may be used, while licenses provide legal terms governing redistribution and modification.

<details><summary>References</summary>
<ul>
<li><a href="https://osfoundry.io/articles/open-weight-vs-open-source-models">Open-Weight vs Open-Source AI Models: What&#x27;s the Difference ...</a></li>
<li><a href="https://www.snowflake.com/en/artificial-intelligence/ai-governance/ai-transparency/">What Is AI Transparency ? Requirements and Best... | Snowflake</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#open-weight models`, `#model cards`, `#AI safety`, `#foundation models`

---