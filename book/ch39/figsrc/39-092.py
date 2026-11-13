import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
R = 10.5
def mini(cx, n):
    cy = 30
    pts = [(cx + R * math.cos(math.radians(360 * k / n)), cy + R * math.sin(math.radians(360 * k / n))) for k in range(n)]
    th = [math.radians(360 * i / 40 / n) for i in range(41)]
    poly(ax, [(cx, cy)] + [(cx + R * math.cos(t), cy + R * math.sin(t)) for t in th], 'varie')
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.7, ls='--', zorder=2))
    for p in pts: disc(ax, p[0], p[1], 1.1, 'sujet')
    text(ax, cx, 14, f'n = {n}', 'sujet', 's')
    text(ax, cx, 9.5, f'360° ÷ {n}', 'varie', 's')
    text(ax, cx, 5, f'= {360 // n}°', 'varie', 's', weight='bold')
for cx, n in ((16, 3), (44, 6), (72, 8)):
    mini(cx, n)
text(ax, 44, 47, 'écart entre deux racines voisines', 'varie', 's')
save(fig, '39-092')
