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
import os

from st2actions.runners.pythonrunner import Action

class DeleteConfigFile(Action):
        
    def run(self, filename):
        os.remove(filename)
        result = "Erased file %s " % filename
        return (True, result)

