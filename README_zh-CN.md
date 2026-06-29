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

- **从近期 X/Twitter 样本中筛选出 11 个 Seed-Audio 1.0 使用案例，原始可用样本为 93 条。**
- 覆盖方向：音频优先视频工作流, 音频剧与场景生成, 参考声音与角色配音探索, 工具与服务商集成, 社交旁白、拟音与成本测试。
- 每个案例都包含原始来源、创作者署名、使用结论、证据类型和发布日期。
- 你可以用这个仓库查找真实工作流、比较优势和限制、发现服务商路径，并把实现工作导向 EvoLink。

> [!NOTE]
> 本地化 README 与英文源文件保持相同的案例顺序、链接、锚点和署名。

> [!NOTE]
> 本仓库优先收录具体工作流证据，而不是纯宣传：演示、设置说明、服务商发布、上手评估和明确限制。

[更新日志](docs/update-log.md) | [维护指南](docs/maintenance.md) | [案例标注审计](docs/case-label-audit.md) | [案例数据](data/use-cases.json) | [预设音色文档](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices)

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
| [工具与服务商集成](#tool-provider-integrations) | 案例 7 |
| [社交旁白、拟音与成本测试](#social-narration-foley-cost-tests) | 案例 9, 案例 11 |
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
| [案例 4: 带环境声的两分钟对白](#case-4) | 用脚本格式编写音频剧 prompt，同时指定环境声、角色声音、背景音乐和逐句表演方向。 | 教程 |
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

<a id="social-narration-foley-cost-tests"></a>
## 社交旁白、拟音与成本测试

| 案例 | 展示重点 | 类型 |
|---|---|---|
| [案例 9: 社交故事旁白内容引擎](#case-9) | 把公开文字故事帖转成音频优先娱乐内容，并评估它能否成为可重复的内容引擎。 | 演示 |
| [案例 11: 低成本测试声音表演与拟音](#case-11) | 在投入下游视频生成前，把 Seed-Audio 作为声音表演和拟音的低成本测试层。 | 评估 |

<a id="case-1"></a>
### 案例 1: [用六人音频引导 Seedance 视频](https://x.com/gokayfem/status/2070429287950188547) (作者 [@gokayfem](https://x.com/gokayfem))

**构建音频优先的视频工作流：先用公开 Seed Audio prompt 生成六个角色对白和背景音效，再进入图像与 Seedance 视频生成。**

- 证据来源：原推公开了实际 Seed Audio 设置：雨夜逃亡面包车场景、六个具名角色、不同声线方向、短对白、发动机怠速、车顶雨声和背景音效，并同时给出后续 Nano Banana Pro 图像 prompt 与 Seedance 2.0 视频 prompt。
- 可复制做法：当音频需要主导整段视频时，先写清角色表、每个角色的声音质感、短句对白和持续环境声，再把它作为后续视频节奏和情绪的参考。
- 实际流程：先生成完整多人对白和环境声底，再生成匹配人物轮廓与氛围的关键视觉图，最后把音频和视觉一起交给 Seedance 做最终运动画面。
- 注意事项：这个来源能证明工作流和 prompt 结构有学习价值，但不能保证长场景里每个角色都永久稳定。正式生产前要专门测试说话人区分、节奏和转场。

[![案例 1 video preview](media/cases/case-01.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-01.mp4)

[打开视频文件](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-01.mp4)

类型: 教程 | 日期: 2026-06-26

<a id="case-2"></a>
### 案例 2: [多片段故事视频的音频规划](https://x.com/gavinpurcell/status/2070246132341727506) (作者 [@gavinpurcell](https://x.com/gavinpurcell))

**评估多片段故事视频中的 agentic soundscape 生成，并保留音效与画面动作仍可能不匹配的限制。**

- 证据来源：作者从一条一分钟多片段低清故事视频出发，明确指出 Seedance 多片段故事里的音频一致性很难，然后测试把视频上下文交给 Claude Code、Codex，并配合 FAL key 生成音景。
- 可复制做法：把 Seed-Audio 当成已有视频的音频修复或规划层，尤其适合一个视频里包含多个镜头、转场、环境声和动作音效的情况。
- 实际流程：先让 agent 读取视频情境并产出逐镜头音频计划，再生成背景声、环境声或音效，最后按每个片段核对声音是否跟画面动作对齐。
- 注意事项：同作者后续说明部分 SFX 仍然没有准确匹配画面动作，所以它是评估案例，不是完整教程。它的价值在于教你如何测试，以及提醒多片段视频仍有错配风险。

[![案例 2 video preview](media/cases/case-02.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-02.mp4)

[打开视频文件](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-02.mp4)

类型: 评估 | 日期: 2026-06-25

<a id="case-3"></a>
### 案例 3: [音频优先的 Seedance 参考工作流](https://x.com/EvoLinkAi/status/2070722722217578562) (作者 [@EvoLinkAi](https://x.com/EvoLinkAi))

**采用官方三步流程：先生成 Seed-Audio，再创建关键视觉图，最后把音频和视觉一起作为 Seedance 2 reference-to-video 的参考。**

- 证据来源：来源明确给出三步流程：先用 Seed-Audio 1.0 生成音频，再生成关键视觉图，最后把音频和视觉一起作为 Seedance 2 reference-to-video 的参考。
- 可复制做法：当音乐、旁白、环境声或节奏应该先决定视频走向时，不要先做视频再补声音，而是先把情绪和时间线写进音频 prompt。
- 实际流程：先确定音频里的情绪弧线、旁白节奏和环境声，再创建匹配场景的图片，最后把两者共同作为参考，让视频模型同时获得时间和视觉方向。
- 注意事项：这是官方式工作流模板，不是独立 benchmark。它适合作为起点，但仍需要单独检查 lip-sync、镜头节奏，以及视频是否真的跟随音频 cue。

[![案例 3 video preview](media/cases/case-03.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-03.mp4)

[打开视频文件](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-03.mp4)

类型: 教程 | 日期: 2026-06-27

<a id="case-4"></a>
### 案例 4: [带环境声的两分钟对白](https://x.com/tarumainfo/status/2071255504907891186) (作者 [@tarumainfo](https://x.com/tarumainfo))

**用脚本格式编写音频剧 prompt，同时指定环境声、角色声音、背景音乐和逐句表演方向。**

- 证据来源：原推给出一个两分钟音频剧 prompt/script，包含 INTENT、AESTHETIC、EXECUTION 结构，并写明环境声、背景音乐、两个角色声线、情绪表达和逐句对白。
- 可复制做法：需要做音频剧而不是单人旁白时，可以照这个结构写：先定义空间和环境声，再定义角色声音，最后在台词里嵌入短促的表演方向。
- 实际流程：把场景写成短剧本，控制每句表演指令不要太长，同时保留持续背景音，让模型既能跟随情绪，也能保持场景质感。
- 注意事项：作者认为结果较好地跟随了 prompt，但长音频仍要检查一致性。生产内容最好把长场景拆成多个 beat，避免角色情绪或背景音乐中途漂移。

[![案例 4 video preview](media/cases/case-04.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-04.mp4)

[打开视频文件](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-04.mp4)

类型: 教程 | 日期: 2026-06-28

<a id="case-5"></a>
### 案例 5: [博物馆导览式场景对白](https://x.com/TomLikesRobots/status/2070923534449119424) (作者 [@TomLikesRobots](https://x.com/TomLikesRobots))

**测试场景级对白推理：Seed-Audio 能从紧凑情境 prompt 中生成台词、表达方式和角色声音。**

- 证据来源：作者给出的紧凑情境是：博物馆导览员向困惑访客解释 crossing the Rubicon 为什么表示越过不可回头的临界点。帖子说明 Seed Audio 生成了对白、表达方式和角色声音。
- 可复制做法：当你不想逐句写剧本，而是希望模型从一个教育场景中推导短对白时，可以给角色关系、要解释的概念和对话语境。
- 实际流程：输入角色身份、解释对象、听众困惑点和语气要求；生成后重点检查讲话是否自然，以及解释是否准确。
- 注意事项：这是演示案例，因为来源证明了场景级语言推理和自然表达，但没有提供完整生产流程。用于教育内容时必须复核事实正确性。

[![案例 5 video preview](media/cases/case-05.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-05.mp4)

[打开视频文件](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-05.mp4)

类型: 演示 | 日期: 2026-06-27

<a id="case-6"></a>
### 案例 6: [参考声音 MC 工作流](https://x.com/JPAI_HEAVEN/status/2070842306329227264) (作者 [@JPAI_HEAVEN](https://x.com/JPAI_HEAVEN))

**从参考素材生成固定 MC 声音，将音频切分后作为 Seedance 2.0 lip-sync 视频参考。**

- 证据来源：原推描述了参考声音工作流：先用来源 voice 作为参考，在 Seed Audio 里生成约一分钟 MC 音频；再把生成音频切分，并交给 Seedance 2.0 做 lip-sync 视频。
- 可复制做法：当系列内容需要固定主持人、播报员或 MC 声音时，可以先做一段较长的干净参考音频，再切成可复用片段。
- 实际流程：先生成一分钟左右的主持声音，挑选发音稳定的片段，按视频台词切分，再作为视频生成或 lip-sync 的声音参考。
- 注意事项：作者明确记录了下游视频生成后声音会轻微变化，因此这个案例是工作流教程，不是声音身份稳定性的保证。最终片段仍需要后期校正。

[![案例 6 video preview](media/cases/case-06.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-06.mp4)

[打开视频文件](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-06.mp4)

类型: 教程 | 日期: 2026-06-27

<a id="case-7"></a>
### 案例 7: [Claude MCP 旁白与多语言配音集成](https://x.com/higgsfield/status/2070916672106680360) (作者 [@higgsfield](https://x.com/higgsfield))

**通过 Higgsfield MCP 在 Claude 内完成旁白、声音克隆和多语言配音，Seed Audio 1.0 是其中的音频能力之一。**

- 证据来源：Higgsfield 表示 Claude 可以通过其 MCP 集成生成音频，覆盖旁白、声音克隆和 50 多种语言配音，能力栈中包含 Seed Audio 1.0。
- 可复制做法：这个案例适合理解 agent 或 no-code 访问路径：创作者不一定直接调用音频 endpoint，也可以在 Claude 里通过 MCP 服务商完成配音任务。
- 实际流程：从短旁白或配音请求开始，在 Claude 内调用 MCP 生成，再检查输出语言、声音身份和媒体工作流是否满足目标。
- 注意事项：这是集成案例，不是质量评测。来源证明了可访问路径和产品入口，但不能独立证明 50 多种语言的配音质量都可靠。

[![案例 7 video preview](media/cases/case-07.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-07.mp4)

[打开视频文件](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-07.mp4)

类型: 集成 | 日期: 2026-06-27

<a id="case-8"></a>
### 案例 8: [参考音频质量与高声线限制](https://x.com/genel_ai/status/2070438167019409582) (作者 [@genel_ai](https://x.com/genel_ai))

**基于实际使用评估日语稳定性、情绪跟随、参考音频精度，以及高声线机械感风险。**

- 证据来源：作者报告了日语实测体验：Seed Audio 的日语语音比 Seedance 2.0 原生音频更稳定，能跟随台词情绪，参考音频精度较高，参考音频最长 30 秒，同时记录不能同时使用音频和图像 reference，高声线更机械。
- 可复制做法：把这个案例当成非英语语音质量检查清单：稳定性、情绪跟随、参考精度、reference 模式限制和高 pitch 风险。
- 实际流程：分别用普通声线和高声线跑短片段，跟参考音频做对比；如果你还需要图像引导，要单独测，因为来源指出音频和图像 reference 不能合用。
- 注意事项：这个案例的核心不是宣称 Seed-Audio 永远更好，而是把表现好和需要谨慎的地方都列出来，所以标注为评估。

[![案例 8 video preview](media/cases/case-08.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-08.mp4)

[打开视频文件](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-08.mp4)

类型: 评估 | 日期: 2026-06-26

<a id="case-9"></a>
### 案例 9: [社交故事旁白内容引擎](https://x.com/deepwhitman/status/2071485165390704837) (作者 [@deepwhitman](https://x.com/deepwhitman))

**把公开文字故事帖转成音频优先娱乐内容，并评估它能否成为可重复的内容引擎。**

- 证据来源：作者用 Seed Audio 1.0 给一条热门 AITA 风格文字帖做旁白，并把这种形式明确描述为可能的 viral content engine。同作者回复补充了原始故事链接。
- 可复制做法：当你想测试文字型社交内容能否变成低成本短视频娱乐内容时，可以用它作为 text-to-narration 模板。
- 实际流程：选择有公开来源的文字故事，拆成旁白段落，生成声音，再搭配简单视觉、字幕或视频素材，最后观察这种格式能否重复生产。
- 注意事项：这是演示案例，不等于版权或增长已经成立。正式使用时要处理授权和来源标注，也要用真实发布数据验证它是否能成为内容渠道。

[![案例 9 video preview](media/cases/case-09.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-09.mp4)

[打开视频文件](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-09.mp4)

类型: 演示 | 日期: 2026-06-29

<a id="case-10"></a>
### 案例 10: [图像引导的角色声音探索](https://x.com/tc50501/status/2070498347824337389) (作者 [@tc50501](https://x.com/tc50501))

**用参考图片做早期角色声音 casting，同时把 pitch 和 tone 稳定性视为未解决的生产风险。**

- 证据来源：作者测试 image-to-audio，只传入女性角色参考图，生成三条约十秒台词；结果两条声质方向接近，一条明显偏高。
- 可复制做法：把图像引导音频用于早期角色声音 casting：先探索一个角色可能听起来是什么方向，而不是直接锁定最终配音。
- 实际流程：用同一角色图测试多条短台词，对比 pitch、tone 和角色感是否一致，只保留跨多条台词仍稳定的候选。
- 注意事项：来源本身指出音高和音色稳定性还不适合固定电影角色声生产，所以它是评估案例，价值在于定义可用的探索阶段和明确风险。

![案例 10 media](media/cases/case-10.jpg)

类型: 评估 | 日期: 2026-06-26

<a id="case-11"></a>
### 案例 11: [低成本测试声音表演与拟音](https://x.com/TomLikesRobots/status/2070288519684108353) (作者 [@TomLikesRobots](https://x.com/TomLikesRobots))

**在投入下游视频生成前，把 Seed-Audio 作为声音表演和拟音的低成本测试层。**

- 证据来源：作者报告早期测试中，voice acting 和 foley 比 Seedance 2 原生音频更好，并提到 15 秒音频测试成本只有几美分。
- 可复制做法：把 Seed-Audio 用作低成本预生产测试层，在投入视频生成前先验证声音表演、拟音和环境声方向是否值得继续。
- 实际流程：先生成 10 到 15 秒短音频，对比它和视频模型原生音频的表现；只有当声音方向足够强时，再进入下游视频生成。
- 注意事项：评论里补充了 reference voice conversion 可能失败，以及生成音频如何最好地进入 Seedance lip-sync 仍未解决。因此它是评估案例，不是完整最终管线。

[![案例 11 video preview](media/cases/case-11.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-11.mp4)

[打开视频文件](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-11.mp4)

类型: 评估 | 日期: 2026-06-25

<a id="acknowledge"></a>
## 致谢

本仓库在案例级别链接公开创作者和服务商内容。每个案例标题都会标注公开来源。

如果来源链接失效、署名错误，或某个说法没有得到链接来源支持，欢迎提交修正。
