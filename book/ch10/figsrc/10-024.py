import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
text(ax, 72, 50, r'$4 \times c$', 'sujet', 'l')
rows = [(34, ['28', '31', '29', '32'], 30, 120), (8, ['48', '49', '51', '52'], 50, 200)]
for y, nums, c, s in rows:
    for i, n in enumerate(nums): box(ax, 3 + i * 12.5, y, 11, 10, 'fixe', label=n)
    arrow(ax, (52, y + 5), (58, y + 5), 'varie')
    box(ax, 59, y, 26, 10, 'varie', label=rf'$c = {c}$')
    text(ax, 72, y - 4, rf'$4 \times {c} = {s}$', 'resultat', 's')
save(fig, '10-024')
