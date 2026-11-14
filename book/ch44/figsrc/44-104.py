import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 44, 82, 'règles posées au départ', 'sujet', 'm')
for i, t in enumerate(['parenthèses sans effet', '0 est neutre', 'chaque entier a un opposé']):
    y = 66 - i * 0
    box(ax, 2 + i * 29, 62, 27, 12, 'sujet')
    text(ax, 15.5 + i * 29, 68, t.split(' ')[0] if False else t, 'sujet', 's') if False else None
labs = [('parenthèses', 'sans effet'), ('0 est', 'neutre'), ('chaque entier', 'a un opposé')]
for i, (a, b) in enumerate(labs):
    x = 15.5 + i * 29
    text(ax, x, 70, a, 'sujet', 's'); text(ax, x, 65, b, 'sujet', 's')
    arrow(ax, (x, 62), (44 + (i - 1) * 10, 50), 'varie')
text(ax, 44, 55, '', 'encre', 's')
text(ax, 18, 56, 'on les contrôle', 'varie', 's', ha='left')
box(ax, 14, 36, 60, 12, 'resultat', label=r'$(\mathbb{Z}, +)$ est un groupe', size='m')
arrow(ax, (44, 36), (44, 24), 'fixe')
text(ax, 44, 17, 'tout le reste s’en déduit', 'fixe', 'm')
save(fig, '44-104')
