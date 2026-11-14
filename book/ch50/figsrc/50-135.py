import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$G$ : 6 éléments', 'fixe', 'm')
labs = ['e', 'r', r'r^2', '', '', '']
for i in range(6):
    role = 'sujet' if i < 3 else 'fixe'
    box(ax, 8 + i * 12.5, 52, 12, 12, role, label=(('$' + labs[i] + '$') if labs[i] else None), weight='bold' if i == 1 else 'normal')
brace(ax, 8, 8 + 2 * 12.5 + 12, 52, 'sujet', label=r'$C(r)$ : 3 éléments')
box(ax, 8, 26, 50, 9, 'resultat', label=r'3 divise 3 : Cauchy sur $C(r)$', size='s')
arrow(ax, (33, 35), (33, 41), 'resultat')
box(ax, 60, 23, 24, 16, 'resultat', fill=True)
text(ax, 72, 33, r'$r$ est', 'resultat', 's'); text(ax, 72, 27, "d'ordre 3", 'resultat', 's')
text(ax, 44, 8, r"cet élément est aussi dans $G$", 'resultat', 's')
save(fig, '50-135')
