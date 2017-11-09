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

class ParseCSRResult(Action):
        
    def run(self, response):

        stringified = response['raw_array']
        
        final = ""

        for key, value in stringified.iteritems():
            # self.logger.info("BGPPING: " + str(stringified[key][3]))
            final = stringified[key][3] 

        if "(0/5)" in final:
            return(True, "Fail, Packet Loss: 100%")
        if "(1/5)" in final:
            return(True, "Fail, Packet Loss: 80%")
        if "(2/5)" in final:
            return(True, "Fail, Packet Loss: 60%")
        if "(3/5)" in final:
            return(True, "Fail, Packet Loss: 40%")
        if "(4/5)" in final:
            return(True, "Success, Packet Loss: 20%")
        if "(5/5)" in final:
            return(True, "Success, Packet Loss: 0%")      

        return (False)
