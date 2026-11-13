import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
xa, xb = 16, 72
def frac(x, top, bot, role):
    text(ax, x, 62, top, role, 'xl', weight='bold'); line(ax, [(x - 4, 57), (x + 4, 57)], role, lw=1.2); text(ax, x, 52, bot, role, 'xl', weight='bold')
frac(xa, '2', '5', 'sujet'); frac(xb, '5', '2', 'autre')
arrow(ax, (xa + 6, 62), (xb - 6, 52), 'varie'); arrow(ax, (xa + 6, 52), (xb - 6, 62), 'varie')
text(ax, 44, 72, 'échanger haut et bas', 'varie', 'm')
text(ax, 44, 36, r'haut : $2\times5=10$', 'encre', 'm')
text(ax, 44, 27, r'bas : $5\times2=10$', 'encre', 'm')
box(ax, 24, 7, 40, 11, 'resultat', label=r'$\frac{2}{5}\times\frac{5}{2}=\frac{10}{10}=1$')
save(fig, '06-062')
