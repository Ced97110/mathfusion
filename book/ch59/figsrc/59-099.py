import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cw, h, y = 5.0, 8, 30
x1 = 6
x2 = x1 + 2 * cw + 10
for i in range(2):
    box(ax, x1 + i * cw, y, cw, h, 'sujet', r=0.3)
for i in range(10):
    box(ax, x2 + i * cw, y, cw, h, 'autre', r=0.3)
text(ax, x1 + 2 * cw + 5, y + h / 2, '⊕', 'encre', 'l')
text(ax, 44, 56, 'M (20 éléments) = Dz₁ ⊕ Dz₂', 'encre', 'm')
text(ax, x1 + cw, y + h + 4, 'Dz₁ : 2', 'sujet', 's')
text(ax, x2 + 5 * cw, y + h + 4, 'Dz₂ : 10 éléments', 'autre', 's')
text(ax, x1 + cw, 20, 'ann z₁ = (2)', 'sujet', 's')
text(ax, x2 + 5 * cw, 20, 'ann z₂ = (10)', 'autre', 's')
text(ax, 44, 8, '(2) ⊇ (10) : ils s’emboîtent', 'fixe', 's')
save(fig, '59-099')
