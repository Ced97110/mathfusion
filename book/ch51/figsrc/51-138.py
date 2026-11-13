import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
specs = [(66, 'sujet', r'$n=ab$, $1<a<n$, $1<b<n$', 'départ'),
         (48, 'varie', r'$0=n1=(a1)(b1)$', 'étape clé'),
         (30, 'fixe', r'intègre : $a1=0$ ou $b1=0$', None),
         (12, 'limite', r'$a<n$ contredit $n$ minimal', 'arrivée')]
for i, (y, role, s, tag) in enumerate(specs):
    box(ax, 22, y, 64, 11, role, label=s)
    if tag: text(ax, 1, y + 5.5, tag, role, 's', ha='left')
    if i < 3: arrow(ax, (54, y), (54, y - 7), 'fixe')
save(fig, '51-138')
