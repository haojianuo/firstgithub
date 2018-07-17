magicians = ['ergou','qiqi','shitou']
great_magicians = []
def make_great(magicians,great_magicians):
      while magicians:
            magician = magicians.pop()
            great_magician = 'the Great ' + magician 
            great_magicians.append(great_magician)

def show_magicianslis(great_magicians):
      for name in great_magicians:
            print(name)

make_great(magicians,great_magicians)
show_magicianslis(great_magicians)