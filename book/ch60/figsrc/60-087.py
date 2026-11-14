import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 4, 56, 32, 12, 'autre', label='ℤₙ (Judson)')
box(ax, 52, 56, 32, 12, 'sujet', label='ℤ/n (chapitre)')
arrow(ax, (37, 62), (51, 62), 'resultat', both=True)
text(ax, 44, 71, 'même groupe', 'resultat', 's')
arrow(ax, (20, 55), (35, 42), 'fixe')
arrow(ax, (68, 55), (53, 42), 'fixe')
cx, cy, r = 44, 28, 12
for h in range(12):
    a = math.radians(90 - 30 * h)
    disc(ax, cx + r * math.cos(a), cy + r * math.sin(a), 1.5, 'sujet')
text(ax, 44, 8, 'n = 12 : 12 positions', 'sujet', 'm')
save(fig, '60-087')
