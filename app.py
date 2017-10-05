# o = open('output','a') #open for append
# for line in open('crupto.txt'):
#    line = line.replace('$' ,'newword')
#    o.write(line + '\n')
# o.close()
import re
from random import choice
import random
o = open('output','w')
pattern = re.compile('.*\n')
data = open('crupto.txt').read()



found = pattern.findall(data)
for w in found:                                                      # w возвращается строкой
    pass
    def rand_url():
        difflink = ['http://kimechanic.com/24zR','http://j.gs/916E','http://quamiller.com/5hi2','http://pintient.com/3EYz']     # рандомные ссылки для поста
        random.shuffle(difflink)
        random_number = random.choice(difflink)
        return random_number


    name = "Download link:'{}' \n".format(rand_url())
    p = "%s%s" % (w, name)
    print(str(p))
    o.write(p)
o.close()

exit()

