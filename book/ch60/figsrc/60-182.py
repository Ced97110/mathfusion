import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
bw, g = 17, (84 - 4 * 17) / 3
xs = [2 + i * (bw + g) for i in range(4)]
labs = ['v', '(T − λ)v', '(T − λ)²v', '0']
roles = ['sujet', 'sujet', 'sujet', 'resultat']
for x, lab, role in zip(xs, labs, roles):
    box(ax, x, 46, bw, 11, role, label=lab, size='s')
for i in range(3):
    arrow(ax, (xs[i] + bw + 0.3, 51.5), (xs[i + 1] - 0.3, 51.5), 'varie')
text(ax, 44, 40, 'chaque flèche : appliquer T − λ', 'varie', 's')
# la formule sur un vecteur w de la chaine
text(ax, 8, 28, 'T w', 'sujet', 'm')
text(ax, 17, 28, '=', 'encre', 'm')
box(ax, 22, 22, 22, 12, 'fixe', label='λ w', size='s')
text(ax, 48, 28, '+', 'encre', 'm')
box(ax, 52, 22, 32, 12, 'varie', label='(T − λ) w', size='s')
text(ax, 33, 17.5, 'reste à sa place', 'fixe', 's')
text(ax, 68, 17.5, 'passe au suivant', 'varie', 's')
text(ax, 44, 7, 'dernier vecteur : suivant = 0', 'resultat', 's')
save(fig, '60-182')
