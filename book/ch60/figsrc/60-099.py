import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 56, r'$8=2^3$ : exposant 3', 'sujet', 'l')
c = 7.0
parts = [[3], [2, 1], [1, 1, 1]]
labs = ['3', '2 + 1', '1 + 1 + 1']
for r, (p, lab) in enumerate(zip(parts, labs)):
    y = 38 - r * 13
    x = 34
    for blk in p:
        for _ in range(blk):
            box(ax, x, y, c, c, 'sujet', r=0.3)
            x += c
        x += 3
    text(ax, 4, y + c / 2, lab, 'encre', 'm', ha='left')
brace(ax, 4, 84, 9, 'resultat', label='3 façons : 3 groupes')
save(fig, '60-099')
