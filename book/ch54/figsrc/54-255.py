import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 30, 68, 'rang : produit développé', 'sujet', 's', )
text(ax, 70, 68, r'$p=x^4-2x^3+x+1$', 'fixe', 's')
rows = [(3, r'$a+c$', r'$-2$'), (2, r'$ac+b+d$', r'$0$'), (1, r'$ad+bc$', r'$1$'), (0, r'$bd$', r'$1$')]
for i, (rk, e, v) in enumerate(rows):
    y = 50 - i * 14
    text(ax, 4, y + 5, f'{rk}', 'varie', 'm', ha='left')
    box(ax, 10, y, 40, 10, 'sujet', label=e)
    line(ax, [(52, y + 6.2), (58, y + 6.2)], 'varie', lw=1.2); line(ax, [(52, y + 3.8), (58, y + 3.8)], 'varie', lw=1.2)
    box(ax, 60, y, 24, 10, 'fixe', label=v)
save(fig, '54-255')
