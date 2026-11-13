import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cfgs = [('sujet', 'sujet', 'sujet', 'sujet', '4 rotations', 'orbite de 1'),
        ('sujet', 'varie', 'sujet', 'varie', '2 rotations', 'orbite de 2'),
        ('sujet', 'sujet', 'sujet', 'varie', '1 rotation', 'orbite de 4')]
for i, cf in enumerate(cfgs):
    cx = 15 + i * 29; cy = 46; h = 8
    corners = [(cx - h, cy - h), (cx + h, cy - h), (cx + h, cy + h), (cx - h, cy + h)]
    poly(ax, corners, 'fixe')
    # roles for corners 1..4; oppose pairs: corners 2 and 4 orange for second
    roles = [cf[0], cf[1], cf[2], cf[3]]
    if i == 1: roles = ['sujet', 'varie', 'sujet', 'varie']
    for p, r in zip(corners, roles):
        disc(ax, p[0], p[1], 3.2, r)
    text(ax, cx, 28, 'stabilisateur', 'fixe', 's')
    box(ax, cx - 12, 17, 24, 7, 'fixe', label=cf[4], size='s')
    box(ax, cx - 12, 6, 24, 7, 'resultat', label=cf[5], size='s')
text(ax, 44, 67, 'colorations du carré : 3 cas', 'encre', 's')
save(fig, '49-294')
