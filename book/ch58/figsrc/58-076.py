import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 2, 38, 84, 36, 'fixe', fill=False, dash=True)
text(ax, 44, 68, '$F$ : un corps', 'sujet', 'm')
for i, lab in enumerate(['ℚ\nfractions', 'ℝ\nréels', 'ℂ\ncomplexes', 'ℤ/pℤ\nhorloge']):
    box(ax, 5 + 20.5 * i, 43, 18.5, 17, 'sujet', label=lab, size='s')
text(ax, 44, 31, 'tout nombre non nul a un inverse', 'encre', 's')
box(ax, 6, 8, 36, 14, 'resultat', label='2 × ½ = 1')
box(ax, 46, 8, 36, 14, 'resultat', label='3 × ⅓ = 1')
save(fig, '58-076')
