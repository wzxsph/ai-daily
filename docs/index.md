---
layout: default
title: Home
---

# AI Daily

<div id="lang-zh" class="lang-section" markdown="1">

每天北京时间 07:30，从国内外 AI 官方博客、技术社区、论文源和 GitHub 趋势中筛选最多 15 条值得关注的更新。每条仅提供翻译标题、双语摘要、重要性、背景、社区讨论和原文链接，不转载全文。

## 每日历史 <a class="rss-icon" href="{{ '/feed-zh.xml' | relative_url }}" aria-label="订阅中文"><svg viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M128.081 415.959c0 35.369-28.672 64.041-64.041 64.041S0 451.328 0 415.959s28.672-64.041 64.041-64.041 64.04 28.673 64.04 64.041zm175.66 47.25c-8.354-154.6-132.185-278.587-286.95-286.95C7.656 175.765 0 183.105 0 192.253v48.069c0 8.415 6.49 15.472 14.887 16.018 111.832 7.284 201.473 96.702 208.772 208.772.547 8.397 7.604 14.887 16.018 14.887h48.069c9.149.001 16.489-7.655 15.995-16.79zm144.249.288C439.596 229.677 251.465 40.445 16.503 32.01 7.473 31.686 0 38.981 0 48.016v48.068c0 8.625 6.835 15.645 15.453 15.999 191.179 7.839 344.627 161.316 352.465 352.465.353 8.618 7.373 15.453 15.999 15.453h48.068c9.034-.001 16.329-7.474 16.005-16.504z"/></svg></a>

<ul>
  {% assign zh_posts = site.posts | where: "lang", "zh" %}
  {% for post in zh_posts limit:30 %}
    <li><a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }}</a></li>
  {% else %}
    <li><em>首份简报生成后会显示在这里。</em></li>
  {% endfor %}
</ul>

## 筛选方法

- 重要性评分不低于 7.5，每日总数不超过 15 条。
- 模型/产品 4 条、Agent/开发工具 4 条、GitHub 趋势 3 条、论文 2 条、产业/政策 2 条。
- 聚合同一事件、优先官方原始信源，再补充媒体和社区讨论。
- 中文和英文基于同一批入选内容生成，所有条目保留可点击原文。

## 信源范围

OpenAI、Google DeepMind、Google AI、Hugging Face、GitHub、NVIDIA、TechCrunch、The Decoder、VentureBeat、量子位、arXiv、OSS Insight、Hacker News、Reddit，以及重点 AI 开发工具的 GitHub Releases。

## 项目说明

AI Daily 基于 [Thysrael/Horizon](https://github.com/Thysrael/Horizon) 构建并保留原项目署名，按 [MIT License](https://github.com/wzxsph/ai-daily/blob/main/LICENSE) 使用。本站只做信息筛选与摘要，版权归原作者和原网站所有。

</div>

<div id="lang-en" class="lang-section" markdown="1">

Every day at 07:30 Asia/Shanghai, AI Daily selects up to 15 high-signal updates from international and Chinese official AI blogs, technical communities, papers, and GitHub trends. Each item contains a translated title, bilingual summary, importance, background, community discussion, and a link to the original—never a republished full article.

## Daily Archive <a class="rss-icon" href="{{ '/feed-en.xml' | relative_url }}" aria-label="Subscribe in English"><svg viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M128.081 415.959c0 35.369-28.672 64.041-64.041 64.041S0 451.328 0 415.959s28.672-64.041 64.041-64.041 64.04 28.673 64.04 64.041zm175.66 47.25c-8.354-154.6-132.185-278.587-286.95-286.95C7.656 175.765 0 183.105 0 192.253v48.069c0 8.415 6.49 15.472 14.887 16.018 111.832 7.284 201.473 96.702 208.772 208.772.547 8.397 7.604 14.887 16.018 14.887h48.069c9.149.001 16.489-7.655 15.995-16.79zm144.249.288C439.596 229.677 251.465 40.445 16.503 32.01 7.473 31.686 0 38.981 0 48.016v48.068c0 8.625 6.835 15.645 15.453 15.999 191.179 7.839 344.627 161.316 352.465 352.465.353 8.618 7.373 15.453 15.999 15.453h48.068c9.034-.001 16.329-7.474 16.005-16.504z"/></svg></a>

<ul>
  {% assign en_posts = site.posts | where: "lang", "en" %}
  {% for post in en_posts limit:30 %}
    <li><a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }}</a></li>
  {% else %}
    <li><em>The first briefing will appear here after it is generated.</em></li>
  {% endfor %}
</ul>

## Method

- Importance score of at least 7.5 and no more than 15 items per day.
- Quotas: models/products 4, agents/developer tools 4, GitHub trends 3, research 2, industry/policy 2.
- Duplicate stories are merged; official primary sources take precedence, with media and community context added where useful.
- Chinese and English editions use the same selected items and retain every original link.

## Sources

OpenAI, Google DeepMind, Google AI, Hugging Face, GitHub, NVIDIA, TechCrunch, The Decoder, VentureBeat, QbitAI, arXiv, OSS Insight, Hacker News, Reddit, and GitHub Releases from major AI developer tools.

## Attribution

AI Daily is built on [Thysrael/Horizon](https://github.com/Thysrael/Horizon), preserves its attribution, and uses it under the [MIT License](https://github.com/wzxsph/ai-daily/blob/main/LICENSE). Copyright in linked material remains with its original authors and publishers.

</div>
