import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cols = [(3, 'limite', ['$z = 0$', r'$0^2+0^2=0$', '÷ 0 : impossible']),
        (46, 'resultat', [r'$z \neq 0$', r'$a^2+b^2\neq 0$', 'inverse existe'])]
roles0 = ['sujet', 'fixe']
for x, role, labs in cols:
    for k, lab in enumerate(labs):
        y = 52 - k * 18
        r = role if k == 2 else roles0[k]
        box(ax, x, y, 39, 11, r, label=lab, dash=(k == 2 and role == 'limite'))
        if k < 2: arrow(ax, (x + 19.5, y - 0.3), (x + 19.5, y - 6.7), 'fixe')
box(ax, 3, 2, 82, 9, 'sujet', label='ℂ∗ : l’étoile retire 0')
save(fig, '44-197')
