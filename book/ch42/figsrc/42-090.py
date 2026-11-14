import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 4, 64, 'phrase longue', 'fixe', 's', ha='left')
text(ax, 4, 14, 'écriture courte', 'sujet', 's', ha='left')
parts = [('sujet', 'il existe un', '∃', 4), ('fixe', 'nombre réel', 'x ∈ ℝ', 32), ('autre', 'carré égal à 2', 'x² = 2', 60)]
for role, ph, sym, x in parts:
    box(ax, x, 44, 24, 14, role, label=ph, size='s')
    box(ax, x, 22, 24, 14, role, label=sym, size='l')
    arrow(ax, (x + 12, 44), (x + 12, 36), 'varie')
save(fig, '42-090')
