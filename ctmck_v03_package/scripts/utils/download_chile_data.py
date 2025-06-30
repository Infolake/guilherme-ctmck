#!/usr/bin/env python3
"""
Download utility for CTMCK complete datasets
Downloads large datasets from Zenodo on-demand
"""
import argparse
import os
import requests
from pathlib import Path

# Zenodo record URLs for different datasets
ZENODO_DATASETS = {
    'stellar_correlations': {
        'url': 'https://zenodo.org/record/15765710/files/stellar_temporal_correlations_full.csv',
        'destination': 'data/stellar_temporal_correlations_full.csv',
        'size_mb': 25.3,
        'description': 'Complete stellar temporal correlation analysis'
    },
    'jwst_reanalysis': {
        'url': 'https://zenodo.org/record/15765710/files/jwst_rotational_bias_analysis.csv', 
        'destination': 'data/jwst_rotational_bias_analysis.csv',
        'size_mb': 52.1,
        'description': 'JWST data with CTMCK rotational bias correction'
    },
    'habitability_grids': {
        'url': 'https://zenodo.org/record/15765710/files/habitability_simulation_grids.h5',
        'destination': 'data/habitability_simulation_grids.h5',
        'size_mb': 201.7,
        'description': '3D habitability maps and simulation grids'
    }
}

def download_dataset(dataset_name, force=False):
    """Download specific dataset from Zenodo"""
    
    if dataset_name not in ZENODO_DATASETS:
        print(f"❌ Unknown dataset: {dataset_name}")
        print(f"📋 Available: {', '.join(ZENODO_DATASETS.keys())}")
        return False
    
    dataset = ZENODO_DATASETS[dataset_name]
    dest_path = Path(dataset['destination'])
    
    # Check if already exists
    if dest_path.exists() and not force:
        print(f"✅ {dataset_name} already downloaded: {dest_path}")
        return True
    
    # Create destination directory
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"🔄 Downloading {dataset_name} ({dataset['size_mb']} MB)...")
    print(f"📝 {dataset['description']}")
    
    try:
        # Download with progress
        response = requests.get(dataset['url'], stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(dest_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        progress = (downloaded / total_size) * 100
                        print(f"\r📥 Progress: {progress:.1f}%", end='', flush=True)
        
        print(f"\n✅ Downloaded: {dest_path}")
        return True
        
    except Exception as e:
        print(f"\n❌ Download failed: {e}")
        # Clean up partial file
        if dest_path.exists():
            dest_path.unlink()
        return False

def main():
    parser = argparse.ArgumentParser(description='Download CTMCK datasets from Zenodo')
    parser.add_argument('--dataset', 
                       choices=list(ZENODO_DATASETS.keys()) + ['all'],
                       required=True,
                       help='Dataset to download')
    parser.add_argument('--force', action='store_true',
                       help='Force re-download if file exists')
    
    args = parser.parse_args()
    
    if args.dataset == 'all':
        print("📦 Downloading all datasets...")
        for dataset_name in ZENODO_DATASETS:
            download_dataset(dataset_name, args.force)
    else:
        download_dataset(args.dataset, args.force)

if __name__ == '__main__':
    main() 