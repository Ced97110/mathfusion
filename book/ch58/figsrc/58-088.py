import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, '$F$ peut être l’un d’eux', 'encre', 'm')
labs = ['ℚ : fractions', 'ℝ : réels', 'ℂ : complexes']
for i, lab in enumerate(labs):
    y = 40 - 17 * i
    box(ax, 2, y, 32, 12, 'sujet', label=lab, size='s')
    arrow(ax, (34, y + 6), (54, 29), 'sujet', lw=0.9)
box(ax, 54, 20, 32, 18, 'resultat', label='$F$ : un corps', size='m')
text(ax, 70, 11, 'division par un\nnombre non nul :\ntoujours possible', 'resultat', 's')
save(fig, '58-088')
