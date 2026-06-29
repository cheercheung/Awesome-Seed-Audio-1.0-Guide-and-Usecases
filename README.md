<div align="center">

<a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=banner&utm_campaign=awesome-seed-audio-1.0-usecases"><img src="images/en.png" alt="Seed-Audio 1.0 usecase repository banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Try it on Evolink](https://img.shields.io/badge/Try_it_on-Evolink-black)](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=badge&utm_campaign=awesome-seed-audio-1.0-usecases)
[![Website](https://img.shields.io/badge/Website-Live-orange)](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=badge&utm_campaign=awesome-seed-audio-1.0-usecases)
[![Docs](https://img.shields.io/badge/Docs-Read-blue)](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=readme&utm_campaign=awesome-seed-audio-1.0-usecases)

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>

# Seed-Audio 1.0 Use Cases: Narration, Audio Drama, Reference Voices, And Audio-First Video

## Introduction

Welcome to the Seed-Audio 1.0 high-signal usecase repository.

**We collect real-world usage cases, creator workflows, provider integrations, evaluations, and practical limits for Seed-Audio 1.0, curated from public X/Twitter sources and EvoLink documentation.**

This English source README focuses on source-linked cases with concrete workflow evidence. Each case title links to its public source, and each author handle links to the creator profile.

[Try Seed-Audio 1.0 on EvoLink](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=readme&utm_campaign=awesome-seed-audio-1.0-usecases)

## Overview

- **12 selected Seed-Audio 1.0 cases from 93 accepted recent X/Twitter posts.**
- Covers Audio-First Video Workflows, Audio Drama And Scene Generation, Reference Voice And Character Casting, Tool And Provider Integrations, Social Narration, Foley, And Cost Tests.
- Each case includes the original source, creator attribution, concise usage takeaway, evidence type, and publication date.
- Use this repo to find practical workflows, compare strengths and limits, discover provider routes, and route implementation work to EvoLink.

> [!NOTE]
> Localized README files preserve the same case order, links, anchors, and attribution as the English source.

> [!NOTE]
> The collection favors concrete workflow evidence over hype: demos, setup notes, provider launches, hands-on evaluations, and clearly stated limitations.

[Update log](docs/update-log.md) | [Maintenance guide](docs/maintenance.md) | [Case data](data/use-cases.json) | [Preset voice docs](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices)

## Quick API Access

Use Seed-Audio 1.0 through the EvoLink audio generation API. Get an API key from [EvoLink](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=readme&utm_campaign=awesome-seed-audio-1.0-usecases), then set it as `EVOLINK_API_KEY` before running the request.

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

The response creates an async task. Poll `GET /v1/tasks/{task_id}` until the task reaches `completed`, `failed`, or `cancelled`.

Read the companion API and skill repo: [doubao-seed-audio-api-skill](https://github.com/EvoLinkAI/doubao-seed-audio-api-skill).

## Menu

| Section | Cases |
|---|---|
| [Audio-First Video Workflows](#audio-first-video) | Case 1, Case 2, Case 3 |
| [Audio Drama And Scene Generation](#audio-drama-scene-generation) | Case 4, Case 5 |
| [Reference Voice And Character Casting](#voice-reference-character-casting) | Case 6, Case 8, Case 10 |
| [Tool And Provider Integrations](#tool-provider-integrations) | Case 7, Case 11 |
| [Social Narration, Foley, And Cost Tests](#social-narration-foley-cost-tests) | Case 9, Case 12 |
| [Acknowledge](#acknowledge) | Credits and correction policy |

<a id="audio-first-video"></a>
## Audio-First Video Workflows

| Case | What it shows | Type |
|---|---|---|
| [Case 1: Six-Speaker Audio To Guide Seedance Video](#case-1) | build an audio-first video pipeline where a public Seed Audio prompt creates six-character dialogue and background effects before image and Seedance video generation. | Tutorial |
| [Case 2: Multi-Clip Story Video Audio Planning](#case-2) | evaluate agent-assisted soundscape generation for multi-clip story videos, including the remaining mismatch risk between effects and on-screen action. | Evaluation |
| [Case 3: Audio-First Seedance Reference Workflow](#case-3) | use a three-step official workflow: generate Seed-Audio first, create a key visual, then feed both audio and visual references into Seedance 2 reference-to-video. | Tutorial |

<a id="audio-drama-scene-generation"></a>
## Audio Drama And Scene Generation

| Case | What it shows | Type |
|---|---|---|
| [Case 4: Two-Minute Dialogue With Ambience](#case-4) | write script-format audio drama prompts with ambience, character voices, background music, and line-level performance direction. | Demo |
| [Case 5: Museum Guide Scene-Level Dialogue](#case-5) | test scene-level dialogue reasoning where Seed-Audio writes delivery and character voices from a compact situational prompt. | Demo |

<a id="voice-reference-character-casting"></a>
## Reference Voice And Character Casting

| Case | What it shows | Type |
|---|---|---|
| [Case 6: Reference Voice MC Workflow](#case-6) | generate a recurring MC voice from reference material, split the resulting audio, and use it as a Seedance 2.0 lip-sync reference. | Tutorial |
| [Case 8: Reference Audio Quality And High-Voice Caveat](#case-8) | evaluate Japanese speech stability, emotion following, reference-audio precision, and high-pitch mechanical artifacts from hands-on use. | Evaluation |
| [Case 10: Image-Guided Character Voice Casting](#case-10) | use reference images for early character voice casting while treating pitch and tone stability as unresolved production risks. | Evaluation |

<a id="tool-provider-integrations"></a>
## Tool And Provider Integrations

| Case | What it shows | Type |
|---|---|---|
| [Case 7: Claude MCP Voiceover And Dubbing Integration](#case-7) | route voiceovers, voice cloning, and multilingual dubbing through Claude via Higgsfield MCP, with Seed Audio 1.0 as part of the audio stack. | Integration |
| [Case 11: WaveSpeedAI Text, Voice, Image-Guided Audio](#case-11) | track provider access for text-to-speech, soundscape generation, preset voices, reference audio, image-guided audio, and tuning controls. | Integration |

<a id="social-narration-foley-cost-tests"></a>
## Social Narration, Foley, And Cost Tests

| Case | What it shows | Type |
|---|---|---|
| [Case 9: Narrated Social Story Engine](#case-9) | turn public text-story posts into narrated social entertainment and evaluate whether the format can become a repeatable content engine. | Demo |
| [Case 12: Voice Acting, Foley, And Low-Cost Testing](#case-12) | use Seed-Audio as a low-cost test layer for voice acting and foley before committing to downstream video generation. | Evaluation |

<a id="case-1"></a>
### Case 1: [Six-Speaker Audio To Guide Seedance Video](https://x.com/gokayfem/status/2070429287950188547) (by [@gokayfem](https://x.com/gokayfem))

**build an audio-first video pipeline where a public Seed Audio prompt creates six-character dialogue and background effects before image and Seedance video generation.**

The source publishes the concrete Seed Audio prompt for a rain-soaked getaway van scene, then pairs it with a Nano Banana Pro image prompt and a Seedance 2.0 video prompt. This is strong evidence for using generated audio as timing, dialogue, and ambience guidance for later video generation.

[![Case 1 media preview](media/cases/case-01.jpg)](media/cases/case-01.mp4)

Type: Tutorial | Date: 2026-06-26

<a id="case-2"></a>
### Case 2: [Multi-Clip Story Video Audio Planning](https://x.com/gavinpurcell/status/2070246132341727506) (by [@gavinpurcell](https://x.com/gavinpurcell))

**evaluate agent-assisted soundscape generation for multi-clip story videos, including the remaining mismatch risk between effects and on-screen action.**

The author explains that consistent audio is difficult in Seedance multi-clip stories, then tests a pipeline where an existing one-minute low-resolution video is handed to Claude Code and Codex with a FAL key. A same-author follow-up says the process was acceptable but some sound effects did not match exactly, so this case should preserve the limitation.

[![Case 2 media preview](media/cases/case-02.jpg)](media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-06-25

<a id="case-3"></a>
### Case 3: [Audio-First Seedance Reference Workflow](https://x.com/EvoLinkAi/status/2070722722217578562) (by [@EvoLinkAi](https://x.com/EvoLinkAi))

**use a three-step official workflow: generate Seed-Audio first, create a key visual, then feed both audio and visual references into Seedance 2 reference-to-video.**

The source explicitly states that audio-first generation gives the video model stronger direction for music, narration, ambience, and timing. The surrounding thread also identifies Seed-Audio as full audio generation rather than only text-to-speech.

[![Case 3 media preview](media/cases/case-03.jpg)](media/cases/case-03.mp4)

Type: Tutorial | Date: 2026-06-27

<a id="case-4"></a>
### Case 4: [Two-Minute Dialogue With Ambience](https://x.com/tarumainfo/status/2071255504907891186) (by [@tarumainfo](https://x.com/tarumainfo))

**write script-format audio drama prompts with ambience, character voices, background music, and line-level performance direction.**

The source includes a two-minute claustrophobic domestic confrontation prompt using INTENT, AESTHETIC, and EXECUTION sections. It specifies fluorescent hum, refrigerator vibration, two character voice profiles, emotional delivery, and full dialogue lines, making it one of the strongest reusable prompt cases.

[![Case 4 media preview](media/cases/case-04.jpg)](media/cases/case-04.mp4)

Type: Demo | Date: 2026-06-28

<a id="case-5"></a>
### Case 5: [Museum Guide Scene-Level Dialogue](https://x.com/TomLikesRobots/status/2070923534449119424) (by [@TomLikesRobots](https://x.com/TomLikesRobots))

**test scene-level dialogue reasoning where Seed-Audio writes delivery and character voices from a compact situational prompt.**

The author gives Seed-Audio a museum-guide prompt explaining the phrase crossing the Rubicon to a confused visitor. The model generated the dialogue, delivery, and character voices; the author then generated a matching image in Nano Banana and used Seedance 2 to make a video.

[![Case 5 media preview](media/cases/case-05.jpg)](media/cases/case-05.mp4)

Type: Demo | Date: 2026-06-27

<a id="case-6"></a>
### Case 6: [Reference Voice MC Workflow](https://x.com/JPAI_HEAVEN/status/2070842306329227264) (by [@JPAI_HEAVEN](https://x.com/JPAI_HEAVEN))

**generate a recurring MC voice from reference material, split the resulting audio, and use it as a Seedance 2.0 lip-sync reference.**

The source describes a two-step test: reference a source voice to generate about one minute of MC audio in Seed Audio, then split that voice and pass it into Seedance 2.0 for video. It also reports a practical caveat: the voice changes slightly during downstream video generation, creating editing work.

[![Case 6 media preview](media/cases/case-06.jpg)](media/cases/case-06.mp4)

Type: Tutorial | Date: 2026-06-27

<a id="case-7"></a>
### Case 7: [Claude MCP Voiceover And Dubbing Integration](https://x.com/higgsfield/status/2070916672106680360) (by [@higgsfield](https://x.com/higgsfield))

**route voiceovers, voice cloning, and multilingual dubbing through Claude via Higgsfield MCP, with Seed Audio 1.0 as part of the audio stack.**

Higgsfield states that Claude can generate audio through its MCP integration, covering voiceovers, voice cloning, and dubbing in 50+ languages powered by Seed Audio 1.0 and ElevenLabs v3. A same-author reply provides the MCP access link, so this is a provider integration case rather than a standalone API tutorial.

[![Case 7 media preview](media/cases/case-07.jpg)](media/cases/case-07.mp4)

Type: Integration | Date: 2026-06-27

<a id="case-8"></a>
### Case 8: [Reference Audio Quality And High-Voice Caveat](https://x.com/genel_ai/status/2070438167019409582) (by [@genel_ai](https://x.com/genel_ai))

**evaluate Japanese speech stability, emotion following, reference-audio precision, and high-pitch mechanical artifacts from hands-on use.**

The source reports that Seed Audio Japanese output was more stable than Seedance 2.0 audio, followed emotion in dialogue, and had strong reference-audio precision with a 30-second maximum. It also records limits: audio and image references cannot be used together, and higher voices can sound more mechanical.

[![Case 8 media preview](media/cases/case-08.jpg)](media/cases/case-08.mp4)

Type: Evaluation | Date: 2026-06-26

<a id="case-9"></a>
### Case 9: [Narrated Social Story Engine](https://x.com/deepwhitman/status/2071485165390704837) (by [@deepwhitman](https://x.com/deepwhitman))

**turn public text-story posts into narrated social entertainment and evaluate whether the format can become a repeatable content engine.**

The author narrates a popular AITA-style post with Seed Audio 1.0 and explicitly frames the result as a possible viral content engine. A same-author reply links the original post, grounding the case in a real text-to-narration workflow.

[![Case 9 media preview](media/cases/case-09.jpg)](media/cases/case-09.mp4)

Type: Demo | Date: 2026-06-29

<a id="case-10"></a>
### Case 10: [Image-Guided Character Voice Casting](https://x.com/tc50501/status/2070498347824337389) (by [@tc50501](https://x.com/tc50501))

**use reference images for early character voice casting while treating pitch and tone stability as unresolved production risks.**

The author tests image-to-audio by passing only a female character reference image and generating three roughly ten-second lines. Two outputs were directionally close, while one was clearly too high, so the source supports character voice exploration but not final voice-lock production.

![Case 10 media](media/cases/case-10.jpg)

Type: Evaluation | Date: 2026-06-26

<a id="case-11"></a>
### Case 11: [WaveSpeedAI Text, Voice, Image-Guided Audio](https://x.com/wavespeed_ai/status/2071214531280543772) (by [@wavespeed_ai](https://x.com/wavespeed_ai))

**track provider access for text-to-speech, soundscape generation, preset voices, reference audio, image-guided audio, and tuning controls.**

WaveSpeedAI announces Seed Audio 1.0 availability and lists natural speech, preset voices, reference audio guidance, image-guided audio, and speed, volume, pitch, and format controls. This is strong provider-route evidence for implementation planning.

[![Case 11 media preview](media/cases/case-11.jpg)](media/cases/case-11.mp4)

Type: Integration | Date: 2026-06-28

<a id="case-12"></a>
### Case 12: [Voice Acting, Foley, And Low-Cost Testing](https://x.com/TomLikesRobots/status/2070288519684108353) (by [@TomLikesRobots](https://x.com/TomLikesRobots))

**use Seed-Audio as a low-cost test layer for voice acting and foley before committing to downstream video generation.**

The source reports early tests where voice acting and foley felt better than native Seedance 2 audio, with a 15-second test costing only a few cents. Comments add useful caveats: reference voice conversion can fail, and the best workflow for using generated audio with Seedance lip-sync remains unresolved.

[![Case 12 media preview](media/cases/case-12.jpg)](media/cases/case-12.mp4)

Type: Evaluation | Date: 2026-06-25

<a id="acknowledge"></a>
## Acknowledge

This repository links to public creator and provider posts at the case level. Public sources are credited in each case heading.

Corrections are welcome when a source link breaks, attribution is wrong, or a claim is not supported by the linked source.
