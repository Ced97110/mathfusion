import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(40)
vals = [r'$t=12$', '360°', '0', '0', '2 m']
names = ['heure', 'angle', 'sinus', 'double', 'hauteur']
ops = [r'$\times 30$', 'sin', r'$\times 2$', '+ 2']
roles = ['fixe', 'sujet', 'sujet', 'sujet', 'resultat']
bw, gap = 12, 6
for i in range(5):
    x = 2 + i * (bw + gap)
    box(ax, x, 18, bw, 10, roles[i], label=vals[i])
    text(ax, x + bw / 2, 13.5, names[i], 'fixe', 's')
    if i < 4:
        arrow(ax, (x + bw + 0.5, 23), (x + bw + gap - 0.5, 23), 'varie')
        text(ax, x + bw + gap / 2, 30, ops[i], 'varie', 's')
save(fig, '32-001')
