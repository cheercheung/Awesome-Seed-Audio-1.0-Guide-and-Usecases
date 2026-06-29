<div align="center">

<a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=banner&utm_campaign=awesome-seed-audio-1.0-usecases"><img src="images/en.png" alt="Seed-Audio 1.0 usecase repository banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Try it on Evolink](https://img.shields.io/badge/Try_it_on-Evolink-black)](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=badge&utm_campaign=awesome-seed-audio-1.0-usecases)
[![Website](https://img.shields.io/badge/Website-Live-orange)](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=badge&utm_campaign=awesome-seed-audio-1.0-usecases)
[![Docs](https://img.shields.io/badge/Docs-Read-blue)](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=readme&utm_campaign=awesome-seed-audio-1.0-usecases)

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>

# Seed-Audio 1.0 使用案例：旁白、音频剧、参考声音与音频优先视频工作流

## 介绍

欢迎来到 Seed-Audio 1.0 高信号使用案例仓库。

**我们基于公开 X/Twitter 来源和 EvoLink 文档，整理 Seed-Audio 1.0 的真实使用案例、创作者工作流、平台集成、评估和实践限制。**

本简体中文 README 保留公开来源链接、作者署名和锚点，同时翻译用户可见说明文字。

[在 EvoLink 上试用 Seed-Audio 1.0](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=readme&utm_campaign=awesome-seed-audio-1.0-usecases)

## 概览

- **从近期 X/Twitter 样本中筛选出 12 个 Seed-Audio 1.0 使用案例，原始可用样本为 93 条。**
- 覆盖方向：音频优先视频工作流, 音频剧与场景生成, 参考声音与角色配音探索, 工具与服务商集成, 社交旁白、拟音与成本测试。
- 每个案例都包含原始来源、创作者署名、使用结论、证据类型和发布日期。
- 你可以用这个仓库查找真实工作流、比较优势和限制、发现服务商路径，并把实现工作导向 EvoLink。

> [!NOTE]
> 本地化 README 与英文源文件保持相同的案例顺序、链接、锚点和署名。

> [!NOTE]
> 本仓库优先收录具体工作流证据，而不是纯宣传：演示、设置说明、服务商发布、上手评估和明确限制。

[更新日志](docs/update-log.md) | [维护指南](docs/maintenance.md) | [案例数据](data/use-cases.json) | [预设音色文档](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices)

## API 快速访问

通过 EvoLink 音频生成 API 使用 Seed-Audio 1.0。先在 [EvoLink](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=readme&utm_campaign=awesome-seed-audio-1.0-usecases) 获取 API key，然后在请求前设置 `EVOLINK_API_KEY`。

```bash
export EVOLINK_API_KEY="your_api_key_here"

curl --request POST \
  --url https://api.evolink.ai/v1/audios/generations \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "doubao-seed-audio-1-0",
    "prompt": "Create a 15-second calm product video audio bed with soft music, a clean studio ambience, and gentle narration.",
    "format": "mp3",
    "sample_rate": 24000
  }'
```

响应会创建一个异步任务。轮询 `GET /v1/tasks/{task_id}`，直到状态变为 `completed`、`failed` 或 `cancelled`。

配套 API 与 skill 仓库：[doubao-seed-audio-api-skill](https://github.com/EvoLinkAI/doubao-seed-audio-api-skill)。

## 目录

| 章节 | 案例 |
|---|---|
| [音频优先视频工作流](#audio-first-video) | 案例 1, 案例 2, 案例 3 |
| [音频剧与场景生成](#audio-drama-scene-generation) | 案例 4, 案例 5 |
| [参考声音与角色配音探索](#voice-reference-character-casting) | 案例 6, 案例 8, 案例 10 |
| [工具与服务商集成](#tool-provider-integrations) | 案例 7, 案例 11 |
| [社交旁白、拟音与成本测试](#social-narration-foley-cost-tests) | 案例 9, 案例 12 |
| [致谢](#acknowledge) | 来源致谢与修正政策 |

<a id="audio-first-video"></a>
## 音频优先视频工作流

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [案例 1: 用六人音频引导 Seedance 视频](#case-1) | 构建音频优先的视频工作流：先用公开 Seed Audio prompt 生成六个角色对白和背景音效，再进入图像与 Seedance 视频生成。 | 教程 |
| [案例 2: 多片段故事视频的音频规划](#case-2) | 评估多片段故事视频中的 agentic soundscape 生成，并保留音效与画面动作仍可能不匹配的限制。 | 评估 |
| [案例 3: 音频优先的 Seedance 参考工作流](#case-3) | 采用官方三步流程：先生成 Seed-Audio，再创建关键视觉图，最后把音频和视觉一起作为 Seedance 2 reference-to-video 的参考。 | 教程 |

<a id="audio-drama-scene-generation"></a>
## 音频剧与场景生成

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [案例 4: 带环境声的两分钟对白](#case-4) | 用脚本格式编写音频剧 prompt，同时指定环境声、角色声音、背景音乐和逐句表演方向。 | 演示 |
| [案例 5: 博物馆导览式场景对白](#case-5) | 测试场景级对白推理：Seed-Audio 能从紧凑情境 prompt 中生成台词、表达方式和角色声音。 | 演示 |

<a id="voice-reference-character-casting"></a>
## 参考声音与角色配音探索

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [案例 6: 参考声音 MC 工作流](#case-6) | 从参考素材生成固定 MC 声音，将音频切分后作为 Seedance 2.0 lip-sync 视频参考。 | 教程 |
| [案例 8: 参考音频质量与高声线限制](#case-8) | 基于实际使用评估日语稳定性、情绪跟随、参考音频精度，以及高声线机械感风险。 | 评估 |
| [案例 10: 图像引导的角色声音探索](#case-10) | 用参考图片做早期角色声音 casting，同时把 pitch 和 tone 稳定性视为未解决的生产风险。 | 评估 |

<a id="tool-provider-integrations"></a>
## 工具与服务商集成

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [案例 7: Claude MCP 旁白与多语言配音集成](#case-7) | 通过 Higgsfield MCP 在 Claude 内完成旁白、声音克隆和多语言配音，Seed Audio 1.0 是其中的音频能力之一。 | 集成 |
| [案例 11: WaveSpeedAI 文本、声音与图像引导音频](#case-11) | 跟踪服务商入口：文本转自然语音、音景生成、预设声音、参考音频、图像引导音频和调参控制。 | 集成 |

<a id="social-narration-foley-cost-tests"></a>
## 社交旁白、拟音与成本测试

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [案例 9: 社交故事旁白内容引擎](#case-9) | 把公开文字故事帖转成音频优先娱乐内容，并评估它能否成为可重复的内容引擎。 | 演示 |
| [案例 12: 低成本测试声音表演与拟音](#case-12) | 在投入下游视频生成前，把 Seed-Audio 作为声音表演和拟音的低成本测试层。 | 评估 |

<a id="case-1"></a>
### 案例 1: [用六人音频引导 Seedance 视频](https://x.com/gokayfem/status/2070429287950188547) (作者 [@gokayfem](https://x.com/gokayfem))

**构建音频优先的视频工作流：先用公开 Seed Audio prompt 生成六个角色对白和背景音效，再进入图像与 Seedance 视频生成。**

原推公开了雨夜逃亡面包车场景的 Seed Audio prompt，并同时给出 Nano Banana Pro 图像 prompt 和 Seedance 2.0 视频 prompt。这是用生成音频指导后续视频节奏、对白和环境声的强证据。

[![案例 1 media preview](media/cases/case-01.jpg)](media/cases/case-01.mp4)

类型: 教程 | 日期: 2026-06-26

<a id="case-2"></a>
### 案例 2: [多片段故事视频的音频规划](https://x.com/gavinpurcell/status/2070246132341727506) (作者 [@gavinpurcell](https://x.com/gavinpurcell))

**评估多片段故事视频中的 agentic soundscape 生成，并保留音效与画面动作仍可能不匹配的限制。**

作者说明 Seedance 多片段故事里的音频一致性很难，于是测试把已有的一分钟低清视频交给 Claude Code 和 Codex，并配合 FAL key 生成音景。同作者后续补充说结果还可以，但部分 SFX 没有准确匹配画面，所以这个案例必须保留限制。

[![案例 2 media preview](media/cases/case-02.jpg)](media/cases/case-02.mp4)

类型: 评估 | 日期: 2026-06-25

<a id="case-3"></a>
### 案例 3: [音频优先的 Seedance 参考工作流](https://x.com/EvoLinkAi/status/2070722722217578562) (作者 [@EvoLinkAi](https://x.com/EvoLinkAi))

**采用官方三步流程：先生成 Seed-Audio，再创建关键视觉图，最后把音频和视觉一起作为 Seedance 2 reference-to-video 的参考。**

原推明确说明，音频优先能给视频模型更强的音乐、旁白、环境声和时间节奏方向。同 thread 还说明 Seed-Audio 面向完整音频生成，不只是文本转语音。

[![案例 3 media preview](media/cases/case-03.jpg)](media/cases/case-03.mp4)

类型: 教程 | 日期: 2026-06-27

<a id="case-4"></a>
### 案例 4: [带环境声的两分钟对白](https://x.com/tarumainfo/status/2071255504907891186) (作者 [@tarumainfo](https://x.com/tarumainfo))

**用脚本格式编写音频剧 prompt，同时指定环境声、角色声音、背景音乐和逐句表演方向。**

原推包含一个两分钟幽闭家庭对峙音频剧 prompt，使用 INTENT、AESTHETIC、EXECUTION 结构，并明确灯管嗡鸣、冰箱振动、两个角色声线、情绪表达和完整台词，是最强的可复用 prompt 案例之一。

[![案例 4 media preview](media/cases/case-04.jpg)](media/cases/case-04.mp4)

类型: 演示 | 日期: 2026-06-28

<a id="case-5"></a>
### 案例 5: [博物馆导览式场景对白](https://x.com/TomLikesRobots/status/2070923534449119424) (作者 [@TomLikesRobots](https://x.com/TomLikesRobots))

**测试场景级对白推理：Seed-Audio 能从紧凑情境 prompt 中生成台词、表达方式和角色声音。**

作者给 Seed-Audio 的 prompt 是让博物馆导览员向困惑访客解释 crossing the Rubicon。模型生成了对白、语气和角色声音；作者随后用 Nano Banana 生成匹配图像，并用 Seedance 2 做成视频。

[![案例 5 media preview](media/cases/case-05.jpg)](media/cases/case-05.mp4)

类型: 演示 | 日期: 2026-06-27

<a id="case-6"></a>
### 案例 6: [参考声音 MC 工作流](https://x.com/JPAI_HEAVEN/status/2070842306329227264) (作者 [@JPAI_HEAVEN](https://x.com/JPAI_HEAVEN))

**从参考素材生成固定 MC 声音，将音频切分后作为 Seedance 2.0 lip-sync 视频参考。**

原推描述了两步测试：先用素材 voice 作为参考，在 Seed Audio 里生成约一分钟 MC 音频；再把音频切分并交给 Seedance 2.0 视频化。作者也记录了实际限制：进入视频生成后声音会轻微变化，需要后期编辑。

[![案例 6 media preview](media/cases/case-06.jpg)](media/cases/case-06.mp4)

类型: 教程 | 日期: 2026-06-27

<a id="case-7"></a>
### 案例 7: [Claude MCP 旁白与多语言配音集成](https://x.com/higgsfield/status/2070916672106680360) (作者 [@higgsfield](https://x.com/higgsfield))

**通过 Higgsfield MCP 在 Claude 内完成旁白、声音克隆和多语言配音，Seed Audio 1.0 是其中的音频能力之一。**

Higgsfield 表示 Claude 可以通过其 MCP 集成生成音频，覆盖 voiceover、voice cloning 和 50 多种语言配音，由 Seed Audio 1.0 与 ElevenLabs v3 驱动。同作者回复给出了 MCP 访问链接，因此这是平台集成案例，不是单独 API 教程。

[![案例 7 media preview](media/cases/case-07.jpg)](media/cases/case-07.mp4)

类型: 集成 | 日期: 2026-06-27

<a id="case-8"></a>
### 案例 8: [参考音频质量与高声线限制](https://x.com/genel_ai/status/2070438167019409582) (作者 [@genel_ai](https://x.com/genel_ai))

**基于实际使用评估日语稳定性、情绪跟随、参考音频精度，以及高声线机械感风险。**

原推报告 Seed Audio 的日语输出比 Seedance 2.0 原生音频更稳定，能跟随台词情绪，参考音频精度较高且最长 30 秒。同时也记录限制：音频和图像不能同时 reference，高声线更容易出现机械感。

[![案例 8 media preview](media/cases/case-08.jpg)](media/cases/case-08.mp4)

类型: 评估 | 日期: 2026-06-26

<a id="case-9"></a>
### 案例 9: [社交故事旁白内容引擎](https://x.com/deepwhitman/status/2071485165390704837) (作者 [@deepwhitman](https://x.com/deepwhitman))

**把公开文字故事帖转成音频优先娱乐内容，并评估它能否成为可重复的内容引擎。**

作者用 Seed Audio 1.0 旁白化了一条热门 AITA 风格帖子，并明确把结果设想为 viral content engine。同作者回复补充了 original post 链接，因此这是有真实文本来源的 text-to-narration 工作流。

[![案例 9 media preview](media/cases/case-09.jpg)](media/cases/case-09.mp4)

类型: 演示 | 日期: 2026-06-29

<a id="case-10"></a>
### 案例 10: [图像引导的角色声音探索](https://x.com/tc50501/status/2070498347824337389) (作者 [@tc50501](https://x.com/tc50501))

**用参考图片做早期角色声音 casting，同时把 pitch 和 tone 稳定性视为未解决的生产风险。**

作者测试 image-to-audio：只传入女性角色参考图，生成三条约十秒台词。结果两条声质方向接近，一条明显偏高，所以它支持早期角色声音探索，但不支持直接作为最终锁定角色声的生产流程。

![案例 10 media](media/cases/case-10.jpg)

类型: 评估 | 日期: 2026-06-26

<a id="case-11"></a>
### 案例 11: [WaveSpeedAI 文本、声音与图像引导音频](https://x.com/wavespeed_ai/status/2071214531280543772) (作者 [@wavespeed_ai](https://x.com/wavespeed_ai))

**跟踪服务商入口：文本转自然语音、音景生成、预设声音、参考音频、图像引导音频和调参控制。**

WaveSpeedAI 宣布 Seed Audio 1.0 已上线，并列出自然语音、预设声音、参考音频引导、图像引导音频，以及 speed、volume、pitch、format 控制。这是实现路径规划所需的强服务商证据。

[![案例 11 media preview](media/cases/case-11.jpg)](media/cases/case-11.mp4)

类型: 集成 | 日期: 2026-06-28

<a id="case-12"></a>
### 案例 12: [低成本测试声音表演与拟音](https://x.com/TomLikesRobots/status/2070288519684108353) (作者 [@TomLikesRobots](https://x.com/TomLikesRobots))

**在投入下游视频生成前，把 Seed-Audio 作为声音表演和拟音的低成本测试层。**

原推报告早期测试中，voice acting 和 foley 比 Seedance 2 原生音频更好，15 秒测试只需几美分。评论也补充了有价值限制：参考声音转换可能失败，生成音频与 Seedance lip-sync 的最佳工作流仍未解决。

[![案例 12 media preview](media/cases/case-12.jpg)](media/cases/case-12.mp4)

类型: 评估 | 日期: 2026-06-25

<a id="acknowledge"></a>
## 致谢

本仓库在案例级别链接公开创作者和服务商内容。每个案例标题都会标注公开来源。

如果来源链接失效、署名错误，或某个说法没有得到链接来源支持，欢迎提交修正。
