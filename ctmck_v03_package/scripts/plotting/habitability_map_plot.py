import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os

# --- Funções de Geração de Gráficos ---

def generate_3d_habitability_map():
    """Gera e salva o Mapa de Habitabilidade Temporal em 3D."""
    # Criação dos eixos t1, t2, t3
    t1 = np.linspace(0, 1, 30)
    t2 = np.linspace(0, 1, 30)
    t3 = np.linspace(0, 1, 30)
    t1_grid, t2_grid, t3_grid = np.meshgrid(t1, t2, t3)

    # Função que representa complexidade emergente
    def complexity(t1, t2, t3):
        return np.exp(-((t1 - 0.4)**2 + (t2 - 0.5)**2 + (t3 - 0.6)**2) * 30)

    # Calcula a complexidade em cada ponto
    complexity_vals = complexity(t1_grid, t2_grid, t3_grid)

    # Seleciona pontos com complexidade acima de um limiar
    threshold = 0.7
    x = t1_grid[complexity_vals > threshold]
    y = t2_grid[complexity_vals > threshold]
    z = t3_grid[complexity_vals > threshold]
    colors = complexity_vals[complexity_vals > threshold]

    # Criar o gráfico 3D
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(x, y, z, c=colors, cmap='plasma', s=25, alpha=0.8)
    
    ax.set_xlabel('t₁ (Local Quantum Time)', fontsize=12)
    ax.set_ylabel('t₂ (Systemic Relational Time)', fontsize=12)
    ax.set_zlabel('t₃ (Cosmological Time)', fontsize=12)
    ax.set_title('Three-Dimensional Temporal Habitability Map', fontsize=16, pad=20)
    
    cbar = fig.colorbar(scatter, ax=ax, label='Emergent Complexity Level', pad=0.1)
    cbar.ax.tick_params(labelsize=10)
    
    # Assegura que o diretório de destino existe
    output_dir = '../../figures/diagrams'
    os.makedirs(output_dir, exist_ok=True)
    
    # Salva a figura
    output_path = os.path.join(output_dir, 'habitability_map_3d.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    
    print(f"Figura 3D salva em: {output_path}")
    plt.show()

def generate_2d_habitability_map():
    """Gera e salva o Mapa de Habitabilidade Temporal em 2D."""
    t1 = np.linspace(0, 1, 100)
    t2 = np.linspace(0, 1, 100)
    t1_grid, t2_grid = np.meshgrid(t1, t2)

    # Função de complexidade/habitabilidade em 2D
    def habitability(t1, t2):
        return np.sin(t1 * np.pi) * np.exp(-((t2 - 0.5)**2) * 10)

    hab_vals = habitability(t1_grid, t2_grid)

    # Criar o gráfico 2D
    fig, ax = plt.subplots(figsize=(12, 9))
    contour = ax.contourf(t1_grid, t2_grid, hab_vals, levels=50, cmap='viridis', alpha=0.8)
    fig.colorbar(contour, ax=ax, label='Habitability Index')
    
    ax.set_xlabel('t₁ (Local Quantum Time)', fontsize=12)
    ax.set_ylabel('t₂ (Systemic Relational Time)', fontsize=12)
    ax.set_title('Temporal Habitability Map (t₁-t₂ Plane)', fontsize=16)
    
    # Pontos estelares
    stars = {
        'O-B': (0.8, 0.8),
        'G (Sol)': (0.5, 0.5),
        'M (Anã Vermelha)': (0.2, 0.3)
    }
    
    for name, (t1_pos, t2_pos) in stars.items():
        ax.plot(t1_pos, t2_pos, 'ro', markersize=10, label=name)
        ax.text(t1_pos + 0.02, t2_pos, name, color='white', fontsize=12, weight='bold')

    ax.legend(title='Stellar Types')
    ax.grid(True, linestyle='--', alpha=0.2)
    
    # Assegura que o diretório de destino existe
    output_dir = '../../figures/diagrams'
    os.makedirs(output_dir, exist_ok=True)
    
    # Salva a figura
    output_path = os.path.join(output_dir, 'habitability_map_2d.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    
    print(f"Figura 2D salva em: {output_path}")
    plt.show()

if __name__ == '__main__':
    print("Gerando Mapas de Habitabilidade Temporal...")
    generate_3d_habitability_map()
    generate_2d_habitability_map()
    print("Geração concluída.") 