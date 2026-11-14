import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 21, 79, '$\\vee$ : joint', 'sujet', 's', weight='bold')
text(ax, 67, 79, '$\\wedge$ : rencontre', 'autre', 's', weight='bold')
rows = [('L3 : $a\\vee a=a$\nPPCM(4, 4) = 4', 'L3 : $a\\wedge a=a$\nPGCD(4, 4) = 4'),
        ('L1 : $a\\vee b=b\\vee a$\nPPCM(4, 6) = PPCM(6, 4)', 'L1 : $a\\wedge b=b\\wedge a$\nPGCD(4, 6) = PGCD(6, 4)')]
for i, (l, r) in enumerate(rows):
    y = 52 - i * 22
    box(ax, 2, y, 38, 16, 'sujet', label=l, size='s')
    box(ax, 48, y, 38, 16, 'autre', label=r, size='s')
    arrow(ax, (41, y + 8), (47, y + 8), 'varie', both=True)
box(ax, 14, 4, 60, 14, 'varie', label='Échanger $\\vee$ et $\\wedge$ :\n$\\leq$ devient $\\geq$', size='s')
save(fig, '79-109')
