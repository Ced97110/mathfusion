import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 87, 'groupe : horloge à 3 positions', 'fixe', 's')
text(ax, 44, 40, 'anneau : les entiers', 'fixe', 's')
line(ax, [(2, 44), (86, 44)], 'fixe', lw=0.5, dash=True)

def clock(cx, cy, step, label):
    pos = [(cx, cy + 6.5), (cx + 5.63, cy - 3.25), (cx - 5.63, cy - 3.25)]
    for i, (px, py) in enumerate(pos):
        disc(ax, px, py, 2.4, 'sujet', label=str(i) if label else None, size='s')
    for i in range(3):
        j = (i + step) % 3
        (px, py), (qx, qy) = pos[i], pos[j]
        d = math.hypot(qx - px, qy - py); ux, uy = (qx - px) / d, (qy - py) / d
        arrow(ax, (px + ux * 2.8, py + uy * 2.8), (qx - ux * 2.8, qy - uy * 2.8), 'varie',
              curve=-0.3 if step == 1 else 0.3)

for cy, el, step, cap in [(70, '1', 1, "décale d'un cran"), (50, '2', 2, 'décale de deux crans')]:
    box(ax, 2, cy - 4.5, 14, 9, 'sujet', label=el)
    arrow(ax, (18, cy), (28, cy), 'varie')
    clock(40, cy, step, el == '1')
    text(ax, 52, cy, cap, 'varie', 's', ha='left')
box(ax, 2, 21.5, 14, 9, 'sujet', label='3')
arrow(ax, (18, 26), (28, 26), 'varie')
box(ax, 30, 21.5, 24, 9, 'varie', label='tripler')
text(ax, 58, 26, '1 ↦ 3\n2 ↦ 6', 'varie', 's', ha='left')
text(ax, 44, 8, "élément → ce qu'il fait", 'resultat', 'm')
save(fig, '57-062')
