import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
rows=[('1  regarder','4 912 + 3 087','sujet'),('2  remplacer','4 900 + 3 100','varie'),('3  calculer','4 900 + 3 100 = 8 000','varie'),('4  écrire avec ≈','4 912 + 3 087 ≈ 8 000','resultat')]
for i,(a,b,r) in enumerate(rows):
    y=64-i*14
    box(ax,2,y,30,9,r,label=a,size='s'); box(ax,36,y,50,9,r,label=b)
    arrow(ax,(17,y),(17,y-5),'fixe')
box(ax,2,4,30,11,'limite',label='jamais  =',size='s'); box(ax,36,4,50,11,'limite',label='4 912 + 3 087 = 8 000\nfaux : la somme est 7 999',size='s')
save(fig,'10-037')
