import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cols = [(16, 'fixe', 'monoïde libre', 'aucune règle', 0), (44, 'sujet', 'groupe libre', r"$xx^{\prime}=1$ seul", 1), (72, 'autre', 'groupe du carré', '+ 3 règles', 4)]
for cx, r, t, s, g in cols:
    text(ax, cx, 60, t, r, 'm')
    text(ax, cx, 6, s, r, 's')
    for row in range(4):
        y = 46 - row * 10
        for k in (0, 1): disc(ax, cx - 4 + k * 8, y, 2.2, r)
        if row < g: box(ax, cx - 8.5, y - 4, 17, 8, r, fill=False, lw=0.9, r=1.5)
save(fig, '49-046')
