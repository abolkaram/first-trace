# First Trace

The question is not whether a sentence exists now. The question is where it first entered the public record.

[Descend through the public core](https://first-trace.pages.dev/) · [Inspect the StudioNet contract](https://explorer-studio.genlayer.com/address/0x26f11497B706D6E1F2C57C2B03C4E117a8a0F9D0)

First Trace pins one ordered timeline manifest containing a bounded claim and three to seven public snapshots. Every snapshot is fetched and bound to an ordered SHA-256 digest. A permissionless location pass asks validators to classify the claim in every frozen layer with a boolean presence vector and a closed basis code: `PRESENT_EXACT`, `PRESENT_SEMANTIC`, or `ABSENT`. The contract derives the earliest index itself.

`pin(manifest_url)` creates `PINNED`. `locate(trace_id)` terminates once as `FOUND` or `NOT_FOUND`. `get_trace` exposes the complete vector, basis codes, labels, URLs, digests, and first index. Duplicate manifests, duplicate snapshots, changed bytes, incomplete vectors, contradictory codes, and replay are rejected.

The public interface is a vertical excavation core. One timeline reel is pinned at the top; visitors descend through dated layers and lift the first positive stratum. It does not reuse a dashboard, card grid, or repeated URL form.

## Verify

```text
python -m pytest -q
genvm-lint contracts/contract.py
python scripts/smoke.py
```

The bundled snapshots are operator-controlled demonstration records and are labelled accordingly.
