import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 57, 'même test : peut-on compter les facteurs ?', 'fixe', 's')
brace(ax, 4, 21, 46, 'autre', label='test ordinaire', down=False, size='s')
brace(ax, 25, 84, 46, 'sujet', label='cas limites', down=False, size='s')
box(ax, 4, 32, 17, 10, 'autre', fill=False, label='7³', size='l')
for x0, lab in [(25, '7¹'), (46, '7⁰'), (67, '0⁵')]:
    box(ax, x0, 32, 17, 10, 'sujet', fill=False, label=lab, size='l')
for cx in [12.5, 33.5, 54.5, 75.5]:
    arrow(ax, (cx, 32), (cx, 25), 'varie')
for cx, lab, role in [(12.5, '343', 'resultat'), (33.5, '7', 'resultat'),
                      (54.5, 'aucune valeur', 'limite'), (75.5, '0', 'resultat')]:
    text(ax, cx, 21, lab, role, 'm')
for cx, lab, role in [(12.5, 'tient\n3 facteurs', 'resultat'), (33.5, 'tient\n1 facteur', 'resultat'),
                      (54.5, 'ne tient pas\n0 facteur', 'limite'), (75.5, 'tient\n5 facteurs', 'resultat')]:
    text(ax, cx, 11, lab, role, 's')
save(fig, '04-072')
