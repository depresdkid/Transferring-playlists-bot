
def getUserIdFromLink(user):
    return user.rpartition('/')[2].rpartition('?')[0]
