import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cx, cy, R = 22, 32, 14
disc(ax, cx, cy, R, 'fixe', fill=False)
for j in range(12):
    a = math.radians(90 - 30 * j)
    px, py = cx + R * math.cos(a), cy + R * math.sin(a)
    if j == 0: disc(ax, px, py, 2.6, 'resultat', label='0', size='s')
    elif j == 5: disc(ax, px, py, 2.6, 'limite', label='5', size='s')
    else: disc(ax, px, py, 1.3, 'sujet')
text(ax, cx, cy, r'$\mathbb{Z}/12\mathbb{Z}$', 'sujet', 's')
text(ax, cx, 8, '12 positions', 'sujet', 's')
box(ax, 46, 40, 40, 10, 'resultat', label='n = 12 : 12 × 1 = 0', size='s')
box(ax, 46, 26, 40, 10, 'resultat', label='n = 24 : 24 × 1 = 0', size='s')
box(ax, 46, 12, 40, 10, 'limite', label='n = 5 : 5 × 1 = 5 ≠ 0', size='s')
text(ax, 66, 55, 'module sur ℤ/nℤ ?', 'encre', 's')
text(ax, 66, 6, 'vert : oui ; rouge : non', 'fixe', 's')
save(fig, '57-209')
