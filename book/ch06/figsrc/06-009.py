import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 54, 50, r'coupée en $b$ morceaux', 'encre')
for y, n in ((34, 4), (20, 8), (6, 100)):
    box(ax, 24, y, 60, 8, 'sujet', r=0.3)
    for k in range(1, n):
        x = 24 + k * 60 / n
        line(ax, [(x, y), (x, y + 8)], 'sujet', lw=0.8 if n <= 8 else 0.3)
    text(ax, 12, y + 4, rf'$b={n}$', 'varie')
save(fig, '06-009')
