import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
rows = [(r'$x^4-4x^2+1$ annule $u$', 'sujet', 'départ'),
        (r'$\sqrt{3}=u^2-2\in\mathbb{Q}(u)$', 'fixe', ''),
        (r'$\sqrt{2}=2u/(1+\sqrt{3})\in\mathbb{Q}(u)$', 'varie', 'décisive'),
        (r'$\mathbb{Q}(u)=E$ : degré 4', 'resultat', 'arrivée')]
ys = [76, 56, 36, 16]
for y, (s, role, tag) in zip(ys, rows):
    box(ax, 4, y, 64, 12, role, label=s, size='s')
    if tag: text(ax, 70, y + 6, tag, role, 's', ha='left')
for y in ys[:-1]:
    arrow(ax, (36, y), (36, y - 8), 'fixe')
save(fig, '61-097')
