import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, 'ℤ/2 ⊕ ℤ/6 : B = (bᵢⱼ)', 'encre', 'm')
cells = [(0, 0, 'b₁₁ modulo 2\n2 choix', 'sujet'), (1, 0, 'b₁₂ mod 6, multiple de 3\n2 choix', 'varie'),
         (0, 1, 'b₂₁ modulo 2\n2 choix', 'sujet'), (1, 1, 'b₂₂ modulo 6\n6 choix', 'sujet')]
for c, r, lab, role in cells:
    box(ax, 5 + c * 40, 46 - r * 20, 38, 18, role, label=lab, size='s')
text(ax, 44, 16, '2 × 2 × 2 × 6 = 48', 'resultat', 'l', weight='bold')
text(ax, 44, 8, 'endomorphismes', 'resultat', 's')
save(fig, '60-196')
