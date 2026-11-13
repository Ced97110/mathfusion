import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [(60, 'ℤ', '3·2 = 2·3', 'resultat'),
        (48, 'ℝ', '$ab=ba$', 'resultat'),
        (36, '$F[x]$', '$(x+1)(x+2)=(x+2)(x+1)$', 'resultat'),
        (12, '$M_2$(ℤ)', '$A$ après $B$ ≠ $B$ après $A$', 'limite')]
for y, ring, test, role in rows:
    box(ax, 2, y, 24, 10, 'sujet', label=ring, size='m')
    box(ax, 30, y, 56, 10, role, label=test, size='s')
text(ax, 58, 28.5, 'une seule sorte de module', 'resultat', 's')
text(ax, 58, 4, 'gauche et droite diffèrent', 'limite', 's')
save(fig, '57-116')
