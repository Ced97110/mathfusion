import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
E = [2, 1]
text(ax, 44, 65, 'case pleine en rangée k : e > k', 'encre', 's')
text(ax, 20, 56, 'exposants e : 2 et 1', 'sujet', 's')
text(ax, 70, 56, 'exposants e : 2 et 1', 'autre', 's')
for c in range(2):
    for k, y in enumerate((18, 28, 38)):
        for x0, role in ((12 + 8 * c, 'sujet'), (62 + 8 * c, 'autre')):
            if E[c] > k:
                box(ax, x0, y, 7, 8, role, r=0.4)
            else:
                box(ax, x0, y, 7, 8, 'fixe', fill=False, dash=True, r=0.4)
for k, y in enumerate((18, 28, 38)):
    d = sum(1 for e in E if e > k)
    text(ax, 44, y + 4, f'k = {k} : dim {d}', 'resultat', 's')
for c in range(2):
    text(ax, 15.5 + 8 * c, 11, f'z{"₁₂"[c]}\ne = {E[c]}', 'sujet', 's')
    text(ax, 65.5 + 8 * c, 11, f'w{"₁₂"[c]}\ne = {E[c]}', 'autre', 's')
text(ax, 44, 3, 'pointillés : e ≤ k, case vide', 'fixe', 's')
save(fig, '60-068')
