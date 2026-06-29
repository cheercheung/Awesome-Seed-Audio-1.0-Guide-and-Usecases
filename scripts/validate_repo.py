#!/usr/bin/env python3
"""Static validation for the Seed-Audio usecase repository template."""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]

LOCALIZED_READMES = [
    "README.md",
    "README_es.md",
    "README_pt.md",
    "README_ja.md",
    "README_ko.md",
    "README_de.md",
    "README_fr.md",
    "README_tr.md",
    "README_zh-TW.md",
    "README_zh-CN.md",
    "README_ru.md",
]

TRANSLATED_READMES = {
    "zh-CN": "README_zh-CN.md",
    "zh-TW": "README_zh-TW.md",
    "es": "README_es.md",
    "pt": "README_pt.md",
    "ja": "README_ja.md",
    "ko": "README_ko.md",
    "de": "README_de.md",
    "fr": "README_fr.md",
    "tr": "README_tr.md",
    "ru": "README_ru.md",
}

LOCALIZED_EXPECTED_SNIPPETS = {
    "README_es.md": ["| Sección | Casos |", "| Caso | Qué muestra | Tipo |", "### Caso 1:", "(por [@"],
    "README_pt.md": ["| Seção | Casos |", "| Caso | O que mostra | Tipo |", "### Caso 1:", "(por [@"],
    "README_ja.md": ["| セクション | ケース |", "| ケース | 注目点 | タイプ |", "### ケース 1:", "(作者 [@"],
    "README_ko.md": ["| 섹션 | 사례 |", "| 사례 | 보여주는 점 | 유형 |", "### 사례 1:", "(작성자 [@"],
    "README_de.md": ["| Abschnitt | Fälle |", "| Fall | Was er zeigt | Typ |", "### Fall 1:", "(von [@"],
    "README_fr.md": ["| Section | Cas |", "| Cas | Ce qu'il montre | Type |", "### Cas 1:", "(par [@"],
    "README_tr.md": ["| Bölüm | Vakalar |", "| Vaka | Neyi gösterir | Tür |", "### Vaka 1:", "(yazar [@"],
    "README_zh-TW.md": ["| 章節 | 案例 |", "| 案例 | 展示重點 | 類型 |", "### 案例 1:", "(作者 [@"],
    "README_zh-CN.md": ["| 章节 | 案例 |", "| 案例 | 展示重点 | 类型 |", "### 案例 1:", "(作者 [@", "证据来源：", "可复制做法：", "实际流程：", "注意事项：", "打开视频文件"],
    "README_ru.md": ["| Раздел | Кейсы |", "| Кейс | Что показывает | Тип |", "### Кейс 1:", "(автор [@"],
}

BANNED_LOCALIZED_PHRASES = [
    "| Section | Cases |",
    "| Case | What it shows | Type |",
    "| [Case ",
    "### Case ",
    "(by [@",
    "Use this case",
    "The source",
    "The response creates",
    "Read the companion",
    "The collection favors",
    "Each case includes the original source",
    "Use this repo",
    "Covers Narration",
    "What it shows",
    "Credits and correction policy",
    "evaluate Seed-Audio",
    "frame Seed-Audio",
    "build an audio-first",
    "structure a three-step",
    "dubbing",
    "downstream",
    "用这个案例评估：",
    "该案例来自公开 X/Twitter 来源，适合作为此使用场景的证据。",
    "用這個案例評估：",
    "該案例來自公開 X/Twitter 來源，適合作為此使用場景的證據。",
    "Usa este caso para evaluar:",
    "Este caso proviene de una fuente pública de X/Twitter",
    "Use este caso para avaliar:",
    "Este caso vem de uma fonte pública do X/Twitter",
    "このケースで評価できること：",
    "このケースは公開 X/Twitter ソースから選定され",
    "이 사례로 평가할 수 있는 것:",
    "이 사례는 공개 X/Twitter 출처에서 선별되었으며",
    "Nutze diesen Fall zur Bewertung von:",
    "Dieser Fall stammt aus einer öffentlichen X/Twitter-Quelle",
    "Utilisez ce cas pour évaluer",
    "Ce cas provient d'une source publique X/Twitter",
    "Bu vakayı şunu değerlendirmek için kullanın:",
    "Bu vaka herkese açık bir X/Twitter kaynağından seçilmiştir",
    "Используйте этот кейс для оценки:",
    "Этот кейс выбран из публичного источника X/Twitter",
]

BANNED_PLACEHOLDERS = [
    "SAUDIO",
    "SDANCE",
    "CLAUDEMCP",
    "WAVESPEEDAI",
    "NANOGPT",
    "HIGGSFIELD",
    "SUNO",
    "AITA_TOKEN",
    "INTENT_TOKEN",
    "AESTHETIC_TOKEN",
    "EXECUTION_TOKEN",
    "API_KEY_TOKEN",
    "MC_TOKEN",
]

REQUIRED_FILES = [
    *LOCALIZED_READMES,
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    ".gitignore",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/case-submission.yml",
    ".github/ISSUE_TEMPLATE/correction.yml",
    "images/en.png",
    "data/source-index.json",
    "data/use-cases.json",
    "data/voice-list.json",
    "data/use-case-translations.json",
    "docs/maintenance.md",
    "docs/recent-x-use-cases.md",
    "docs/update-log.md",
    "docs/case-label-audit.md",
    "scripts/build_readmes.py",
]

EXPECTED_SELECTION_POLICY = "strong_evidence_public_sources_only"
PRIVATE_PUBLICATION_PATTERNS = [
    ".codex/",
    "USECASE_",
    "data/ingested_tweets.json",
    "github-repo-banner-output/",
]
RAW_MEDIA_BASE = "https://raw.githubusercontent.com/cheercheung/Awesome-Seed-Audio-1.0-Guide-and-Usecases/main"

REQUIRED_ENGLISH_SNIPPETS = [
    "Seed-Audio 1.0 Use Cases",
    "images/en.png",
    "Try_it_on-Evolink",
    "Quick API Access",
    "Preset voice docs",
    "Menu",
    "Case 11: Voice Acting, Foley, And Low-Cost Testing",
    "video preview",
    "Open video file",
    RAW_MEDIA_BASE,
    "https://api.evolink.ai/v1/audios/generations",
    "doubao-seed-audio-1-0",
    "Acknowledge",
]

REQUIRED_ZH_CN_NOTE_PARTS = ["证据来源：", "可复制做法：", "实际流程：", "注意事项："]

VALID_TYPES = {"Demo", "Tutorial", "Evaluation", "Integration", "Benchmark", "Limit"}
EXPECTED_ACCEPTED_COUNT = 93
EXPECTED_SELECTED_COUNT = 11
EXPECTED_REVIEW_QUEUE_COUNT = 20
PUBLIC_FILES_TO_SCAN = [
    "README.md",
    "data/source-index.json",
    "data/use-cases.json",
    "data/use-case-translations.json",
    "data/voice-list.json",
    "docs/maintenance.md",
    "docs/recent-x-use-cases.md",
    "docs/update-log.md",
    "docs/case-label-audit.md",
    "CONTRIBUTING.md",
]


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def anchored_section(text: str, anchor: str) -> str:
    marker = f"<a id=\"{anchor}\"></a>"
    if marker not in text:
        return ""
    rest = text.split(marker, 1)[1]
    headings = list(re.finditer(r"\n## ", rest))
    if len(headings) >= 2:
        return rest[: headings[1].start()]
    return rest


def table_rows(section: str) -> list[str]:
    return [line for line in section.splitlines() if line.startswith("| [") and "https://x.com/" in line]


def tracked_files() -> list[str]:
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def main() -> int:
    errors: list[str] = []
    selected_source_urls: set[str] = set()
    expected_case_count = EXPECTED_SELECTED_COUNT
    expected_media_paths: list[str] = []

    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"missing required file: {rel}")
        elif path.stat().st_size == 0:
            errors.append(f"empty required file: {rel}")

    for rel in tracked_files():
        if any(rel == pattern.rstrip("/") or rel.startswith(pattern) for pattern in PRIVATE_PUBLICATION_PATTERNS):
            errors.append(f"private/internal file is tracked publicly: {rel}")

    if (ROOT / "README.md").exists():
        readme = read_text("README.md")
        for snippet in REQUIRED_ENGLISH_SNIPPETS:
            if snippet not in readme:
                errors.append(f"README.md missing snippet: {snippet}")
        if "utm_source=github" not in readme:
            errors.append("README.md missing GitHub UTM links")
        if "## Prompt Cases" in readme:
            errors.append("README.md still contains legacy prompt-case section")
        case_headings = re.findall(r"^### Case (\d+): \[(.+?)\]\((https://x\.com/[^)]+)\) \(by \[@([^]]+)\]\((https://x\.com/[^)]+)\)\)", readme, flags=re.M)
        if len(case_headings) != expected_case_count:
            errors.append(f"README.md expected {expected_case_count} template case headings, found {len(case_headings)}")
        if sorted(int(row[0]) for row in case_headings) != list(range(1, expected_case_count + 1)):
            errors.append(f"README.md case numbers are not exactly 1..{expected_case_count}")
        anchors = re.findall(r"<a id=\"case-(\d+)\"></a>", readme)
        if sorted(int(item) for item in anchors) != list(range(1, expected_case_count + 1)):
            errors.append(f"README.md case anchors are not exactly case-1..case-{expected_case_count}")

    for rel in PUBLIC_FILES_TO_SCAN:
        path = ROOT / rel
        if path.exists():
            text = path.read_text(encoding="utf-8")
            if "/Users/" in text:
                errors.append(f"{rel} contains local /Users path")
            if ".codex" in text:
                errors.append(f"{rel} contains local .codex path")
            if "USECASE_" in text:
                errors.append(f"{rel} contains internal USECASE audit filename")

    for rel in LOCALIZED_READMES:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        case_count = len(re.findall(r"^### .+? \d+:", text, flags=re.M))
        if case_count != expected_case_count:
            errors.append(f"{rel} expected {expected_case_count} cases, found {case_count}")
        if "images/en.png" not in text:
            errors.append(f"{rel} missing banner image")
        if "utm_source=github" not in text:
            errors.append(f"{rel} missing GitHub UTM links")
        if rel != "README.md":
            for snippet in LOCALIZED_EXPECTED_SNIPPETS[rel]:
                if snippet not in text:
                    errors.append(f"{rel} missing localized snippet: {snippet}")
            for phrase in BANNED_LOCALIZED_PHRASES:
                if phrase in text:
                    errors.append(f"{rel} contains untranslated or broken phrase: {phrase}")
            for placeholder in BANNED_PLACEHOLDERS:
                if placeholder in text:
                    errors.append(f"{rel} contains unreplaced placeholder: {placeholder}")

    use_cases_path = ROOT / "data/use-cases.json"
    case_numbers: list[int] = []
    if use_cases_path.exists():
        payload = json.loads(use_cases_path.read_text(encoding="utf-8"))
        metadata = payload.get("metadata") or {}
        cases = payload.get("cases") or []
        categories = payload.get("categories") or []
        readme_text = read_text("README.md") if (ROOT / "README.md").exists() else ""
        if metadata.get("accepted_count") != EXPECTED_ACCEPTED_COUNT:
            errors.append(f"use-cases metadata expected accepted_count={EXPECTED_ACCEPTED_COUNT}")
        if metadata.get("selected_case_count") != expected_case_count:
            errors.append(f"use-cases metadata expected selected_case_count={expected_case_count}")
        if metadata.get("review_queue_count") != EXPECTED_REVIEW_QUEUE_COUNT:
            errors.append(f"use-cases metadata expected review_queue_count={EXPECTED_REVIEW_QUEUE_COUNT}")
        if metadata.get("selection_policy") != EXPECTED_SELECTION_POLICY:
            errors.append("use-cases metadata expected public strong-evidence selection policy")
        if len(cases) != expected_case_count:
            errors.append(f"use-cases.json expected {expected_case_count} cases, found {len(cases)}")
        if len(categories) < 5:
            errors.append("use-cases.json expected at least 5 categories")
        numbers = [case.get("number") for case in cases]
        case_numbers = [number for number in numbers if isinstance(number, int)]
        if numbers != list(range(1, expected_case_count + 1)):
            errors.append(f"use-cases.json case numbers are not exactly 1..{expected_case_count} in order")
        source_urls = []
        for case in cases:
            source_urls.append(case.get("source_url"))
            for key in ["title", "source_url", "author", "author_url", "type", "date", "takeaway", "notes"]:
                if not case.get(key):
                    errors.append(f"case {case.get('number')} missing {key}")
            notes = str(case.get("notes", ""))
            for required_note_part in ["Source evidence:", "What to copy:", "Watch-outs:"]:
                if required_note_part not in notes:
                    errors.append(f"case {case.get('number')} notes missing actionable section: {required_note_part}")
            if len(notes) < 420:
                errors.append(f"case {case.get('number')} notes are not detailed enough")
            if not str(case.get("source_url", "")).startswith("https://x.com/"):
                errors.append(f"case {case.get('number')} invalid source_url")
            if not str(case.get("author_url", "")).startswith("https://x.com/"):
                errors.append(f"case {case.get('number')} invalid author_url")
            if case.get("type") not in VALID_TYPES:
                errors.append(f"case {case.get('number')} invalid type: {case.get('type')}")
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(case.get("date", ""))):
                errors.append(f"case {case.get('number')} invalid date: {case.get('date')}")
            if case.get("evidence_strength") != "strong":
                errors.append(f"case {case.get('number')} expected evidence_strength=strong")
            media = case.get("media")
            if not isinstance(media, dict):
                errors.append(f"case {case.get('number')} missing media object")
            else:
                media_type = media.get("type")
                media_path = media.get("path")
                if media_type not in {"video", "image"}:
                    errors.append(f"case {case.get('number')} invalid media type: {media_type}")
                if not media_path:
                    errors.append(f"case {case.get('number')} missing media path")
                else:
                    local_media = ROOT / media_path
                    expected_media_paths.append(media_path)
                    if not local_media.is_file():
                        errors.append(f"case {case.get('number')} missing media file: {media_path}")
                    elif local_media.stat().st_size < 1024:
                        errors.append(f"case {case.get('number')} media file too small: {media_path}")
                    if media_path not in readme_text:
                        errors.append(f"README.md missing media path for case {case.get('number')}: {media_path}")
                if media_type == "video":
                    thumb_path = media.get("thumbnail_path")
                    if not thumb_path:
                        errors.append(f"case {case.get('number')} missing video thumbnail_path")
                    else:
                        local_thumb = ROOT / thumb_path
                        expected_media_paths.append(thumb_path)
                        if not local_thumb.is_file():
                            errors.append(f"case {case.get('number')} missing video thumbnail file: {thumb_path}")
                        elif local_thumb.stat().st_size < 1024:
                            errors.append(f"case {case.get('number')} video thumbnail too small: {thumb_path}")
                        if thumb_path not in readme_text:
                            errors.append(f"README.md missing media thumbnail for case {case.get('number')}: {thumb_path}")
                    raw_media_url = f"{RAW_MEDIA_BASE}/{media_path}"
                    if raw_media_url not in readme_text:
                        errors.append(f"README.md missing raw video link for case {case.get('number')}: {raw_media_url}")
                    if "Open video file" not in readme_text:
                        errors.append("README.md missing video fallback link")
        if len(source_urls) != len(set(source_urls)):
            errors.append("use-cases.json contains duplicate source URLs")
        selected_source_urls = set(source_urls)
        for rel in LOCALIZED_READMES:
            path = ROOT / rel
            if path.exists():
                text = path.read_text(encoding="utf-8")
                for media_path in expected_media_paths:
                    if media_path not in text:
                        errors.append(f"{rel} missing media path: {media_path}")

    voice_path = ROOT / "data/voice-list.json"
    if voice_path.exists():
        voice_payload = json.loads(voice_path.read_text(encoding="utf-8"))
        voice_meta = voice_payload.get("metadata") or {}
        voices = voice_payload.get("voices") or []
        voice_types = [voice.get("voice_type") for voice in voices]
        non_chinese_voices = [voice for voice in voices if voice.get("language_group") != "chinese"]
        chinese_voices = [voice for voice in voices if voice.get("language_group") == "chinese"]

        if voice_meta.get("source_type") != "evolink_docs_voice_list":
            errors.append("voice list metadata expected source_type=evolink_docs_voice_list")
        if voice_meta.get("voice_count") != 23:
            errors.append("voice list metadata expected voice_count=23")
        if voice_meta.get("non_chinese_voice_count") != 15:
            errors.append("voice list metadata expected non_chinese_voice_count=15")
        if voice_meta.get("chinese_voice_count") != 8:
            errors.append("voice list metadata expected chinese_voice_count=8")
        if len(voices) != 23:
            errors.append(f"voice list expected 23 voices, found {len(voices)}")
        if len(voice_types) != len(set(voice_types)):
            errors.append("voice list contains duplicate voice_type values")
        for voice in voices:
            for key in ["scenario", "voice_name", "voice_type", "language", "language_group"]:
                if not voice.get(key):
                    errors.append(f"voice row missing {key}: {voice}")
            if voice.get("language_group") not in {"chinese", "non_chinese"}:
                errors.append(f"voice row has invalid language_group: {voice.get('voice_type')}")

        source_doc_url = voice_meta.get("source_doc_url")
        for rel in LOCALIZED_READMES:
            path = ROOT / rel
            if path.exists():
                text = path.read_text(encoding="utf-8")
                if source_doc_url not in text:
                    errors.append(f"{rel} missing preset voice documentation link")
                if "<a id=\"voice-list\"></a>" in text:
                    errors.append(f"{rel} should not render a front preset voice section")
                if any(voice_type and voice_type in text for voice_type in voice_types):
                    errors.append(f"{rel} should link to voice documentation instead of rendering voice rows")

    translations_path = ROOT / "data/use-case-translations.json"
    if translations_path.exists():
        translations = json.loads(translations_path.read_text(encoding="utf-8"))
        for locale, rel in TRANSLATED_READMES.items():
            rows = translations.get(locale)
            if not isinstance(rows, dict):
                errors.append(f"use-case-translations missing locale: {locale}")
                continue
            readme_text = read_text(rel) if (ROOT / rel).exists() else ""
            for number in case_numbers or list(range(1, expected_case_count + 1)):
                row = rows.get(str(number), {})
                for field in ["takeaway", "notes"]:
                    value = row.get(field)
                    if not value:
                        errors.append(f"use-case-translations {locale} case {number} missing {field}")
                        continue
                    if len(value) < 24:
                        errors.append(f"use-case-translations {locale} case {number} {field} too short")
                    for placeholder in BANNED_PLACEHOLDERS:
                        if placeholder in value:
                            errors.append(f"use-case-translations {locale} case {number} {field} contains placeholder {placeholder}")
                    for phrase in BANNED_LOCALIZED_PHRASES:
                        if phrase in value:
                            errors.append(f"use-case-translations {locale} case {number} {field} contains generic phrase: {phrase}")
                    if value not in readme_text:
                        errors.append(f"{rel} does not include translated {field} for case {number}")
                    if locale == "zh-CN" and field == "notes":
                        for required_note_part in REQUIRED_ZH_CN_NOTE_PARTS:
                            if required_note_part not in value:
                                errors.append(f"use-case-translations zh-CN case {number} notes missing actionable section: {required_note_part}")
                        if len(value) < 180:
                            errors.append(f"use-case-translations zh-CN case {number} notes are not detailed enough")

    source_index = ROOT / "data/source-index.json"
    if source_index.exists():
        data = json.loads(source_index.read_text(encoding="utf-8"))
        search_rows = [item for item in data if item.get("id") == "public-seed-audio-search-2026-06-29"]
        if len(search_rows) != 1:
            errors.append("source index missing public-seed-audio-search-2026-06-29")
        else:
            row = search_rows[0]
            if row.get("accepted_count") != EXPECTED_ACCEPTED_COUNT:
                errors.append(f"source index expected accepted_count={EXPECTED_ACCEPTED_COUNT}")
            if row.get("review_queue_count") != EXPECTED_REVIEW_QUEUE_COUNT:
                errors.append(f"source index expected review_queue_count={EXPECTED_REVIEW_QUEUE_COUNT}")
            if row.get("selected_case_count") != expected_case_count:
                errors.append(f"source index expected selected_case_count={expected_case_count}")
            if row.get("selection_policy") != EXPECTED_SELECTION_POLICY:
                errors.append("source index expected public strong-evidence selection policy")
            if "data/voice-list.json" not in row.get("outputs", []):
                errors.append("source index missing data/voice-list.json output")
            if "media/cases/" not in row.get("outputs", []):
                errors.append("source index missing media/cases/ output")
            if row.get("media_download_count") != expected_case_count:
                errors.append(f"source index expected media_download_count={expected_case_count}")
            forbidden_keys = ["media_download_manifest", "source_audit"]
            for key in forbidden_keys:
                if key in row:
                    errors.append(f"source index should not expose internal field: {key}")
            for output in row.get("outputs", []):
                if output.startswith(".codex/") or output.startswith("USECASE_") or output == "data/ingested_tweets.json":
                    errors.append(f"source index exposes internal output: {output}")

    audit_path = ROOT / "docs/case-label-audit.md"
    if audit_path.exists():
        audit_text = audit_path.read_text(encoding="utf-8")
        for number in range(1, expected_case_count + 1):
            if f"| {number} |" not in audit_text:
                errors.append(f"case-label-audit missing case {number}")
        for snippet in ["Changed from Demo to Tutorial", "previous WaveSpeedAI provider-access case was removed", "Public cases: 11"]:
            if snippet not in audit_text:
                errors.append(f"case-label-audit missing snippet: {snippet}")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    print(f"root={ROOT}")
    print("localized_readmes=11")
    print(f"case_count={expected_case_count}")
    print(f"x_search_sample_count={EXPECTED_ACCEPTED_COUNT}")
    print("public_release_clean=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
