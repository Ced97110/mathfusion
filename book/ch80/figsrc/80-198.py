import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
heads = ['(0,0)', '(0,1)', '(1,0)', '(1,1)']
x0, cw = 24, 15
for i, h in enumerate(heads):
    box(ax, x0 + i * cw, 36, 12, 12, 'sujet', label=h, size='s')
    box(ax, x0 + i * cw, 20, 12, 12, 'fixe', dash=True, fill=False, label=h, size='s')
text(ax, 21, 42, 'dans', 'sujet', 's', ha='right')
text(ax, 21, 26, 'hors', 'fixe', 's', ha='right')
brace(ax, x0, x0 + 3 * cw + 12, 18, 'varie', '4 positions, 2 choix chacune', True, 's')
text(ax, 44, 4, r'$2\times2\times2\times2=16$', 'resultat', 'l')
save(fig, '80-198')
