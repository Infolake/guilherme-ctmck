# scripts/plotting/fig1_geometry_6d.py
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np

plt.rcParams.update({
    "font.size": 11,
    "font.family": "serif",
    "mathtext.fontset": "dejavuserif",
})

# -------------------------------------------
tau1, tau2, tau3 = 1.0, 4.835e-3, 2.875e-4
fig = plt.figure(figsize=(10, 7), constrained_layout=True)
gs  = gridspec.GridSpec(2, 2, figure=fig, height_ratios=[1.2, 1])

# ----- (a) torus temporal ------------------------------------------------
from mpl_toolkits.mplot3d import Axes3D           # noqa: F401
ax1 = fig.add_subplot(gs[0, 0], projection="3d")
t = np.linspace(0, 2*np.pi, 200)
ax1.plot(tau1*np.cos(t), tau1*np.sin(t), 0*t, "r", lw=3, label=fr"$t_1\;(\tau_1={tau1:.1f})$")
ax1.plot(0*t, tau2*np.cos(t), tau2*np.sin(t), "g", lw=3, label=fr"$t_2\;(\tau_2={tau2:.1e})$")
ax1.plot(tau3*np.cos(t), 0*t, tau3*np.sin(t), "b", lw=3, label=fr"$t_3\;(\tau_3={tau3:.1e})$")
ax1.set_xlabel("$t_1$"), ax1.set_ylabel("$t_2$"), ax1.set_zlabel("$t_3$")
ax1.set_title(r"Temporal Torus  $T^{3}=S^{1}_{(1)}\times S^{1}_{(2)}\times S^{1}_{(3)}$", pad=10)
ax1.legend(fontsize=8, loc="upper left")

# ----- (b) espaço emergente ----------------------------------------------
ax2 = fig.add_subplot(gs[0, 1], projection="3d")
x = y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)
Z = 0.15*np.sin(X)*np.cos(Y)
ax2.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8, linewidth=0)
ax2.set(xlabel="x", ylabel="y", zlabel="z")
ax2.set_title("Emergent 3D Space\nfrom Temporal Dynamics", pad=12)

# ----- (c) bloco de texto com métrica -------------------------------------
ax3 = fig.add_subplot(gs[1, 0])
ax3.axis("off")
eq1 = (r"$ds^{2} = -\,c^{2}(dt_{1}^{2} + \alpha\,dt_{2}^{2}"
       r" + \beta\,dt_{3}^{2}) + dx^{2}+dy^{2}+dz^{2}$")
ax3.text(0.5, 0.85, eq1, ha="center",
         bbox=dict(fc="#D7ECFF", ec="none", pad=0.4))

ax3.text(0.5, 0.63,
         r"$\alpha=(\tau_{2}/\tau_{1})^{2},\;\; \beta=(\tau_{3}/\tau_{1})^{2}$",
         ha="center")
ax3.text(0.5, 0.47,
         fr"$\tau_1:\tau_2:\tau_3 = 1: {tau2/tau1:.4e}: {tau3/tau1:.4e}$",
         ha="center", bbox=dict(fc="#FFFCC9", ec="none", pad=0.3))
ax3.text(0.5, 0.30,
         r"$M^{6}=\mathbb{R}^{3}_{\text{space}}\times T^{3}_{\text{time}}$",
         ha="center", style="italic")

# ----- (d) hierarquia de escalas -----------------------------------------
ax4 = fig.add_subplot(gs[1, 1])
labels = ["Quantum\n(particles)", "Intermediate\n(interactions)", "Cosmic\n(universe)"]
taus   = [tau1, tau2, tau3]
colors = ["#ff6666", "#66b266", "#4da6ff"]
ypos   = np.arange(len(labels))[::-1]   # para barra começar em baixo

for y, tval, lab, col in zip(ypos, taus, labels, colors):
    ax4.barh(y, tval, color=col, alpha=0.9)
ax4.set_yticks(ypos)
ax4.set_yticklabels(labels, fontsize=8)
ax4.set_xscale("log"), ax4.set_xlabel("Temporal Radius $\\tau_i$")
ax4.set_title("Temporal Scale Hierarchy", pad=8)

# ajuste fino opcional
fig.subplots_adjust(hspace=0.32)
fig.savefig("figures/fig1_geometry_6d.png", dpi=300)
print("✓ fig1_geometry_6d.png gerada")
