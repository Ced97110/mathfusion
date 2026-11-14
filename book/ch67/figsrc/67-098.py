import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
cx, cy, R = 40, 66, 22
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.6, ls='--', zorder=1))
arrow(ax, (cx - 28, cy), (cx + 31, cy), 'fixe', lw=0.6)
text(ax, cx + 36, cy + 3.2, 'réels', 'fixe', 's')
P = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in (0, 120, 240)]
disc(ax, *P[0], 2.6, 'sujet'); disc(ax, *P[1], 2.6, 'limite'); disc(ax, *P[2], 2.6, 'limite')
text(ax, P[0][0] - 6, P[0][1] + 6, 'dans le corps', 'sujet', 's', ha='left')
text(ax, P[1][0] + 4, P[1][1] + 4, 'non réelle', 'limite', 's', ha='left')
text(ax, P[2][0] + 4, P[2][1] - 4, 'non réelle', 'limite', 's', ha='left')
for Q in P[1:]:
    arrow(ax, (P[0][0] - 1.5, P[0][1] + (1.2 if Q[1] > cy else -1.2)), (Q[0] + 2.2, Q[1] + (-2 if Q[1] > cy else 2)), 'limite', lw=0.8)
    text(ax, (P[0][0] + Q[0]) / 2 + 2, (P[0][1] + Q[1]) / 2, '×', 'limite', 'l')
text(ax, 44, 33, r'racines de $x^3=2$ : 3 solutions', 'encre', 's')
box(ax, 2, 6, 40, 16, 'sujet', label='corps $\\mathbb{Q}(\\sqrt[3]{2})$ :\ndegré 3', size='s')
box(ax, 46, 6, 40, 16, 'autre', label='groupe de Galois :\n1 élément', size='s')
text(ax, 44, 14, '$\\neq$', 'limite', 'l')
save(fig, '67-098')
