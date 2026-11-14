import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 2, 84, 60, 'autre', fill=False, dash=True)
text(ax, 44, 56, 'théorème de structure, matrice nulle', 'autre', 's')
w, g, x0 = 20, 7, 7
vecs = ['(1, 0, 0)', '(0, 1, 0)', '(0, 0, 1)']
for i, v in enumerate(vecs):
    x = x0 + i * (w + g)
    box(ax, x, 28, w, 14, 'sujet', label=v)
    text(ax, x + w / 2, 46, r'copie de $\mathbb{Z}$', 'sujet', 's')
    if i < 2:
        text(ax, x + w + g / 2, 35, r'$\oplus$', 'encre', 'l')
text(ax, 44, 19, r'$\mathbb{Z}^3=\mathbb{Z}\oplus\mathbb{Z}\oplus\mathbb{Z}$', 'sujet', 'm')
text(ax, 44, 9, 'chapitre 58 : aucune torsion', 'resultat', 's')
save(fig, '59-129')
