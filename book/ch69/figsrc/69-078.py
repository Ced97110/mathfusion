import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
f = numberline(ax, 18, 66, 64, 1, 2, step=1, arrow_right=False)
disc(ax, f(2 ** 0.5), 64, 1.5, 'resultat')
colA = ['−', '+', '+']
colB = ['+', '+', '+']
ys = [48, 39, 30]
for k, y in enumerate(ys):
    box(ax, 13, y, 10, 8, 'fixe', label=colA[k])
    box(ax, 61, y, 10, 8, 'fixe', label=colB[k])
    text(ax, 42, y + 4, r'$f_%d$' % k, 'encre', 'm')
text(ax, 18, 23, r'$V(1)=1$', 'sujet', 'm')
text(ax, 66, 23, r'$V(2)=0$', 'sujet', 'm')
box(ax, 12, 4, 64, 13, 'resultat', label=r'$V(1)-V(2)=1-0=1$' + '\n' + 'racine entre 1 et 2 (dans ℝ)')
save(fig, '69-078')
