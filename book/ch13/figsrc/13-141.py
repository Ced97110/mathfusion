import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(65)
for x, w_, t in [(2, 24, r'$3\times3=9$'), (28, 32, r'$(-3)\times(-3)=9$'), (62, 24, r'$0\times0=0$')]:
    box(ax, x, 48, w_, 10, 'resultat', label=t, size='s')
text(ax, 44, 62, 'un carré est toujours positif', 'resultat', 's')
y = 20
f = numberline(ax, 8, 72, y, -9, 9, 3)
line(ax, [(f(0), y + 4), (72, y + 4)], 'resultat', lw=2)
text(ax, 58, y + 8, 'carrés possibles', 'resultat', 's')
disc(ax, f(-9), y, 1.6, 'limite')
text(ax, f(-9) - 1, y + 8, 'carré de −9 ?', 'limite', 's', ha='left')
text(ax, 44, 5, 'aucun carré ne vaut −9', 'limite', 's')
save(fig, '13-141')
