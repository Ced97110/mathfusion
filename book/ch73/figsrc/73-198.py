import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def dot(ax, p, role, r=1.5): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))
def arc(ax, c, r, a0, a1, role, lw=1.1, head=True):
    pts = [P(c, r, a0 + (a1 - a0) * i / 40) for i in range(41)]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-4], pts[-1], role, lw)

fig, ax = canvas(104)
text(ax, 44, 98, 'somme des carrés', 'sujet', 's', weight='bold')
f = numberline(ax, 12, 70, 84, 0, 180, 90, arrow_right=False)
arrow(ax, (f(0), 88), (f(90), 88), 'varie', curve=-0.45)
arrow(ax, (f(90), 88), (f(180), 88), 'varie', curve=-0.45)
text(ax, f(45), 96, '', 'varie', 's')
dot(ax, (f(180), 84), 'resultat', 1.8)
text(ax, f(45), 76 + 14, 'quart', 'varie', 's'); text(ax, f(135), 76 + 14, 'quart', 'varie', 's')
text(ax, 44, 64, 'demi-tour = carré du quart de tour', 'resultat', 's')
line(ax, [(4, 58), (84, 58)], 'fixe', lw=0.5)
text(ax, 44, 52, 'forme  Q = xy', 'autre', 's', weight='bold')
box(ax, 6, 30, 26, 9, 'autre', label='(3, 4)', size='s')
box(ax, 56, 30, 26, 9, 'limite', label='(−3, −4)', size='s')
arrow(ax, (33, 34.5), (55, 34.5), 'varie')
text(ax, 44, 41, 'a = −1', 'varie', 's')
text(ax, 44, 20, 'a × a = −1 ?', 'limite', 's')
text(ax, 44, 11, 'aucun réel : pas un carré', 'limite', 's')
save(fig, '73-198')
