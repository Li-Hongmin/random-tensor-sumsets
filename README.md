# Concentration of Random Tensor Sumsets

[![verify](https://github.com/Li-Hongmin/random-tensor-sumsets/actions/workflows/verify.yml/badge.svg)](https://github.com/Li-Hongmin/random-tensor-sumsets/actions/workflows/verify.yml) [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.24054505-blue)](https://doi.org/10.5281/zenodo.24054505)

**Hongmin Li** (Institute of Science Tokyo; The University of Tokyo) · ORCID [0000-0003-0228-0600](https://orcid.org/0000-0003-0228-0600)

Main result of the manuscript: for the random sets A_n ⊂ Z^n of Cutler–Pebody–Sarkar and every fixed nonzero integer k, the variance of |A_n + kA_n| is small enough that the cardinality concentrates at the exponential rate of its mean, as conjectured by Cutler, Pebody and Sarkar.

- Manuscript on rStation: <https://rstation.ai/problems/math/papers/2/v2> (version 2)
- Archived on Zenodo: concept DOI [10.5281/zenodo.24054505](https://doi.org/10.5281/zenodo.24054505) (all versions); this repository mirrors version 2, DOI [10.5281/zenodo.24054513](https://doi.org/10.5281/zenodo.24054513)

## Contents

- `paper/paper.md`, `paper/random-tensor-sumsets.pdf` — the manuscript (version 2).
- `verification/` — the supplement of that version, unpacked unchanged; its own README describes each file.
- `.github/workflows/verify.yml` — reruns every check below on each push.

## What the programs check

| Check | Command (run inside `verification/`) |
|---|---|
| Finite checks of the lemmas | `python check_lemmas.py` |

The programs check the finite and exact computations used in the manuscript; the mathematical arguments are those written in the paper.

## Reproducing

```sh
cd verification
python check_lemmas.py
```

Requirements: Python 3.9+. Run the commands from a copy if you want to keep the recorded outputs untouched.

## Cite

```bibtex
@misc{li2026randomtensorsumsets,
  author    = {Li, Hongmin},
  title     = {Concentration of Random Tensor Sumsets},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.24054505},
  url       = {https://doi.org/10.5281/zenodo.24054505}
}
```

## License

Manuscript and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code: MIT (see `LICENSE`).
