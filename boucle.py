import numpy as np
import matplotlib.pyplot as plt

# Définir les équations paramétriques
def parametric_curve(t,a,b):
    xh = 2*np.sin(t)
    yh = 2*np.cos(t)
    xm = 3*np.sin(12*t)
    ym = 3*np.cos(12*t)
    x=(a*xh+b*xm)/(a+b)
    y=(a*yh+b*ym)/(a+b)
    return x, y

# Générer les valeurs de t
t = np.linspace(0, 2 * np.pi, 1000)
a=0.945
b=1-a
# Calculer les points de la courbe
x, y = parametric_curve(t,a,b)

# Tracer la courbe
plt.plot(x, y)
plt.title(f'Courbe paramétrique {b/a:2.3f}')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')

# Définir les limites des axes pour zoomer
plt.xlim(-0.2, 0.2)
plt.ylim(-2, -1.5)

# Sauvegarder la figure dans un fichier
plt.savefig('courbe_parametrique.png')
plt.close()