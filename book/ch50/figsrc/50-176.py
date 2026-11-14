import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
pieces = [(14, '5', 'sujet', r'$q=5$'), (30, '≢', 'limite', 'pas congru'), (44, '1', 'encre', 'reste 1'), (64, '(mod 3)', 'autre', r'$p=3$')]
for x, s, r, lab in pieces:
    text(ax, x, 50, s, r, 'xl')
    line(ax, [(x, 46), (x, 42)], r, lw=0.8)
    text(ax, x, 38, lab, r, 's')
text(ax, 44, 26, r'$5-1=4$ : pas un multiple de 3', 'resultat', 'm') if False else None
box(ax, 20, 12, 48, 10, 'resultat', label=r'$5-1=4$ : pas multiple de 3', size='s')
arrow(ax, (44, 33.5), (44, 22.5), 'resultat')
save(fig, '50-176')
