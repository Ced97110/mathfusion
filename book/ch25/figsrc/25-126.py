import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="varie", n=24):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role)
fig, ax = canvas(62)
text(ax, 44, 57, '1/0 demande n × 0 = 1', 'sujet', 'm', weight='bold')
for i, s in enumerate(['5 × 0', '1 000 000 × 0', 'n’importe quel n × 0']):
    y = 42 - i * 11
    box(ax, 6, y - 4, 38, 8, 'fixe', label=s, size='s')
    arrow(ax, (45, y), (53, y), 'varie')
    box(ax, 54, y - 4, 10, 8, 'limite', label='0', size='s')
    text(ax, 76, y, '≠ 1', 'limite', 's', weight='bold')
text(ax, 44, 12, 'aucun nombre ne convient', 'limite', 'm', weight='bold')
text(ax, 44, 5, 'tan 90° n’existe pas', 'limite', 's')
save(fig, '25-126')
