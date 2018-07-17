
def make_album(name,album_name,number=''):
      album = {'name':name,'album_name':album_name}
      return album
while True:
      print("(enter 'q' at any time to quit)")
      name = input('请输入歌手名：')
      if name == 'q':
            break
      album_name = input('请输入专辑名：')
      if album_name == 'q':
            break
      print(make_album(name,album_name))