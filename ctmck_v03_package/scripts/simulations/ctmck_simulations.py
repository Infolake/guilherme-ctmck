#!/usr/bin/env python3
"""
CTMCK Numerical Simulations
Cosmogênese Temporal Multidimensional Camargo-Kletetschka

Numerical simulations for CTMCK theory predictions

Author: Guilherme de Camargo
Date: 2025-01-26
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, odeint
from scipy.optimize import minimize
import pandas as pd

class CTMCKSimulations:
    """
    Numerical simulations for CTMCK theory
    """
    
    def __init__(self):
        """Initialize simulation parameters"""
        # Physical constants
        self.c = 3e8  # m/s
        self.G = 6.67e-11  # m³/kg/s²
        self.hbar = 1.05e-34  # J⋅s
        self.m_planck = 2.18e-8  # kg
        self.l_planck = 1.62e-35  # m
        self.t_planck = 5.39e-44  # s
        
        # CTMCK parameters
        self.kappa_squared = 1e-10  # Torsion coupling constant
        self.a_min = self.l_planck  # Minimum scale factor
        
    def modified_friedmann_system(self, t, y, rho_func, k=0):
        """
        Solve the modified Friedmann equation with torsion
        y = [a, a_dot]
        """
        a, a_dot = y
        
        # Density evolution (matter-dominated)
        rho = rho_func(a)
        
        # Torsion term (simplified model)
        sigma_squared = self.calculate_torsion_density(a)
        
        # Modified Friedmann equation
        H_squared = (8 * np.pi * self.G * rho / 3) - (k / a**2) + \
                   (self.kappa_squared * sigma_squared / 24)
        
        # Avoid negative H²
        H_squared = max(H_squared, 0)
        
        # Acceleration equation
        a_ddot = -4 * np.pi * self.G * a * rho / 3 + \
                 self.kappa_squared * sigma_squared * a / 24
        
        return [a_dot, a_ddot]
    
    def calculate_torsion_density(self, a):
        """
        Calculate torsion density σ² as function of scale factor
        """
        # Torsion becomes significant near Planck scale
        sigma_squared = 1e50 * np.exp(-a / self.a_min)
        return sigma_squared
    
    def simulate_bounce_universe(self, t_span=(-10, 10), n_points=1000):
        """
        Simulate the bounce universe evolution
        """
        print("Simulating bounce universe evolution...")
        
        # Time array in Planck units
        t_eval = np.linspace(t_span[0], t_span[1], n_points)
        
        # Initial conditions at bounce
        y0 = [self.a_min, 0]  # a(0) = a_min, a_dot(0) = 0
        
        # Density function (matter-dominated)
        def rho_matter(a):
            rho_0 = 1e-26  # kg/m³ (approximate current density)
            a_0 = 1e26  # m (current scale factor)
            return rho_0 * (a_0 / a)**3
        
        # Solve the system
        sol = solve_ivp(self.modified_friedmann_system, t_span, y0, 
                       t_eval=t_eval, args=(rho_matter,), 
                       method='RK45', rtol=1e-6)
        
        if sol.success:
            print("Bounce simulation completed successfully!")
            return sol.t, sol.y[0], sol.y[1]  # t, a(t), a_dot(t)
        else:
            print("Bounce simulation failed!")
            return None, None, None
    
    def simulate_galaxy_formation(self, z_max=15, n_redshifts=100):
        """
        Simulate galaxy formation with inherited seeds
        """
        print("Simulating galaxy formation with CTMCK inherited seeds...")
        
        # Redshift array
        z_values = np.linspace(0, z_max, n_redshifts)
        
        # Standard ΛCDM formation timescale
        def t_form_standard(z):
            return 1e9 * (1 + z)**(-1.5)  # years
        
        # CTMCK enhanced formation (inherited seeds)
        def t_form_ctmck(z):
            enhancement_factor = 0.1  # 10x faster
            return t_form_standard(z) * enhancement_factor
        
        # Galaxy mass evolution
        def M_galaxy_standard(z):
            return 1e10 * np.exp(-0.5 * (z - 8))  # M☉
        
        def M_galaxy_ctmck(z):
            return 1e11 * np.exp(-0.2 * (z - 8))  # M☉
        
        # Calculate arrays
        t_standard = np.array([t_form_standard(z) for z in z_values])
        t_ctmck = np.array([t_form_ctmck(z) for z in z_values])
        M_standard = np.array([M_galaxy_standard(z) for z in z_values])
        M_ctmck = np.array([M_galaxy_ctmck(z) for z in z_values])
        
        results = {
            'redshift': z_values,
            'formation_time_standard': t_standard,
            'formation_time_ctmck': t_ctmck,
            'mass_standard': M_standard,
            'mass_ctmck': M_ctmck
        }
        
        print("Galaxy formation simulation completed!")
        return results
    
    def simulate_neutrino_oscillations(self, L_baseline=1000, n_energies=100):
        """
        Simulate neutrino oscillations with CTMCK mass predictions
        """
        print("Simulating neutrino oscillations with CTMCK masses...")
        
        # CTMCK mass predictions
        m1, m2, m3 = 0.001, 0.009, 0.05  # eV (approximate)
        delta_m21_sq = m2**2 - m1**2
        delta_m31_sq = m3**2 - m1**2
        
        # Mixing angles (standard values)
        theta12 = np.radians(33.5)
        theta13 = np.radians(8.5)
        theta23 = np.radians(45)
        
        # Energy range
        E_values = np.logspace(-1, 2, n_energies)  # GeV
        
        # Oscillation probabilities
        def P_oscillation(E, L, delta_m_sq, theta):
            return np.sin(2 * theta)**2 * np.sin(1.27 * delta_m_sq * L / E)**2
        
        # Calculate probabilities
        P_12 = np.array([P_oscillation(E, L_baseline, delta_m21_sq, theta12) 
                        for E in E_values])
        P_13 = np.array([P_oscillation(E, L_baseline, delta_m31_sq, theta13) 
                        for E in E_values])
        
        results = {
            'energy': E_values,
            'probability_12': P_12,
            'probability_13': P_13,
            'mass_sum_ctmck': m1 + m2 + m3
        }
        
        print(f"CTMCK neutrino mass sum: {results['mass_sum_ctmck']:.3f} eV")
        return results
    
    def simulate_torsional_waves(self, f_max=1, n_frequencies=1000):
        """
        Simulate LISA-band torsional gravitational waves
        """
        print("Simulating LISA-band torsional waves...")
        
        # Frequency array
        f_values = np.logspace(-4, np.log10(f_max), n_frequencies)  # Hz
        
        # CTMCK torsional wave spectrum
        def strain_torsional(f):
            f_peak = 1e-2  # Hz (CTMCK prediction)
            A_0 = 1e-20  # Strain amplitude
            sigma_f = 0.5  # Frequency width
            
            return A_0 * np.exp(-0.5 * (np.log10(f / f_peak) / sigma_f)**2)
        
        # Calculate strain spectrum
        strain = np.array([strain_torsional(f) for f in f_values])
        
        # LISA sensitivity curve (approximate)
        def lisa_sensitivity(f):
            # Simplified LISA sensitivity
            return 1e-20 * (f / 1e-3)**(-2) * np.sqrt(1 + (f / 1e-2)**2)
        
        sensitivity = np.array([lisa_sensitivity(f) for f in f_values])
        
        results = {
            'frequency': f_values,
            'strain': strain,
            'lisa_sensitivity': sensitivity,
            'peak_frequency': 1e-2
        }
        
        print("Torsional wave simulation completed!")
        return results
    
    def simulate_kk_resonances(self, E_max=10, n_energies=1000):
        """
        Simulate TeV Kaluza-Klein resonances
        """
        print("Simulating TeV Kaluza-Klein resonances...")
        
        # Energy array
        E_values = np.linspace(1, E_max, n_energies)  # TeV
        
        # CTMCK KK resonance peaks
        E_resonances = [2.3, 4.1]  # TeV
        widths = [0.1, 0.1]  # TeV
        amplitudes = [1e-12, 8e-13]  # pb
        
        # Calculate cross section
        cross_section = np.zeros_like(E_values)
        for E_res, width, amp in zip(E_resonances, widths, amplitudes):
            cross_section += amp * np.exp(-0.5 * ((E_values - E_res) / width)**2)
        
        # Background cross section
        background = 1e-15 * np.ones_like(E_values)
        total_cross_section = cross_section + background
        
        results = {
            'energy': E_values,
            'cross_section': total_cross_section,
            'resonance_energies': E_resonances,
            'resonance_widths': widths
        }
        
        print("KK resonance simulation completed!")
        return results
    
    def run_all_simulations(self):
        """
        Run all CTMCK simulations
        """
        print("=" * 60)
        print("CTMCK Numerical Simulations Suite")
        print("=" * 60)
        
        # Store all results
        results = {}
        
        # 1. Bounce universe
        t, a, a_dot = self.simulate_bounce_universe()
        if t is not None:
            results['bounce'] = {'time': t, 'scale_factor': a, 'scale_factor_dot': a_dot}
        
        # 2. Galaxy formation
        results['galaxy_formation'] = self.simulate_galaxy_formation()
        
        # 3. Neutrino oscillations
        results['neutrino'] = self.simulate_neutrino_oscillations()
        
        # 4. Torsional waves
        results['torsional_waves'] = self.simulate_torsional_waves()
        
        # 5. KK resonances
        results['kk_resonances'] = self.simulate_kk_resonances()
        
        print("=" * 60)
        print("All simulations completed!")
        print("=" * 60)
        
        return results
    
    def save_results(self, results, filename='ctmck_simulation_results.npz'):
        """
        Save simulation results to file
        """
        print(f"Saving results to {filename}...")
        np.savez_compressed(filename, **results)
        print("Results saved successfully!")

def main():
    """
    Main simulation runner
    """
    # Initialize simulator
    sim = CTMCKSimulations()
    
    # Run all simulations
    results = sim.run_all_simulations()
    
    # Save results
    sim.save_results(results)
    
    # Print summary
    print("\nSimulation Summary:")
    print("-" * 40)
    for key in results.keys():
        print(f"✓ {key.replace('_', ' ').title()} simulation completed")

if __name__ == "__main__":
    main() 