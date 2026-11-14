import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# the 15 non-zero elements of the field with 16 elements as alpha^k (k = 0..14) ; alpha^3 reaches only k = 0, 3, 6, 9, 12
cx, cy, R = 24, 38, 19
text(ax, 24, 72, 'corps à 16 éléments', 'sujet', 'm')
for k in range(15):
    a = math.radians(90 - k * 24)
    sub = (k % 3 == 0)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 2.0, 'varie' if sub else 'sujet')
text(ax, cx, cy, '15 éléments\nnon nuls', 'sujet', 's')
box(ax, 50, 52, 36, 11, 'sujet', label=r'$\alpha$ : 15 puissances', size='s')
box(ax, 50, 36, 36, 11, 'varie', label=r'$\alpha^3$ : 5 puissances', size='s')
arrow(ax, (68, 35), (68, 28), 'resultat')
box(ax, 50, 14, 36, 13, 'resultat', label=r'$\mathbb{F}_2(\alpha^3)$ = 16 éléments', size='s')
save(fig, '67-088')
