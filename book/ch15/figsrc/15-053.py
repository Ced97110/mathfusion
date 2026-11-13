import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 42, 63, 'aucune lettre\nen bas', 'fixe', 's')
text(ax, 61, 63, 'exposants\nentiers ≥ 0', 'fixe', 's')
rows = [(46, r'$3x^2 + 1$', 'sujet', ['ok', 'ok'], 'polynôme', 'resultat'),
        (30, r'$5 \div x$', 'limite', ['no', None], 'non', 'limite'),
        (14, r'$x^{-2}$', 'limite', [None, 'no'], 'non', 'limite')]
for y, e, r, marks, verdict, vr in rows:
    box(ax, 3, y - 5, 27, 10, r, label=e)
    for cx, m in zip((42, 61), marks):
        if m == 'ok': disc(ax, cx, y, 3.2, 'resultat', label='✓')
        elif m == 'no': disc(ax, cx, y, 3.2, 'limite', label='✗')
    box(ax, 70, y - 4, 15, 8, vr, label=verdict, size='s')
save(fig, '15-053')
