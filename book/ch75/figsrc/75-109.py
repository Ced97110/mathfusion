import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
d = 14
def panel(cx, free):
    for i in range(2):
        for j in range(2):
            role = 'resultat' if (i, j) in free else 'limite'
            disc(ax, cx - d / 2 + i * d, 28 + j * d, 3.0, role)
panel(22, [(0, 1), (1, 1)])
panel(66, [])
line(ax, [(8, 28), (36, 28)], 'limite', lw=1.1, dash=True)
text(ax, 22, 56, r'dernière colonne $u_2$', 'sujet', 's')
text(ax, 66, 56, r'une colonne de plus', 'autre', 's')
text(ax, 22, 14, r'$q^n-q^{n-1}=4-2=2$', 'resultat', 's')
text(ax, 66, 14, r'$4-4=0$ choix', 'limite', 's')
text(ax, 22, 8, 'droite de $u_1$ retirée', 'limite', 's')
text(ax, 66, 8, 'tout le plan retiré', 'limite', 's')
save(fig, '75-109')
