import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'mots de 7 bits en classes', 'encre', 'm', weight='bold')
text(ax, 2.75, 46, 'le code = un sous-groupe', 'sujet', 's', ha='left')
w, h, gx, x0 = 18, 12, 3.5, 2.75
labs = ['000', '001', '010', '011', '100', '101', '110', '111']
for k, s in enumerate(labs):
    r, c = divmod(k, 4)
    box(ax, x0 + c * (w + gx), 30 - r * 16, w, h, 'sujet' if k == 0 else 'fixe', label=s, size='m')
text(ax, 44, 8, 'étiquette de chaque classe = syndrome', 'fixe', 's')
save(fig, '68-214')
