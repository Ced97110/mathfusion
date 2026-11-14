import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 22, 60, r'$C = \{000, 111\}$', 'resultat', 'm')
text(ax, 66, 60, r'$C = \{001, 010\}$', 'limite', 'm')
box(ax, 3, 28, 38, 28, 'resultat', fill=False, dash=True)
box(ax, 47, 28, 38, 28, 'limite', fill=False, dash=True)
for x, w in [(7, '000'), (25, '111')]:
    box(ax, x, 41, 14, 8, 'sujet', label=w)
for x, w in [(51, '001'), (69, '010')]:
    box(ax, x, 41, 14, 8, 'sujet', label=w)
text(ax, 22, 21, '000 + 111 = 111', 'resultat', 's')
text(ax, 22, 14, '111 + 111 = 000', 'resultat', 's')
text(ax, 22, 6, 'la somme reste dans $C$', 'resultat', 's')
arrow(ax, (66, 28), (66, 20), 'limite')
text(ax, 69, 24, '001 + 010', 'limite', 's', ha='left')
box(ax, 56, 10, 20, 9, 'limite', label='011')
text(ax, 66, 5, 'pas dans $C$', 'limite', 's')
save(fig, '68-101')
