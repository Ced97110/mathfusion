import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(40)
tok = [(13, r'$73 \times 46$', 'fixe'), (31, r'$\approx$', 'sujet'), (49, r'$70 \times 50$', 'varie'), (66, '=', 'resultat'), (79, '3 500', 'resultat')]
for x, s, r in tok: text(ax, x, 30, s, r, 'l', weight='bold' if s in ('=', r'$\approx$') else 'normal')
arrow(ax, (31, 17), (31, 26), 'sujet'); arrow(ax, (66, 17), (66, 26), 'resultat')
text(ax, 31, 12, 'à peu près égal à', 'sujet', 's'); text(ax, 70, 12, 'exactement égal', 'resultat', 's')
save(fig, '10-020')
