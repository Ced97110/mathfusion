import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
xs = [11, 33, 55, 77]
text(ax, 44, 59, r'une rotation de 90° = $+1$', 'varie', 'm')
for i, x in enumerate(xs):
    a = math.radians(90 * i)
    pts = [(x + 6.5 * math.sqrt(2) * math.cos(a + math.radians(45 + 90 * k)),
            47 + 6.5 * math.sqrt(2) * math.sin(a + math.radians(45 + 90 * k))) for k in range(4)]
    poly(ax, pts, 'sujet')
    disc(ax, pts[0][0] * 0.78 + x * 0.22, pts[0][1] * 0.78 + 47 * 0.22, 1.5, 'varie')
    text(ax, x, 33, f'{90 * i}°', 'sujet', 'm')
    disc(ax, x, 13, 5, 'autre', label=str(i))
    arrow(ax, (x, 30), (x, 19), 'fixe')
    if i < 3:
        arrow(ax, (x + 9.5, 47), (x + 12.5, 47), 'varie')
        arrow(ax, (x + 6, 13), (x + 16, 13), 'varie')
text(ax, 44, 3.5, 'horloge à 4 positions', 'autre', 's')
save(fig, '48-193')
