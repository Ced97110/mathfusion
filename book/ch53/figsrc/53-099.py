import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cx, cy, R, N = 25, 28, 20, 55
for k in range(N):
    a = math.pi / 2 - 2 * math.pi * k / N
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 1.2, 'varie' if k == 0 else 'sujet')
text(ax, cx, cy + 3, r'$\mathbb{Z}/55\mathbb{Z}$', 'sujet', 'l')
text(ax, cx, cy - 3, '55 cases', 'sujet', 's')
text(ax, cx, cy + R + 4.5, '0', 'varie', 's')
text(ax, cx - 8.5, cy + R + 2.5, '54', 'sujet', 's')
box(ax, 56, 30, 28, 12, 'resultat', label=r'$n$ = 55', size='m')
text(ax, 70, 24, r'$n = 5 \times 11$', 'encre', 's')
text(ax, 70, 16, 'public :', 'encre', 's')
text(ax, 70, 11, 'tout le monde', 'encre', 's')
text(ax, 70, 6, 'le connaît', 'encre', 's')
save(fig, '53-099')
