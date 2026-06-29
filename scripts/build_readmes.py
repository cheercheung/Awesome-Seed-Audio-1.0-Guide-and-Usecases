#!/usr/bin/env python3
"""Build source and localized README files from data/use-cases.json."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data" / "use-cases.json").read_text(encoding="utf-8"))
CASE_TRANSLATIONS = json.loads((ROOT / "data" / "use-case-translations.json").read_text(encoding="utf-8"))
VOICE_DATA = json.loads((ROOT / "data" / "voice-list.json").read_text(encoding="utf-8"))
VOICE_SOURCES = VOICE_DATA["voices"]
VOICE_DOCS_URL = VOICE_DATA["metadata"]["source_doc_url"]
CAMPAIGN = "awesome-seed-audio-1.0-usecases"
RAW_MEDIA_BASE = "https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main"


LOCALES = {
    "en": {"file": "README.md", "label": "English", "color": "111111"},
    "es": {"file": "README_es.md", "label": "Español", "color": "ffb703"},
    "pt": {"file": "README_pt.md", "label": "Português", "color": "2a9d8f"},
    "ja": {"file": "README_ja.md", "label": "日本語", "color": "52b788"},
    "ko": {"file": "README_ko.md", "label": "한국어", "color": "4ea8de"},
    "de": {"file": "README_de.md", "label": "Deutsch", "color": "f4a261"},
    "fr": {"file": "README_fr.md", "label": "Français", "color": "e76f51"},
    "tr": {"file": "README_tr.md", "label": "Türkçe", "color": "d62828"},
    "zh-TW": {"file": "README_zh-TW.md", "label": "繁體中文", "color": "8338ec"},
    "zh-CN": {"file": "README_zh-CN.md", "label": "简体中文", "color": "ef476f"},
    "ru": {"file": "README_ru.md", "label": "Русский", "color": "577590"},
}

UI = {
    "en": {
        "title": "Seed-Audio 1.0 Use Cases: Narration, Audio Drama, Reference Voices, And Audio-First Video",
        "intro_h": "Introduction",
        "intro": "Welcome to the Seed-Audio 1.0 high-signal usecase repository.",
        "summary": "We collect real-world usage cases, creator workflows, provider integrations, evaluations, and practical limits for Seed-Audio 1.0, curated from public X/Twitter sources and EvoLink documentation.",
        "source_note": "This English source README focuses on source-linked cases with concrete workflow evidence. Each case title links to its public source, and each author handle links to the creator profile.",
        "try": "Try Seed-Audio 1.0 on EvoLink",
        "overview": "Overview",
        "overview_1": "{n} selected Seed-Audio 1.0 cases from {sample} accepted recent X/Twitter posts.",
        "overview_2": "Covers {categories}.",
        "overview_3": "Each case includes the original source, creator attribution, concise usage takeaway, evidence type, and publication date.",
        "overview_4": "Use this repo to find practical workflows, compare strengths and limits, discover provider routes, and route implementation work to EvoLink.",
        "note_1": "Localized README files preserve the same case order, links, anchors, and attribution as the English source.",
        "note_2": "The collection favors concrete workflow evidence over hype: demos, setup notes, provider launches, hands-on evaluations, and clearly stated limitations.",
        "links": "[Update log](docs/update-log.md) | [Maintenance guide](docs/maintenance.md) | [Case label audit](docs/case-label-audit.md) | [Case data](data/use-cases.json)",
        "api_h": "Quick API Access",
        "api_1": "Use Seed-Audio 1.0 through the EvoLink audio generation API. Get an API key from [EvoLink]({url}), then set it as `EVOLINK_API_KEY` before running the request.",
        "api_2": "The response creates an async task. Poll `GET /v1/tasks/{task_id}` until the task reaches `completed`, `failed`, or `cancelled`.",
        "api_3": "Read the companion API and skill repo: [doubao-seed-audio-api-skill](https://github.com/EvoLinkAI/doubao-seed-audio-api-skill).",
        "menu": "Menu",
        "section": "Section",
        "cases": "Cases",
        "case": "Case",
        "what": "What it shows",
        "type": "Type",
        "date": "Date",
        "ack": "Acknowledge",
        "ack_row": "Credits and correction policy",
        "ack_1": "This repository links to public creator and provider posts at the case level. Public sources are credited in each case heading.",
        "ack_2": "Corrections are welcome when a source link breaks, attribution is wrong, or a claim is not supported by the linked source.",
        "open_video": "Open video file",
        "local_note": "{title}",
        "local_detail": "{notes}",
    },
    "zh-CN": {
        "title": "Seed-Audio 1.0 使用案例：旁白、音频剧、参考声音与音频优先视频工作流",
        "intro_h": "介绍",
        "intro": "欢迎来到 Seed-Audio 1.0 高信号使用案例仓库。",
        "summary": "我们基于公开 X/Twitter 来源和 EvoLink 文档，整理 Seed-Audio 1.0 的真实使用案例、创作者工作流、平台集成、评估和实践限制。",
        "source_note": "本简体中文 README 保留公开来源链接、作者署名和锚点，同时翻译用户可见说明文字。",
        "try": "在 EvoLink 上试用 Seed-Audio 1.0",
        "overview": "概览",
        "overview_1": "从近期 X/Twitter 样本中筛选出 {n} 个 Seed-Audio 1.0 使用案例，原始可用样本为 {sample} 条。",
        "overview_2": "覆盖方向：{categories}。",
        "overview_3": "每个案例都包含原始来源、创作者署名、使用结论、证据类型和发布日期。",
        "overview_4": "你可以用这个仓库查找真实工作流、比较优势和限制、发现服务商路径，并把实现工作导向 EvoLink。",
        "note_1": "本地化 README 与英文源文件保持相同的案例顺序、链接、锚点和署名。",
        "note_2": "本仓库优先收录具体工作流证据，而不是纯宣传：演示、设置说明、服务商发布、上手评估和明确限制。",
        "links": "[更新日志](docs/update-log.md) | [维护指南](docs/maintenance.md) | [案例标注审计](docs/case-label-audit.md) | [案例数据](data/use-cases.json)",
        "api_h": "API 快速访问",
        "api_1": "通过 EvoLink 音频生成 API 使用 Seed-Audio 1.0。先在 [EvoLink]({url}) 获取 API key，然后在请求前设置 `EVOLINK_API_KEY`。",
        "api_2": "响应会创建一个异步任务。轮询 `GET /v1/tasks/{task_id}`，直到状态变为 `completed`、`failed` 或 `cancelled`。",
        "api_3": "配套 API 与 skill 仓库：[doubao-seed-audio-api-skill](https://github.com/EvoLinkAI/doubao-seed-audio-api-skill)。",
        "menu": "目录",
        "section": "章节",
        "cases": "案例",
        "case": "案例",
        "what": "展示重点",
        "type": "类型",
        "date": "日期",
        "ack": "致谢",
        "ack_row": "来源致谢与修正政策",
        "ack_1": "本仓库在案例级别链接公开创作者和服务商内容。每个案例标题都会标注公开来源。",
        "ack_2": "如果来源链接失效、署名错误，或某个说法没有得到链接来源支持，欢迎提交修正。",
        "open_video": "打开视频文件",
        "local_note": "用这个案例评估：{title}。",
        "local_detail": "该案例来自公开 X/Twitter 来源，适合作为此使用场景的证据。来源链接和作者主页保留在标题中。",
    },
    "zh-TW": {
        "title": "Seed-Audio 1.0 使用案例：旁白、音訊劇、參考聲音與音訊優先影片工作流",
        "intro_h": "介紹",
        "intro": "歡迎來到 Seed-Audio 1.0 高訊號使用案例倉庫。",
        "summary": "我們基於公開 X/Twitter 來源和 EvoLink 文件，整理 Seed-Audio 1.0 的真實使用案例、創作者工作流、平台整合、評估與實務限制。",
        "source_note": "本繁體中文 README 保留公開來源連結、作者署名和錨點，同時翻譯使用者可見說明文字。",
        "try": "在 EvoLink 上試用 Seed-Audio 1.0",
        "overview": "總覽",
        "overview_1": "從近期 X/Twitter 樣本中篩選出 {n} 個 Seed-Audio 1.0 使用案例，原始可用樣本為 {sample} 則。",
        "overview_2": "涵蓋方向：{categories}。",
        "overview_3": "每個案例都包含原始來源、創作者署名、使用結論、證據類型與發布日期。",
        "overview_4": "你可以用這個倉庫查找真實工作流、比較優勢和限制、發現服務商路徑，並把實作工作導向 EvoLink。",
        "note_1": "本地化 README 與英文源文件保持相同的案例順序、連結、錨點與署名。",
        "note_2": "本倉庫優先收錄具體工作流證據，而不是純宣傳：演示、設定說明、服務商發布、上手評估和明確限制。",
        "links": "[更新日誌](docs/update-log.md) | [維護指南](docs/maintenance.md) | [案例標註審計](docs/case-label-audit.md) | [案例資料](data/use-cases.json)",
        "api_h": "API 快速存取",
        "api_1": "透過 EvoLink 音訊生成 API 使用 Seed-Audio 1.0。先在 [EvoLink]({url}) 取得 API key，然後在請求前設定 `EVOLINK_API_KEY`。",
        "api_2": "回應會建立一個非同步任務。輪詢 `GET /v1/tasks/{task_id}`，直到狀態變為 `completed`、`failed` 或 `cancelled`。",
        "api_3": "配套 API 與 skill 倉庫：[doubao-seed-audio-api-skill](https://github.com/EvoLinkAI/doubao-seed-audio-api-skill)。",
        "menu": "目錄",
        "section": "章節",
        "cases": "案例",
        "case": "案例",
        "what": "展示重點",
        "type": "類型",
        "date": "日期",
        "ack": "致謝",
        "ack_row": "來源致謝與修正政策",
        "ack_1": "本倉庫在案例層級連結公開創作者和服務商內容。每個案例標題都會標註公開來源。",
        "ack_2": "如果來源連結失效、署名錯誤，或某個說法沒有得到連結來源支持，歡迎提交修正。",
        "open_video": "打開影片檔案",
        "local_note": "用這個案例評估：{title}。",
        "local_detail": "該案例來自公開 X/Twitter 來源，適合作為此使用場景的證據。來源連結和作者主頁保留在標題中。",
    },
}

UI.update(
    {
        "ja": {
            "title": "Seed-Audio 1.0 ユースケース：ナレーション、音声ドラマ、参照音声、音声先行の動画制作",
            "intro_h": "紹介",
            "intro": "Seed-Audio 1.0 の高シグナルなユースケース集です。",
            "summary": "公開 X/Twitter ソースと EvoLink ドキュメントに基づき、実例、クリエイターのワークフロー、統合、評価、実用上の制約を整理しています。",
            "source_note": "この日本語 README は公開ソースリンク、作者クレジット、アンカーを保持しつつ、ユーザー向け説明文を翻訳しています。",
            "try": "EvoLink で Seed-Audio 1.0 を試す",
            "overview": "概要",
            "overview_1": "最近の X/Twitter サンプル {sample} 件から、Seed-Audio 1.0 のユースケース {n} 件を選定しました。",
            "overview_2": "対象領域：{categories}。",
            "overview_3": "各ケースには、元ソース、作者クレジット、活用ポイント、証拠タイプ、公開日を含めています。",
            "overview_4": "実用ワークフロー、強みと制約、プロバイダー経路、EvoLink での実装導線を確認するために使えます。",
            "note_1": "ローカライズ版 README は英語版と同じケース順、リンク、アンカー、帰属を保持します。",
            "note_2": "このコレクションは宣伝文句ではなく、デモ、設定メモ、プロバイダー公開、実使用評価、明示された制約などの具体的証拠を重視します。",
            "links": "[更新ログ](docs/update-log.md) | [メンテナンスガイド](docs/maintenance.md) | [ケースラベル監査](docs/case-label-audit.md) | [ケースデータ](data/use-cases.json)",
            "api_h": "API クイックアクセス",
            "api_1": "EvoLink の音声生成 API から Seed-Audio 1.0 を使用できます。[EvoLink]({url}) で API key を取得し、リクエスト前に `EVOLINK_API_KEY` を設定してください。",
            "api_2": "レスポンスは非同期タスクを作成します。`GET /v1/tasks/{task_id}` をポーリングし、状態が `completed`、`failed`、または `cancelled` になるまで待ちます。",
            "api_3": "関連 API・skill リポジトリ：[doubao-seed-audio-api-skill](https://github.com/EvoLinkAI/doubao-seed-audio-api-skill)。",
            "menu": "メニュー",
            "section": "セクション",
            "cases": "ケース",
            "case": "ケース",
            "what": "注目点",
            "type": "タイプ",
            "date": "日付",
            "ack": "謝辞",
            "ack_row": "クレジットと修正ポリシー",
            "ack_1": "このリポジトリはケース単位で公開クリエイターやプロバイダーの投稿へリンクしています。公開ソースは各ケース見出しで明記します。",
            "ack_2": "リンク切れ、誤った帰属、またはリンク先で裏付けられていない主張があれば修正を歓迎します。",
            "local_note": "このケースで評価できること：{title}。",
            "local_detail": "このケースは公開 X/Twitter ソースから選定され、この利用シーンの根拠として使えます。ソースリンクと作者プロフィールは見出しに保持しています。",
        },
        "ko": {
            "title": "Seed-Audio 1.0 사용 사례: 내레이션, 오디오 드라마, 참조 음성, 오디오 우선 영상 워크플로",
            "intro_h": "소개",
            "intro": "Seed-Audio 1.0의 신뢰도 높은 사용 사례 저장소입니다.",
            "summary": "공개 X/Twitter 출처와 EvoLink 문서를 바탕으로 실제 사용 사례, 크리에이터 워크플로, 통합, 평가, 실무상 한계를 정리합니다.",
            "source_note": "이 한국어 README는 공개 출처 링크, 작성자 표시, 앵커를 유지하면서 사용자에게 보이는 설명을 번역합니다.",
            "try": "EvoLink에서 Seed-Audio 1.0 사용해 보기",
            "overview": "개요",
            "overview_1": "최근 X/Twitter 샘플 {sample}개에서 Seed-Audio 1.0 사용 사례 {n}개를 선별했습니다.",
            "overview_2": "포함 범위: {categories}.",
            "overview_3": "각 사례에는 원본 출처, 작성자 표시, 활용 요점, 증거 유형, 게시일이 포함됩니다.",
            "overview_4": "실제 워크플로, 강점과 한계, 제공자 경로, EvoLink 구현 방향을 확인하는 데 사용할 수 있습니다.",
            "note_1": "현지화 README는 영어 원본과 동일한 사례 순서, 링크, 앵커, 출처 표시를 유지합니다.",
            "note_2": "이 컬렉션은 과장보다 데모, 설정 노트, 제공자 출시, 실제 평가, 명확한 한계 같은 구체적 증거를 우선합니다.",
            "links": "[업데이트 로그](docs/update-log.md) | [유지관리 가이드](docs/maintenance.md) | [사례 라벨 감사](docs/case-label-audit.md) | [사례 데이터](data/use-cases.json)",
            "api_h": "빠른 API 접근",
            "api_1": "EvoLink 오디오 생성 API로 Seed-Audio 1.0을 사용할 수 있습니다. [EvoLink]({url})에서 API key를 받은 뒤 요청 전에 `EVOLINK_API_KEY`를 설정하세요.",
            "api_2": "응답은 비동기 작업을 생성합니다. 상태가 `completed`, `failed`, `cancelled` 중 하나가 될 때까지 `GET /v1/tasks/{task_id}`를 폴링하세요.",
            "api_3": "관련 API 및 skill 저장소: [doubao-seed-audio-api-skill](https://github.com/EvoLinkAI/doubao-seed-audio-api-skill).",
            "menu": "메뉴",
            "section": "섹션",
            "cases": "사례",
            "case": "사례",
            "what": "보여주는 점",
            "type": "유형",
            "date": "날짜",
            "ack": "감사의 말",
            "ack_row": "크레딧 및 수정 정책",
            "ack_1": "이 저장소는 사례 단위로 공개 크리에이터와 제공자 게시물에 연결합니다. 공개 출처는 각 사례 제목에 표시됩니다.",
            "ack_2": "출처 링크가 깨졌거나, 표시가 잘못되었거나, 주장에 근거가 부족하면 수정을 제안해 주세요.",
            "local_note": "이 사례로 평가할 수 있는 것: {title}.",
            "local_detail": "이 사례는 공개 X/Twitter 출처에서 선별되었으며 해당 사용 장면의 근거로 활용할 수 있습니다. 출처 링크와 작성자 프로필은 제목에 유지됩니다.",
        },
    }
)

for key, values in {
    "es": ("Casos de uso de Seed-Audio 1.0: narración, audio drama, voces de referencia y video con audio primero", "Introducción", "Repositorio de casos de uso de alta señal para Seed-Audio 1.0.", "Recopilamos casos reales, flujos de creadores, integraciones, evaluaciones y límites prácticos de Seed-Audio 1.0 a partir de fuentes públicas de X/Twitter y documentación de EvoLink.", "Este README en español conserva enlaces de fuente, atribución y anclas, y traduce el texto visible para el lector.", "Probar Seed-Audio 1.0 en EvoLink", "Resumen", "Seleccionamos {n} casos de Seed-Audio 1.0 a partir de {sample} publicaciones recientes aceptadas de X/Twitter.", "Cubre: {categories}.", "Cada caso incluye fuente original, atribución del creador, conclusión de uso, tipo de evidencia y fecha de publicación.", "Usa este repositorio para encontrar flujos reales, comparar fortalezas y límites, descubrir rutas de proveedor y llevar la implementación a EvoLink.", "Los README localizados conservan el mismo orden de casos, enlaces, anclas y atribución que la fuente inglesa.", "La colección prioriza evidencia concreta sobre hype: demos, notas de configuración, lanzamientos de proveedores, evaluaciones prácticas y límites claros.", "[Registro de cambios](docs/update-log.md) | [Guía de mantenimiento](docs/maintenance.md) | [Datos de casos](data/use-cases.json)", "Acceso rápido a la API", "Usa Seed-Audio 1.0 mediante la API de generación de audio de EvoLink. Obtén una API key en [EvoLink]({url}) y configura `EVOLINK_API_KEY` antes de enviar la solicitud.", "La respuesta crea una tarea asíncrona. Consulta `GET /v1/tasks/{task_id}` hasta que el estado sea `completed`, `failed` o `cancelled`.", "Repositorio complementario de API y skill: [doubao-seed-audio-api-skill](https://github.com/EvoLinkAI/doubao-seed-audio-api-skill).", "Menú", "Sección", "Casos", "Caso", "Qué muestra", "Tipo", "Fecha", "Agradecimientos", "Créditos y política de correcciones", "Este repositorio enlaza publicaciones públicas de creadores y proveedores en cada caso. La fuente pública aparece en el encabezado del caso.", "Se aceptan correcciones si una fuente deja de funcionar, la atribución es incorrecta o una afirmación no está respaldada por el enlace.", "Usa este caso para evaluar: {title}.", "Este caso proviene de una fuente pública de X/Twitter y sirve como evidencia para este escenario de uso. El enlace de origen y el perfil del autor se conservan en el encabezado."),
    "pt": ("Casos de uso do Seed-Audio 1.0: narração, áudio drama, vozes de referência e vídeo guiado por áudio", "Introdução", "Repositório de casos de uso de alto sinal para Seed-Audio 1.0.", "Reunimos casos reais, fluxos de criadores, integrações, avaliações e limites práticos do Seed-Audio 1.0 a partir de fontes públicas do X/Twitter e da documentação da EvoLink.", "Este README em português preserva links de fonte, atribuição e âncoras, enquanto traduz o texto visível ao leitor.", "Testar Seed-Audio 1.0 na EvoLink", "Visão geral", "Selecionamos {n} casos de Seed-Audio 1.0 a partir de {sample} publicações recentes aceitas do X/Twitter.", "Abrange: {categories}.", "Cada caso inclui fonte original, atribuição do criador, conclusão de uso, tipo de evidência e data de publicação.", "Use este repositório para encontrar fluxos reais, comparar forças e limites, descobrir rotas de provedores e levar a implementação para a EvoLink.", "Os READMEs localizados preservam a mesma ordem de casos, links, âncoras e atribuição da fonte em inglês.", "A coleção prioriza evidência concreta em vez de hype: demos, notas de configuração, lançamentos de provedores, avaliações práticas e limites claros.", "[Registro de atualizações](docs/update-log.md) | [Guia de manutenção](docs/maintenance.md) | [Dados dos casos](data/use-cases.json)", "Acesso rápido à API", "Use o Seed-Audio 1.0 pela API de geração de áudio da EvoLink. Obtenha uma API key na [EvoLink]({url}) e configure `EVOLINK_API_KEY` antes da requisição.", "A resposta cria uma tarefa assíncrona. Consulte `GET /v1/tasks/{task_id}` até que o estado seja `completed`, `failed` ou `cancelled`.", "Repositório complementar de API e skill: [doubao-seed-audio-api-skill](https://github.com/EvoLinkAI/doubao-seed-audio-api-skill).", "Menu", "Seção", "Casos", "Caso", "O que mostra", "Tipo", "Data", "Agradecimentos", "Créditos e política de correções", "Este repositório aponta para publicações públicas de criadores e provedores em cada caso. A fonte pública aparece no título do caso.", "Correções são bem-vindas quando um link quebra, a atribuição está errada ou uma afirmação não é sustentada pela fonte.", "Use este caso para avaliar: {title}.", "Este caso vem de uma fonte pública do X/Twitter e serve como evidência para este cenário de uso. O link de origem e o perfil do autor permanecem no título."),
    "de": ("Seed-Audio 1.0 Anwendungsfälle: Narration, Audio-Drama, Referenzstimmen und Audio-First-Video", "Einführung", "Ein kuratiertes Repository mit belastbaren Seed-Audio 1.0 Anwendungsfällen.", "Wir sammeln reale Anwendungsfälle, Creator-Workflows, Integrationen, Bewertungen und praktische Grenzen aus öffentlichen X/Twitter-Quellen und EvoLink-Dokumentation.", "Diese deutsche README behält Quellenlinks, Attribution und Anker bei und übersetzt den sichtbaren Lesetext.", "Seed-Audio 1.0 auf EvoLink testen", "Überblick", "Aus {sample} akzeptierten aktuellen X/Twitter-Beiträgen wurden {n} Seed-Audio 1.0 Fälle ausgewählt.", "Abgedeckte Bereiche: {categories}.", "Jeder Fall enthält Originalquelle, Creator-Attribution, Nutzungserkenntnis, Evidenztyp und Veröffentlichungsdatum.", "Nutze dieses Repository, um reale Workflows zu finden, Stärken und Grenzen zu vergleichen, Provider-Routen zu entdecken und Implementierung zu EvoLink zu führen.", "Lokalisierte READMEs behalten dieselbe Fallreihenfolge, Links, Anker und Attribution wie die englische Quelle.", "Die Sammlung priorisiert konkrete Workflow-Evidenz statt Hype: Demos, Setup-Notizen, Provider-Launches, praktische Bewertungen und klare Grenzen.", "[Update-Log](docs/update-log.md) | [Wartungsleitfaden](docs/maintenance.md) | [Falldaten](data/use-cases.json)", "Schneller API-Zugang", "Verwende Seed-Audio 1.0 über die Audio-Generierungs-API von EvoLink. Hole einen API key bei [EvoLink]({url}) und setze vor der Anfrage `EVOLINK_API_KEY`.", "Die Antwort erstellt eine asynchrone Aufgabe. Frage `GET /v1/tasks/{task_id}` ab, bis der Status `completed`, `failed` oder `cancelled` ist.", "Begleitendes API- und Skill-Repository: [doubao-seed-audio-api-skill](https://github.com/EvoLinkAI/doubao-seed-audio-api-skill).", "Menü", "Abschnitt", "Fälle", "Fall", "Was er zeigt", "Typ", "Datum", "Danksagung", "Credits und Korrekturrichtlinie", "Dieses Repository verlinkt öffentliche Creator- und Provider-Beiträge auf Fallebene. Die öffentliche Quelle steht in jeder Fallüberschrift.", "Korrekturen sind willkommen, wenn ein Link defekt ist, Attribution falsch ist oder eine Aussage nicht durch die Quelle gestützt wird.", "Nutze diesen Fall zur Bewertung von: {title}.", "Dieser Fall stammt aus einer öffentlichen X/Twitter-Quelle und dient als Evidenz für dieses Nutzungsszenario. Quellenlink und Autorprofil bleiben in der Überschrift erhalten."),
    "fr": ("Cas d'utilisation de Seed-Audio 1.0 : narration, fiction audio, voix de référence et vidéo pilotée par l'audio", "Introduction", "Dépôt de cas d'utilisation à fort signal pour Seed-Audio 1.0.", "Nous rassemblons des cas réels, workflows de créateurs, intégrations, évaluations et limites pratiques à partir de sources publiques X/Twitter et de la documentation EvoLink.", "Ce README français conserve les liens de source, l'attribution et les ancres, tout en traduisant le texte visible.", "Essayer Seed-Audio 1.0 sur EvoLink", "Aperçu", "{n} cas Seed-Audio 1.0 ont été sélectionnés à partir de {sample} publications X/Twitter récentes acceptées.", "Couvre : {categories}.", "Chaque cas inclut la source originale, l'attribution du créateur, le point d'usage, le type de preuve et la date de publication.", "Utilisez ce dépôt pour trouver des workflows réels, comparer forces et limites, découvrir les routes de fournisseurs et orienter l'implémentation vers EvoLink.", "Les README localisés conservent le même ordre de cas, liens, ancres et attributions que la source anglaise.", "La collection privilégie les preuves concrètes plutôt que le buzz : démos, notes de configuration, lancements de fournisseurs, évaluations pratiques et limites explicites.", "[Journal des mises à jour](docs/update-log.md) | [Guide de maintenance](docs/maintenance.md) | [Données des cas](data/use-cases.json)", "Accès rapide à l'API", "Utilisez Seed-Audio 1.0 via l'API de génération audio d'EvoLink. Obtenez une API key sur [EvoLink]({url}), puis définissez `EVOLINK_API_KEY` avant la requête.", "La réponse crée une tâche asynchrone. Interrogez `GET /v1/tasks/{task_id}` jusqu'à l'état `completed`, `failed` ou `cancelled`.", "Dépôt API et skill associé : [doubao-seed-audio-api-skill](https://github.com/EvoLinkAI/doubao-seed-audio-api-skill).", "Menu", "Section", "Cas", "Cas", "Ce qu'il montre", "Type", "Date", "Remerciements", "Crédits et politique de correction", "Ce dépôt relie les publications publiques de créateurs et de fournisseurs au niveau de chaque cas. La source publique est indiquée dans chaque titre.", "Les corrections sont bienvenues lorsqu'un lien est cassé, une attribution est erronée ou une affirmation n'est pas soutenue par la source.", "Utilisez ce cas pour évaluer : {title}.", "Ce cas provient d'une source publique X/Twitter et sert de preuve pour ce scénario d'usage. Le lien source et le profil de l'auteur restent dans le titre."),
    "tr": ("Seed-Audio 1.0 Kullanım Örnekleri: anlatım, sesli drama, referans sesler ve ses öncelikli video", "Giriş", "Seed-Audio 1.0 için yüksek sinyalli kullanım örnekleri deposu.", "Açık X/Twitter kaynakları ve EvoLink belgelerine dayanarak gerçek kullanım örneklerini, üretici iş akışlarını, entegrasyonları, değerlendirmeleri ve pratik sınırları topluyoruz.", "Bu Türkçe README kaynak bağlantılarını, atıfları ve ankrajları korur; kullanıcıya görünen açıklama metnini çevirir.", "Seed-Audio 1.0'ı EvoLink'te dene", "Genel bakış", "Yakın tarihli kabul edilmiş {sample} X/Twitter gönderisinden {n} Seed-Audio 1.0 vakası seçildi.", "Kapsam: {categories}.", "Her vaka özgün kaynak, üretici atfı, kullanım sonucu, kanıt türü ve yayın tarihi içerir.", "Bu repoyu gerçek iş akışlarını bulmak, güçlü ve zayıf yönleri karşılaştırmak, sağlayıcı yollarını keşfetmek ve uygulamayı EvoLink'e yönlendirmek için kullanın.", "Yerelleştirilmiş README dosyaları İngilizce kaynakla aynı vaka sırasını, bağlantıları, ankrajları ve atıfları korur.", "Koleksiyon abartı yerine somut iş akışı kanıtlarını önceler: demolar, kurulum notları, sağlayıcı duyuruları, pratik değerlendirmeler ve açık sınırlar.", "[Güncelleme günlüğü](docs/update-log.md) | [Bakım rehberi](docs/maintenance.md) | [Vaka verisi](data/use-cases.json)", "Hızlı API erişimi", "Seed-Audio 1.0'ı EvoLink ses üretim API'si üzerinden kullanın. [EvoLink]({url}) üzerinden API key alın ve isteği göndermeden önce `EVOLINK_API_KEY` ayarlayın.", "Yanıt asenkron bir görev oluşturur. Durum `completed`, `failed` veya `cancelled` olana kadar `GET /v1/tasks/{task_id}` adresini yoklayın.", "Eşlik eden API ve skill deposu: [doubao-seed-audio-api-skill](https://github.com/EvoLinkAI/doubao-seed-audio-api-skill).", "Menü", "Bölüm", "Vakalar", "Vaka", "Neyi gösterir", "Tür", "Tarih", "Teşekkür", "Atıflar ve düzeltme politikası", "Bu repo, her vaka düzeyinde herkese açık üretici ve sağlayıcı gönderilerine bağlantı verir. Kamu kaynağı her vaka başlığında yer alır.", "Kaynak bağlantısı bozulduğunda, atıf yanlış olduğunda veya bir iddia bağlantılı kaynakça desteklenmediğinde düzeltmeler memnuniyetle karşılanır.", "Bu vakayı şunu değerlendirmek için kullanın: {title}.", "Bu vaka herkese açık bir X/Twitter kaynağından seçilmiştir ve bu kullanım senaryosu için kanıt olarak kullanılabilir. Kaynak bağlantısı ve yazar profili başlıkta korunur."),
    "ru": ("Варианты использования Seed-Audio 1.0: озвучка, аудиодрама, референсные голоса и видео от аудио", "Введение", "Репозиторий с проверенными вариантами использования Seed-Audio 1.0.", "Мы собираем реальные кейсы, рабочие процессы авторов, интеграции, оценки и практические ограничения на основе публичных источников X/Twitter и документации EvoLink.", "Этот русский README сохраняет ссылки на источники, атрибуцию и якоря, а пользовательский текст переведен.", "Попробовать Seed-Audio 1.0 на EvoLink", "Обзор", "Из {sample} принятых недавних публикаций X/Twitter выбрано {n} кейсов Seed-Audio 1.0.", "Охват: {categories}.", "Каждый кейс содержит исходный источник, атрибуцию автора, вывод по применению, тип доказательства и дату публикации.", "Используйте репозиторий, чтобы находить реальные рабочие процессы, сравнивать сильные стороны и ограничения, находить маршруты провайдеров и переходить к реализации через EvoLink.", "Локализованные README сохраняют тот же порядок кейсов, ссылки, якоря и атрибуцию, что и английский источник.", "Коллекция отдает приоритет конкретным доказательствам вместо хайпа: демо, заметкам по настройке, запускам провайдеров, практическим оценкам и явным ограничениям.", "[Журнал обновлений](docs/update-log.md) | [Руководство по поддержке](docs/maintenance.md) | [Данные кейсов](data/use-cases.json)", "Быстрый доступ к API", "Используйте Seed-Audio 1.0 через API генерации аудио EvoLink. Получите API key на [EvoLink]({url}), затем задайте `EVOLINK_API_KEY` перед запросом.", "Ответ создает асинхронную задачу. Опрашивайте `GET /v1/tasks/{task_id}`, пока статус не станет `completed`, `failed` или `cancelled`.", "Связанный репозиторий API и skill: [doubao-seed-audio-api-skill](https://github.com/EvoLinkAI/doubao-seed-audio-api-skill).", "Меню", "Раздел", "Кейсы", "Кейс", "Что показывает", "Тип", "Дата", "Благодарности", "Кредиты и политика исправлений", "Этот репозиторий ссылается на публичные публикации авторов и провайдеров на уровне каждого кейса. Публичный источник указан в заголовке кейса.", "Исправления приветствуются, если ссылка сломана, атрибуция неверна или утверждение не подтверждается источником.", "Используйте этот кейс для оценки: {title}.", "Этот кейс выбран из публичного источника X/Twitter и подходит как доказательство для данного сценария. Ссылка на источник и профиль автора сохранены в заголовке."),
}.items():
    (
        title,
        intro_h,
        intro,
        summary,
        source_note,
        try_text,
        overview,
        overview_1,
        overview_2,
        overview_3,
        overview_4,
        note_1,
        note_2,
        links,
        api_h,
        api_1,
        api_2,
        api_3,
        menu,
        section,
        cases,
        case,
        what,
        type_label,
        date,
        ack,
        ack_row,
        ack_1,
        ack_2,
        local_note,
        local_detail,
    ) = values
    UI[key] = {
        "title": title,
        "intro_h": intro_h,
        "intro": intro,
        "summary": summary,
        "source_note": source_note,
        "try": try_text,
        "overview": overview,
        "overview_1": overview_1,
        "overview_2": overview_2,
        "overview_3": overview_3,
        "overview_4": overview_4,
        "note_1": note_1,
        "note_2": note_2,
        "links": links,
        "api_h": api_h,
        "api_1": api_1,
        "api_2": api_2,
        "api_3": api_3,
        "menu": menu,
        "section": section,
        "cases": cases,
        "case": case,
        "what": what,
        "type": type_label,
        "date": date,
        "ack": ack,
        "ack_row": ack_row,
        "ack_1": ack_1,
        "ack_2": ack_2,
        "local_note": local_note,
        "local_detail": local_detail,
    }

BY_LABELS = {
    "en": "by",
    "es": "por",
    "pt": "por",
    "ja": "作者",
    "ko": "작성자",
    "de": "von",
    "fr": "par",
    "tr": "yazar",
    "zh-TW": "作者",
    "zh-CN": "作者",
    "ru": "автор",
}

for locale, label in BY_LABELS.items():
    UI[locale]["by"] = label

VOICE_COPY = {
    "en": {
        "voice_h": "Preset Voice List",
        "voice_menu": "Non-Chinese preset voices",
        "voice_intro": "These preset voices can be passed in `audio_references` by using their `voice_type` as the Voice ID. The English README renders only non-Chinese rows here; use the voice source file for the complete list.",
        "voice_source_label": "Complete voice source file",
        "voice_docs_label": "EvoLink voice docs",
        "voice_other_note": "Use the voice source file for the complete preset voice list.",
        "voice_col_scenario": "Scenario",
        "voice_col_name": "Voice name",
        "voice_col_type": "voice_type",
        "voice_col_language": "Language",
    },
    "zh-CN": {
        "voice_h": "预设音色列表",
        "voice_menu": "中文预设音色",
        "voice_intro": "这些预设音色可以作为 `audio_references` 传入，其中 `voice_type` 就是 Voice ID。本简体中文页只展示前 50 个中文相关音色；完整列表请查看音色来源文件。",
        "voice_source_label": "完整音色来源文件",
        "voice_docs_label": "EvoLink 音色文档",
        "voice_other_note": "完整预设音色列表请查看音色来源文件。",
        "voice_col_scenario": "场景",
        "voice_col_name": "音色名称",
        "voice_col_type": "voice_type",
        "voice_col_language": "语言/方言/口音",
    },
    "zh-TW": {
        "voice_h": "預設音色列表",
        "voice_menu": "中文預設音色",
        "voice_intro": "這些預設音色可以作為 `audio_references` 傳入，其中 `voice_type` 就是 Voice ID。本繁體中文頁只展示前 50 個中文相關音色；完整列表請查看音色來源檔案。",
        "voice_source_label": "完整音色來源檔案",
        "voice_docs_label": "EvoLink 音色文件",
        "voice_other_note": "完整預設音色列表請查看音色來源檔案。",
        "voice_col_scenario": "場景",
        "voice_col_name": "音色名稱",
        "voice_col_type": "voice_type",
        "voice_col_language": "語言/方言/口音",
    },
    "ja": {
        "voice_h": "プリセット音色一覧",
        "voice_menu": "音色ソースファイル",
        "voice_intro": "これらのプリセット音色は `audio_references` に渡すことができ、`voice_type` が Voice ID になります。この日本語版では長い表を表示せず、音色ソースファイルを案内します。",
        "voice_source_label": "完全な音色ソースファイル",
        "voice_docs_label": "EvoLink 音色ドキュメント",
        "voice_other_note": "完全なプリセット音色一覧は音色ソースファイルで確認してください。",
    },
    "ko": {
        "voice_h": "프리셋 음색 목록",
        "voice_menu": "음색 출처 파일",
        "voice_intro": "이 프리셋 음색은 `audio_references`에 전달할 수 있으며 `voice_type`이 Voice ID입니다. 한국어 README에는 긴 표를 넣지 않고 음색 출처 파일로 안내합니다.",
        "voice_source_label": "전체 음색 출처 파일",
        "voice_docs_label": "EvoLink 음색 문서",
        "voice_other_note": "전체 프리셋 음색 목록은 음색 출처 파일에서 확인하세요.",
    },
    "es": {
        "voice_h": "Lista de voces predefinidas",
        "voice_menu": "Archivo de voces",
        "voice_intro": "Estas voces predefinidas se pueden pasar en `audio_references`; `voice_type` es el Voice ID. Este README en español no renderiza la tabla larga y dirige al archivo de voces.",
        "voice_source_label": "Archivo completo de voces",
        "voice_docs_label": "Documentación de voces de EvoLink",
        "voice_other_note": "Consulta el archivo de voces para revisar la lista completa.",
    },
    "pt": {
        "voice_h": "Lista de vozes predefinidas",
        "voice_menu": "Arquivo de vozes",
        "voice_intro": "Estas vozes predefinidas podem ser passadas em `audio_references`; `voice_type` é o Voice ID. Este README em português não renderiza a tabela longa e aponta para o arquivo de vozes.",
        "voice_source_label": "Arquivo completo de vozes",
        "voice_docs_label": "Documentação de vozes da EvoLink",
        "voice_other_note": "Consulte o arquivo de vozes para ver a lista completa.",
    },
    "de": {
        "voice_h": "Liste der voreingestellten Stimmen",
        "voice_menu": "Stimmdatei",
        "voice_intro": "Diese voreingestellten Stimmen können in `audio_references` übergeben werden; `voice_type` ist die Voice ID. Diese deutsche README rendert keine lange Tabelle und verweist auf die Stimmdatei.",
        "voice_source_label": "Vollständige Stimmdatei",
        "voice_docs_label": "EvoLink Stimmdokumentation",
        "voice_other_note": "Die vollständige Liste steht in der Stimmdatei.",
    },
    "fr": {
        "voice_h": "Liste des voix prédéfinies",
        "voice_menu": "Fichier des voix",
        "voice_intro": "Ces voix prédéfinies peuvent être passées dans `audio_references`; `voice_type` est le Voice ID. Ce README français ne rend pas le long tableau et renvoie vers le fichier des voix.",
        "voice_source_label": "Fichier complet des voix",
        "voice_docs_label": "Documentation des voix EvoLink",
        "voice_other_note": "Consultez le fichier des voix pour la liste complète.",
    },
    "tr": {
        "voice_h": "Hazır ses listesi",
        "voice_menu": "Ses dosyası",
        "voice_intro": "Bu hazır sesler `audio_references` içinde geçirilebilir; `voice_type` Voice ID değeridir. Türkçe README uzun tabloyu işlemez ve ses dosyasına yönlendirir.",
        "voice_source_label": "Tam ses dosyası",
        "voice_docs_label": "EvoLink ses dokümanı",
        "voice_other_note": "Tam liste için ses dosyasını inceleyin.",
    },
    "ru": {
        "voice_h": "Список предустановленных голосов",
        "voice_menu": "Файл голосов",
        "voice_intro": "Эти предустановленные голоса можно передавать в `audio_references`; `voice_type` является Voice ID. Русская README не выводит длинную таблицу и направляет к файлу голосов.",
        "voice_source_label": "Полный файл голосов",
        "voice_docs_label": "Документация голосов EvoLink",
        "voice_other_note": "Полный список смотрите в файле голосов.",
    },
}

for locale, copy in VOICE_COPY.items():
    UI[locale].update(copy)

VOICE_DOC_LABELS = {
    "en": "Preset voice docs",
    "zh-CN": "预设音色文档",
    "zh-TW": "預設音色文件",
    "ja": "プリセット音色ドキュメント",
    "ko": "프리셋 음색 문서",
    "es": "Documentación de voces predefinidas",
    "pt": "Documentação de vozes predefinidas",
    "de": "Dokumentation der voreingestellten Stimmen",
    "fr": "Documentation des voix prédéfinies",
    "tr": "Hazır ses dokümanı",
    "ru": "Документация предустановленных голосов",
}

for locale, label in VOICE_DOC_LABELS.items():
    UI[locale]["links"] = f"{UI[locale]['links']} | [{label}]({VOICE_DOCS_URL})"

CATEGORY_TITLES = {
    "zh-CN": ["旁白与短视频", "音频优先视频工作流", "音频剧与场景生成", "参考声音与角色配音探索", "工具与服务商集成", "长内容、成本与限制"],
    "zh-TW": ["旁白與短影音", "音訊優先影片工作流", "音訊劇與場景生成", "參考聲音與角色配音探索", "工具與服務商整合", "長內容、成本與限制"],
    "ja": ["ナレーションと短尺動画", "音声先行の動画ワークフロー", "音声ドラマとシーン生成", "参照音声とキャラクター音声探索", "ツールとプロバイダー統合", "長尺コンテンツ、コスト、制約"],
    "ko": ["내레이션과 숏폼 영상", "오디오 우선 영상 워크플로", "오디오 드라마와 장면 생성", "참조 음성과 캐릭터 보이스 탐색", "도구 및 제공자 통합", "롱폼, 비용, 한계"],
    "es": ["Narración y video corto", "Flujos de video con audio primero", "Audio drama y generación de escenas", "Voces de referencia y casting de personajes", "Integraciones de herramientas y proveedores", "Contenido largo, coste y límites"],
    "pt": ["Narração e vídeo curto", "Workflows de vídeo guiados por áudio", "Áudio drama e geração de cena", "Vozes de referência e casting de personagens", "Integrações de ferramentas e provedores", "Conteúdo longo, custo e limites"],
    "de": ["Narration und Kurzvideo", "Audio-First-Video-Workflows", "Audio-Drama und Szenengenerierung", "Referenzstimmen und Character Casting", "Tool- und Provider-Integrationen", "Langform, Kosten und Grenzen"],
    "fr": ["Narration et vidéo courte", "Workflows vidéo pilotés par l'audio", "Fiction audio et génération de scènes", "Voix de référence et casting de personnages", "Intégrations d'outils et de fournisseurs", "Long format, coût et limites"],
    "tr": ["Anlatım ve kısa video", "Ses öncelikli video iş akışları", "Sesli drama ve sahne üretimi", "Referans sesler ve karakter sesi seçimi", "Araç ve sağlayıcı entegrasyonları", "Uzun içerik, maliyet ve sınırlar"],
    "ru": ["Озвучка и короткие видео", "Видео-процессы от аудио", "Аудиодрама и генерация сцен", "Референсные голоса и подбор голоса персонажа", "Интеграции инструментов и провайдеров", "Длинный формат, стоимость и ограничения"],
}

TYPE_LABELS = {
    "zh-CN": {"Demo": "演示", "Tutorial": "教程", "Evaluation": "评估", "Integration": "集成", "Benchmark": "基准", "Limit": "限制"},
    "zh-TW": {"Demo": "演示", "Tutorial": "教學", "Evaluation": "評估", "Integration": "整合", "Benchmark": "基準", "Limit": "限制"},
    "ja": {"Demo": "デモ", "Tutorial": "チュートリアル", "Evaluation": "評価", "Integration": "統合", "Benchmark": "ベンチマーク", "Limit": "制約"},
    "ko": {"Demo": "데모", "Tutorial": "튜토리얼", "Evaluation": "평가", "Integration": "통합", "Benchmark": "벤치마크", "Limit": "한계"},
    "es": {"Demo": "Demo", "Tutorial": "Tutorial", "Evaluation": "Evaluación", "Integration": "Integración", "Benchmark": "Benchmark", "Limit": "Límite"},
    "pt": {"Demo": "Demo", "Tutorial": "Tutorial", "Evaluation": "Avaliação", "Integration": "Integração", "Benchmark": "Benchmark", "Limit": "Limite"},
    "de": {"Demo": "Demo", "Tutorial": "Tutorial", "Evaluation": "Bewertung", "Integration": "Integration", "Benchmark": "Benchmark", "Limit": "Grenze"},
    "fr": {"Demo": "Démo", "Tutorial": "Tutoriel", "Evaluation": "Évaluation", "Integration": "Intégration", "Benchmark": "Benchmark", "Limit": "Limite"},
    "tr": {"Demo": "Demo", "Tutorial": "Rehber", "Evaluation": "Değerlendirme", "Integration": "Entegrasyon", "Benchmark": "Benchmark", "Limit": "Sınır"},
    "ru": {"Demo": "Демо", "Tutorial": "Руководство", "Evaluation": "Оценка", "Integration": "Интеграция", "Benchmark": "Бенчмарк", "Limit": "Ограничение"},
}

CASE_TITLES = {
    "zh-CN": ["Vlog 风格短视频旁白", "短视频创作者旁白适配", "用六人音频引导 Seedance 视频", "多片段故事视频的音频规划", "音频优先的 Seedance 参考工作流", "带环境声的两分钟对白", "博物馆导览式场景对白", "故事播客与电影感旁白", "参考声音 MC 工作流", "Claude MCP 旁白与多语言配音集成", "参考音频质量与高声线限制", "创作者工作台配音总结", "电子书转有声书工作流", "社交故事旁白内容引擎", "图像引导的角色声音探索", "WaveSpeedAI 文本、声音与图像引导音频", "NanoGPT 参考音频与参考图访问", "音乐剧场景实验", "专用音乐模型对比限制", "低成本测试声音表演与拟音"],
    "zh-TW": ["Vlog 風格短影音旁白", "短影音創作者旁白適配", "用六人音訊引導 Seedance 影片", "多片段故事影片的音訊規劃", "音訊優先的 Seedance 參考工作流", "帶環境聲的兩分鐘對白", "博物館導覽式場景對白", "故事 Podcast 與電影感旁白", "參考聲音 MC 工作流", "Claude MCP 旁白與多語配音整合", "參考音訊品質與高聲線限制", "創作者工作台配音摘要", "電子書轉有聲書工作流", "社群故事旁白內容引擎", "圖像引導的角色聲音探索", "WaveSpeedAI 文字、聲音與圖像引導音訊", "NanoGPT 參考音訊與參考圖存取", "音樂劇場景實驗", "專用音樂模型對比限制", "低成本測試聲音表演與擬音"],
    "ja": ["Vlog 風ショート動画ナレーション", "ショート動画クリエイター向けナレーション適性", "6 人の音声で Seedance 動画を誘導", "マルチクリップ物語動画の音声設計", "音声先行の Seedance 参照ワークフロー", "環境音付き 2 分間ダイアログ", "博物館ガイド風の場面対話", "ストーリーポッドキャストと映画的ナレーション", "参照音声 MC ワークフロー", "Claude MCP のボイスオーバーと多言語吹き替え統合", "参照音声品質と高音ボイスの制約", "クリエイター作業環境でのボイスオーバー整理", "電子書籍からオーディオブックへのワークフロー", "SNS ストーリー朗読エンジン", "画像参照によるキャラクター音声探索", "WaveSpeedAI のテキスト・音声・画像参照オーディオ", "NanoGPT の参照音声と参照画像アクセス", "ミュージカルシーン実験", "専用音楽モデルとの比較上の制約", "声の演技とフォーリーの低コスト検証"],
    "ko": ["Vlog 스타일 숏폼 내레이션", "숏폼 크리에이터 내레이션 적합성", "6명 음성으로 Seedance 영상 유도", "멀티클립 스토리 영상의 오디오 설계", "오디오 우선 Seedance 참조 워크플로", "환경음이 포함된 2분 대화", "박물관 안내 장면 대화", "스토리 팟캐스트와 영화적 내레이션", "참조 음성 MC 워크플로", "Claude MCP 보이스오버 및 다국어 더빙 통합", "참조 오디오 품질과 높은 음역 제한", "크리에이터 작업공간 보이스오버 요약", "전자책을 오디오북으로 바꾸는 워크플로", "소셜 스토리 내레이션 엔진", "이미지 기반 캐릭터 음성 탐색", "WaveSpeedAI의 텍스트, 음성, 이미지 참조 오디오", "NanoGPT 참조 오디오와 이미지 접근", "뮤지컬 장면 실험", "전용 음악 모델과의 비교 한계", "음성 연기와 폴리의 저비용 테스트"],
}

for key, titles in {
    "es": ["Narración de video corto estilo Vlog", "Ajuste de narración para creadores de video corto", "Audio de seis hablantes para guiar video en Seedance", "Planificación de audio para historias multiclips", "Flujo Seedance con audio primero", "Diálogo de dos minutos con ambiente", "Diálogo de escena con guía de museo", "Podcast narrativo y narración cinematográfica", "Flujo de MC con voz de referencia", "Integración de locución y doblaje en Claude MCP", "Calidad de audio de referencia y límite en voces agudas", "Resumen de locución en espacio de creador", "Flujo de ebook a audiolibro", "Motor de narración para historias sociales", "Casting de voz de personaje guiado por imagen", "Audio guiado por texto, voz e imagen en WaveSpeedAI", "Acceso a audio e imagen de referencia en NanoGPT", "Experimento de escena musical", "Límite frente a modelos musicales dedicados", "Prueba de bajo coste para actuación de voz y foley"],
    "pt": ["Narração de vídeo curto estilo Vlog", "Adequação de narração para criadores de vídeo curto", "Áudio com seis falantes para guiar vídeo no Seedance", "Planejamento de áudio para histórias em múltiplos clipes", "Workflow Seedance guiado primeiro por áudio", "Diálogo de dois minutos com ambiência", "Diálogo de cena com guia de museu", "Podcast narrativo e narração cinematográfica", "Workflow de MC com voz de referência", "Integração de narração e dublagem no Claude MCP", "Qualidade de áudio de referência e limite em vozes agudas", "Resumo de narração em espaço de criador", "Workflow de ebook para audiolivro", "Motor de narração para histórias sociais", "Casting de voz de personagem guiado por imagem", "Áudio guiado por texto, voz e imagem no WaveSpeedAI", "Acesso a áudio e imagem de referência no NanoGPT", "Experimento de cena musical", "Limite frente a modelos musicais dedicados", "Teste de baixo custo para atuação vocal e foley"],
    "de": ["Vlog-artige Kurzvideo-Narration", "Narrationsfit für Kurzvideo-Creator", "Sechs Sprecher als Audioführung für Seedance-Video", "Audioplanung für Multi-Clip-Storyvideos", "Audio-First Seedance-Referenzworkflow", "Zwei-Minuten-Dialog mit Atmosphäre", "Szenendialog mit Museumsführer", "Story-Podcast und filmische Narration", "MC-Workflow mit Referenzstimme", "Claude MCP Integration für Voiceover und Synchronisation", "Referenzaudio-Qualität und Grenze hoher Stimmen", "Voiceover-Zusammenfassung für Creator-Workspace", "Workflow von E-Book zu Audiobook", "Narrationsmaschine für Social Stories", "Bildgeführtes Casting von Charakterstimmen", "Text-, Stimmen- und bildgeführtes Audio bei WaveSpeedAI", "Referenzaudio- und Bildzugang bei NanoGPT", "Musical-Szenenexperiment", "Grenze gegenüber spezialisierten Musikmodellen", "Günstiger Test für Voice Acting und Foley"],
    "fr": ["Narration de vidéo courte façon Vlog", "Pertinence de la narration pour créateurs de vidéos courtes", "Audio à six voix pour guider une vidéo Seedance", "Planification audio pour récit multi-clips", "Workflow Seedance piloté d'abord par l'audio", "Dialogue de deux minutes avec ambiance", "Dialogue de scène avec guide de musée", "Podcast narratif et narration cinématographique", "Workflow de MC avec voix de référence", "Intégration voix off et doublage dans Claude MCP", "Qualité de l'audio de référence et limite des voix aiguës", "Synthèse voix off dans l'espace créateur", "Workflow ebook vers livre audio", "Moteur de narration pour histoires sociales", "Casting de voix de personnage guidé par image", "Audio guidé par texte, voix et image chez WaveSpeedAI", "Accès audio et image de référence dans NanoGPT", "Expérience de scène musicale", "Limite face aux modèles musicaux dédiés", "Test économique pour jeu vocal et bruitage"],
    "tr": ["Vlog tarzı kısa video anlatımı", "Kısa video üreticileri için anlatım uygunluğu", "Seedance videosunu yönlendiren altı konuşmacılı ses", "Çok klipli hikaye videosu için ses planlama", "Ses öncelikli Seedance referans iş akışı", "Ambiyanslı iki dakikalık diyalog", "Müze rehberi sahne diyaloğu", "Hikaye podcast'i ve sinematik anlatım", "Referans sesli MC iş akışı", "Claude MCP seslendirme ve dublaj entegrasyonu", "Referans ses kalitesi ve tiz ses sınırı", "Üretici çalışma alanında seslendirme özeti", "E-kitaptan sesli kitaba iş akışı", "Sosyal hikaye anlatım motoru", "Görüntü kılavuzlu karakter sesi seçimi", "WaveSpeedAI'de metin, ses ve görüntü kılavuzlu audio", "NanoGPT'de referans ses ve görüntü erişimi", "Müzikal sahne deneyi", "Özel müzik modellerine kıyasla sınır", "Ses oyunculuğu ve foley için düşük maliyetli test"],
    "ru": ["Озвучка короткого видео в стиле Vlog", "Подход к озвучке для авторов коротких видео", "Аудио с шестью голосами для управления видео Seedance", "Аудиопланирование для многофрагментной истории", "Audio-first рабочий процесс Seedance", "Двухминутный диалог с атмосферой", "Сценический диалог с музейным гидом", "Сторителлинг-подкаст и кинематографичная озвучка", "MC-процесс с референсным голосом", "Интеграция озвучки и дубляжа в Claude MCP", "Качество референсного аудио и ограничение высоких голосов", "Сводка озвучки в рабочем пространстве автора", "Процесс из ebook в аудиокнигу", "Движок озвучки социальных историй", "Подбор голоса персонажа по изображению", "Текстовое, голосовое и image-guided аудио в WaveSpeedAI", "Доступ к референсному аудио и изображению в NanoGPT", "Эксперимент с музыкальной сценой", "Ограничение по сравнению со специализированными музыкальными моделями", "Недорогой тест озвучки и foley"],
}.items():
    CASE_TITLES[key] = titles

CASE_BY_NUMBER = {case["number"]: case for case in DATA["cases"]}


def tr(locale: str, key: str) -> str:
    return UI.get(locale, {}).get(key, UI["en"][key])


def localized_category_title(locale: str, category: dict, index: int) -> str:
    if locale == "en":
        return category["title"]
    localized_titles = category.get("localized_titles") or {}
    if localized_titles.get(locale):
        return localized_titles[locale]
    return CATEGORY_TITLES[locale][index]


def localized_case_title(locale: str, case: dict) -> str:
    if locale == "en":
        return case["title"]
    localized_titles = case.get("localized_titles") or {}
    if localized_titles.get(locale):
        return localized_titles[locale]
    return CASE_TITLES[locale][case["number"] - 1]


def localized_type(locale: str, case_type: str) -> str:
    return TYPE_LABELS.get(locale, {}).get(case_type, case_type)


def localized_takeaway(locale: str, case: dict) -> str:
    if locale == "en":
        return case["takeaway"].strip()
    translated = CASE_TRANSLATIONS.get(locale, {}).get(str(case["number"]), {})
    if "takeaway" in translated:
        return translated["takeaway"]
    title = localized_case_title(locale, case)
    return tr(locale, "local_note").format(title=title)


def localized_notes(locale: str, case: dict) -> str:
    if locale == "en":
        return case["notes"]
    translated = CASE_TRANSLATIONS.get(locale, {}).get(str(case["number"]), {})
    if "notes" in translated:
        return translated["notes"]
    title = localized_case_title(locale, case)
    return tr(locale, "local_detail").format(title=title, notes=case["notes"])


VOICE_SCENARIO_LABELS = {
    "zh-CN": {"Multilingual": "多语言", "General": "通用", "Education": "教育"},
    "zh-TW": {"Multilingual": "多語言", "General": "通用", "Education": "教育"},
}

VOICE_ZH_TW_NAMES = {
    "温暖阿虎/Alvin 2.0": "溫暖阿虎/Alvin 2.0",
    "萌丫头/Cutey 2.0": "萌丫頭/Cutey 2.0",
    "贴心女声/Candy 2.0": "貼心女聲/Candy 2.0",
    "鸡汤妹妹/Hope 2.0": "雞湯妹妹/Hope 2.0",
    "磁性解说男声/Morgan 2.0": "磁性解說男聲/Morgan 2.0",
    "Tina老师 2.0": "Tina老師 2.0",
}

VOICE_ZH_TW_LANGUAGES = {
    "中文、日语、印尼语、墨西哥西班牙语；方言：四川话、陕西话、东北话": "中文、日語、印尼語、墨西哥西班牙語；方言：四川話、陝西話、東北話",
    "中文（英文名 Brayan）": "中文（英文名 Brayan）",
    "中文（英文名 Alvin）": "中文（英文名 Alvin）",
    "中文（英文名 Cutey）": "中文（英文名 Cutey）",
    "中文（英文名 Candy）": "中文（英文名 Candy）",
    "中文（英文名 Hope）": "中文（英文名 Hope）",
    "中文（英文名 Morgan）": "中文（英文名 Morgan）",
    "中文、英式英语（支持中英双语教学场景）": "中文、英式英語（支援中英雙語教學場景）",
}


def localized_voice_scenario(locale: str, voice: dict) -> str:
    scenario = voice.get("scenario")
    return VOICE_SCENARIO_LABELS.get(locale, {}).get(scenario, scenario)


def localized_voice_name(locale: str, voice: dict) -> str:
    name = voice.get("voice_name")
    if locale == "zh-TW":
        return VOICE_ZH_TW_NAMES.get(name, name)
    return name


def localized_voice_language(locale: str, voice: dict) -> str:
    language = voice.get("language", "")
    if locale == "en":
        return re.sub(r"\s*[（(][^()（）]*[\)）]", "", language).strip()
    if locale == "zh-TW":
        return VOICE_ZH_TW_LANGUAGES.get(language, language)
    return language


def markdown_cell(value: object) -> str:
    return " ".join(str(value or "").split()).replace("|", "\\|")


def truncate(value: object, limit: int) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def badge(label: str, color: str, target: str) -> str:
    return f"[![{label}](https://img.shields.io/badge/{quote(label, safe='')}-{color})]({target})"


def category_anchor(category: dict) -> str:
    return category["id"]


def build_header(locale: str) -> list[str]:
    lang_badges = " ".join(badge(item["label"], item["color"], item["file"]) for item in LOCALES.values())
    return [
        "<div align=\"center\">",
        "",
        f"<a href=\"https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=banner&utm_campaign={CAMPAIGN}\"><img src=\"images/en.png\" alt=\"Seed-Audio 1.0 usecase repository banner\" width=\"760\"></a>",
        "",
        "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)",
        f"[![Try it on Evolink](https://img.shields.io/badge/Try_it_on-Evolink-black)](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=badge&utm_campaign={CAMPAIGN})",
        f"[![Website](https://img.shields.io/badge/Website-Live-orange)](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=badge&utm_campaign={CAMPAIGN})",
        f"[![Docs](https://img.shields.io/badge/Docs-Read-blue)](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=readme&utm_campaign={CAMPAIGN})",
        "",
        lang_badges,
        "",
        "</div>",
        "",
        f"# {tr(locale, 'title')}",
        "",
    ]


def build_quick_api(locale: str) -> list[str]:
    url = f"https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=readme&utm_campaign={CAMPAIGN}"
    return [
        f"## {tr(locale, 'api_h')}",
        "",
        tr(locale, "api_1").format(url=url),
        "",
        "```bash",
        "export EVOLINK_API_KEY=\"your_api_key_here\"",
        "",
        "curl --request POST \\",
        "  --url https://api.evolink.ai/v1/audios/generations \\",
        "  --header \"Authorization: Bearer ${EVOLINK_API_KEY}\" \\",
        "  --header \"Content-Type: application/json\" \\",
        "  --data '{",
        "    \"model\": \"doubao-seed-audio-1-0\",",
        "    \"prompt\": \"Create a 15-second calm product video audio bed with soft music, a clean studio ambience, and gentle narration.\",",
        "    \"format\": \"mp3\",",
        "    \"sample_rate\": 24000",
        "  }'",
        "```",
        "",
        tr(locale, "api_2"),
        "",
        tr(locale, "api_3"),
        "",
    ]


def build_menu(locale: str) -> list[str]:
    lines = [f"## {tr(locale, 'menu')}", "", f"| {tr(locale, 'section')} | {tr(locale, 'cases')} |", "|---|---|"]
    for index, category in enumerate(DATA["categories"]):
        case_list = ", ".join(f"{tr(locale, 'case')} {number}" for number in category["case_numbers"])
        lines.append(f"| [{localized_category_title(locale, category, index)}](#{category_anchor(category)}) | {case_list} |")
    lines.append(f"| [{tr(locale, 'ack')}](#acknowledge) | {tr(locale, 'ack_row')} |")
    lines.append("")
    return lines


def build_voice_list(locale: str) -> list[str]:
    docs_url = VOICE_DATA["metadata"]["source_doc_url"]
    lines = [
        "<a id=\"voice-list\"></a>",
        f"## {tr(locale, 'voice_h')}",
        "",
        tr(locale, "voice_intro"),
        "",
        f"{tr(locale, 'voice_source_label')}: [data/voice-list.json](data/voice-list.json)",
        f"{tr(locale, 'voice_docs_label')}: [{docs_url}]({docs_url})",
        "",
    ]

    if locale == "en":
        rows = [voice for voice in VOICE_SOURCES if voice.get("language_group") != "chinese"]
    elif locale in {"zh-CN", "zh-TW"}:
        rows = [voice for voice in VOICE_SOURCES if voice.get("language_group") == "chinese"][:50]
    else:
        return [*lines, tr(locale, "voice_other_note"), ""]

    lines.extend(
        [
            f"| {tr(locale, 'voice_col_scenario')} | {tr(locale, 'voice_col_name')} | {tr(locale, 'voice_col_type')} | {tr(locale, 'voice_col_language')} |",
            "|---|---|---|---|",
        ]
    )
    for voice in rows:
        lines.append(
            f"| {markdown_cell(localized_voice_scenario(locale, voice))} | {markdown_cell(localized_voice_name(locale, voice))} | `{markdown_cell(voice.get('voice_type'))}` | {markdown_cell(localized_voice_language(locale, voice))} |"
        )
    lines.append("")
    return lines


def build_category_tables(locale: str) -> list[str]:
    lines: list[str] = []
    for index, category in enumerate(DATA["categories"]):
        lines.extend(
            [
                f"<a id=\"{category_anchor(category)}\"></a>",
                f"## {localized_category_title(locale, category, index)}",
                "",
                f"| {tr(locale, 'case')} | {tr(locale, 'what')} | {tr(locale, 'type')} |",
                "|---|---|---|",
            ]
        )
        for number in category["case_numbers"]:
            case = CASE_BY_NUMBER[number]
            title = localized_case_title(locale, case)
            takeaway = localized_takeaway(locale, case)
            lines.append(f"| [{tr(locale, 'case')} {number}: {title}](#case-{number}) | {takeaway} | {localized_type(locale, case['type'])} |")
        lines.append("")
    return lines


def build_case_details(locale: str) -> list[str]:
    lines = []
    for case in DATA["cases"]:
        title = localized_case_title(locale, case)
        takeaway = localized_takeaway(locale, case)
        notes = localized_notes(locale, case)
        lines.extend(
            [
                f"<a id=\"case-{case['number']}\"></a>",
                f"### {tr(locale, 'case')} {case['number']}: [{title}]({case['source_url']}) ({tr(locale, 'by')} [@{case['author']}]({case['author_url']}))",
                "",
                f"**{takeaway}**",
                "",
                notes,
                "",
            ]
        )
        media = case.get("media") or {}
        if media.get("type") == "video" and media.get("thumbnail_path") and media.get("path"):
            video_url = f"{RAW_MEDIA_BASE}/{media['path']}"
            lines.extend(
                [
                    f"[![{tr(locale, 'case')} {case['number']} video preview]({media['thumbnail_path']})]({video_url})",
                    "",
                    f"[{tr(locale, 'open_video')}]({video_url})",
                    "",
                ]
            )
        elif media.get("type") == "image" and media.get("path"):
            lines.extend(
                [
                    f"![{tr(locale, 'case')} {case['number']} media]({media['path']})",
                    "",
                ]
            )
        lines.extend(
            [
                f"{tr(locale, 'type')}: {localized_type(locale, case['type'])} | {tr(locale, 'date')}: {case['date']}",
                "",
            ]
        )
    return lines


def build_readme(locale: str) -> str:
    meta = DATA["metadata"]
    categories = ", ".join(localized_category_title(locale, category, index) for index, category in enumerate(DATA["categories"]))
    lines = build_header(locale)
    lines.extend(
        [
            f"## {tr(locale, 'intro_h')}",
            "",
            tr(locale, "intro"),
            "",
            f"**{tr(locale, 'summary')}**",
            "",
            tr(locale, "source_note"),
            "",
            f"[{tr(locale, 'try')}](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=readme&utm_campaign={CAMPAIGN})",
            "",
            f"## {tr(locale, 'overview')}",
            "",
            f"- **{tr(locale, 'overview_1').format(n=meta['selected_case_count'], sample=meta['accepted_count'])}**",
            f"- {tr(locale, 'overview_2').format(categories=categories)}",
            f"- {tr(locale, 'overview_3')}",
            f"- {tr(locale, 'overview_4')}",
            "",
            "> [!NOTE]",
            f"> {tr(locale, 'note_1')}",
            "",
            "> [!NOTE]",
            f"> {tr(locale, 'note_2')}",
            "",
            tr(locale, "links"),
            "",
        ]
    )
    lines.extend(build_quick_api(locale))
    lines.extend(build_menu(locale))
    lines.extend(build_category_tables(locale))
    lines.extend(build_case_details(locale))
    lines.extend(
        [
            "<a id=\"acknowledge\"></a>",
            f"## {tr(locale, 'ack')}",
            "",
            tr(locale, "ack_1"),
            "",
            tr(locale, "ack_2"),
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    for key, loc in LOCALES.items():
        path = ROOT / loc["file"]
        path.write_text(build_readme(key), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
