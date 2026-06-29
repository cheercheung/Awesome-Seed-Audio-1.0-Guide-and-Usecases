# Pull Request Checklist

## Case Evidence

- [ ] Every new case has a public source link.
- [ ] Every new case has a creator profile link.
- [ ] Claims are grounded in the source and do not invent prompts, scores, audio results, or pricing.
- [ ] Case type is one of: Demo, Tutorial, Evaluation, Integration, Benchmark, Limit.
- [ ] Date uses `YYYY-MM-DD`.

## README Structure

- [ ] Each new case has a stable `<a id="case-x"></a>` anchor.
- [ ] Case heading uses `### Case X: [Title](source-link) (by [@author](author-link))`.
- [ ] Menu links point to `#case-x`.
- [ ] English and localized README files keep the same case order and source links.
- [ ] No raw source exports, internal curation datasets, or local source paths are committed.

## Maintenance

- [ ] `docs/maintenance.md` still reflects current repository policy.
- [ ] `python3 scripts/build_readmes.py` has been run when case data changed.
- [ ] `python3 scripts/validate_repo.py` passes.
