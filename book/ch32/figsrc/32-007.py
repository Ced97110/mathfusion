import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
eqs = [r'$2+2\sin(30t)=3$', r'$2\sin(30t)=1$', r'$\sin(30t)=0{,}5$', r'$t=1$']
ops = ['retirer 2', 'diviser par 2', 'défaire le sinus']
roles = ['sujet', 'sujet', 'sujet', 'resultat']
bw, bh, gap = 46, 10, 9
for i in range(4):
    y = 74 - bh - i * (bh + gap)
    box(ax, 8, y, bw, bh, roles[i], label=eqs[i])
    if i < 3:
        arrow(ax, (8 + bw / 2, y - 0.5), (8 + bw / 2, y - gap + 0.5), 'varie')
        text(ax, 8 + bw / 2 + 3, y - gap / 2, ops[i], 'varie', 'm', ha='left')
save(fig, '32-007')
