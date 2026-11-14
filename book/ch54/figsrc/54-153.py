import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'$157=13\times12+1$', 'encre', 'm')
# 13 cases d'un « 12 » : le quotient compte les cases, puis 1 reste
s, gap = 4.6, 1.4
x0 = 2
for i in range(13):
    box(ax, x0 + i * (s + gap), 52, s, 9, 'sujet', r=0.4)
xr = x0 + 13 * (s + gap) + 1
box(ax, xr, 52, 3.6, 9, 'fixe', r=0.4)
brace(ax, x0, x0 + 13 * (s + gap) - gap, 50, 'sujet', label='13 fois 12 : le quotient', depth=1.6)
text(ax, xr + 1.8, 68, 'reste 1', 'fixe', 's', ha='right')
# polynômes
text(ax, 44, 33, r'$x^3-2x^2+4=q\,(x-1)+3$', 'encre', 'm')
box(ax, 18, 10, 38, 11, 'sujet', label=r'$q=x^2-x-1$')
text(ax, 37, 4, 'quotient : le polynôme qui multiplie', 'sujet', 's')
save(fig, '54-153')
