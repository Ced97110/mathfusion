import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def dot(ax, p, role, r=1.5): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))

fig, ax = canvas(100)
for y in (66, 34):
    line(ax, [(3, y), (85, y)], 'fixe', lw=0.5)
text(ax, 4, 88, 'dim 1', 'encre', 's', ha='left', weight='bold')
text(ax, 4, 54, 'dim 2', 'encre', 's', ha='left', weight='bold')
text(ax, 4, 22, 'dim ≥ 3', 'encre', 's', ha='left', weight='bold')
f = numberline(ax, 20, 48, 82, -1, 1, 1, labels=False, arrow_right=False)
disc(ax, f(1), 82, 3.4, 'sujet', label='1', size='s')
disc(ax, f(-1), 82, 3.4, 'limite', label='−1', size='s')
text(ax, f(-1), 74, 'déterminant −1', 'limite', 's', ha='left')
text(ax, 34, 94, 'O = {1, −1}', 'fixe', 's')
text(ax, 68, 85, 'SO = {1}', 'sujet', 's')
text(ax, 68, 79, 'pas simple', 'limite', 's')
c = (26, 47); r = 9
ax.add_patch(Circle(c, r, ec=COL['autre'], fc=FILL['autre'], lw=0.8, zorder=2))
pa = [P(c, r + 3, 0 + 30 * i / 20) for i in range(21)]
pb = [P(c, r + 3, 30 + 60 * i / 20) for i in range(21)]
line(ax, pa, 'varie', lw=1.2); line(ax, pb, 'autre', lw=1.2)
arrow(ax, pb[-3], pb[-1], 'autre', 1.2)
dot(ax, P(c, r, 0), 'sujet', 1.4); dot(ax, P(c, r, 90), 'resultat', 1.4)
text(ax, *P(c, r + 7, 15), 'α', 'varie', 's'); text(ax, *P(c, r + 7, 62), 'β', 'autre', 's')
text(ax, 64, 54, 'R(α) R(β) = R(β) R(α)', 'sujet', 's')
text(ax, 64, 46, 'simple si nombre premier', 'autre', 's')
box(ax, 18, 10, 66, 12, 'resultat')
text(ax, 51, 16, 'le vrai théorème commence', 'resultat', 's')
save(fig, '73-199')
