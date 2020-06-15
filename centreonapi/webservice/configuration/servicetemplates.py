# -*- coding: utf-8 -*-

from centreonapi.webservice import Webservice

class Servicetemplates(object):

    def __init__(self):
        """
        Constructor
        """
        self.webservice = Webservice.getInstance()

    def list(self):
        """
        Get service template list
        """
        return self.webservice.call_clapi('show', 'STPL')

