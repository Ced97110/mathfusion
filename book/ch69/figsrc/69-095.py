import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
w, g = 22.0, 6.0
x0 = (88 - 3 * w - 2 * g) / 2
cx = [x0 + w / 2 + i * (w + g) for i in range(3)]
labs = [r'$f_0(1)=-1$', r'$f_1(1)=0$', r'$f_2(1)=1$']
roles = ['sujet', 'fixe', 'sujet']
for i in range(3):
    box(ax, cx[i] - w / 2, 30, w, 12, roles[i], label=labs[i], size='m', dash=(i == 1))
arrow(ax, (cx[0], 29), (cx[2], 29), 'varie', curve=0.3, both=True)
text(ax, cx[1], 15.5, r'$f_0(1)=-f_2(1)$', 'varie', 'm')
box(ax, 20, 2, 48, 8, 'resultat', label='voisins opposés : V stable', size='m')
save(fig, '69-095')
