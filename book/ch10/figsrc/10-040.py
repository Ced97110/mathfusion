import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
line(ax, [(44, 4), (44, 46)], 'fixe', dash=True)
for cx, role, t, e, ex, er, v, err, msg in ((22, 'resultat', '5 203 − 3 015', '≈ 5 200 − 3 000 = 2 200', 'exact 2 188', 'erreur 12', 2188, 12, 'erreur petite'), (66, 'limite', '5 203 − 5 160', '≈ 5 200 − 5 200 = 0', 'exact 43', 'erreur 43', 43, 43, 'erreur = tout le résultat')):
    text(ax, cx, 44, t, role, 'm'); text(ax, cx, 37, e, 'varie', 's')
    box(ax, cx - 19, 24, 38, 7, 'resultat', label=ex, size='s')
    wd = max(38 * err / v, 3.2)
    box(ax, cx - 19, 13, wd, 7, 'varie', label=None, r=0.3)
    if err == 43: text(ax, cx, 16.5, er, 'varie', 's')
    else: text(ax, cx - 19 + wd + 1, 16.5, er, 'varie', 's', ha='left')
    text(ax, cx, 6, msg, role, 's')
save(fig, '10-040')
