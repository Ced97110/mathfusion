import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 22, 74, r'$F[u]$', 'sujet', 'xl', weight='bold')
text(ax, 66, 74, r'$F(u)$', 'autre', 'xl', weight='bold')
ops = [('+', 56), (r'$-$', 44), (r'$\times$', 32), (r'$\div$', 20)]
for i, (s, y) in enumerate(ops):
    r1 = 'limite' if i == 3 else 'resultat'
    box(ax, 12, y - 5, 20, 10, r1, label=s, size='l')
    box(ax, 56, y - 5, 20, 10, 'resultat', label=s, size='l')
text(ax, 22, 10, 'comme les entiers', 'sujet', 's')
text(ax, 66, 10, 'comme les fractions', 'autre', 's')
save(fig, '61-077')
