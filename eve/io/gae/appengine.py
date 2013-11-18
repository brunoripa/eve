from google.appengine.ext import ndb
from eve.io.base import DataLayer
from eve.io.base import AbstractModel


class GaeModel(object):
    
    def __init__(self, obj):
        self._fields = {}
        for k, v in obj._properties.iteritems():
            self._fields[k] = v

    def __setitem__(self, key, value):
        self._fields[key] = value


    def __getitem__(self, key):

        # We want the expection raised here, in case...
        return self._fields[key]


class GaeLayer(DataLayer):

    WRAPPER_CLASS = GaeModel

    def find(self, resource, req):
        
        result = []
        gql_query = 'select * from %s' % resource
        q = ndb.query(gql_query)
        
        # Improve this
        for item in q:
            result.append(self.WRAPPER_CLASS(item)) 

        return result
