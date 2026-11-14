import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
text(ax, 44, 72, r'$D_4$ : 8 mouvements', 'encre', 'l')
CO = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
def sq(cx, cy, k, d, role):
    s = 10
    box(ax, cx - s / 2, cy - s / 2, s, s, role, r=0.4)
    for idx, r2 in ((k % 4, 'varie'), ((k + d) % 4, 'autre')):
        dx, dy = CO[idx]
        disc(ax, cx + dx * 3.2, cy + dy * 3.2, 1.3, r2)
xs = [16 + 18 * i for i in range(4)]
box(ax, 3, 33, 82, 34, 'sujet', fill=False, dash=True)
text(ax, 44, 63, r'$\langle r\rangle$ : 4 rotations', 'sujet', 'm')
for i, (x, lab) in enumerate(zip(xs, ['rien', '¼ tour', '½ tour', '¾ tour'])):
    sq(x, 50, i, 1, 'sujet'); text(ax, x, 38, lab, 'sujet', 's')
box(ax, 3, 5, 82, 24, 'fixe', fill=False, dash=True)
for i, x in enumerate(xs): sq(x, 22, i, -1, 'fixe')
text(ax, 44, 8.5, '4 retournements', 'fixe', 'm')
save(fig, '47-001')
