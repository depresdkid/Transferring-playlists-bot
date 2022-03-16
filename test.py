def GetUserFromLink(link):
    return link.rpartition('/')[2].rpartition('?')[0]

print(GetUserFromLink('https://open.spotify.com/track/0KeFtMjfct36OSXzOU4wYK?si=kobu9gkRTiSwuxkbdcTDLw&utm_source=copy-link'))