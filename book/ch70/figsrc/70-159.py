import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 74, r'$x^{\prime}=x/m-y$ pour $(1\,;\,1)$ et $(3\,;\,2)$', 'encre', 's')
# m = 1 : x' = 0 and 1
f = numberline(ax, 8, 72, 48, -1, 2, step=0.5, every=2, arrow_right=False)
text(ax, 2, 65, r'$m=1$ : valeurs 0 et 1, différentes', 'resultat', 's', ha='left')
for v, role, lab in ((0, 'sujet', '(1 ; 1)'), (1, 'autre', '(3 ; 2)')):
    line(ax, [(f(v), 48), (f(v), 52)], role, dash=True)
    disc(ax, f(v), 53, 1.4, role)
    text(ax, f(v), 58, lab, role, 's')
# m = 2 : x' = -1/2 for both
g = numberline(ax, 8, 72, 20, -1, 2, step=0.5, every=2, arrow_right=False)
text(ax, 2, 37, r'$m=2$ : même valeur $-0{,}5$', 'limite', 's', ha='left')
line(ax, [(g(-0.5), 20), (g(-0.5), 29)], 'limite', dash=True)
disc(ax, g(-0.5), 25, 1.4, 'sujet'); text(ax, g(-0.5) + 3, 25, '(1 ; 1)', 'sujet', 's', ha='left')
disc(ax, g(-0.5), 30, 1.4, 'autre'); text(ax, g(-0.5) + 3, 30, '(3 ; 2)', 'autre', 's', ha='left')
save(fig, '70-159')
