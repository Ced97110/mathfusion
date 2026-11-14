import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 14, 59, 'on connaît', 'encre', 'm')
text(ax, 74, 59, 'on cherche', 'encre', 'm')
L = [(r'$\sin A = 0{,}6$', 'sujet'), (r'$\cos A = 0{,}8$', 'sujet'), (r'$\sin B = 0{,}8$', 'autre'), (r'$\cos B = 0{,}6$', 'autre')]
ys = [44, 32, 20, 8]
for (lab, role), y in zip(L, ys):
    box(ax, 2, y, 24, 9, role, label=lab)
    arrow(ax, (26, y + 4.5), (33, 34 - (ys.index(y))*5 + 0), role, lw=0.8)
box(ax, 33, 14, 22, 24, 'varie', label='additions,\nmultiplications', size='s')
box(ax, 62, 30, 24, 9, 'resultat', dash=True, label=r'$\sin(A+B)=\,?$')
box(ax, 62, 14, 24, 9, 'resultat', dash=True, label=r'$\cos(A+B)=\,?$')
arrow(ax, (55, 29), (62, 34.5), 'varie', lw=0.8)
arrow(ax, (55, 23), (62, 18.5), 'varie', lw=0.8)
save(fig, '34-008')
