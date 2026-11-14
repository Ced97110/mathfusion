import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def dot(ax, p, role, r=1.5): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))

fig, ax = canvas(88)
ca = (30, 46); cb = (56, 46); r = 22
d = cb[0] - ca[0]; xm = (ca[0] + cb[0]) / 2; hh = math.sqrt(r * r - (d / 2) ** 2)
a0 = math.degrees(math.atan2(hh, d / 2))
pts = [P(ca, r, a) for a in [-a0 + 2 * a0 * i / 40 for i in range(41)]] + [P(cb, r, 180 + a) for a in [-a0 + 2 * a0 * i / 40 for i in range(41)]]
poly(ax, pts, 'resultat')
ax.add_patch(Circle(ca, r, ec=COL['sujet'], fc='none', lw=1.1, zorder=3))
ax.add_patch(Circle(cb, r, ec=COL['autre'], fc='none', lw=1.1, zorder=3))
for s, (x, y) in {'2': (19, 56), '4': (19, 38), '8': (28, 47), '3': (65, 56), '9': (65, 38)}.items():
    text(ax, x, y, s, 'sujet' if s in '248' else 'autre', 'l')
text(ax, xm, 46, '6', 'resultat', 'l', weight='bold')
text(ax, 22, 76, '{2, 4, 6, 8}', 'sujet', 's')
text(ax, 64, 76, '{3, 6, 9}', 'autre', 's')
text(ax, 44, 12, r'$\{2,4,6,8\}\cap\{3,6,9\}=\{6\}$', 'encre', 'm')
text(ax, 44, 21, 'éléments communs : {6}', 'resultat', 's')
save(fig, '73-201')
