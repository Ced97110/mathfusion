import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 19, 62, 'tour de radicaux', 'sujet', 's', weight='bold')
text(ax, 69, 62, 'suite normale abélienne', 'autre', 's', weight='bold')
box(ax, 2, 8, 34, 50, 'sujet', fill=False, dash=True)
box(ax, 52, 8, 34, 50, 'autre', fill=False, dash=True)
ys = [46, 30, 14]
Lt = [r'$F_1$', r'$F_2$', r'$F_{r+1}$']
Rt = [r'$G_1$', r'$G_2$', r'$\{e\}$']
for i, y in enumerate(ys):
    box(ax, 6, y, 26, 9, 'sujet', label=Lt[i])
    box(ax, 56, y, 26, 9, 'autre', label=Rt[i])
    if i < 2:
        arrow(ax, (12, y), (12, ys[i + 1] + 9), 'varie')
        text(ax, 15, y - 3.5, r'$+\sqrt[n]{a}$', 'varie', 's', ha='left')
        arrow(ax, (62, y), (62, ys[i + 1] + 9), 'varie')
        text(ax, 65, y - 3.5, 'abélien', 'varie', 's', ha='left')
text(ax, 44, 34, r'$\Leftrightarrow$', 'resultat', 'xl', weight='bold')
text(ax, 44, 26, 'Galois', 'resultat', 's')
save(fig, '64-094')
