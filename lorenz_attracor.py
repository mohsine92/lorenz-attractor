import numpy as np  
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
from typing import List, Tuple, Optional

# Configuration Parameters
# Paramètres du système de Lorenz (valeurs classiques)
SIGMA = 10.0
BETA = 8.0 / 3.0
RHO = 28.0

# Paramètres de simulation
TIME_START = 0.0
TIME_END = 40.0
NUM_POINTS = 1001

# Paramètres d'animation
ANIMATION_INTERVAL = 25 # ms entre chaque frame
TRAIL_LENGTH = 100 # Nombre de points à afficher dans la traînée

# Conditions initiales (peut être modifié)
INITIAL_POSITIONS = [
    [0.0, 1.0, 1.0], # Première trajectoire
    [20.0, 6.1, 21.0] # Deuxième trajectoire
]

# Couleurs des trajectoires
COLORS = ['#FF4444', '#4444FF'] # Rouge et Bleu

# System Definition
def lorenz_system(vector: List[float], t: float, sigma: float, beta: float, rho: float) -> List[float]:
    x, y, z = vector
    
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    
    return [dx_dt, dy_dt, dz_dt]


# Numerical Solving
def solve_lorenz_system(initial_position: List[float], 
                       time_points: np.ndarray,
                       sigma: float = SIGMA,
                       beta: float = BETA,
                       rho: float = RHO) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    positions = odeint(lorenz_system, initial_position, time_points, args=(sigma, beta, rho))
    x_sol = positions[:, 0]
    y_sol = positions[:, 1]
    z_sol = positions[:, 2]
    
    return x_sol, y_sol, z_sol


# Visualization Setup
def setup_plot() -> Tuple[plt.Figure, plt.Axes]:
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')
    
    # Configuration des axes
    ax.set_xlabel('X', fontsize=12, fontweight='bold')
    ax.set_ylabel('Y', fontsize=12, fontweight='bold')
    ax.set_zlabel('Z', fontsize=12, fontweight='bold')
    ax.set_title('Attracteur de Lorenz - Simulation Chaotique', fontsize=14, fontweight='bold', pad=20)
    
    # Style de la grille
    ax.grid(True, alpha=0.3)
    
    return fig, ax


# Animation Function
def create_animation(fig: plt.Figure, 
                    ax: plt.Axes,
                    solutions: List[Tuple[np.ndarray, np.ndarray, np.ndarray]],
                    initial_positions: List[List[float]],
                    colors: List[str],
                    time_points: np.ndarray,
                    trail_length: int = TRAIL_LENGTH,
                    interval: int = ANIMATION_INTERVAL,
                    save_path: Optional[str] = None) -> FuncAnimation:

    # Initialisation des lignes vides
    lines = []
    for i, (x_sol, y_sol, z_sol) in enumerate(solutions):
        line, = ax.plot([], [], [], color=colors[i], 
                       linewidth=2, 
                       alpha=0.8,
                       label=f'Trajectoire {i+1}: {initial_positions[i]}')
        lines.append(line)
    
    # Configuration de la légende
    ax.legend(loc='upper left', fontsize=9, framealpha=0.9)
    
    def update(frame: int):
        """Fonction de mise à jour pour chaque frame."""
        for i, (x_sol, y_sol, z_sol) in enumerate(solutions):
            # Calcul de la fenêtre de points à afficher
            lower_lim = max(0, frame - trail_length)
            upper_lim = frame + 1
            
            # Extraction des points actuels
            x_current = x_sol[lower_lim:upper_lim]
            y_current = y_sol[lower_lim:upper_lim]
            z_current = z_sol[lower_lim:upper_lim]
            
            # Mise à jour de la ligne
            lines[i].set_data(x_current, y_current)
            lines[i].set_3d_properties(z_current)
        
        # Ajustement automatique des limites des axes
        if frame > 0:
            all_x = np.concatenate([sol[0][:frame+1] for sol in solutions])
            all_y = np.concatenate([sol[1][:frame+1] for sol in solutions])
            all_z = np.concatenate([sol[2][:frame+1] for sol in solutions])
            
            ax.set_xlim([all_x.min() - 5, all_x.max() + 5])
            ax.set_ylim([all_y.min() - 5, all_y.max() + 5])
            ax.set_zlim([all_z.min() - 5, all_z.max() + 5])
        
        return lines
    
    # Création de l'animation
    animation = FuncAnimation(
        fig, 
        update, 
        frames=len(time_points), 
        interval=interval, 
        blit=False,
        repeat=True
    )
    
    # Sauvegarde optionnelle
    if save_path:
        print(f"Sauvegarde de l'animation dans {save_path}...")
        animation.save(save_path, writer='pillow', fps=1000//interval)
        print("Animation sauvegardée avec succès!")
    
    return animation


# Main Execution
def main():
    "Fonction principale qui orchestre la simulation et la visualisation."
    print("=" * 60)
    print("Simulation de l'Attracteur de Lorenz")
    print("=" * 60)
    print(f"Paramètres: σ={SIGMA}, β={BETA:.3f}, ρ={RHO}")
    print(f"Temps: {TIME_START} à {TIME_END} ({NUM_POINTS} points)")
    print(f"Conditions initiales: {INITIAL_POSITIONS}")
    print("=" * 60)
    
    # Création des points de temps
    time_points = np.linspace(TIME_START, TIME_END, NUM_POINTS)
    
    # Résolution du système pour chaque condition initiale
    print("\nCalcul des trajectoires...")
    solutions = []
    for i, initial_pos in enumerate(INITIAL_POSITIONS):
        print(f"  Trajectoire {i+1}/{len(INITIAL_POSITIONS)}...")
        x_sol, y_sol, z_sol = solve_lorenz_system(initial_pos, time_points)
        solutions.append((x_sol, y_sol, z_sol))
    print("Calcul terminé!\n")
    
    # Configuration du graphique
    fig, ax = setup_plot()
    
    # Création de l'animation
    print("Création de l'animation...")
    animation = create_animation(
        fig, ax, solutions, INITIAL_POSITIONS, COLORS, time_points,
        trail_length=TRAIL_LENGTH,
        interval=ANIMATION_INTERVAL,
        save_path=lorenz_animation.gif
    )
    
    # Affichage

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
