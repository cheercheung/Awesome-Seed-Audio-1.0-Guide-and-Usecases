# Recent X-Derived Seed-Audio Use Cases

Date: 2026-06-29  
Search window: 2026-06-24 through 2026-06-29 UTC  
Query set: `"seed audio"`, `"Seed-Audio"`, `"SeedAudio"`  
Accepted sample: 93 deduplicated X/Twitter posts from 182 raw returned posts  
Candidate review queue: 20  
Selected public cases after source review: 12  
Selected cases with downloaded media: 12
Preset voice list: documentation link only

## Collection Notes

The collection used recent public X/Twitter searches with low engagement thresholds because the task was to discover use cases from recent discussion, not only high-like posts.

After the initial 20-candidate review, every candidate was checked against its original X/Twitter post and available thread context. The public README now keeps only strong-evidence cases: posts with concrete prompts, workflows, access paths, hands-on evaluations, or explicit limitation evidence.

The public preset voice list remains stored in [data/voice-list.json](../data/voice-list.json), but README files now point readers to the official EvoLink preset voice documentation instead of rendering a long voice table.

## Template Output

The public repository now follows the usecase template:

- each selected item is rendered as `Case X`
- each retained case has `evidence_strength=strong`
- each case has a public source link
- each case has an author profile link
- each case renders downloaded local media from `media/cases/`
- each case has a type and publication date
- case order is shared across English and localized README files
- raw X exports remain local audit artifacts and are not part of public release content

## Category Summary

| Category | Cases |
|---|---|
| Audio-First Video Workflows | Case 1-3 |
| Audio Drama And Scene Generation | Case 4-5 |
| Reference Voice And Character Casting | Case 6, Case 8, Case 10 |
| Tool And Provider Integrations | Case 7, Case 11 |
| Social Narration, Foley, And Cost Tests | Case 9, Case 12 |

## Representative Case Set

The selected cases are stored in [data/use-cases.json](../data/use-cases.json). The rendered README source is generated with:

```bash
python3 scripts/build_readmes.py
```

Validation is performed with:

```bash
python3 scripts/validate_repo.py
```

## Public Selection Policy

Medium- and weak-evidence candidates are excluded from the public README set under the final strong-only policy.
