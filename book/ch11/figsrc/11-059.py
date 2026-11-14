import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def frac(ax, x, y, top, bot, rt, rb, w=11, size="m", dy=2.8):
    text(ax, x, y + dy, top, rt, size); text(ax, x, y - dy, bot, rb, size); line(ax, [(x - w / 2, y), (x + w / 2, y)], "encre", lw=0.8)
fig, ax = canvas(66)
text(ax, 20, 60, 'départ : $b$', 'sujet', 'm', weight='bold'); text(ax, 68, 60, 'arrivée : mesure $a$', 'resultat', 'm', weight='bold')
for y, dep, arr, lab, op in ((38, r'$b$ = 12 po', r'$a$ = 1 pied', 'vers les pieds', r'÷ 12'), (12, r'$b$ = 1 pied', r'$a$ = 12 po', 'vers les pouces', r'× 12')):
    box(ax, 4, y, 32, 10, 'sujet', label=dep, size='m')
    box(ax, 52, y, 32, 10, 'resultat', label=arr, size='m', weight='bold')
    arrow(ax, (36, y + 5), (52, y + 5), 'varie', lw=1.2)
    text(ax, 44, y + 8.5, op, 'varie', 'm', weight='bold')
    text(ax, 44, y - 3.5, lab, 'varie', 's')
save(fig, '11-059')
