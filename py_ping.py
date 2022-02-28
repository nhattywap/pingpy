import subprocess

def ping(start_ip, end_ip):
	ip1 = [int(num) for num in start_ip.split('.')]
	ip2 = [int(num) for num in end_ip.split('.')]

	if len(ip1) == len(ip2):
		ip_con = []
		ip_chan1 = []
		ip_chan2 = []

		for i in range(len(ip1)):
			if ip1[i] == ip2[i]:
				ip_con.append(ip1[i])

			else:
				ip_chan1.append(ip1[i])
				ip_chan2.append(ip2[i])

		for j in range(len(ip_chan1)):
			if ip_chan1[j] < ip_chan2[j]:
				continue
			else:
				raise AttributeError('start ip must be less than end ip')

		for k in range(len(ip_chan1)):
			ip_chan1.reverse()
			ip_chan2.reverse()

			ip_chan_copy = ip_chan1.copy()

			for l in range(ip_chan1[k], ip_chan2[k]):
				ip_chan_copy[k] = l
				ip_chan_copy.reverse()

				_ip = '.'.join([str(num) for num in ip_con + ip_chan_copy])
				
				response = subprocess.run('ping %s' %(_ip), capture_output=True, shell=True)
				
				_stdout = str(response.stdout).replace('\\r\\n', '').replace("\'", '').split(',')

				print(_ip)
				for out in _stdout[1:]:
					print(out)
				
#ping('192.168.1.1', '192.168.1.255')




