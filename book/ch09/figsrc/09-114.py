import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
L, R, M = 22, 66, 44
rows = [(r'$\frac{3}{4}$', r'$\frac{?}{8}$', 'sujet'), (r'$24$', r'$4 \times ?$', 'sujet'), (r'$6$', r'$?$', 'resultat')]
text(ax, M, 81, 'même geste des deux côtés', 'varie', 's', weight='bold')
for i, (a, b, ro) in enumerate(rows):
    y = 60 - i * 26
    box(ax, L - 10, y, 20, 13, ro, label=a); box(ax, R - 10, y, 20, 13, ro, label=b)
    text(ax, M, y + 6.5, '=', 'encre', 'l')
for i, lab in enumerate(['× 32  (4 × 8)', '÷ 4']):
    y0 = 60 - i * 26 - 1; y1 = y0 - 11
    arrow(ax, (L, y0), (L, y1), 'varie'); arrow(ax, (R, y0), (R, y1), 'varie')
    arrow(ax, (L + 2, (y0 + y1) / 2), (R - 2, (y0 + y1) / 2), 'varie', lw=0.6, both=True)
    ax.add_patch(Rectangle((M - 9, (y0 + y1) / 2 - 2.6), 18, 5.2, fc='white', ec='none', zorder=4))
    text(ax, M, (y0 + y1) / 2, lab, 'varie', 's')
save(fig, '09-114')
