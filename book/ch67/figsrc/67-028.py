import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
text(ax, 13, 84, 'élément', 'sujet', 's')
text(ax, 46, 84, r'$a\cdot1+b\cdot\alpha$', 'fixe', 's')
text(ax, 77, 84, 'mot', 'resultat', 's')
els = ['0', '1', r'$\alpha$', r'$\alpha+1$']
ex = [r'$0\cdot1+0\cdot\alpha$', r'$1\cdot1+0\cdot\alpha$', r'$0\cdot1+1\cdot\alpha$', r'$1\cdot1+1\cdot\alpha$']
wd = ['00', '10', '01', '11']
for i in range(4):
    y = 62 - 19 * i + 6
    box(ax, 4, y, 18, 12, 'sujet', label=els[i])
    arrow(ax, (22, y + 6), (27, y + 6), 'fixe')
    box(ax, 27, y, 38, 12, 'fixe', label=ex[i], size='s')
    arrow(ax, (65, y + 6), (70, y + 6), 'fixe')
    box(ax, 70, y, 14, 12, 'resultat', label=wd[i], size='l')
save(fig, '67-028')
