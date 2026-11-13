import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
bx, bw, bh = 20, 66, 11
rows = [(70, 'sujet', r'$x=4\cos t$   $y=4\sin t$', 't'),
        (50, 'sujet', r'$\cos t=x/4$   $\sin t=y/4$', 't'),
        (30, 'sujet', r'$(x/4)^2+(y/4)^2=1$', 'x'),
        (10, 'resultat', r'$x^2+y^2=16$', '')]
labs = ['isoler cos t et sin t', 'mettre dans cos² t + sin² t = 1', 'multiplier par 16']
for i, (y, role, lab, badge) in enumerate(rows):
    box(ax, bx, y, bw, bh, role, label=lab, size='m')
    if i < 3:
        arrow(ax, (bx + 14, y), (bx + 14, y - 9), 'varie')
        text(ax, bx + 18, y - 4.5, labs[i], 'varie', 's', ha='left')
for y in (70, 50):
    disc(ax, 9, y + bh / 2, 4, 'varie', label='t', size='m')
box(ax, 2, 10 + 0.5, 15, 10, 'resultat', label='sans t', size='s') if False else None
text(ax, 9, 10 + bh / 2, 'sans t', 'resultat', 's')
text(ax, 9, 30 + bh / 2, 'sans t', 'resultat', 's')
text(ax, 53, 4, 't = 60° : x = 2 ; y ≈ 3,46 ; 4 + 12 = 16', 'encre', 's') if False else None
text(ax, 32, 4, '60° : x = 2 ; y ≈ 3,46', 'encre', 's')
text(ax, 72, 4, '4 + 12 = 16', 'resultat', 's')
save(fig, '40-094')
