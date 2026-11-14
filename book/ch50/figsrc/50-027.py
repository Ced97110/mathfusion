import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r'éléments de $\mathbb{Z}/8\mathbb{Z}$ classés par ordre', 'sujet', 's')
rows = [(52, 'ordre 1 = 2⁰', ['0']), (38, 'ordre 2 = 2¹', ['4']), (24, 'ordre 4 = 2²', ['2', '6']), (10, 'ordre 8 = 2³', ['1', '3', '5', '7'])]
for y, lab, els in rows:
    text(ax, 3, y, lab, 'resultat', 's', ha='left')
    for j, e in enumerate(els):
        disc(ax, 42 + 10.5 * j, y, 4.2, 'sujet', label=e, size='m')
save(fig, '50-027')
