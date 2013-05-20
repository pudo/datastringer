import requests
from urlparse import urljoin
import os
import json


class DataStringerException(Exception):
    pass


class DataStringer(object):
    """ DataStringer allows users to easily submit data records
    (``frames``) to the datawi.re service via its REST API. """

    def __init__(self,
                 host='http://datawi.re',
                 api_key=None,
                 service=None,
                 event=None,
                 sync=False):
        self.host = host
        if api_key is None:
            api_key = os.environ.get('DATAWIRE_SECRET')
        self.api_key = api_key
        self.service = service
        self.event = event
        self.sync = sync

    def _put(self, path, data, params):
        if self.api_key is None:
            raise DataStringerException('No API key is configured.')
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'ApiKey %s' % self.api_key,
        }
        res = requests.put(urljoin(self.host, path),
                           data=json.dumps(data),
                           params=params,
                           headers=headers)
        data = res.json()
        if res.status_code != 200:
            message = '%(name)s: %(description)s' % data
            raise DataStringerException(message)
        return data

    def submit(self, frame, service=None, event=None, sync=None):
        service = service or self.service
        if service is None:
            raise DataStringerException('No service is configured.')
        event = event or self.event
        if event is None:
            raise DataStringerException('No event is configured.')
        sync = sync if sync is not None else self.sync
        path = '/api/1/frames/%s/%s' % (service, event)
        return self._put(path, frame, {'sync': sync})

    def __repr__(self):
        return '<DataStringer(%s,%s,%s)>' % (self.host,
                                             self.service,
                                             self.event)

if __name__ == '__main__':
    stringer = DataStringer(host='http://localhost:5000', api_key='shalalala')
    stringer.service = 'test'
    stringer.event = 'default'
    stringer.submit({'message': 'lala', 'value': 6})
