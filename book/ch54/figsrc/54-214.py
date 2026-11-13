import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'racine de $x^3-2x^2+4$ : où chercher ?', 'sujet', 'm')
# top line: all the fractions between -4 and 4, step 1/8 (the integers are left out)
text(ax, 44, 57, 'des fractions : une infinité', 'varie', 'm')
f = numberline(ax, 8, 76, 46, -4, 4, step=1, labels=False, size='s')
for k in range(-32, 33):
    if k % 8: disc(ax, f(k / 8), 46, 0.5, 'varie')
text(ax, 83.5, 49.5, '…', 'varie', 'm')
# bottom line: integers only, the divisors of 4 are highlighted
text(ax, 44, 30, 'des entiers : quelques-uns', 'sujet', 'm')
g = numberline(ax, 8, 76, 18, -4, 4, step=1, size='s')
for v in (-4, -2, -1, 1, 2, 4):
    disc(ax, g(v), 18, 1.5, 'sujet')
text(ax, 44, 4, r'ceux qui divisent 4 : $\pm1,\pm2,\pm4$', 'sujet', 's')
save(fig, '54-214')
