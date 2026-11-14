import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
vals = ['+30', '−15', '−10', '−6', '+5', '+3', '+2', '−1']
bw, gap, x0, y = 8.6, 1.0, 6, 44
for i, v in enumerate(vals):
    box(ax, x0 + i * (bw + gap), y, bw, 10, 'sujet' if v[0] == '+' else 'varie', label=v, size='s')
def span(a, b, s):
    xa = x0 + a * (bw + gap); xb = x0 + b * (bw + gap) - gap
    brace(ax, xa, xb, y, 'fixe', label=s, down=True)
span(0, 1, r'$|U|=0$'); span(1, 4, r'$|U|=1$'); span(4, 7, r'$|U|=2$'); span(7, 8, r'$|U|=3$')
text(ax, 44, 63, r'signe $(-1)^{|U|}$ fois $g(U)$', 'fixe', 's')
arrow(ax, (44, 31), (44, 24), 'varie')
box(ax, 22, 8, 44, 14, 'resultat', label=r'$f(\emptyset)=8$', size='l')
save(fig, '80-368')
