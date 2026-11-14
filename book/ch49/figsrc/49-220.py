import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, 'chaque orbite apporte 4 croix', 'fixe', 's')
for k in range(3):
    x0 = 8 + k * 26
    box(ax, x0 - 2, 22, 22, 24, 'sujet', dash=True, r=1)
    for i in range(2):
        for j in range(2):
            cx, cy = x0 + 4 + i * 10, 28 + j * 10
            ax.plot([cx - 2, cx + 2], [cy - 2, cy + 2], color=COL['sujet'], lw=1.1, solid_capstyle='round', zorder=3)
            ax.plot([cx - 2, cx + 2], [cy + 2, cy - 2], color=COL['sujet'], lw=1.1, solid_capstyle='round', zorder=3)
    text(ax, x0 + 9, 15.5, r'$|G|$ = 4', 'sujet', 's')
brace(ax, 6, 82, 12, 'varie', depth=1.6)
text(ax, 44, 3, r'$k$ = 3 orbites : $N = 3 \times 4 = 12$', 'resultat', 'm')
save(fig, '49-220')
