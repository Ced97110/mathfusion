import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
s, y0 = 6, 24
box(ax, 4, y0, s, s, 'sujet', r=0.3)
for k in range(2): box(ax, 16 + k * s, y0, s, s, 'autre', r=0.3)
for g in range(2):
    for k in range(2): box(ax, 34 + g * (2 * s + 1.5) + k * s, y0, s, s, 'autre', r=0.3)
text(ax, 7, y0 - 4, '1', 'sujet', 's'); text(ax, 22, y0 - 4, r'$p$', 'autre', 's'); text(ax, 47, y0 - 4, r'$p^2$', 'autre', 's'); text(ax, 68, y0 + 3, '…', 'fixe', 'l')
brace(ax, 4, 60, y0 + 8, 'fixe', label=r'$n_p$ = somme des tailles', down=False)
text(ax, 44, 12, r'paquets de $p$ : rien ne reste', 'autre', 's')
text(ax, 44, 6, r'reste 1 modulo $p$', 'resultat', 's')
save(fig, '50-103')
