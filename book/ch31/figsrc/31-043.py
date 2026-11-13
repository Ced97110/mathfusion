import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def B(ax, x, y, w, h, role, label, size='m', weight='normal'): return box(ax, x, y, w, h, role, label=label, size=size, weight=weight)
fig, ax = canvas(56)
text(ax, 36, 51, 'cos θ ÷ sin θ', 'sujet', 'm', weight='bold'); text(ax, 68, 51, '1 ÷ tan θ', 'autre', 'm', weight='bold')
for y, a, c1, r1, c2, r2 in [(32, '40°', '≈ 1,19', 'resultat', '≈ 1,19', 'resultat'), (14, '90°', '0 ÷ 1 = 0', 'resultat', "n'existe pas", 'limite')]:
    text(ax, 10, y + 5.5, a, 'encre', 'l', weight='bold')
    B(ax, 22, y, 28, 11, r1, c1); B(ax, 54, y, 28, 11, r2, c2)
text(ax, 44, 3.5, 'on garde cos θ ÷ sin θ', 'resultat', 'm')
save(fig, '31-043')
