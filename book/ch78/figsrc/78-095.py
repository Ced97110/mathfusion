import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u = 4.5; xs = [5, 13.5, 40, 57]; ns = [1, 2, 3, 4]; roles = ['sujet', 'sujet', 'autre', 'autre']
for x, n, r in zip(xs, ns, roles):
    box(ax, x, 18, n * u, n * u, r, r=0.3)
    text(ax, x + n * u / 2, 13.5, rf'${n}^2$', r, 's')
brace(ax, 5, 22.5, 40, 'sujet', r'$Q(x)=5$', down=False)
brace(ax, 40, 75, 40, 'autre', r'$Q(y)=25$', down=False)
text(ax, 44, 55, r'$Q(x,y)=5+25=30$', 'resultat', 'm')
text(ax, 44, 5, '4 carrés : 1, 2, 3, 4', 'fixe', 's')
save(fig, '78-095')
