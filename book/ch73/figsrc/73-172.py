import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def grid(ox, cols):
    for (a, b), r in cols.items(): disc(ax, ox + a * 10, 30 + b * 10, 2.4, r)
nz = {(a, b): 'sujet' for a in range(3) for b in range(3)}; nz[(0, 0)] = 'fixe'
grid(14, nz)
g2 = {(a, b): 'resultat' for a in range(3) for b in range(3)}
g2[(0, 0)] = 'varie'; g2[(1, 1)] = 'varie'; g2[(2, 2)] = 'varie'
grid(58, g2)
line(ax, [(58, 30), (78, 50)], 'varie', dash=True)
text(ax, 24, 58, 'colonne 1', 'sujet', 'm'); text(ax, 68, 58, 'colonne 2', 'resultat', 'm')
text(ax, 24, 21, 'non nul : 8 choix', 'sujet', 's')
text(ax, 68, 21, 'droite de v : 3', 'varie', 's'); text(ax, 68, 15, 'hors droite : 6 choix', 'resultat', 's')
text(ax, 44, 5, r'$8\times 6=48$', 'resultat', 'l')
save(fig, '73-172')
