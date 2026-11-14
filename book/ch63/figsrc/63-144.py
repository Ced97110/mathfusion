import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
box(ax, 22, 68, 44, 10, role='fixe', label='x³ − 2 : séparable')
rx = [22, 44, 66]
for c, t in zip(rx, ['r', 'jr', 'j²r']):
    disc(ax, c, 52, 6, role='sujet', label=t)
    arrow(ax, (44 + (c - 44) * 0.5, 67.2), (c, 58.3), 'varie')
    arrow(ax, (c, 45.7), (44 + (c - 44) * 0.6, 40.4), 'varie')
box(ax, 8, 28, 72, 12, role='resultat', label='E = ℚ(r, j) : [E:ℚ] = 6')
arrow(ax, (44, 27.2), (44, 22.2), 'varie')
text(ax, 44, 18, 'G = S₃ : 6 éléments', 'sujet', 'm', weight='bold')
for i, t in enumerate(['1', 'σ', 'σ²', 'τ', 'στ', 'σ²τ']):
    box(ax, 2 + 14.8 * i * 0.973, 4, 12, 9, role='sujet', label=t)
save(fig, '63-144')
