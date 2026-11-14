import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, 'pour tout x dans ℝ, x² ≥ 0', 'encre', 'm')
parts = [('sujet', '∀', 'pour tout', 4, 14), ('fixe', 'x', 'un objet', 20, 14),
         ('fixe', '∈ ℝ', 'dans les réels', 36, 20), ('autre', 'x² ≥ 0', 'condition', 60, 24)]
for role, s, mean, x, w_ in parts:
    box(ax, x, 28, w_ - 2, 14, role, label=s, size='l')
    text(ax, x + (w_ - 2) / 2, 21, mean, role, 's')
brace(ax, 4, 54, 46, 'sujet', label='pour quels objets', down=False)
brace(ax, 60, 82, 46, 'autre', label='vraie pour chacun', down=False)
save(fig, '42-089')
