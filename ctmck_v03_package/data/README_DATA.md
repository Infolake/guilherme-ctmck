# 📊 CTMCK Data Directory

## 📁 Structure

```
data/
└── sample/          # Sample datasets for quick testing
```

## 🌌 **Complete Datasets**

For complete research datasets including:
- **Full stellar temporal correlations** (20+ MB)
- **Chilean telescope catalogs** (100+ MB)  
- **JWST reanalysis data** (50+ MB)
- **Habitability simulation grids** (200+ MB)

**Download from our Zenodo repository:**
📥 **DOI:** [10.5281/zenodo.15765710](https://doi.org/10.5281/zenodo.15765710)

## 🚀 **Quick Download Script**

```python
# Use our helper script to download specific datasets
python scripts/utils/download_chile_data.py --dataset stellar_correlations
python scripts/utils/download_chile_data.py --dataset jwst_reanalysis
```

## 📋 **Sample Data Usage**

The `sample/` directory contains small subsets suitable for:
- Testing analysis scripts
- Reproducing key figures  
- Educational demonstrations
- CI/CD pipeline validation

For production research, always use the complete datasets from Zenodo. 