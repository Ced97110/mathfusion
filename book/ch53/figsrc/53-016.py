import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def clock(cx, cy, n, r, start, steps, role, s_lab, e_lab):
    pos = lambda i, rr: (cx + rr * math.cos(math.radians(90 - i * 360 / n)), cy + rr * math.sin(math.radians(90 - i * 360 / n)))
    for i in range(n):
        x, y = pos(i, r)
        if i == start % n: disc(ax, x, y, 1.7, role)
        elif i == (start + steps) % n: disc(ax, x, y, 1.7, 'resultat')
        else: disc(ax, x, y, 0.9, 'fixe')
    x, y = pos(start, r + 4.5); text(ax, x, y, s_lab, role, 's')
    x, y = pos(start + steps, r + 4.5); text(ax, x, y, e_lab, 'resultat', 's')
    pts = [pos(start + steps * k / 24, r - 5) for k in range(25)]
    line(ax, pts, 'varie', lw=1.3); arrow(ax, pts[-3], pts[-1], 'varie', lw=1.3)
clock(22, 36, 12, 15, 10, 4, 'autre', '10', '2')
clock(66, 36, 26, 15, 23, 3, 'sujet', '23', '0')
text(ax, 22, 61, 'horloge à 12 cases', 'autre', 's')
text(ax, 66, 61, 'horloge à 26 cases', 'sujet', 's')
text(ax, 22, 12, '10 + 4 = 14 → 2', 'encre', 's')
text(ax, 66, 12, '23 + 3 = 26 → 0', 'encre', 's')
text(ax, 44, 4, 'après la dernière : retour', 'encre', 's')
save(fig, '53-016')
