#!/usr/bin/env python3
"""
CTMCK Plotting Script
Visualization tools for CTMCK theory analysis

Author: Guilherme de Camargo
Date: 2025-01-26
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Set style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class CTMCKPlots:
    """
    Plotting class for CTMCK theory visualizations
    """
    
    def __init__(self):
        """Initialize plotting parameters"""
        self.fig_size = (10, 8)
        self.dpi = 300
        
    def plot_three_temporal_manifold(self):
        """
        Visualize the 3-temporal manifold structure
        """
        fig = plt.figure(figsize=(12, 10))
        
        # Create 3D temporal space
        ax1 = fig.add_subplot(221, projection='3d')
        
        # Generate temporal coordinates
        t1 = np.linspace(-2, 2, 20)
        t2 = np.linspace(-2, 2, 20)
        T1, T2 = np.meshgrid(t1, t2)
        T3 = np.sin(T1) * np.cos(T2)
        
        ax1.plot_surface(T1, T2, T3, alpha=0.7, cmap='viridis')
        ax1.set_xlabel('t₁')
        ax1.set_ylabel('t₂')
        ax1.set_zlabel('t₃')
        ax1.set_title('3-Temporal Manifold')
        
        # Metric signature visualization
        ax2 = fig.add_subplot(222)
        signature = [1, 1, 1, -1, -1, -1]
        dimensions = ['t₁', 't₂', 't₃', 'x', 'y', 'z']
        colors = ['red' if s > 0 else 'blue' for s in signature]
        
        ax2.bar(dimensions, signature, color=colors, alpha=0.7)
        ax2.set_ylabel('Metric Signature')
        ax2.set_title('6D Metric Signature')
        ax2.axhline(y=0, color='black', linestyle='-', alpha=0.3)
        
        # Schwarzschild parameter evolution
        ax3 = fig.add_subplot(223)
        r_values = np.logspace(24, 27, 100)  # meters
        M_values = np.logspace(50, 55, 100)  # kg
        
        R, M = np.meshgrid(r_values, M_values)
        S_param = 2 * 6.67e-11 * M / (3e8**2 * R)
        
        contour = ax3.contour(np.log10(R), np.log10(M), S_param, levels=[0.5, 0.98, 1.0, 1.5])
        ax3.clabel(contour, inline=True, fontsize=8)
        ax3.set_xlabel('log₁₀(R) [m]')
        ax3.set_ylabel('log₁₀(M) [kg]')
        ax3.set_title('Schwarzschild Parameter 2GM/(c²R)')
        
        # Neutrino mass hierarchy
        ax4 = fig.add_subplot(224)
        mass_hierarchy = [0.001, 0.009, 0.05]  # eV (approximate)
        neutrino_types = ['νₑ', 'νμ', 'ντ']
        ctmck_prediction = 0.29
        
        bars = ax4.bar(neutrino_types, mass_hierarchy, alpha=0.7, label='Individual masses')
        ax4.axhline(y=ctmck_prediction, color='red', linestyle='--', 
                   label=f'CTMCK Σmν = {ctmck_prediction} eV')
        ax4.set_ylabel('Mass [eV]')
        ax4.set_title('Neutrino Mass Predictions')
        ax4.legend()
        
        plt.tight_layout()
        plt.savefig('figures/ctmck_theory_overview.png', dpi=self.dpi, bbox_inches='tight')
        plt.show()
        
    def plot_bounce_dynamics(self):
        """
        Visualize the Einstein-Cartan bounce dynamics
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Bounce trajectory
        t = np.linspace(-10, 10, 1000)
        a_min = 1e-35  # Planck length scale
        
        # Scale factor evolution
        a_t = a_min * np.cosh(t) + 1e-30
        
        ax1.plot(t, a_t, 'b-', linewidth=2, label='Scale factor a(t)')
        ax1.axhline(y=a_min, color='red', linestyle='--', alpha=0.7, label='Minimum radius')
        ax1.set_xlabel('Time [Planck units]')
        ax1.set_ylabel('Scale Factor a(t) [m]')
        ax1.set_title('Einstein-Cartan Bounce')
        ax1.set_yscale('log')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Torsion effects
        sigma_squared = 1e10 * np.exp(-t**2)  # Torsion density
        
        ax2.plot(t, sigma_squared, 'g-', linewidth=2, label='Torsion density σ²')
        ax2.axvline(x=0, color='red', linestyle='--', alpha=0.7, label='Bounce point')
        ax2.set_xlabel('Time [Planck units]')
        ax2.set_ylabel('Torsion Density σ²')
        ax2.set_title('Torsion Evolution')
        ax2.set_yscale('log')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('figures/bounce_dynamics.png', dpi=self.dpi, bbox_inches='tight')
        plt.show()
        
    def plot_jwst_predictions(self):
        """
        Plot JWST ultra-massive galaxy predictions
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Galaxy mass vs redshift
        z_values = np.linspace(8, 15, 100)
        
        # Standard ΛCDM prediction
        M_standard = 1e10 * np.exp(-0.5 * (z_values - 8))
        
        # CTMCK prediction (inherited seeds)
        M_ctmck = 1e11 * np.exp(-0.2 * (z_values - 8))
        
        # JWST observations (approximate)
        z_obs = [10, 11, 12, 13, 14]
        M_obs = [1e11, 8e10, 5e10, 3e10, 2e10]
        M_obs_err = [2e10, 1.5e10, 1e10, 8e9, 5e9]
        
        ax1.plot(z_values, M_standard, 'b--', label='Standard ΛCDM', alpha=0.7)
        ax1.plot(z_values, M_ctmck, 'r-', linewidth=2, label='CTMCK prediction')
        ax1.errorbar(z_obs, M_obs, yerr=M_obs_err, fmt='ko', 
                    label='JWST observations', capsize=5)
        
        ax1.set_xlabel('Redshift z')
        ax1.set_ylabel('Galaxy Mass [M☉]')
        ax1.set_title('Ultra-massive Galaxies at High Redshift')
        ax1.set_yscale('log')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Formation timescale comparison
        formation_times_standard = [2e9, 1.5e9, 1e9, 8e8, 5e8]  # years
        formation_times_ctmck = [2e8, 1.5e8, 1e8, 8e7, 5e7]  # years (10x faster)
        
        x_pos = np.arange(len(z_obs))
        width = 0.35
        
        ax2.bar(x_pos - width/2, formation_times_standard, width, 
               label='Standard', alpha=0.7)
        ax2.bar(x_pos + width/2, formation_times_ctmck, width, 
               label='CTMCK', alpha=0.7)
        
        ax2.set_xlabel('Redshift z')
        ax2.set_ylabel('Formation Time [years]')
        ax2.set_title('Galaxy Formation Timescales')
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(z_obs)
        ax2.set_yscale('log')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('figures/jwst_predictions.png', dpi=self.dpi, bbox_inches='tight')
        plt.show()
        
    def plot_observable_signatures(self):
        """
        Plot the 5 observable signatures of CTMCK
        """
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        axes = axes.flatten()
        
        # 1. LISA torsional waves
        f = np.logspace(-4, 0, 1000)  # Hz
        strain = 1e-20 * np.exp(-(np.log10(f) + 2)**2 / 0.5)  # Gaussian peak at 10^-2 Hz
        
        axes[0].loglog(f, strain, 'b-', linewidth=2)
        axes[0].axvline(x=1e-2, color='red', linestyle='--', label='CTMCK peak')
        axes[0].set_xlabel('Frequency [Hz]')
        axes[0].set_ylabel('Strain')
        axes[0].set_title('LISA Torsional Waves')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # 2. KK Resonances
        energy = np.linspace(1, 6, 1000)  # TeV
        cross_section = 1e-12 * (np.exp(-(energy - 2.3)**2 / 0.1) + 
                                np.exp(-(energy - 4.1)**2 / 0.1))
        
        axes[1].plot(energy, cross_section, 'g-', linewidth=2)
        axes[1].axvline(x=2.3, color='red', linestyle='--', alpha=0.7)
        axes[1].axvline(x=4.1, color='red', linestyle='--', alpha=0.7)
        axes[1].set_xlabel('Energy [TeV]')
        axes[1].set_ylabel('Cross Section [pb]')
        axes[1].set_title('TeV KK Resonances')
        axes[1].grid(True, alpha=0.3)
        
        # 3. Neutrino mass sensitivity
        experiments = ['KATRIN', 'KATRIN II', 'Future']
        sensitivity = [2.0, 0.2, 0.1]  # eV
        ctmck_pred = 0.29
        
        bars = axes[2].bar(experiments, sensitivity, alpha=0.7)
        axes[2].axhline(y=ctmck_pred, color='red', linestyle='--', 
                       label=f'CTMCK: {ctmck_pred} eV')
        axes[2].set_ylabel('Sensitivity [eV]')
        axes[2].set_title('Neutrino Mass Sensitivity')
        axes[2].legend()
        axes[2].grid(True, alpha=0.3)
        
        # 4. Galaxy rotation bias
        angles = np.linspace(0, 2*np.pi, 100)
        bias_strength = 0.15
        expected_flat = np.ones_like(angles) * 0.5
        observed_bias = 0.5 + bias_strength * np.cos(angles)
        
        axes[3].plot(angles, expected_flat, 'b--', label='No bias expected', alpha=0.7)
        axes[3].plot(angles, observed_bias, 'r-', linewidth=2, label='Observed bias')
        axes[3].set_xlabel('Angle [rad]')
        axes[3].set_ylabel('Rotation Fraction')
        axes[3].set_title('Galaxy Rotation Bias')
        axes[3].legend()
        axes[3].grid(True, alpha=0.3)
        
        # 5. Schwarzschild parameter evolution
        cosmic_time = np.linspace(0, 13.8, 1000)  # Gyr
        S_param_evolution = 0.98 + 0.02 * np.sin(cosmic_time / 2)
        
        axes[4].plot(cosmic_time, S_param_evolution, 'purple', linewidth=2)
        axes[4].axhline(y=1.0, color='red', linestyle='--', alpha=0.7, label='S = 1')
        axes[4].axhline(y=0.98, color='orange', linestyle='--', alpha=0.7, label='CTMCK prediction')
        axes[4].set_xlabel('Cosmic Time [Gyr]')
        axes[4].set_ylabel('Schwarzschild Parameter')
        axes[4].set_title('Cosmic Evolution')
        axes[4].legend()
        axes[4].grid(True, alpha=0.3)
        
        # Remove the 6th subplot
        fig.delaxes(axes[5])
        
        plt.tight_layout()
        plt.savefig('figures/observable_signatures.png', dpi=self.dpi, bbox_inches='tight')
        plt.show()

def main():
    """
    Generate all CTMCK plots
    """
    print("Generating CTMCK visualization plots...")
    
    plotter = CTMCKPlots()
    
    # Create output directory if it doesn't exist
    import os
    os.makedirs('figures', exist_ok=True)
    
    # Generate plots
    plotter.plot_three_temporal_manifold()
    plotter.plot_bounce_dynamics()
    plotter.plot_jwst_predictions()
    plotter.plot_observable_signatures()
    
    print("All plots generated successfully!")

if __name__ == "__main__":
    main() 