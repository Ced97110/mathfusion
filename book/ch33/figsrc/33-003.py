import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
x0, y0 = 8, 48
L = 70
poly(ax, [(x0, y0), (x0 + L, y0), (x0 + L, y0 + L / 12)], 'sujet')
text(ax, x0 + 12, y0 + 2.6, r'$\theta$', 'sujet')
text(ax, x0 + L / 2, y0 - 4, 'avance 6 m', 'autre')
text(ax, x0 + L - 2, y0 + 11, 'montée 0,5 m', 'varie', ha='right')
labels = [r'$\tan\,\theta = 0{,}5\ /\ 6$', r'$\tan\,\theta = 1/12$', r'$\tan\,\theta \approx 0{,}0833$']
roles = ['encre', 'fixe', 'resultat']
for i, (lab, r) in enumerate(zip(labels, roles)):
    yy = 33 - i * 14
    box(ax, 8, yy, 56, 9, r, label=lab)
    if i: arrow(ax, (36, yy + 14), (36, yy + 9.6), 'varie')
text(ax, 66, 29, 'on divise', 'varie', 's', ha='left')
text(ax, 66, 15, 'on simplifie', 'varie', 's', ha='left')
save(fig, '33-003')
