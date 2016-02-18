import smtplib

fromaddr = 'jonsnow@gameofthrones.com'
toaddrs  = 'ankit.jaggi@live.in'
username = ""
password = ""
to_addrs = ["mohit@designbids.in", "agrwalmohit@gmail.com"]
test_addr = ["yo.ankit@gmail.com", "ankit.jaggi@live.in"]

for addr in to_addrs:
	name = addr[0:addr.find('@')]
	print name
	message = """From: Jon Snow <jonsnow@gameofthrones.com>
To: %s <%s>
MIME-Version: 1.0
Content-type: text/html
Subject: I'm alive!

<img width="30px" src='http://dabdfce6.ngrok.io/openmail?email=%s' alt="Tracker" />
<h1>I'm alive but I still know nothing.</h1>
<p>Come see me live on April 24, 2016</p>

""" % (name, addr, addr)
	print addr
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(username,password)
		server.sendmail(fromaddr, addr, message)
		server.quit()
		print "Mail Sent successfully"
	except:
		print "Error sending mail"





