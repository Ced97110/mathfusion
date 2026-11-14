import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def ring(cx, cy, r, n, role):
    for k in range(n):
        a = math.pi / 2 - 2 * math.pi * k / n
        disc(ax, cx + r * math.cos(a), cy + r * math.sin(a), 1.0, role)
ring(24, 58, 11, 7, 'resultat')
ring(64, 58, 11, 26, 'limite')
text(ax, 24, 41, 'horloge à 7 cases', 'resultat', 's')
text(ax, 64, 41, 'horloge à 26 cases', 'limite', 's')
box(ax, 4, 22, 40, 12, 'resultat', label='2 × 4 = 8 = 7 + 1', size='s')
box(ax, 46, 22, 40, 12, 'limite', label='PGCD(2 ; 26) = 2', size='s')
text(ax, 24, 17, '2 a un inverse', 'resultat', 's')
text(ax, 66, 17, '2 n’a pas d’inverse', 'limite', 's')
text(ax, 44, 6, 'AES : un corps à 256 éléments', 'sujet', 'm')
save(fig, '53-191')
