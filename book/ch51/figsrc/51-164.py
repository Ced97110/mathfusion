import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$GL_n(R)$', 'encre', 'xl')
xs = [4, 32, 60]
roles = ['sujet', 'varie', 'autre']
syms = [r'$GL$', r'$n$', r'$R$']
labs = ['groupe des matrices\ninversibles', 'taille :\nn lignes et\nn colonnes', "anneau d'où\nviennent les cases"]
for x, ro, s, lb in zip(xs, roles, syms, labs):
    box(ax, x, 34, 24, 16, ro, label=s, size='xl')
    text(ax, x + 12, 22, lb, ro, 's')
text(ax, 44, 6, r'$n=2$, $R$ = les réels', 'fixe', 's')
save(fig, '51-164')
