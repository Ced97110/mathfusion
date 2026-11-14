import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
xs = [14 + i * 20 for i in range(4)]
y = 34
text(ax, 44, 60, 'ℤ/4ℤ : libre, base (1)', 'resultat', 's', weight='bold')
brace(ax, xs[0] - 5, xs[3] + 5, 50, 'resultat', down=False, label=None)
for i, x in enumerate(xs):
    inside = i in (0, 2)
    disc(ax, x, y, 5.2, 'sujet' if inside else 'fixe', label=str(i), size='m')
# sous-module {0, 2}
brace(ax, xs[0] - 5, xs[2] + 5, 25, 'sujet', label='sous-module {0, 2}', down=True)
# 2 x 2 = 0
text(ax, 44, 11, '2 × 2 = 4 = 0, avec 2 ≠ 0', 'limite', 's')
box(ax, 14, 1, 60, 7, 'limite', label='la famille (2) est liée : pas libre', size='s')
save(fig, '58-322')
