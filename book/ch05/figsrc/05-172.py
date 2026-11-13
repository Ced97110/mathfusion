import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
for i,v in enumerate(['3','5','17','257','65 537']):
    box(ax,2+i*17,46,15,9,'resultat',label=v,size='s')
brace(ax,2,85,46,'resultat','n = 0 à 4 : tous premiers')
arrow(ax,(44,37),(44,29),'limite')
box(ax,2,16,84,12,'limite',label='n = 5 : 4 294 967 297',size='m')
text(ax,44,9,r'$=641\times6\,700\,417$ : composé','limite','s')
save(fig,'05-172')
