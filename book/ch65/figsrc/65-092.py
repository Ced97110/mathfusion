import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 60, 64, r'$G_f$ : 24 éléments', 'sujet', 'm')
for g in range(6):
    x = 4 + g * 14
    role = 'varie' if g == 0 else 'sujet'
    for q in range(4):
        cx = x + (q % 2) * 5.5
        cy = 46 + (q // 2) * 5.5
        box(ax, cx, cy, 4.5, 4.5, role, r=0.4, lw=0.6)
    arrow(ax, (x + 5, 45), (x + 5, 23), 'fixe')
    box(ax, x - 1, 13, 12, 9, 'autre', r=0.6, size='s', label='identité' if g == 0 else r'$\pi_%d$' % (g + 1))
text(ax, 24, 60.5, r'noyau $G_f \cap V$ : 4', 'varie', 's')
text(ax, 34, 6, r'groupe de $g$ : image de $G_f$', 'autre', 's')
text(ax, 77, 6, r'$24 = 6 \times 4$', 'encre', 's')
save(fig, '65-092')
