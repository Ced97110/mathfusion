import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
xs = [18 + 14 * i for i in range(5)]
ytop, ybot = 52, 22
text(ax, 5, ytop, 'ℕ', 'sujet', 'l'); text(ax, 5, ybot, 'ℤ', 'sujet', 'l')
img = {0: 2, 1: 3, 2: 1, 3: 4, 4: 0}   # k -> index in ℤ row (-2..2)
for k in range(5):
    role = 'varie' if k % 2 else 'sujet'
    box(ax, xs[k] - 5, ytop - 4, 10, 8, role, label=str(k), size='m')
    j = img[k]; v = j - 2
    box(ax, xs[j] - 5, ybot - 4, 10, 8, role, label=str(v).replace('-', '−'), size='m')
    arrow(ax, (xs[k], ytop - 4.5), (xs[j], ybot + 4.5), role, lw=0.9)
text(ax, 44, 11, 'impairs → positifs', 'varie', 's')
text(ax, 44, 5.5, 'pairs → négatifs et 0', 'sujet', 's')
save(fig, '43-133')
