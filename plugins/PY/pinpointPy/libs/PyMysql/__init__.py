# ------------------------------------------------------------------------------
#  Copyright  2020. NAVER Corp.                                                -
#                                                                              -
#  Licensed under the Apache License, Version 2.0 (the "License");             -
#  you may not use this file except in compliance with the License.            -
#  You may obtain a copy of the License at                                     -
#                                                                              -
#   http://www.apache.org/licenses/LICENSE-2.0                                 -
#                                                                              -
#  Unless required by applicable law or agreed to in writing, software         -
#  distributed under the License is distributed on an "AS IS" BASIS,           -
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    -
#  See the License for the specific language governing permissions and         -
#  limitations under the License.                                              -
# ------------------------------------------------------------------------------

from ...Interceptor import Interceptor,intercept_once

@intercept_once
def monkey_patch():
    try:
        import pymysql
        from pymysql.cursors import Cursor
        from .PyMysqlPlugin import PyMysqlPlugin


        Interceptors = [
            Interceptor(Cursor, 'execute', PyMysqlPlugin),
        ]
        for interceptor in Interceptors:
            interceptor.enable()


    except ImportError as e:
        # do nothing
        print(e)

__all__=['monkey_patch']