import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
cs, x0, y0 = 12, 8, 10
for i in range(3):
    for j in range(2):
        box(ax, x0 + i * cs, y0 + j * cs, cs, cs, 'resultat', r=0.2)
brace(ax, x0, x0 + 3 * cs, y0 + 2 * cs, 'resultat', label=r'$a=3$ colonnes prises', down=False)
xr = x0 + 3 * cs + 3
line(ax, [(xr, y0), (xr, y0 + 2 * cs)], 'resultat')
text(ax, xr + 2, y0 + cs, r'$c=2$' + '\nlignes', 'resultat', 's', ha='left')
text(ax, 70, 42, r'$a\times c$', 'sujet', 'xl', weight='bold')
text(ax, 70, 30, r'$=3\times2=6$', 'resultat', 'l')
text(ax, 70, 22, 'cases vertes', 'resultat', 's')
save(fig, '06-054')
