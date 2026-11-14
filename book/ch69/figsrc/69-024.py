import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for i, (name, ok) in enumerate([('ℝ', True), ('ℚ', True), ('ℂ', False)]):
    x = 3 + 28.5 * i
    cx = x + 12.75
    box(ax, x, 10, 25.5, 48, 'fixe', fill=False)
    text(ax, cx, 51, name, 'sujet', 'xl')
    line(ax, [(cx - 10, 36), (cx + 10, 36)], 'fixe')
    line(ax, [(cx, 35), (cx, 37)], 'fixe')
    if ok:
        box(ax, cx + 0.5, 39, 10, 7, 'resultat', label='P')
        text(ax, cx, 26, 'ordonnable', 'resultat', 's')
        text(ax, cx, 19, 'un P existe', 'resultat', 's')
    else:
        box(ax, cx + 0.5, 39, 10, 7, 'limite', label='?', dash=True)
        text(ax, cx, 26, 'non ordonnable', 'limite', 's')
        text(ax, cx, 19, 'aucun P possible', 'limite', 's')
save(fig, '69-024')
