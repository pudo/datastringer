datastringer - datawi.re Python client
======================================

[datawi.re](http://datawi.re) is a stream monitoring service for data feeds.
It allows journalists, researchers and other users to keep track of data about 
topics, people and organisations that they are interested in. This Python
client library can be used to easily add user notifications to any scraper
or database client by sending feshly acquired data through datawi.re.

The library submits new data records (called ``frames``) to the service. To
submit records, a service profile must first be created on datawi.re so that 
frames can be rendered appropriately.


Usage
-----

To use the client, you need to specify at least an API key - this key is
visible on your datawi.re settings page:

    from datastringer import DataStringer

    stringer = DataStringer(api_key='<your api key>')

If no key is specified, ``datastringer`` will attempt to use the environment 
variable ``DATAWIRE_SECRET`` to access the API. 

After instantiation, the client can be used to submit frames like this:

    data = {'message': 'hello, world!'}
    stringer.submit(data, service='test', event='default')

Alternatively, both the service name and the event type can be set statically:

    stringer.service = 'test'
    stringer.event = 'default'
    stringer.submit(data)


Contact and registering a service
---------------------------------

At present, all services on [datawi.re](http://datawi.re) are curated by our
team. If you want to submit a feed, we're keen to first discuss the data
quality and reliabilty that you're able to provide so that we can be 
accountable to our users. Please contact us at: info@datawi.re.


License
-------

Copyright (c) 2013, Friedrich Lindenberg, Annabel Church

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
