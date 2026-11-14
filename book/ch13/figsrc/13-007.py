import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, 'le même trait, deux rôles', 'encre', 'm')
for x, s, r in [(14, '3', 'sujet'), (22, '−', 'varie'), (30, '5', 'sujet')]:
    text(ax, x, 32, s, r, 'xl')
brace(ax, 10, 34, 26, 'varie', label='entre deux nombres', down=True)
text(ax, 22, 11, 'opération', 'varie', 'm')
text(ax, 62, 32, '−', 'sujet', 'xl'); text(ax, 70, 32, '2', 'sujet', 'xl')
brace(ax, 58, 74, 26, 'sujet', label='devant un seul nombre', down=True)
text(ax, 66, 11, 'partie du nombre', 'sujet', 'm')
line(ax, [(44, 8), (44, 40)], 'fixe', dash=True)
save(fig, '13-007')
