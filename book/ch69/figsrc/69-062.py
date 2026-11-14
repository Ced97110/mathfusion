import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
labs = ['propriété (i)\nracines carrées', 'propriété (ii)\ndegré impair', 'théorie de Galois\n(chapitre 63)']
for k, lab in enumerate(labs):
    x = 3 + 28 * k
    box(ax, x, 62, 26, 12, 'fixe', label=lab, size='s')
    arrow(ax, (x + 13, 62), (x + 13, 48.5), 'fixe')
box(ax, 3, 34, 82, 14, 'sujet', label='pour tout $R$ réel clos :\n$R(i)$ est algébriquement clos')
arrow(ax, (44, 34), (44, 18.5), 'varie')
text(ax, 47, 26.5, 'cas $R$ = ℝ', 'varie', 's', ha='left')
box(ax, 19, 3, 50, 14, 'resultat', label='ℂ = ℝ(i) est\nalgébriquement clos')
save(fig, '69-062')
