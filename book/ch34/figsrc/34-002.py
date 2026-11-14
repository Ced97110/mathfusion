import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
a = 70/75; c = 70/5625
text(ax, 6, 65, r'angles : 30° + 45° = 75°', 'encre', 'm', ha='left')
box(ax, 6, 52, 30*a, 8, 'sujet', label='30°')
box(ax, 6 + 30*a, 52, 45*a, 8, 'autre', label='45°')
box(ax, 6, 41, 75*a, 8, 'resultat', label='75°')
text(ax, 6, 33, r'carrés : 30² + 45² ≠ 75²', 'encre', 'm', ha='left')
box(ax, 6, 21, 900*c, 8, 'sujet', label='900')
box(ax, 6 + 900*c, 21, 2025*c, 8, 'autre', label='2025')
text(ax, 6 + 2925*c + 2, 25, '= 2925', 'limite', 'm', ha='left')
box(ax, 6, 9, 5625*c, 8, 'resultat', label=r'5625 = $75^2$')
save(fig, '34-002')
