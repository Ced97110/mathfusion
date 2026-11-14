import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
words = ['000', '001', '010', '011', '100', '101', '110', '111']
text(ax, 44, 57, 'les 8 mots de 3 bits', 'fixe', 'm', weight='bold')
for i, w in enumerate(words):
    col, row = i % 4, i // 4
    role = 'sujet' if w in ('000', '111') else 'fixe'
    box(ax, 3 + col * 21, 38 - row * 11, 19, 8, role, label=w, weight='bold' if role == 'sujet' else 'normal')
box(ax, 3, 10, 7, 6, 'sujet')
text(ax, 13, 13, r'mots du code $C$ : 2 mots, $2^k$ avec $k = 1$', 'sujet', 's', ha='left')
box(ax, 3, 2, 7, 6, 'fixe')
text(ax, 13, 5, 'hors du code : ne vient que du bruit', 'fixe', 's', ha='left')
save(fig, '68-033')
