import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for x0, role, t in ((3, 'sujet', 'plan 1 : non dégénéré'), (47, 'limite', 'plan 2 : dégénéré')):
    box(ax, x0, 14, 38, 46, role, label=None)
    text(ax, x0 + 19, 55, t, role, 's')
# plan 1
o = (14, 30); s = 14
arrow(ax, o, (o[0] + s, o[1]), 'sujet', lw=1.4)
arrow(ax, o, (o[0] + s, o[1] + s), 'sujet', lw=1.4)
text(ax, o[0] + s + 1, o[1] - 2.5, r'$(1\ ;\ 0)$', 'sujet', 's', ha='left')
text(ax, o[0] + s - 1, o[1] + s + 3, r'$(1\ ;\ 1)$', 'sujet', 's', ha='left')
text(ax, 22, 42 + 0.0, '', 'sujet', 's')
# plan 2
o2 = (66, 20)
arrow(ax, o2, (o2[0], o2[1] + 26), 'limite', lw=1.6)
text(ax, o2[0] + 2, o2[1] + 24, r'$(0\ ;\ 1)$', 'limite', 's', ha='left')
text(ax, 22, 9, 'seul 0 est orthogonal à tout', 'sujet', 's')
text(ax, 66, 9, r'$(0\ ;\ 1)$ : orthogonal à tout', 'limite', 's')
text(ax, 22, 62.5, '', 'sujet', 's')
save(fig, '72-052')
