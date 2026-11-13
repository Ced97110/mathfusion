import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
c = 6.5
rows = [('ℝ : dim. 1', None), ('ℂ : dim. 2', 'ℝ'), ('ℍ : dim. 4', 'ℂ'), ('𝕆 : dim. 8', 'ℍ')]
for r, (nm, prev) in enumerate(rows):
    y = 6 + 20 * r; n = 2 ** r
    text(ax, 3, y + 3.2, nm, 'encre', 'm', ha='left')
    if prev is None:
        box(ax, 32, y, c, c, 'sujet', r=0.5, label='x', size='s')
    else:
        w = c * n / 2
        box(ax, 32, y, w, c, 'sujet', r=0.5, label='u∈' + prev, size='s')
        box(ax, 32 + w + 2, y, w, c, 'autre', r=0.5, label='v∈' + prev, size='s')
    if r < 3:
        arrow(ax, (22, y + 8.5), (22, y + 18.5), 'varie', lw=1.4)
        text(ax, 25, y + 13.5, '×2', 'varie', 's', ha='left')
save(fig, '78-030')
