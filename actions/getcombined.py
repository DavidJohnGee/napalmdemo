# encoding: utf-8

"""
Copyright 2017 Brocade Communications Systems, Inc.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys

from st2actions.runners.pythonrunner import Action
from st2client.client import Client
from st2client.models import KeyValuePair

class GetNBGPPingAddresses(Action):
        
    def run(self):

        self.client = Client(base_url='http://localhost')
        
        queryresult1 = self.client.keys.query(prefix="NBGPPING")
        iplist = []

        queryresult2 = self.client.keys.query(prefix="NBGPDEV")
        nbgplist = []

        for key in queryresult1:
            _name = key.name
            _ip = _name.split(':')[1]
            iplist.append(_ip)

        for key in queryresult2:
            _name = key.name
            _nname = _name.split(':')[1]
            nbgplist.append(_nname)
         
        '''I can't see blue on Windows!. Now we will build a dict for every entry on every device.'''

        combinedlist = []
        for dev in nbgplist:
           for ip in iplist:
               combinedlist.append({'device': dev, 'ip': ip})


        if combinedlist:
            return (True, combinedlist)
        return (False)
