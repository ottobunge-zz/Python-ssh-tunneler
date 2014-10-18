Python-ssh-tunneler
===================

Little script to create, detect and kill local ssh tunnels

Setup:
======

create an object with:

*localport (port tunneling from, local side)

*remoteport (port tunneling to, server side)

*sshport (port ssh is runnin on, server machine, defaul = 22)

*host (remote host)

*user (user on remote host)

*idfile (private key user uses to id in remote host)

*host2 (this can be localhost, and the tunel will give you localhost on the remotehost)

Available functions:
====================

*makeTunnel(), creates desired tunnel, returns tunnel process id, or false, depending on success of creation

*checkTunnel(), returns tunnel process id, or false, depending if tunnel exists or not

*killTunnel(), kills current tunnel, returns tunnel process id, or false, depending on success of deletion

*checkOpenPort(): Checks if local port is being used or not, returns True or False, if used or not

both killtunnel and maketunnel check first before making the tunnel

example: ssh = Tunnel(localport,remoteport,sshport,host,user,idfile)
