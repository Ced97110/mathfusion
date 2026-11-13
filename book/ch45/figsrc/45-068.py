import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
X = [4 + i * 21 for i in range(4)]; bw = 15
top = ['0', '2', '1', '3']; bot = ['nulle', 'demi', 'quart', '3 quarts']
for i in range(4):
    inn = i < 2
    box(ax, X[i], 48, bw, 9, 'sujet' if inn else 'fixe', label=top[i]); box(ax, X[i], 16, bw, 9, 'resultat' if inn else 'fixe', label=bot[i], size='s')
    arrow(ax, (X[i] + bw / 2, 48), (X[i] + bw / 2, 25.5), 'varie' if inn else 'fixe', lw=1.0 if inn else 0.7)
box(ax, 1.5, 44.5, 39, 16, 'sujet', fill=False, dash=True); box(ax, 1.5, 12.5, 39, 16, 'resultat', fill=False, dash=True)
text(ax, 21, 67, 'sous-groupe : 2 éléments', 'sujet', 's'); text(ax, 21, 6, 'image : 2 éléments', 'resultat', 's')
text(ax, 15, 36.5, r'$\eta$', 'varie', 'l')
save(fig, '45-068')
