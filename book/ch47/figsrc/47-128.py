import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 44, 82, 'tous vrais, ou tous faux', 'resultat', 'm')
for y, lab, n in [(60, r'$gN=Ng$', 1), (36, r'$gNg^{-1}\subseteq N$', 2), (12, r'$gNg^{-1}=N$', 3)]:
    box(ax, 19, y, 50, 12, 'sujet', label=lab, size='m')
    text(ax, 2, y + 6, 'énoncé %d' % n, 'sujet', 's', ha='left')
arrow(ax, (44, 59.5), (44, 48.5), 'resultat', both=True)
text(ax, 48, 54, 'calcul court', 'encre', 's', ha='left')
arrow(ax, (44, 35.5), (44, 24.5), 'resultat', both=True)
text(ax, 48, 30, 'appliquer à g⁻¹', 'encre', 's', ha='left')
save(fig, '47-128')
