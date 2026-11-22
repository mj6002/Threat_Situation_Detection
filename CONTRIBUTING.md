# Contributing

Two people, one repo, a hard deadline. These rules exist to avoid merge conflicts and surprises.

## Workflow

1. Pick an issue (or create one) and say in a comment that you are taking it.
2. Branch from `main`: `feat/<module>-<short-name>`, `fix/<short-name>`, `docs/<short-name>`.
3. Keep PRs small (about a day of work). Open a PR early as a draft if you want feedback.
4. The other person reviews and merges. Do not push directly to `main`.
5. Before opening a PR: `ruff check .` and `pytest` both pass.

## Ownership (avoids conflicts)

Each module has one owner (see the status table in the README). Edit another person's module only through a PR they review. `types.py`, `configs/default.yaml` and `pipeline.py` are shared: announce changes in an issue first.

## The contract rule

A detector returns `DetectorOutput(name, score in [0,1], confidence in [0,1])`. If you need more information passed along, put it in `meta`. Do not change the signature without agreement, because the other person's code depends on it.

## Never commit

Datasets, videos, model weights, `.env` files, or our staged clips. They are in `.gitignore`; do not force-add them. Share large files through a shared drive and note the path in `docs/DATASETS.md`.

## Commit messages

Short and specific: `crowd: add optical-flow speed feature`. One idea per commit.

## Writing about results

Report real numbers only, always next to a baseline, and include failure cases. Call the harassment module a *risk pattern detector*, never a harassment detector.
