import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 62, 'nombre de 1 pair', 'resultat', 's')
text(ax, 66, 62, 'nombre de 1 impair', 'limite', 's')
for X0, role, a, b, s in [(4, 'resultat', '011', '101', '110'), (48, 'limite', '001', '010', '011')]:
    box(ax, X0, 14, 38, 44, role, fill=False, dash=True)
    box(ax, X0 + 3, 43, 14, 9, 'sujet', label=a)
    box(ax, X0 + 21, 43, 14, 9, 'sujet', label=b)
    arrow(ax, (X0 + 10, 43), (X0 + 15, 31), 'varie')
    arrow(ax, (X0 + 28, 43), (X0 + 23, 31), 'varie')
    box(ax, X0 + 12, 21, 14, 9, role, label=s)
text(ax, 22, 6, r'$H(x+y)=Hx+Hy=0$', 'resultat', 's')
text(ax, 66, 6, '$x+y$ n’est pas solution', 'limite', 's')
save(fig, '68-111')
