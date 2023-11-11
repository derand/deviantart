"""
    deviantart.user
    ^^^^^^^^^^^^^^^
    
    Data model of the user object
    
    :copyright: (c) 2015 by Kevin Eichhorn
"""

class User(object):

    def __init__(self):
        self.userid = None
        self.username = None
        self.usericon = None
        self.usertype = None
        self.is_watching = None
        self.details = None
        self.geo = None
        self.profile = None
        self.stats = None
        self.collections = None
        self.galleries = None

    def from_dict(self, d):
        usr = d['user'] if 'user' in d and isinstance(d['user'], dict) else d

        self.userid = usr['userid']
        self.username = usr['username']
        self.usericon = usr['usericon']
        self.usertype = usr['type']
        
        if 'is_watching' in d:
            self.is_watching = d['is_watching']
            
        if 'details' in d:
            self.details = d['details']
            
        if 'geo' in d:
            self.geo = d['geo']
            
        if 'profile' in d:
            self.profile = d['profile']
            
        if 'stats' in d:
            self.stats = d['stats']

        if 'collections' in d:
            self.collections = d['collections']

        if 'galleries' in d:
            self.galleries = d['galleries']

    def __repr__(self):
        return self.username
