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

- **11 selected Seed-Audio 1.0 cases from 93 accepted recent X/Twitter posts.**
- Covers Audio-First Video Workflows, Audio Drama And Scene Generation, Reference Voice And Character Casting, Tool And Provider Integrations, Social Narration, Foley, And Cost Tests.
- Each case includes the original source, creator attribution, concise usage takeaway, evidence type, and publication date.
- Use this repo to find practical workflows, compare strengths and limits, discover provider routes, and route implementation work to EvoLink.

> [!NOTE]
> Localized README files preserve the same case order, links, anchors, and attribution as the English source.

> [!NOTE]
> The collection favors concrete workflow evidence over hype: demos, setup notes, provider launches, hands-on evaluations, and clearly stated limitations.

[Update log](docs/update-log.md) | [Maintenance guide](docs/maintenance.md) | [Case label audit](docs/case-label-audit.md) | [Case data](data/use-cases.json) | [Preset voice docs](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices)

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
| [Tool And Provider Integrations](#tool-provider-integrations) | Case 7 |
| [Social Narration, Foley, And Cost Tests](#social-narration-foley-cost-tests) | Case 9, Case 11 |
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
| [Case 4: Two-Minute Dialogue With Ambience](#case-4) | write script-format audio drama prompts with ambience, character voices, background music, and line-level performance direction. | Tutorial |
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

<a id="social-narration-foley-cost-tests"></a>
## Social Narration, Foley, And Cost Tests

| Case | What it shows | Type |
|---|---|---|
| [Case 9: Narrated Social Story Engine](#case-9) | turn public text-story posts into narrated social entertainment and evaluate whether the format can become a repeatable content engine. | Demo |
| [Case 11: Voice Acting, Foley, And Low-Cost Testing](#case-11) | use Seed-Audio as a low-cost test layer for voice acting and foley before committing to downstream video generation. | Evaluation |

<a id="case-1"></a>
### Case 1: [Six-Speaker Audio To Guide Seedance Video](https://x.com/gokayfem/status/2070429287950188547) (by [@gokayfem](https://x.com/gokayfem))

**build an audio-first video pipeline where a public Seed Audio prompt creates six-character dialogue and background effects before image and Seedance video generation.**

- Source evidence: The post exposes the actual Seed Audio setup: a getaway-van scene with six named speakers, distinct voice directions, short dialogue lines, engine idle, rain on the roof, and background effects in one generated audio pass. It also shows the downstream image prompt and Seedance 2.0 video prompt, so this is more than a showcase clip.
- What to copy: Use this pattern when the audio needs to drive the whole scene: cast each speaker, define a voice texture, write short lines, and include continuous ambience that can become timing guidance for the later video model.
- Practical workflow: first generate the full multi-speaker audio bed, then create a key visual with matching character silhouettes and mood, then feed audio plus visual context into Seedance for final motion.
- Watch-outs: The evidence supports workflow design and prompt structure; it does not prove perfect speaker separation in every longer scene, so test character identity and timing before using it for production dialogue.

[![Case 1 video preview](media/cases/case-01.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-01.mp4)

[Open video file](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-01.mp4)

Type: Tutorial | Date: 2026-06-26

<a id="case-2"></a>
### Case 2: [Multi-Clip Story Video Audio Planning](https://x.com/gavinpurcell/status/2070246132341727506) (by [@gavinpurcell](https://x.com/gavinpurcell))

**evaluate agent-assisted soundscape generation for multi-clip story videos, including the remaining mismatch risk between effects and on-screen action.**

- Source evidence: The author starts from a one-minute multi-clip low-resolution video, says consistent audio is difficult in Seedance prompts, and tests an agent-assisted audio pass using Claude Code, Codex, and a FAL key.
- What to copy: Treat Seed-Audio as a repair or planning layer for existing multi-clip video, especially when one prompt has to cover changing shots, transitions, ambience, and effects.
- Practical workflow: give the agent the video context, ask it to produce a scene-by-scene audio plan, generate the soundtrack or effects pass, then compare the result against each clip rather than judging the full minute as one block.
- Watch-outs: The same source reports that some effects still miss the exact on-screen action. This is why the case is labeled Evaluation, not Tutorial: it teaches a useful test method and preserves the mismatch risk.

[![Case 2 video preview](media/cases/case-02.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-02.mp4)

[Open video file](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-02.mp4)

Type: Evaluation | Date: 2026-06-25

<a id="case-3"></a>
### Case 3: [Audio-First Seedance Reference Workflow](https://x.com/EvoLinkAi/status/2070722722217578562) (by [@EvoLinkAi](https://x.com/EvoLinkAi))

**use a three-step official workflow: generate Seed-Audio first, create a key visual, then feed both audio and visual references into Seedance 2 reference-to-video.**

- Source evidence: The source states a three-step pipeline: generate audio with Seed-Audio 1.0, generate a key visual, then use both as references in Seedance 2 reference-to-video.
- What to copy: Use this when music, narration, ambience, or pacing should lead the video instead of being added after the video is done.
- Practical workflow: decide the emotional rhythm in the audio prompt first, create or choose an image that matches the scene, then use both references so the video model has timing and visual direction at the same time.
- Watch-outs: This is an official workflow pattern rather than an independent benchmark. It is useful as a starting recipe, but you still need to test lip-sync, cut timing, and whether the generated video follows the audio cues closely enough.

[![Case 3 video preview](media/cases/case-03.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-03.mp4)

[Open video file](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-03.mp4)

Type: Tutorial | Date: 2026-06-27

<a id="case-4"></a>
### Case 4: [Two-Minute Dialogue With Ambience](https://x.com/tarumainfo/status/2071255504907891186) (by [@tarumainfo](https://x.com/tarumainfo))

**write script-format audio drama prompts with ambience, character voices, background music, and line-level performance direction.**

- Source evidence: The post includes a concrete two-minute prompt/script using INTENT, AESTHETIC, and EXECUTION sections. It specifies ambience, background music, two character voice profiles, emotional delivery, and line-by-line dialogue.
- What to copy: Use the script format when you need an audio drama scene rather than a single narration voice. Put the environment first, then define character voices, then write compact performance directions inside the dialogue.
- Practical workflow: draft the scene as a short script, limit each line direction to a few words, include persistent background sound, and listen for whether the model follows both the emotion and the pacing.
- Watch-outs: The source says the result followed the prompt closely, but long-form consistency still needs review. For production, split long scenes into smaller beats if character emotion or background music drifts.

[![Case 4 video preview](media/cases/case-04.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-04.mp4)

[Open video file](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-04.mp4)

Type: Tutorial | Date: 2026-06-28

<a id="case-5"></a>
### Case 5: [Museum Guide Scene-Level Dialogue](https://x.com/TomLikesRobots/status/2070923534449119424) (by [@TomLikesRobots](https://x.com/TomLikesRobots))

**test scene-level dialogue reasoning where Seed-Audio writes delivery and character voices from a compact situational prompt.**

- Source evidence: The author provides the compact prompt: a museum guide explains why “crossing the Rubicon” means passing a point of no return to a confused visitor. The post says Seed Audio generated the dialogue, delivery, and character voices.
- What to copy: Use this case when you want Seed-Audio to infer a short educational exchange from a compact situation rather than writing every line manually.
- Practical workflow: give the model the roles, the concept to explain, and the conversational relationship; then evaluate whether the generated speech sounds natural and whether the explanation remains correct.
- Watch-outs: This is a Demo because the source demonstrates scene-level language reasoning and natural delivery, but it does not provide a repeatable benchmark. Check factual accuracy if you use the pattern for education.

[![Case 5 video preview](media/cases/case-05.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-05.mp4)

[Open video file](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-05.mp4)

Type: Demo | Date: 2026-06-27

<a id="case-6"></a>
### Case 6: [Reference Voice MC Workflow](https://x.com/JPAI_HEAVEN/status/2070842306329227264) (by [@JPAI_HEAVEN](https://x.com/JPAI_HEAVEN))

**generate a recurring MC voice from reference material, split the resulting audio, and use it as a Seedance 2.0 lip-sync reference.**

- Source evidence: The post describes a two-step reference-voice workflow: generate about one minute of MC audio from source voice material, split that generated voice, and pass it into Seedance 2.0 for lip-sync video.
- What to copy: Use this when a recurring host, announcer, or MC voice needs to carry a series and you want a reusable audio reference before video generation.
- Practical workflow: generate a longer clean voice sample, cut it into short usable segments, use those segments as references for video, then edit any drift after the video pass.
- Watch-outs: The author explicitly says the voice changes slightly when Seedance turns it into video. That caveat is central: this is a Tutorial for workflow construction, not a guarantee of stable voice identity.

[![Case 6 video preview](media/cases/case-06.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-06.mp4)

[Open video file](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-06.mp4)

Type: Tutorial | Date: 2026-06-27

<a id="case-7"></a>
### Case 7: [Claude MCP Voiceover And Dubbing Integration](https://x.com/higgsfield/status/2070916672106680360) (by [@higgsfield](https://x.com/higgsfield))

**route voiceovers, voice cloning, and multilingual dubbing through Claude via Higgsfield MCP, with Seed Audio 1.0 as part of the audio stack.**

- Source evidence: Higgsfield states that Claude can generate audio through its MCP integration, covering voiceovers, voice cloning, and dubbing in 50+ languages powered partly by Seed Audio 1.0.
- What to copy: Use this case to understand a no-code or agent-facing access path: instead of calling an audio endpoint directly, creators can route voiceover and dubbing tasks through Claude plus an MCP provider.
- Practical workflow: start with a short voiceover or dubbing request inside Claude, use the MCP route for generation, then inspect whether the output fits the target language, voice identity, and media workflow.
- Watch-outs: This is Integration, not a quality evaluation. The post proves availability and workflow surface, but it does not independently verify dubbing quality across all 50+ languages.

[![Case 7 video preview](media/cases/case-07.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-07.mp4)

[Open video file](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-07.mp4)

Type: Integration | Date: 2026-06-27

<a id="case-8"></a>
### Case 8: [Reference Audio Quality And High-Voice Caveat](https://x.com/genel_ai/status/2070438167019409582) (by [@genel_ai](https://x.com/genel_ai))

**evaluate Japanese speech stability, emotion following, reference-audio precision, and high-pitch mechanical artifacts from hands-on use.**

- Source evidence: The author reports hands-on Japanese usage: more stable Japanese speech than Seedance 2.0 audio, emotion following in dialogue, strong reference-audio precision with a 30-second maximum, no simultaneous audio-plus-image reference, and mechanical artifacts in higher voices.
- What to copy: Use this as a checklist for evaluating speech quality in Japanese or other non-English production tests: stability, emotion following, reference precision, reference-mode limits, and pitch artifacts.
- Practical workflow: run short clips across normal and high-pitch voices, compare outputs against the reference audio, and separately test image-guided workflows because this source says audio and image references cannot be combined.
- Watch-outs: This is an Evaluation because its main value is the limitation map. The strongest lesson is not “Seed-Audio is always better,” but where it behaves well and where it still needs testing.

[![Case 8 video preview](media/cases/case-08.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-08.mp4)

[Open video file](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-08.mp4)

Type: Evaluation | Date: 2026-06-26

<a id="case-9"></a>
### Case 9: [Narrated Social Story Engine](https://x.com/deepwhitman/status/2071485165390704837) (by [@deepwhitman](https://x.com/deepwhitman))

**turn public text-story posts into narrated social entertainment and evaluate whether the format can become a repeatable content engine.**

- Source evidence: The author narrates a popular AITA-style post with Seed Audio 1.0 and frames it as a possible repeatable viral content engine. A same-author reply links the original story source.
- What to copy: Use this when testing whether text-heavy social posts can become low-friction narrated entertainment for short-form platforms.
- Practical workflow: choose a public text story, adapt it into narration segments, generate the voice pass, then pair it with simple visuals or captions and measure whether the format works as a repeatable content pipeline.
- Watch-outs: This is a Demo, not a rights or growth guarantee. You still need permission or proper source handling for the story content, plus audience testing before calling it a scalable channel.

[![Case 9 video preview](media/cases/case-09.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-09.mp4)

[Open video file](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-09.mp4)

Type: Demo | Date: 2026-06-29

<a id="case-10"></a>
### Case 10: [Image-Guided Character Voice Casting](https://x.com/tc50501/status/2070498347824337389) (by [@tc50501](https://x.com/tc50501))

**use reference images for early character voice casting while treating pitch and tone stability as unresolved production risks.**

- Source evidence: The author passes only a female character reference image and generates three roughly ten-second voice lines. Two outputs are directionally close, while one is clearly too high.
- What to copy: Use image-guided audio as an early casting tool: explore what a character might sound like before recording final dialogue or locking a voice model.
- Practical workflow: test several short lines from the same character image, compare pitch, tone, and personality direction, then keep only candidates that remain stable across multiple lines.
- Watch-outs: The source itself warns that pitch and tone stability are not ready for fixed film-character voice operation. This is Evaluation because it defines both the useful casting use and the production risk.

![Case 10 media](media/cases/case-10.jpg)

Type: Evaluation | Date: 2026-06-26

<a id="case-11"></a>
### Case 11: [Voice Acting, Foley, And Low-Cost Testing](https://x.com/TomLikesRobots/status/2070288519684108353) (by [@TomLikesRobots](https://x.com/TomLikesRobots))

**use Seed-Audio as a low-cost test layer for voice acting and foley before committing to downstream video generation.**

- Source evidence: The author reports early tests where voice acting and foley felt better than native Seedance 2 audio, and says a 15-second audio test cost only a few cents.
- What to copy: Use Seed-Audio as a cheap pre-production test layer before spending time on final video generation, especially for scenes where voice acting, foley, or ambience determines whether the idea works.
- Practical workflow: generate short 10-15 second audio tests first, compare them against native video-model audio, and only move to downstream video when the audio direction is strong enough.
- Watch-outs: Comments add unresolved issues around reference voice conversion and using generated audio with Seedance lip-sync. This remains Evaluation because it validates a low-cost testing role, not a complete final pipeline.

[![Case 11 video preview](media/cases/case-11.jpg)](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-11.mp4)

[Open video file](https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main/media/cases/case-11.mp4)

Type: Evaluation | Date: 2026-06-25

<a id="acknowledge"></a>
## Acknowledge

This repository links to public creator and provider posts at the case level. Public sources are credited in each case heading.

Corrections are welcome when a source link breaks, attribution is wrong, or a claim is not supported by the linked source.
