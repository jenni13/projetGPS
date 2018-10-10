#! /usr/bin/python2
import webbrowser
long = 48.8589507
latt = 2.2770205
url = "http://maps.google.com/maps?q="+str(long)+","+str(latt)
chrome_path = '/usr/bin/google-chrome %s'
webbrowser.get(chrome_path).open(url)
