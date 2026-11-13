import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
disc(ax, 22, 36, 19, 'sujet', fill=False, lw=1.2); text(ax, 22, 60, r'$\mathcal{S}$', 'sujet', 'l')
disc(ax, 22, 46, 4.6, 'resultat', label=r'$P_B$', size='s')
text(ax, 28.5, 46, 'taille 1', 'resultat', 's', ha='left')
disc(ax, 11, 28, 4.6, 'sujet', label=r'$P_A$', size='s'); disc(ax, 33, 28, 4.6, 'sujet', label=r'$P_C$', size='s')
arrow(ax, (16.2, 28), (27.8, 28), 'varie', both=True); text(ax, 22, 21, 'taille 2', 'varie', 's')
steps = [('fixe', r'$k=3$, $2\nmid 3$'), ('varie', r'$Q$ agit sur $\mathcal{S}$'),
         ('resultat', 'une orbite de taille 1'), ('resultat', r'donc $Q=P_j=P_B$')]
for i, (role, lab) in enumerate(steps):
    y = 52 - 16 * i
    box(ax, 46, y, 40, 10, role, label=lab, size='s', lw=1.4 if i in (1, 3) else 0.8)
    if i: arrow(ax, (66, y + 16), (66, y + 10.8), 'varie' if i == 2 else 'fixe')
save(fig, '50-110')
