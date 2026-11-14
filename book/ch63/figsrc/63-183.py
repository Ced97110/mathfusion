import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 21, 82, 'chaîne de corps', 'autre', 'm', weight='bold')
text(ax, 67, 82, 'chaîne de groupes', 'sujet', 'm', weight='bold')
ys = [62, 38, 14]
fields = [r'$F$', r'$F(\sqrt[n]{a})$', r'$\cdots$']
groups = [r'$G$', r'$\cdots$', r'$\{1\}$']
for f, g, y in zip(fields, groups, ys):
    box(ax, 4, y, 34, 12, 'autre', label=f)
    box(ax, 50, y, 34, 12, 'sujet', label=g)
    arrow(ax, (39, y + 6), (49, y + 6), 'resultat', both=True, lw=0.8)
for y in (50, 26):
    line(ax, [(21, y), (21, y + 12)], 'autre', lw=1.0)
    line(ax, [(55, y), (55, y + 12)], 'sujet', lw=1.0)
    text(ax, 23, y + 6, r'ajouter $\sqrt[n]{a}$', 'varie', 's', ha='left')
    text(ax, 57, y + 6, 'quotient commutatif', 'resultat', 's', ha='left')
text(ax, 44, 7, r'(γ) : normal $\Leftrightarrow$ galoisien'.replace('γ', r'$\gamma$'), 'resultat', 's')
save(fig, '63-183')
