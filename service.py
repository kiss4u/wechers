# -*- coding: utf-8 -*-
import other
import face
import piccut
import film

serviceList = [face, piccut, film, other]

def getallService():
	fucService = '-----功能列表-----'
	i = 1;
	for service in serviceList:
		if service.show():
			fucService += '\n' + str(i) + ' : ' + service.getFunInfo()
			i = i + 1
	return fucService
