import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 4, 62, 80, 10, 'sujet', label='z₁ ∈ ℤ/2 :  2 × z₁ = 0', size='m')
text(ax, 44, 55, 'w ∈ ℤ/3 : il faut 2 × w = 0', 'encre', 's')
rows = [(0, 'resultat', '2 × 0 = 0 : accepté'), (1, 'limite', '2 × 1 = 2 ≠ 0 : refusé'), (2, 'limite', '2 × 2 = 1 ≠ 0 : refusé')]
for i, (w, role, lab) in enumerate(rows):
    y = 41 - i * 14
    disc(ax, 12, y, 5, role, label=str(w), size='m')
    arrow(ax, (18, y), (24, y), role)
    box(ax, 25, y - 5.5, 59, 11, role, label=lab, size='m')
save(fig, '60-194')
