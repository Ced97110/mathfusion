import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(104)
H = 13
box(ax, 2, 88, 84, H, 'autre', label=r'$\dfrac{w}{\tan\alpha}+\dfrac{w}{\tan\beta}=AB$')
text(ax, 84, 94.5, '127,1 m', 'resultat', 's', ha='right', weight='bold')
box(ax, 2, 67, 84, H, 'fixe', label=r'$w\,\dfrac{\cos\alpha}{\sin\alpha}+w\,\dfrac{\cos\beta}{\sin\beta}=AB$')
box(ax, 2, 46, 84, H, 'fixe', label=r'$\dfrac{w\,(\cos\alpha\,\sin\beta+\cos\beta\,\sin\alpha)}{\sin\alpha\,\sin\beta}=AB$')
box(ax, 2, 23, 84, H, 'varie', label=r'$\dfrac{w\,\sin(\alpha+\beta)}{\sin\alpha\,\sin\beta}=AB$')
box(ax, 2, 2, 84, 13, 'sujet', label=r'$w=\dfrac{AB\,\sin\alpha\,\sin\beta}{\sin(\alpha+\beta)}$')
text(ax, 84, 8.5, '127,1 m', 'resultat', 's', ha='right', weight='bold')
for y0, y1, note in ((88, 80, 'tan = sin ÷ cos'), (67, 59, 'dénominateur commun'),
                     (46, 36, 'sin(α + β) = sin α cos β + cos α sin β'), (23, 15, 'on isole w')):
    arrow(ax, (9, y0), (9, y1 + 0.3), 'varie')
    if y0 == 46:
        box(ax, 15, 37.2, 71, 7.6, 'varie', label=note, size='s', weight='bold')
    else:
        text(ax, 14, (y0 + y1) / 2, note, 'varie', 's', ha='left')
save(fig, '38-068')
