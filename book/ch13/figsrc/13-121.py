import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
text(ax, 22, 91, 'le haut', 'sujet', 'm'); text(ax, 66, 91, 'le bas', 'autre', 'm')
H_ = ['−6(4 − 7) − 2(8 − 9)', '−6 × (−3) − 2 × (−1)', '18 + 2', '20']
B_ = ['−(4 + 1) + 1', '−5 + 1', '−4']
for i, s in enumerate(H_):
    y = 76 - i * 15
    box(ax, 1, y, 42, 9, 'sujet', label=s, size='s')
    if i: arrow(ax, (22, y + 15), (22, y + 9), 'varie')
for i, s in enumerate(B_):
    y = 76 - i * 15
    box(ax, 45, y, 42, 9, 'autre', label=s, size='s')
    if i: arrow(ax, (66, y + 15), (66, y + 9), 'varie')
arrow(ax, (22, 31), (36, 17), 'resultat'); arrow(ax, (66, 46), (52, 17), 'resultat')
box(ax, 14, 5, 60, 11, 'resultat', label='20 ÷ (−4) = −5', size='l')
save(fig, '13-121')
