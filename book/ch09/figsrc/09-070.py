import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 53, 'per centum', 'sujet', 'l')
text(ax, 44, 46.5, 'pour chaque cent', 'sujet', 'm')
s = 2.4
for g in range(3):
    x0 = 6 + g * 28.5
    for i in range(100):
        r_, c_ = divmod(i, 10)
        role = 'resultat' if i < 35 else 'fixe'
        ax.add_patch(Rectangle((x0 + c_ * s, 14 + (9 - r_) * s), s, s, ec=COL['fixe'], fc=FILL[role], lw=0.2, zorder=2))
    brace(ax, x0, x0 + 24, 14, 'fixe', label='100')
    text(ax, x0 + 12, 3.5, '35 pris', 'resultat', 's')
save(fig, '09-070')
