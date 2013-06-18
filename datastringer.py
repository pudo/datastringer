import requests
from requests.exceptions import RequestException
from datetime import datetime
from urlparse import urljoin
import os
import json

DEFAULT_HOST = os.environ.get('DATAWIRE_HOST', 'http://api.datawi.re')
DEFAULT_KEY = os.environ.get('DATAWIRE_SECRET')


class DataStringerException(Exception):
    pass


class DataStringer(object):
    """ DataStringer allows users to easily submit data records
    (``frames``) to the datawi.re service via its REST API. """

    def __init__(self,
                 host=None,
                 api_key=None,
                 service=None,
                 event=None,
                 sync=False):
        self.host = host or DEFAULT_HOST
        self.api_key = api_key or DEFAULT_KEY
        self.service = service
        self.event = event
        self.sync = sync

    def _put(self, path, data, params, headers=None):
        if self.api_key is None:
            raise DataStringerException('No API key is configured.')
        _headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'ApiKey %s' % self.api_key,
        }
        if headers is not None:
            _headers.update(headers)
        try:
            res = requests.put(urljoin(self.host, path),
                               data=json.dumps(data),
                               params=params,
                               headers=_headers)
            data = res.json()
        except RequestException, ex:
            raise DataStringerException(unicode(ex))
        if res.status_code != 200:
            message = '%(name)s: %(description)s' % data
            raise DataStringerException(message)
        return data

    def submit(self, frame, service=None, event=None, sync=None,
               action_at=None, source_url=None, details_url=None):
        service = service or self.service
        if service is None:
            raise DataStringerException('No service is configured.')
        event = event or self.event
        if event is None:
            raise DataStringerException('No event is configured.')
        sync = sync if sync is not None else self.sync

        headers = {
            'X-Source-Location': source_url.encode('utf-8'),
            'X-Details-Location': details_url.encode('utf-8')
        }
        if action_at is not None:
            if isinstance(action_at, datetime):
                action_at = action_at.isoformat()
            headers['X-Action-Time'] = action_at

        path = '/api/1/frames/%s/%s' % (service, event)
        return self._put(path, frame, {'sync': sync}, headers=headers)

    def __repr__(self):
        return '<DataStringer(%s,%s,%s)>' % (self.host,
                                             self.service,
                                             self.event)

if __name__ == '__main__':
    stringer = DataStringer(host='http://localhost:5000', api_key='shalalala')
    stringer.service = 'test'
    stringer.event = 'default'
    stringer.submit({'message': 'lala', 'value': 6})
