import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
sq, gap, x0 = 3.0, 0.7, 5.0
def row(y, ngrey):
    box(ax, x0, y, sq, sq, 'sujet', r=0.3)
    for i in range(ngrey):
        box(ax, x0 + (i + 1) * (sq + gap), y, sq, sq, 'fixe', r=0.3)
text(ax, 6, 63, 'dans le carré de 0 à 12 :', 'encre', 's', ha='left')
text(ax, 6, 58, r'169 croisements : 10 points de K', 'encre', 's', ha='left')
text(ax, 6, 53, r'$169:10\approx17$ gris pour 1 bleu', 'encre', 's', ha='left')
row(46, 17)
text(ax, 6, 37, 'en moyenne : 20 gris pour 1 bleu', 'encre', 's', ha='left')
row(30, 20)
text(ax, 6, 21, 'un carré bleu = un point de K ; gris = les autres', 'fixe', 's', ha='left')
box(ax, 8, 3, 72, 11, 'sujet', label=r'$20=|$déterminant$|=$ aire du parallélogramme', size='s')
save(fig, '59-017')
