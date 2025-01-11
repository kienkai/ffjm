import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Définir les équations paramétriques
def parametric_curve(t, a, b):
    xh = 2 * np.sin(t)
    yh = 2 * np.cos(t)
    xm = 3 * np.sin(12 * t)
    ym = 3 * np.cos(12 * t)
    x = (a * xh + b * xm) / (a + b)
    y = (a * yh + b * ym) / (a + b)
    return x, y

# Streamlit sliders
a = st.slider('Valeur de a', 0, 10000, 9550,step=1)
zoom = st.slider('Zoom', 0, 3000, 3000,step = 1)
x_center = st.slider('Déplacement en x', -5.0, 5.0, 0.0)
y_center = st.slider('Déplacement en y', -2.0, 2.0, 0.0,step=0.001)

# Calculer la valeur de b
b = 10000 - a

# Générer les valeurs de t
t = np.linspace(0, 2 * np.pi, 1000)
print(a,b)
# Calculer les points de la courbe
x, y = parametric_curve(t, a, b)

# Tracer la courbe
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title(f'Courbe paramétrique {b/a:2.8f}')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
ax.axis('equal')

# Définir les limites des axes pour zoomer et se déplacer
ax.set_xlim(x_center - zoom/1000, x_center + zoom/1000)
ax.set_ylim(y_center - zoom/1000, y_center + zoom/1000)

# Afficher la figure dans Streamlit
st.pyplot(fig)