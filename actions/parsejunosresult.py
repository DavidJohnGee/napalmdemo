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

class ParseJunosResponse(Action):
        
    def run(self, response):

        if 'error' in response['raw']:
            processed = "Fail, " + str(response['raw']['error']) + str("%")

        if 'success' in response['raw']:
            processed = "Success, Packet Loss: " + str(response['raw']['success']['packet_loss']) + str("%")

        if processed:
            return (True, processed)
        return (False)
