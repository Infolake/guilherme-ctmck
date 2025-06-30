
# CTMCK: Observable Signatures of a Three-Temporal Bounce-Universe

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15765710.svg)](https://doi.org/10.5281/zenodo.15765710)
[![arXiv](https://img.shields.io/badge/arXiv-PENDING-b31b1b.svg)](https://arxiv.org/abs/PENDING)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository contains the complete theoretical framework and computational tools for the **Camargo–Kletetschka Multidimensional Temporal Cosmogenesis (CTMCK)** model, which extends three-dimensional time theory to bouncing black-hole cosmology.

### Key Predictions

- 🌊 **Gravitational Wave Background**: Peak at f ≃ 100 μHz (LISA-optimal)
- 🔭 **Cosmological Tensions**: Simultaneous H₀ and S₈ tension resolution  
- 🌌 **JWST Anomalies**: Natural explanation for ultra-massive z > 10 galaxies
- 🔬 **Neutrino Masses**: Σmν = 0.29±0.05 eV (HiLLiPoP+DESI compatible)

## Repository Structure

```
guilherme-ctmck/
├── docs/
│   ├── ctmck_article_v03.tex    # Main LaTeX source
│   ├── ctmck_article_v03.pdf    # Final article (4 pages)
│   ├── appendices_ctmck.md      # Complete derivations
│   └── cover_letter_JCAP_template.md
├── figures/
│   ├── fig1_geometry_6d.png     # 6D temporal geometry
│   ├── fig2_gw_spectrum.png     # Gravitational wave spectrum
│   ├── fig3_tensions_resolution.png  # Cosmological parameter tensions
│   ├── fig4_particle_masses.png # Particle mass hierarchy
│   └── fig5_predictions_timeline.png # Experimental roadmap
├── scripts/
│   ├── analysis/                # Data analysis tools
│   ├── simulations/             # CTMCK simulations
│   └── plotting/                # Figure generation
├── data/
│   └── processed/               # Processed datasets
├── compile_check.sh             # LaTeX build script
└── Makefile                     # Build automation
```


## Article Versions

- **ctmck_article_v03.tex**: Monolithic version — all sections inline, ready for arXiv/Zenodo submission and full reproducibility.
- **ctmck_article_modular.tex**: Modular version — uses `\input{}` for each section, recommended for collaborative editing and ongoing development.

## Quick Start

> **Note on large files**  
> All high-resolution figures (`*.png`) and the compiled manuscript (`*.pdf`)
> are tracked via **Git LFS**.  
> Make sure you have LFS enabled (`git lfs install`) before cloning.

### Building the Article

```bash
# Clone repository
git clone https://github.com/guilherme-ctmck/guilherme-ctmck.git
cd guilherme-ctmck

# Build PDF (requires LaTeX)
./compile_check.sh
# or
make pdf
```

### Running Analysis Scripts

```bash
# Install Python dependencies
pip install -r requirements.txt

# Run CTMCK analysis
python scripts/analysis/ctmck_analysis.py

# Generate figures
python scripts/plotting/generate_habitability_maps.py
```

## Key Results

### Theoretical Framework

The CTMCK model extends Kletetschka's 3D temporal mechanics to cosmological scales, deriving:

- **Temporal radius hierarchy**: τ₁:τ₂:τ₃ = 1:4.835×10⁻³:2.875×10⁻⁴
- **Bounce density**: ρ_bounce = (c⁷/G²ℏ)τ₁⁻¹τ₂⁻¹τ₃⁻¹  
- **GW spectrum**: Ω_GW(f) = A(f/1μHz)⁻²/³ exp(-f/f_b)

### Observational Signatures

| Observable | CTMCK Prediction | Detectability |
|------------|------------------|---------------|
| GW Background | f_peak ≃ 100 μHz | LISA (2030s) |
| H₀ tension | Resolved via modified expansion | Current surveys |
| S₈ tension | Reduced through structure formation | Euclid, Roman |
| Neutrino masses | Σmν = 0.29±0.05 eV | CMB-S4, DESI |
| High-z galaxies | Enhanced formation at z > 10 | JWST ongoing |

## Experimental Roadmap

### Near-term (2025-2027)
- **CMB**: Planck legacy, ACT, SPT constraints
- **BAO**: DESI Year 1-3 data releases  
- **Supernovae**: Pantheon+ extended samples

### Medium-term (2028-2032)
- **LISA**: Direct GW background detection
- **Euclid**: Precision cosmological parameters
- **Roman**: High-z galaxy statistics
- **CMB-S4**: Ultimate neutrino mass sensitivity

### Long-term (2032+)
- **Einstein Telescope**: Enhanced GW sensitivity
- **30m telescopes**: Individual high-z galaxy studies

## Citation

If you use this work, please cite:

```bibtex
@article{Camargo2025CTMCK,
  title={Observable Signatures of a Three-Temporal Bounce-Universe Inside a Black Hole},
  author={Camargo, Guilherme de},
  journal={arXiv preprint arXiv:PENDING},
  year={2025},
  doi={10.5281/zenodo.15765710}
}
```

## Author

**Dr. Guilherme de Camargo**  
Independent Researcher  
📧 guilherme@medsuite.com.br  
🔗 [ORCID: 0009-0004-8913-9419](https://orcid.org/0009-0004-8913-9419)

Emergency physician and independent researcher developing unified theories of fundamental physics through three-dimensional time frameworks.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Last updated: June 2025 | Version 0.3*