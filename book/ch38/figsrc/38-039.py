import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
k = 0.0092                                  # mm par mètre : BS = 5 451 m -> 50 mm
beta = math.radians(21.25)
bs = 5450.73 * k
B = (6.0, 38.0)
H = (B[0] + bs * math.cos(beta), B[1])
S = (H[0], B[1] + bs * math.sin(beta))
poly(ax, [B, H, S], 'fixe')
line(ax, [S, H], 'fixe', dash=True, lw=0.8)
line(ax, [B, S], 'sujet', lw=2.0)
text(ax, B[0], B[1] - 3.5, 'B', 'sujet', 's')
text(ax, S[0] - 1, S[1] + 3, 'S', 'sujet', 's')
text(ax, H[0], B[1] - 3.5, 'H', 'fixe', 's')
text(ax, B[0] + 15, B[1] + 16, 'BS ≈ 5 451 m', 'sujet', 's', weight='bold')
text(ax, H[0] + 2, (B[1] + S[1]) / 2, 'h', 'fixe', 's', ha='left')
# BS est un nombre intermédiaire
box(ax, 2, 6, 22, 9, 'autre', label='triangle ABS', size='s')
box(ax, 33, 6, 22, 9, 'sujet', label='BS', size='m', weight='bold')
box(ax, 64, 6, 22, 9, 'resultat', label='h', size='m', weight='bold')
arrow(ax, (24.5, 10.5), (32.5, 10.5), 'varie')
arrow(ax, (55.5, 10.5), (63.5, 10.5), 'varie')
text(ax, 44, 21, 'BS : nombre intermédiaire', 'sujet', 's')
save(fig, '38-039')
