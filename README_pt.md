<div align="center">

<a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=banner&utm_campaign=awesome-seed-audio-1.0-usecases"><img src="images/en.png" alt="Seed-Audio 1.0 usecase repository banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Try it on Evolink](https://img.shields.io/badge/Try_it_on-Evolink-black)](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=badge&utm_campaign=awesome-seed-audio-1.0-usecases)
[![Website](https://img.shields.io/badge/Website-Live-orange)](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=badge&utm_campaign=awesome-seed-audio-1.0-usecases)
[![Docs](https://img.shields.io/badge/Docs-Read-blue)](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=readme&utm_campaign=awesome-seed-audio-1.0-usecases)

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>

# Casos de uso do Seed-Audio 1.0: narração, áudio drama, vozes de referência e vídeo guiado por áudio

## Introdução

Repositório de casos de uso de alto sinal para Seed-Audio 1.0.

**Reunimos casos reais, fluxos de criadores, integrações, avaliações e limites práticos do Seed-Audio 1.0 a partir de fontes públicas do X/Twitter e da documentação da EvoLink.**

Este README em português preserva links de fonte, atribuição e âncoras, enquanto traduz o texto visível ao leitor.

[Testar Seed-Audio 1.0 na EvoLink](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=readme&utm_campaign=awesome-seed-audio-1.0-usecases)

## Visão geral

- **Selecionamos 12 casos de Seed-Audio 1.0 a partir de 93 publicações recentes aceitas do X/Twitter.**
- Abrange: Workflows de vídeo guiados por áudio, Áudio drama e geração de cena, Vozes de referência e casting de personagens, Integrações de ferramentas e provedores, Narração social, foley e testes de custo.
- Cada caso inclui fonte original, atribuição do criador, conclusão de uso, tipo de evidência e data de publicação.
- Use este repositório para encontrar fluxos reais, comparar forças e limites, descobrir rotas de provedores e levar a implementação para a EvoLink.

> [!NOTE]
> Os READMEs localizados preservam a mesma ordem de casos, links, âncoras e atribuição da fonte em inglês.

> [!NOTE]
> A coleção prioriza evidência concreta em vez de hype: demos, notas de configuração, lançamentos de provedores, avaliações práticas e limites claros.

[Registro de atualizações](docs/update-log.md) | [Guia de manutenção](docs/maintenance.md) | [Dados dos casos](data/use-cases.json) | [Documentação de vozes predefinidas](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices)

## Acesso rápido à API

Use o Seed-Audio 1.0 pela API de geração de áudio da EvoLink. Obtenha uma API key na [EvoLink](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=readme&utm_campaign=awesome-seed-audio-1.0-usecases) e configure `EVOLINK_API_KEY` antes da requisição.

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

A resposta cria uma tarefa assíncrona. Consulte `GET /v1/tasks/{task_id}` até que o estado seja `completed`, `failed` ou `cancelled`.

Repositório complementar de API e skill: [doubao-seed-audio-api-skill](https://github.com/EvoLinkAI/doubao-seed-audio-api-skill).

## Menu

| Seção | Casos |
|---|---|
| [Workflows de vídeo guiados por áudio](#audio-first-video) | Caso 1, Caso 2, Caso 3 |
| [Áudio drama e geração de cena](#audio-drama-scene-generation) | Caso 4, Caso 5 |
| [Vozes de referência e casting de personagens](#voice-reference-character-casting) | Caso 6, Caso 8, Caso 10 |
| [Integrações de ferramentas e provedores](#tool-provider-integrations) | Caso 7, Caso 11 |
| [Narração social, foley e testes de custo](#social-narration-foley-cost-tests) | Caso 9, Caso 12 |
| [Agradecimentos](#acknowledge) | Créditos e política de correções |

<a id="audio-first-video"></a>
## Workflows de vídeo guiados por áudio

| Caso | O que mostra | Tipo |
|---|---|---|
| [Caso 1: Áudio com seis falantes para guiar vídeo no Seedance](#case-1) | Crie um fluxo de trabalho de vídeo que prioriza o áudio, onde diálogos com vários alto-falantes e efeitos de fundo orientam a geração posterior de vídeo. | Tutorial |
| [Caso 2: Planejamento de áudio para histórias em múltiplos clipes](#case-2) | Testar se o Seed-Audio 1.0 pode reduzir problemas de tempo e consistência em histórias de vídeo com vários clipes. | Avaliação |
| [Caso 3: Workflow Seedance guiado primeiro por áudio](#case-3) | Estruture um fluxo de trabalho de três etapas: gere áudio, crie um visual principal e use ambos como referências Seedance. | Tutorial |

<a id="audio-drama-scene-generation"></a>
## Áudio drama e geração de cena

| Caso | O que mostra | Tipo |
|---|---|---|
| [Caso 4: Diálogo de dois minutos com ambiência](#case-4) | Avalie o Seed-Audio 1.0 para cenas compactas de drama de áudio com múltiplas vozes, ambiente e música de fundo. | Demo |
| [Caso 5: Diálogo de cena com guia de museu](#case-5) | Teste o raciocínio de linguagem em nível de cena onde Seed-Audio gera diálogo, entrega e vozes de personagens distintas. | Demo |

<a id="voice-reference-character-casting"></a>
## Vozes de referência e casting de personagens

| Caso | O que mostra | Tipo |
|---|---|---|
| [Caso 6: Workflow de MC com voz de referência](#case-6) | Avalie fluxos de trabalho de voz de referência para MC recorrentes ou narração em série antes da geração de vídeo posterior. | Tutorial |
| [Caso 8: Qualidade de áudio de referência e limite em vozes agudas](#case-8) | Avaliar a fala japonesa, o acompanhamento de emoções, a precisão do áudio de referência e o risco de som sintético de alta frequência. | Avaliação |
| [Caso 10: Casting de voz de personagem guiado por imagem](#case-10) | Avaliar o áudio da imagem de referência como o elenco inicial da voz do personagem, e não como a produção final do bloqueio de voz. | Avaliação |

<a id="tool-provider-integrations"></a>
## Integrações de ferramentas e provedores

| Caso | O que mostra | Tipo |
|---|---|---|
| [Caso 7: Integração de narração e dublagem no Claude MCP](#case-7) | Avalie o Seed-Audio 1.0 como parte de um espaço de trabalho criativo nativo do assistente para narração, clonagem de voz e dublagem. | Integração |
| [Caso 11: Áudio guiado por texto, voz e imagem no WaveSpeedAI](#case-11) | Rastreie o suporte do provedor para fala natural, vozes predefinidas, áudio de referência, áudio guiado por imagem e controles de ajuste. | Integração |

<a id="social-narration-foley-cost-tests"></a>
## Narração social, foley e testes de custo

| Caso | O que mostra | Tipo |
|---|---|---|
| [Caso 9: Motor de narração para histórias sociais](#case-9) | Teste formatos de narração de histórias sociais onde as postagens de texto se tornam entretenimento com foco no áudio. | Demo |
| [Caso 12: Teste de baixo custo para atuação vocal e foley](#case-12) | Avalie o Seed-Audio 1.0 como uma camada de iteração de baixo custo para dublagem e foley antes de se comprometer com a geração de vídeo. | Avaliação |

<a id="case-1"></a>
### Caso 1: [Áudio com seis falantes para guiar vídeo no Seedance](https://x.com/gokayfem/status/2070429287950188547) (por [@gokayfem](https://x.com/gokayfem))

**Crie um fluxo de trabalho de vídeo que prioriza o áudio, onde diálogos com vários alto-falantes e efeitos de fundo orientam a geração posterior de vídeo.**

A fonte inclui um fluxo de trabalho Seed Audio mais Seedance concreto e uma configuração de estilo prompt para seis pessoas com efeitos de fundo.

[![Caso 1 media preview](media/cases/case-01.jpg)](media/cases/case-01.mp4)

Tipo: Tutorial | Data: 2026-06-26

<a id="case-2"></a>
### Caso 2: [Planejamento de áudio para histórias em múltiplos clipes](https://x.com/gavinpurcell/status/2070246132341727506) (por [@gavinpurcell](https://x.com/gavinpurcell))

**Testar se o Seed-Audio 1.0 pode reduzir problemas de tempo e consistência em histórias de vídeo com vários clipes.**

A fonte descreve o uso de um vídeo gerado e um API key para produzir Seed Audio para um fluxo de trabalho de história com vários clipes.

[![Caso 2 media preview](media/cases/case-02.jpg)](media/cases/case-02.mp4)

Tipo: Avaliação | Data: 2026-06-25

<a id="case-3"></a>
### Caso 3: [Workflow Seedance guiado primeiro por áudio](https://x.com/EvoLinkAi/status/2070722722217578562) (por [@EvoLinkAi](https://x.com/EvoLinkAi))

**Estruture um fluxo de trabalho de três etapas: gere áudio, crie um visual principal e use ambos como referências Seedance.**

A fonte fornece um fluxo de trabalho conciso onde o áudio fornece música, narração, ambiente e direção de tempo para o vídeo.

[![Caso 3 media preview](media/cases/case-03.jpg)](media/cases/case-03.mp4)

Tipo: Tutorial | Data: 2026-06-27

<a id="case-4"></a>
### Caso 4: [Diálogo de dois minutos com ambiência](https://x.com/tarumainfo/status/2071255504907891186) (por [@tarumainfo](https://x.com/tarumainfo))

**Avalie o Seed-Audio 1.0 para cenas compactas de drama de áudio com múltiplas vozes, ambiente e música de fundo.**

A fonte relata um experimento de diálogo de dois minutos usando uma estrutura INTENT, AESTHETIC, EXECUTION estilo autor.

[![Caso 4 media preview](media/cases/case-04.jpg)](media/cases/case-04.mp4)

Tipo: Demo | Data: 2026-06-28

<a id="case-5"></a>
### Caso 5: [Diálogo de cena com guia de museu](https://x.com/TomLikesRobots/status/2070923534449119424) (por [@TomLikesRobots](https://x.com/TomLikesRobots))

**Teste o raciocínio de linguagem em nível de cena onde Seed-Audio gera diálogo, entrega e vozes de personagens distintas.**

A fonte descreve um guia de museu e um alerta confuso ao visitante, onde o modelo produzia um diálogo natural e uma entrega de personagem.

[![Caso 5 media preview](media/cases/case-05.jpg)](media/cases/case-05.mp4)

Tipo: Demo | Data: 2026-06-27

<a id="case-6"></a>
### Caso 6: [Workflow de MC com voz de referência](https://x.com/JPAI_HEAVEN/status/2070842306329227264) (por [@JPAI_HEAVEN](https://x.com/JPAI_HEAVEN))

**Avalie fluxos de trabalho de voz de referência para MC recorrentes ou narração em série antes da geração de vídeo posterior.**

A fonte descreve a geração de cerca de um minuto de voz MC a partir do material de referência e, em seguida, sua divisão para vídeo Seedance. Ela também observa a deriva de voz na etapa posterior como uma advertência prática.

[![Caso 6 media preview](media/cases/case-06.jpg)](media/cases/case-06.mp4)

Tipo: Tutorial | Data: 2026-06-27

<a id="case-7"></a>
### Caso 7: [Integração de narração e dublagem no Claude MCP](https://x.com/higgsfield/status/2070916672106680360) (por [@higgsfield](https://x.com/higgsfield))

**Avalie o Seed-Audio 1.0 como parte de um espaço de trabalho criativo nativo do assistente para narração, clonagem de voz e dublagem.**

Foi a publicação de maior engajamento da amostra e apresenta o Seed Audio dentro de um fluxo de trabalho do Claude MCP.

[![Caso 7 media preview](media/cases/case-07.jpg)](media/cases/case-07.mp4)

Tipo: Integração | Data: 2026-06-27

<a id="case-8"></a>
### Caso 8: [Qualidade de áudio de referência e limite em vozes agudas](https://x.com/genel_ai/status/2070438167019409582) (por [@genel_ai](https://x.com/genel_ai))

**Avaliar a fala japonesa, o acompanhamento de emoções, a precisão do áudio de referência e o risco de som sintético de alta frequência.**

A fonte relata saída japonesa estável, acompanhamento de emoções, forte precisão de áudio de referência e uma ressalva de que vozes mais altas podem soar mais mecânicas.

[![Caso 8 media preview](media/cases/case-08.jpg)](media/cases/case-08.mp4)

Tipo: Avaliação | Data: 2026-06-26

<a id="case-9"></a>
### Caso 9: [Motor de narração para histórias sociais](https://x.com/deepwhitman/status/2071485165390704837) (por [@deepwhitman](https://x.com/deepwhitman))

**Teste formatos de narração de histórias sociais onde as postagens de texto se tornam entretenimento com foco no áudio.**

A fonte descreve a narração de uma história popular no estilo AITA e a enquadra como uma ideia de mecanismo de conteúdo repetível.

[![Caso 9 media preview](media/cases/case-09.jpg)](media/cases/case-09.mp4)

Tipo: Demo | Data: 2026-06-29

<a id="case-10"></a>
### Caso 10: [Casting de voz de personagem guiado por imagem](https://x.com/tc50501/status/2070498347824337389) (por [@tc50501](https://x.com/tc50501))

**Avaliar o áudio da imagem de referência como o elenco inicial da voz do personagem, e não como a produção final do bloqueio de voz.**

A fonte relata que a imagem de um personagem pode sugerir uma direção de voz, enquanto a estabilidade do tom e do tom ainda precisa de verificação para vozes fixas de personagens no estilo de filme.

![Caso 10 media](media/cases/case-10.jpg)

Tipo: Avaliação | Data: 2026-06-26

<a id="case-11"></a>
### Caso 11: [Áudio guiado por texto, voz e imagem no WaveSpeedAI](https://x.com/wavespeed_ai/status/2071214531280543772) (por [@wavespeed_ai](https://x.com/wavespeed_ai))

**Rastreie o suporte do provedor para fala natural, vozes predefinidas, áudio de referência, áudio guiado por imagem e controles de ajuste.**

A fonte é uma nota de lançamento do provedor que lista os controles de velocidade, volume, tom e formato junto com a disponibilidade do Seed Audio.

[![Caso 11 media preview](media/cases/case-11.jpg)](media/cases/case-11.mp4)

Tipo: Integração | Data: 2026-06-28

<a id="case-12"></a>
### Caso 12: [Teste de baixo custo para atuação vocal e foley](https://x.com/TomLikesRobots/status/2070288519684108353) (por [@TomLikesRobots](https://x.com/TomLikesRobots))

**Avalie o Seed-Audio 1.0 como uma camada de iteração de baixo custo para dublagem e foley antes de se comprometer com a geração de vídeo.**

A fonte relata os primeiros testes em que a dublagem e o foley foram melhores do que o áudio Seedance nativo, com baixo custo para experimentos curtos.

[![Caso 12 media preview](media/cases/case-12.jpg)](media/cases/case-12.mp4)

Tipo: Avaliação | Data: 2026-06-25

<a id="acknowledge"></a>
## Agradecimentos

Este repositório aponta para publicações públicas de criadores e provedores em cada caso. A fonte pública aparece no título do caso.

Correções são bem-vindas quando um link quebra, a atribuição está errada ou uma afirmação não é sustentada pela fonte.
