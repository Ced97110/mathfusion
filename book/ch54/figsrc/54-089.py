import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cw, x0 = 8.6, 14
A = [3, 0, 0, 2]; B = [2, 0, -1, 0, 4]
P = [6, 0, -3, 4, 12, -2, 0, 8]
for r in range(8):
    text(ax, x0 + (r + 0.5) * cw, 56, str(r), 'fixe', 's')
text(ax, 7, 56, 'rang', 'fixe', 's')
rows = [(A, 'fixe', 44, r'$a_j$'), (B, 'autre', 32, r'$b_k$'), (P, 'sujet', 14, r'$p_i$')]
for vals, role, y, lab in rows:
    text(ax, 7, y + 4, lab, role, 'l')
    for r, v in enumerate(vals):
        rl = 'resultat' if (vals is P and r == 2) else role
        box(ax, x0 + r * cw + 0.3, y, cw - 0.6, 8, rl, label=str(v).replace('-', '−'), size='s')
text(ax, 44, 24, 'le produit', 'sujet', 's')
arrow(ax, (x0 + 2.5 * cw, 13), (x0 + 2.5 * cw, 8.5), 'resultat')
text(ax, x0 + 2.5 * cw, 4, r'$p_2=-3$', 'resultat', 'm')
save(fig, '54-089')
