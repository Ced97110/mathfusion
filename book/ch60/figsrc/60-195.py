import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, 'w₁ = b₁₁ z₁ + b₁₂ z₂', 'encre', 'm')
text(ax, 44, 58, '2 × b₁₂ multiple de 6', 'sujet', 's')
cx, cy, R, rd = 44, 30, 14, 3.5
for h in range(6):
    a = math.radians(90 - 60 * h)
    ok = h in (0, 3)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), rd, 'resultat' if ok else 'fixe', label=str(h), size='s')
text(ax, cx, cy, 'ℤ/6', 'fixe', 's')
text(ax, 38, 44, '2 × 0 = 0', 'resultat', 's', ha='right')
text(ax, 38, 16, '2 × 3 = 6', 'resultat', 's', ha='right')
text(ax, 44, 5, 'b₁₂ ∈ {0, 3}', 'resultat', 'm', weight='bold')
text(ax, 2, 5, 'd₁ = 2, d₂ = 6', 'fixe', 's', ha='left')
save(fig, '60-195')
