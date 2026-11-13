import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'$\Delta=(x_1-x_2)^2$', 'encre', 'l')
w = 34
xa, xb = 3, 51
box(ax, xa, 44, w, 12, 'sujet', label=r'$x_1=5\,,\ x_2=2$')
box(ax, xb, 44, w, 12, 'sujet', label=r'$x_1=2\,,\ x_2=5$')
arrow(ax, (xa + w + 2, 50), (xb - 2, 50), 'varie', lw=1.2)
text(ax, 44, 55, 'échange', 'varie', 's')
for x, lab in ((xa, r'$(5-2)^2=3^2=9$'), (xb, r'$(2-5)^2=(-3)^2=9$')):
    arrow(ax, (x + w / 2, 43), (x + w / 2, 33), 'fixe')
    box(ax, x, 20, w, 12, 'resultat', label=lab, size='s')
text(ax, 44, 9, 'même résultat : 9', 'resultat', 'm', weight='bold')
save(fig, '55-111')
