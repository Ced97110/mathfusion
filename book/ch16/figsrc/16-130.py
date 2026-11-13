import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role="fixe", label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(66)
text(ax, 60, 60, r'$x$ vaut 3, puis 4, puis 5', 'encre', 's')
rows = [(r'$x$ + 3 = 7' + '\nconditionnelle', 'sujet', ['faux', 'vrai', 'faux']),
        (r'2$x$ = 2$x$' + '\ntoujours vraie', 'fixe', ['vrai'] * 3),
        (r'$x$ = $x$ + 1' + '\ntoujours fausse', 'fixe', ['faux'] * 3)]
for i, (lab, role, vals) in enumerate(rows):
    y = 40 - i * 19
    box(ax, 2, y, 30, 14, role, lab, 's')
    for j, v in enumerate(vals):
        box(ax, 34 + j * 18, y, 16, 14, 'resultat' if v == 'vrai' else 'limite', v, 's')
save(fig, '16-130')
