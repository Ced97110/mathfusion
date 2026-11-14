import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
def chain(y, a, b, role_b):
    box(ax, 3, y - 4, 21, 8, 'sujet', label=a)
    arrow(ax, (25, y), (62, y), 'varie')
    text(ax, 43.5, y + 3.6, '÷ 24, puis ÷ 7', 'varie', 's')
    box(ax, 63, y - 4, 22, 8, role_b, label=b)
def weeks(y, partial):
    for i in range(12):
        x = 3.9 + i * 6.7
        if partial and i == 11:
            box(ax, x, y, 6, 7, 'limite', fill=False, dash=True, r=0.5)
            box(ax, x, y, 5.43, 7, 'limite', r=0.4)
        else:
            box(ax, x, y, 6, 7, 'resultat', r=0.5)
chain(76, '2 016 h', '12 sem', 'resultat'); weeks(58, False)
chain(48, '2 000 h', '≈ 11,9 sem', 'limite'); weeks(30, True)
line(ax, [(77.6, 30), (45.4, 20)], 'limite', lw=0.5, dash=True); line(ax, [(83.6, 30), (84, 20)], 'limite', lw=0.5, dash=True)
for i in range(7):
    x = 45.4 + i * 5.6
    box(ax, x, 14, 5, 6, 'limite', fill=False, r=0.3, lw=0.5)
    box(ax, x, 14, 5 if i < 6 else 5 / 3, 6, 'varie', r=0.3, lw=0.5)
text(ax, 3, 17, 'reste :\n6 j 8 h', 'varie', 's', ha='left')
text(ax, 23, 5, 'grande case = 1 semaine', 'resultat', 's')
text(ax, 66, 5, 'petite case = 1 jour', 'varie', 's')
save(fig, '11-141')
