import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
# gauche : Q et R, 1 + 1 = 2, pas 0
text(ax, 25, 62, r'dans $\mathbb{Q}$ et $\mathbb{R}$', 'resultat', 'm')
f = numberline(ax, 5, 38, 38, 0, 3, step=1, arrow_right=False, role='fixe')
for v in (0, 1, 2):
    disc(ax, f(v), 38, 1.6, 'resultat' if v == 2 else 'sujet')
arrow(ax, (f(1), 42), (f(2), 42), 'varie', curve=-0.5)
text(ax, f(1), 50, r'$1+1=2$', 'resultat', 'm')
text(ax, 25, 18, r'$2\neq0$ : caractéristique $\neq2$', 'resultat', 's')
line(ax, [(44, 8), (44, 64)], 'fixe', dash=True)
# droite : {0, 1}, 1 + 1 = 0
text(ax, 66, 62, r'ensemble $\{0,\,1\}$', 'limite', 'm')
disc(ax, 56, 38, 4, 'sujet', label='0', size='m')
disc(ax, 76, 38, 4, 'sujet', label='1', size='m')
arrow(ax, (74, 42.5), (58, 42.5), 'limite', curve=0.45)
text(ax, 66, 50, r'$1+1=0$', 'limite', 'm')
text(ax, 66, 24, 'caractéristique 2 :', 'limite', 's')
text(ax, 66, 19, 'écarté du chapitre', 'limite', 's')
save(fig, '65-020')
