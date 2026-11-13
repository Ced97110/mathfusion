import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 23, 56, 'horloge à 12 heures', 'encre', 's')
text(ax, 65, 56, 'symétries du triangle', 'encre', 's')
cx, cy, R = 23, 33, 12
for i in range(12):
    a = math.radians(90 - 30 * i)
    if i == 0:
        disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 2.3, 'resultat', label='$e$', size='s')
    else:
        disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 1.8, 'fixe')
text(ax, cx, cy, r"$G'=\{e\}$", 'resultat', 's')
text(ax, cx, 14, 'abélien', 'resultat', 'm')
text(ax, cx, 8, 'tous les couples commutent', 'resultat', 's')
cx = 65
box(ax, cx - 16, 36, 32, 11, 'sujet')
for dx in (-11, 0, 11):
    disc(ax, cx + dx, 41.5, 3.3, 'sujet', label=('$e$' if dx == -11 else None), size='s')
    disc(ax, cx + dx, 27, 3.3, 'fixe')
text(ax, cx, 51, r"$G'$ : 3 éléments", 'sujet', 's')
text(ax, cx, 14, 'non abélien', 'limite', 'm')
text(ax, cx, 8, 'des couples ne commutent pas', 'limite', 's')
save(fig, '50-215')
