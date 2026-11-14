import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cw, ch = 3.3, 3.0
for c in range(12):
    for r in range(10):
        box(ax, 4 + c * cw, 14 + r * ch, cw, ch, 'sujet', r=0.2, lw=0.3)
box(ax, 4 + 11 * cw, 14 + 9 * ch, cw, ch, 'varie', r=0.2, lw=0.6)
text(ax, 24, 8.5, '120 paires', 'sujet', 's')
box(ax, 54, 22, 30, 22, 'varie', fill=False)
for k in range(6):
    disc(ax, 59 + (k % 3) * 10, 28 + (k // 3) * 9, 2.6, 'varie')
text(ax, 69, 49, '6 pour une paire', 'varie', 's')
arrow(ax, (4 + 12 * cw + 0.5, 14 + 9.5 * ch), (59, 44.5), 'varie', curve=-0.2, lw=0.8)
text(ax, 62, 8.5, r'$120\times 6=720$', 'resultat', 'm')
save(fig, '75-127')
