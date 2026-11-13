import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 64, r'6 sous-groupes de $\mathbb{Z}/12\mathbb{Z}$', 'sujet', 's', weight='bold')
labs = [r'$\{0\}$', r'$K=\langle6\rangle$', r'$\langle4\rangle$', r'$\langle3\rangle$', r'$\langle2\rangle$', r'$G$']
gens = [12, 6, 4, 3, 2, 1]
for j in (0, 3, 6, 9):
    text(ax, 28 + 4.9*j + 2.4, 56, str(j), 'fixe', 's')
for i, (lab, g) in enumerate(zip(labs, gens)):
    y = 46 - i * 8.5
    role = 'autre' if g == 6 else 'sujet'
    text(ax, 2, y + 3, lab, role, 's', ha='left')
    for j in range(12):
        ok = j % g == 0
        box(ax, 28 + 4.9*j, y, 4.9, 6, role if ok else 'fixe', fill=ok, lw=0.5, r=0.4)
save(fig, '48-096')
