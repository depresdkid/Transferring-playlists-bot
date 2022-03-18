# TODO хочу так же сделать тут проверку, что можно было кидать свой id без ссылки, т.к. его легко получить и в
#  будующем валидацию что гворить пользовотелю что он даун не то кидает

# TODO ПОИСК ПЛЕЛИСТОВ ПО ПРОФИЛЮ
import users
from api import Api

api = Api()

a = api.getUserPlaylists(users.users[0])
b = api.getTracksFromPlaylist(a[0])

print("a")
