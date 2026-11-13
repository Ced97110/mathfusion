import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
C = (26, 40); R = 22
for n in range(12):
    a = math.radians(90 - 30 * n); x, y = C[0] + R * math.cos(a), C[1] + R * math.sin(a)
    if n in (0, 4, 8): role = 'sujet'
    elif n in (3, 6, 9): role = 'autre'
    else: role = 'resultat'
    disc(ax, x, y, 4.3, role, label=str(n), size='s')
    if n in (0, 3, 6, 9): disc(ax, x, y, 5.6, 'autre', fill=False)
text(ax, 54, 56, 'bleu : 0, 4, 8 (H₂)\nviolet : 0, 3, 6, 9 (H₃)\nvert : sommes en plus', 'encre', 's', ha='left')
text(ax, 54, 24, 'union : 6 nombres\nproduit : 12 nombres', 'encre', 's', ha='left')
save(fig, '79-157')
