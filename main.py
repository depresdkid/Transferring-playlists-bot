# TODO хочу так же сделать тут проверку, что можно было кидать свой id без ссылки, т.к. его легко получить и в
#  будующем валидацию что гворить пользовотелю что он даун не то кидает

# TODO ПОИСК ПЛЕЛИСТОВ ПО ПРОФИЛЮ
import users
from api import Api

api = Api()

for user in users.users:
    playlists = api.getUserPlaylists(user)
    userName = api.getUser(user)
    for pl in playlists:
        api.fillPlaylistWithTracks(pl)
        api.writeTracksInFile(userName, pl)
