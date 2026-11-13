import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, 'ce carré divise-t-il 75 ?', 'encre', 's')
for x, n, r in [(4, '4', 'fixe'), (25, '9', 'fixe'), (46, '16', 'fixe'), (67, '25', 'resultat')]:
    box(ax, x, 34, 17, 12, role=r, fill=True, label=n, size='l')
    text(ax, x+8.5, 29.5, 'oui' if n == '25' else 'non', 'resultat' if n == '25' else 'limite', 's')
arrow(ax, (75.5, 26), (75.5, 16), 'resultat')
box(ax, 30, 4, 54, 12, role='resultat', fill=True, label=r'$75=25\times3$')
save(fig, '22-076')
