import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, 'Si 0 allait sur 2 :', 'limite', 's')
disc(ax, 14, 46, 5, 'sujet', label='0')
xs = [44 + i * 12 for i in range(4)]
for i, x in enumerate(xs):
    disc(ax, x, 46, 4.5, 'resultat' if i == 0 else ('limite' if i == 2 else 'fixe'), label=str(i))
arrow(ax, (16, 51), (xs[2] - 2, 50.8), 'limite', curve=-0.42)
text(ax, 24, 59, r'$f$', 'limite', 's')
box(ax, 2, 26, 38, 10, 'sujet', label=r'$f(0+0)=f(0)=2$', size='s')
box(ax, 48, 26, 38, 10, 'autre', label=r'$f(0)+f(0)=2+2=0$', size='s')
text(ax, 44, 31, '≠', 'limite', 'xl', weight='bold')
text(ax, 44, 17, 'contradiction : 0 sur 2 impossible', 'limite', 's')
text(ax, 44, 7, 'Donc 0 va sur 0, automatique', 'resultat', 'm', weight='bold')
save(fig, '48-023')
