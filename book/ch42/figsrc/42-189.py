import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
text(ax, 14, 91, 'écritures', 'autre', 's'); text(ax, 44, 91, 'fraction irréductible', 'sujet', 's')
text(ax, 76, 91, r'garder $p$', 'resultat', 's')
def group(cy, lefts, mid, res):
    n = len(lefts); h = 11; gap = 3
    top = cy + (n * h + (n - 1) * gap) / 2
    for i, a in enumerate(lefts):
        y = top - h - i * (h + gap)
        box(ax, 4, y, 20, h, 'autre', label=a, size='m')
        arrow(ax, (24.5, y + h / 2), (33.5, cy + (y + h / 2 - cy) * 0.25), 'varie')
    box(ax, 34, cy - 7, 20, 14, 'sujet', label=mid, size='l')
    arrow(ax, (54.5, cy), (66.5, cy), 'varie')
    box(ax, 67, cy - 7, 18, 14, 'resultat', label=res, size='l')
group(66, (r'$\dfrac{2}{4}$', r'$\dfrac{4}{8}$', r'$\dfrac{3}{6}$'), r'$\dfrac{1}{2}$', '1')
line(ax, [(2, 40), (86, 40)], 'fixe', lw=0.5, dash=True)
group(20, (r'$\dfrac{6}{8}$', r'$\dfrac{9}{12}$'), r'$\dfrac{3}{4}$', '3')
save(fig, '42-189')
