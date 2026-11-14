import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cols = [
    (3, 'sujet', r'$p=2$ : $\mathbb{F}_4$ sur $\mathbb{F}_2$',
     [r'$\eta(\alpha)=\alpha^2=\alpha+1$', r'$\eta^2(\alpha)=\alpha+2$', r'$\eta^2=\mathrm{id}$ donc $2=0$'],
     r'vrai : $1+1=0$ dans $\mathbb{F}_2$', 'resultat'),
    (47, 'autre', r'sur $\mathbb{Q}$ : $\mathbb{Q}(\sqrt{2})$',
     [r'$\eta(c)=c+1$', r'$\eta^2(c)=c+2$', r'$\eta^2=\mathrm{id}$ donc $2=0$'],
     r'faux dans $\mathbb{Q}$ : $2\neq0$', 'limite'),
]
ys = [50, 36, 22]
for x, role, head, boxes, verdict, vrole in cols:
    cx = x + 19
    text(ax, cx, 64, head, role)
    for y, s in zip(ys, boxes):
        box(ax, x, y, 38, 9, role, label=s, size='s')
    for y in ys[:2]:
        arrow(ax, (cx, y), (cx, y - 4.8), 'fixe')
    arrow(ax, (cx, ys[2]), (cx, 14.8), 'fixe')
    box(ax, x, 5, 38, 9, vrole, label=verdict, size='s')
save(fig, '67-154')
