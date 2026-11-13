import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
p, w, x0 = 1.85, 1.55, 3.3
for i in range(30): box(ax, x0 + i * p, 52, w, 6, 'fixe', r=0.2, lw=0.5)
for i in range(44):
    box(ax, x0 + i * p, 38, w, 6, 'sujet' if i < 24 else 'varie', r=0.2, lw=0.5)
brace(ax, x0, x0 + 30 * p - 0.3, 59, 'fixe', label='groupe : 30 éléments', down=False)
xl = x0 + 30 * p - 0.15
line(ax, [(xl, 36), (xl, 60)], 'limite', lw=1.0, dash=True)
text(ax, 72, 48, 'au-delà de 30', 'limite', 's')
brace(ax, x0, x0 + 24 * p - 0.3, 37, 'sujet', label=r'$6 \times 4 = 24$ (ordre 5)', down=True)
brace(ax, x0 + 24 * p, x0 + 44 * p - 0.3, 37, 'varie', label=r'$10 \times 2 = 20$ (ordre 3)', down=True)
text(ax, 44, 22, r'$24 + 20 = 44 > 30$', 'limite', 'l')
text(ax, 44, 13, 'impossible', 'limite', 'm')
save(fig, '50-186')
