import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
s = 2.4
for g, (k, role, lab) in enumerate([(1, 'varie', '1 % = 1/100'), (26, 'sujet', '26 % = 26/100'), (100, 'resultat', '100 % = 1')]):
    x0 = 5 + g * 29
    for i in range(100):
        r_, c_ = divmod(i, 10)
        rl = role if i < k else 'fixe'
        ax.add_patch(Rectangle((x0 + c_ * s, 14 + (9 - r_) * s), s, s, ec=COL['fixe'], fc=FILL[rl], lw=0.2, zorder=2))
    text(ax, x0 + 12, 9, lab, role, 's')
    text(ax, x0 + 12, 3.5, f'{k} carreau' + ('x' if k > 1 else ''), 'fixe', 's')
save(fig, '09-071')
