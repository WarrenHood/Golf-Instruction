from random import *
n = 1
while(n < 400):
    f = str(n)+'.html'
    file = open(f,'w')
    file.write('<!DOCTYPE html><html><body><center><h1>Test Page '+str(n)+'</h1></center>')
    for i in range(15):
        file.write('<center><h1>'+str(int(random()*10000000000000000000000000000000000000000000000000000000000000000000))+'</h2></center>')
    file.write('</body></html>')
    file.close()
    n += 1
