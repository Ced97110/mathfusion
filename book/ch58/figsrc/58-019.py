import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
# le transporteur remplace chaque sac : e1 -> (2, 1), e2 -> (1, 3)
q, g = 3.2, 0.9
def lot(x, y, nb, nv, role):
    w, h = 16.0, 12.5
    box(ax, x, y, w, h, role, r=0.6)
    for i in range(nb):
        box(ax, x + 1.5 + i * (q + g), y + 6.6, q, q, 'sujet', r=0.3, lw=0.6)
    for i in range(nv):
        box(ax, x + 1.5 + i * (q + g), y + 1.8, q, q, 'autre', r=0.3, lw=0.6)
text(ax, 44, 55, 'le transporteur remplace chaque sac', 'encre', 'm', weight='bold')
for y, lab, nb, nv, ans in [(32, r'$e_1$', 1, 0, '(2, 1)'), (10, r'$e_2$', 0, 1, '(1, 3)')]:
    lot(6, y, nb, nv, 'fixe')
    text(ax, 14, y - 3.5, lab, 'sujet' if nb else 'autre', 's')
    arrow(ax, (25, y + 6.2), (45, y + 6.2), 'varie', lw=1.4)
    text(ax, 35, y + 10.5, lab + r'$\ \mapsto\ $' + ans.replace(', ', r',\ ').join(['$', '$']), 'varie', 'm', weight='bold')
    lot(48, y, 2 if nb else 1, 1 if nb else 3, 'varie')
    text(ax, 56, y - 3.5, ans, 'varie', 's')
save(fig, '58-019')
