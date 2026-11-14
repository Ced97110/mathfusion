import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, '≅', 'resultat', 'xl')
cx, cy, r = 20, 36, 14
def P(h, rr=r):
    a = math.radians(90 - 30 * h)
    return (cx + rr * math.cos(a), cy + rr * math.sin(a))
text(ax, 20, 58, 'ℤ/12', 'fixe', 'm')
text(ax, 67, 58, 'ℤ/4 ⊕ ℤ/3', 'fixe', 'm')
for h in range(12):
    role = {5: 'sujet', 7: 'autre'}.get(h)
    disc(ax, *P(h), 2 if role else 1.3, role or 'fixe')
text(ax, *P(5, 19), '5', 'sujet', 'm')
text(ax, *P(7, 19), '7', 'autre', 'm')
special = {(1, 2): 'sujet', (3, 1): 'autre'}
for a in range(4):
    for b in range(3):
        role = special.get((a, b), 'fixe')
        box(ax, 52 + 10 * b, 44 - 9 * a, 9, 8, role, label=f'({a},{b})' if (a, b) in special else None, size='s', r=0.4)
text(ax, 44, 8, '5 → (1, 2)  ;  7 → (3, 1)', 'encre', 's')
save(fig, '60-082')
