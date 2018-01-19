import os, mimetypes, sys
import email.parser
import email.header
import email.utils
from email.message import Message
from .mailTool import MailTool

class MailParser(MailTool):
	'''
	methods for parsing message text, attachments
	'''

	def walkNamedParts(self, message):
		'''
		walk the message object using message.walk()
		filter the 'multipart' and 'message/rfc822' type
		otherwise invoke the self.partName() to get the Designed filename
		and the ContentType
		finally yield the (filename, ContentType, messagePart)
		'''
		for (ix, part) in enumerate(message.walk()):
			fulltype = part.get_content_type()
			maintype = part.get_content_maintype()
			if maintype == 'multipart':
				continue
			elif fulltype == 'message/rfc822':
				continue
			else:
				filename, conType = self.partName(part, ix)
				yield (filename, conType, part)

	def partName(self, part, ix):
		'''
		get filename and contentType of this part of message
		filename: 1) get from the part.get_filename()
				  2) if 1) failed get from part.get_param('name')
				  3) else contentType gusses the mimetype 
				     and return the part-ddd.xxx
		contentType: get from the part.get_content_type()
		'''
		filename = part.get_filename()
		conType = part.get_content_type()
		if not filename:
			filename = part.get_param('name')
		if not filename:
			if conType = 'text/plain':
				ext = '.txt'
			else:
				ext = mimetypes.guess_extension(conType)
				if not ext:
					ext = '.bin'
			filename = 'part-%03d%s',(ix, ext)
		return (filename, conType)

	def saveParts(self, savedir, message):
		'''
		using the self.wakNameParts(self, message) to get all the  
		parts info of the message
		then save the parts and return partfiles
		'''
		if not os.path.exists(savedir):
			os.mkdir(savedir)
		partfiles = []
		for (filename, conType, part) in self.walkNamedParts(message):
			fullname = os.path.join(savedir, filename)
			fileObj = open(fullname, 'wb')
			content = part.get_payload(decode=True)
			if not isinstance(content, bytes):
				content = b'(no content)'
			fileObj.write(content)
			fileObj.close()
			partfiles.append((conType, fullname))
		return partfiles

	def saveOnePart(self, savedir, partname, message):
		'''
		to find and save one part of the message
		'''
		if not os.path.exists(savedir):
			os.mkdir(savedir)
		fullname = os.path.join(savedir, partname)
		(conType, content) = self.findOnePart(partname, message)
		if not isinstance(content, bytes):
			content = b'(no content)'
		open(fullname, 'wb').write(content)
		return (conType, fullname)

	def partsList(self, message):
		'''
		return the filenames list of the part in the message
		'''
		validParts = self.walkNamedParts(message)
		return [filename for (filename,conType,part) in validParts]

	def findOnePart(self, partname, message):
		'''
		find the part's contentType and content given the partname
		intend to be used in conjunction with the partsList
		'''
		for (filename, conType, part) in self.walkNamedParts(message):
			if filename == partname:
				content = part.get_payload(decode=True)
				return (conType, content)
		raise KeyError('Part %s Not found in message')

	def decodePayload(self, part, toStr=True):
		'''
		decode the part payload using part.get_payload(decode=1)
		if toStr is True then decode the payload to Unicode String
		'''
		payload = part.get_payload(decode=True)
		if toStr:
			charTries = []
			enchdr = part.get_content_charset()
			if enchdr:
				charTries += [enchdr]
			charTries += [sys.getdefaultencoding(), 'utf8','latin1','gbk']
			for charset in charTries:
				try:
					payload = payload.decode(charset)
					break
				except (UnicodeError, LookupError):
					pass
			else:
				payload = '--Sorry: cannot decode Unicode text--'
		return payload

	def findMainText(self, message, toStr=True):
		'''
		find the main text of the message
		text/plain first
		text/html second
		text/* third
		then failed 
		'''
		for part in message.walk():
			conType = part.get_content_type()
			if conType == 'text/plain':
				return conType, self.decodePayload(part, toStr)

		for part in message.walk():
			conType = part.get_content_type()
			if conType == 'text/html':
				return conType, self.decodePayload(part, toStr)

		for part in message.walk():
			conType = part.get_content_maintype()
			if conType == 'text':
				return part.get_content_type(), self.decodePayload(part, toStr)
		#could not find text part in the message
		failtext = '[No text to display]' if toStr else b'[No text to display]'
		return 'text/plain', failtext
		
	def decodeHeader(self, rawHeader):
		try:
			parts = email.header.decode_header(rawHeader)
			decoded = []
			for (part, enc) in parts:
				if enc is None:
					if not isinstance(part, bytes):
						decoded += [part]
					else:
						decoded += [part.decode('raw-unicode-escape')
				else:
					decoded += [part.decode(enc)]
			return ' '.join(decoded)
		except:
			return rawHeader

	def decodeAddrHeader(self, rawHeader):
		try:
			pairs = email.utils.getaddresses([rawHeader])
			decoded = []
			for (name, addr) in pairs:
				try:
					name = self.decodeHeader(name)
				except:
					name = None
				joined = email.utils.formataddr((name, addr))
				decoded.append(joined)
			return ', '.join(decoded)
		except:
			return self.decodeHeader(rawHeader)

	def splitAddresses(self, field):
		try:
			pairs = email.utils.getaddress([field])
			return [email.utils.formataddr(pair) for pair in pairs]
		except:
			return ''

	
	#the error message for returning when parsed fail
	errorMessage = Message()
	errorMessage.set_payload('[Unable to parse message - format error]')

	def parseHeader(self, fulltext):
		try:
			return email.parser.Parser().parsestr(fulltext)
		except:
			return self.errorMessage

	def parseMessage(self, fulltext):
		try:
			return email.parser.Parser().parsestr(fulltext)
		except:
			return self.errorMessage

	def parseMessageRaw(self, fulltext):
		try:
			return email.parser.HeaderParser().parsestr(fulltext)
		except:
			return self.errorMessage
