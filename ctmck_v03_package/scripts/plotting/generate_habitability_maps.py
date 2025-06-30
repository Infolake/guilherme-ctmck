#!/usr/bin/env python3
"""
CTMCK Temporal Habitability Maps Generation
Author: Guilherme de Camargo
Date: 2025-01-26
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os

def create_output_directory():
    """Create output directory if it doesn't exist"""
    output_dir = '../../figures/diagrams'
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def generate_3d_habitability_map():
    """Generate 3D Temporal Habitability Map"""
    print("Generating 3D Temporal Habitability Map...")
    
    # Create axes t1, t2, t3
    t1 = np.linspace(0, 1, 30)
    t2 = np.linspace(0, 1, 30)
    t3 = np.linspace(0, 1, 30)
    t1_grid, t2_grid, t3_grid = np.meshgrid(t1, t2, t3)

    # Function representing emergent complexity as a function of three temporal dimensions
    def complexity(t1, t2, t3):
        return np.exp(-((t1 - 0.4)**2 + (t2 - 0.5)**2 + (t3 - 0.6)**2) * 30)

    # Calculate complexity at each point
    complexity_vals = complexity(t1_grid, t2_grid, t3_grid)

    # Select points with complexity above threshold
    threshold = 0.7
    x, y, z = t1_grid[complexity_vals > threshold], t2_grid[complexity_vals > threshold], t3_grid[complexity_vals > threshold]
    colors = complexity_vals[complexity_vals > threshold]

    # Create 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(x, y, z, c=colors, cmap='plasma', s=20)
    ax.set_xlabel('t₁ (Quantum Time)')
    ax.set_ylabel('t₂ (Relational Time)')
    ax.set_zlabel('t₃ (Cosmological Time)')
    ax.set_title('Three-Dimensional Temporal Habitability Map')
    fig.colorbar(scatter, ax=ax, label='Emergent Complexity')

    plt.tight_layout()
    
    # Save
    output_dir = create_output_directory()
    output_path = os.path.join(output_dir, 'habitability_map_3d.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ 3D Map saved at: {output_path}")
    
    plt.close()

def generate_2d_habitability_map():
    """Generate 2D Temporal Habitability Map"""
    print("Generating 2D Temporal Habitability Map...")
    
    # Time axes representing the three temporal dimensions
    t1 = np.linspace(0.01, 1, 100)
    t2 = np.linspace(0.01, 1, 100)
    t3 = np.linspace(0.01, 1, 100)
    T1, T2 = np.meshgrid(t1, t2)

    # Define "emergent complexity" function as didactic example
    # (maximum when t2 and t3 are moderate, t1 low)
    complexity = np.exp(-10 * (T1 - 0.3)**2) * np.exp(-10 * (T2 - 0.6)**2)

    # Create contour plot
    plt.figure(figsize=(8, 6))
    cp = plt.contourf(T1, T2, complexity, levels=20, cmap='viridis')
    plt.colorbar(cp, label='Emergent Complexity Index')
    plt.xlabel('Local Quantum Time (t₁)')
    plt.ylabel('Systemic Relational Time (t₂)')
    plt.title('Temporal Habitability Map (t₁ vs t₂)\nwith t₃ implicit as stable plane')
    plt.scatter([0.1, 0.3, 0.5], [0.9, 0.6, 0.2], color='red')
    plt.text(0.1, 0.9, 'O-B', color='white')
    plt.text(0.3, 0.6, 'G (Sol)', color='white')
    plt.text(0.5, 0.2, 'M', color='white')
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.tight_layout()
    
    # Salvar
    output_dir = create_output_directory()
    output_path = os.path.join(output_dir, 'habitability_map_2d.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Mapa 2D salvo em: {output_path}")
    
    plt.close()

def main():
    """Função principal"""
    print("=" * 60)
    print("Gerando Mapas de Habitabilidade Temporal CTMCK")
    print("=" * 60)
    
    try:
        # Gerar ambos os mapas
        generate_3d_habitability_map()
        generate_2d_habitability_map()
        
        print("=" * 60)
        print("✅ Ambas as imagens foram geradas com sucesso!")
        print("📁 Localização: figures/diagrams/")
        print("   - habitability_map_3d.png")
        print("   - habitability_map_2d.png")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Erro ao gerar imagens: {e}")

if __name__ == "__main__":
    main() 