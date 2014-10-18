import commands, os, time
class Tunnel:
	def __init__(self, localport, remoteport, sshport, host, user, host2,idfile):
		self.localport = localport
		self.remoteport = remoteport
		self.sshport = sshport
		self.host = host
		self.user = user
		self.idfile = idfile
		self.host2 = host2
		self.command = 'ssh -f ' + self.user+'@'+self.host + ' -L ' + self.localport + ':' + self.host2 + ':' + self.remoteport + ' -N -p ' + self.sshport + ' -i ' + self.idfile
	def checkOpenPort(self):
		portcheck = 'netstat -a | grep :' + self.localport
		portcheckout = commands.getoutput(portcheck)
		if self.localport in portcheckout:
			return True
		else:
			return False

	def checkTunnel(self):
		isAlive = commands.getoutput('ps aux')
		if self.checkOpenPort() and self.command.replace(self.idfile,'') not in isAlive:
			print 'Port ', self.localport, ' already in use, please use another one!'
			return True
		else:		
			if self.command.replace(self.idfile,'') in isAlive:
				self.tunnelid = commands.getoutput("ps aux |  grep \"" + self.command.replace(self.idfile,'') + "\" | awk '{print $2}' |head -1")
				return self.tunnelid
			else:
				return False
		
	def makeTunnel(self):
		self.check = self.checkTunnel()
		if self.check:
			if self.check == True:
				return False
			else:
				print 'Tunnel Already exists! with process id:', self.check
				return False	
		else:
			os.system(self.command)
			if self.checkTunnel():
				return True
			else:
				return False

	def killTunnel(self):
		if self.checkTunnel():
			os.system('kill -9 ' + self.tunnelid)
			if self.checkTunnel():
				return False				
			else:
				return True
		else:
			return False


