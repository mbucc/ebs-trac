# Evidence-Based scheduling plugin for Trac.
# 
# Copyright (c) 2010, Mark Bucciarelli <mark@crosscutmedia.com>
# 
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# 

from trac.core import *
from trac.web.main import IRequestHandler

import ebstrac

class EBSComponent(Component):
	implements(IRequestHandler)

	def match_request(self, req):
		return req.path_info.startswith('/ebs/')

	def process_request(self, req):

		#self.log.debug("PATH_INFO: %s" % (req.path_info,))

		# /ebs/mark/tickets --> a[1]='ebs', a[2]='mark', ...
		# if trailing slash, len() == 5.
		a = req.path_info.split('/')
		if len(a) in (4,5) and a[3] == 'tickets':
			user = a[2]
			ebstrac.handlers.ticketget(self.env, req, user)
		else:
			ebstrac.handlers.error(req, "invalid url")