# -*- coding: utf-8 -*-
# Version Leapro_Bypass_Alphat_Lovers v.3.a#
#thanks to Allah S.w.t,
#thanks to all family: Alphat Lovers,pasukan panci,"LIAR TEAM PROTECTOR"
#tanpa all family saya bukanlah apa".
#thanks to : Virlis (Lea Liar)<=>Tirta (Liar)<=>Arjun (kang ange)
#Gunakanlah dengan bijak,jangan sombong,ataupun songong setelah bisa.
#----ingat----diatas langit masih ada langit----#
"""じєαᴘʀᴏ ᴠ.3.ᴀ"""
from line import *
from datetime import datetime, timedelta
from time import sleep
from threading import Thread
from multiprocessing import Pool,Process
from urllib.parse import urlencode
from shutil import copyfile
import subprocess as cmd
import platform
import requests, json
import LineService, Menu, time, signal, livejson, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, urllib, urllib.parse, atexit, asyncio, traceback
from Naked.toolshed.shell import execute_js 
from random import randint

""" strat """

with open('tokenJs.json', 'r') as bolo:
     pin = json.load(bolo)
cl = LINE(pin['token'],appName='CHANNELCP\t2.9.1\tAndroid OS\t5.1.1')
pin['token'] = cl.authToken
ka = LINE(pin['token2'],appName='CHANNELCP\t2.9.1\tAndroid OS\t5.1.1')
pin['token2'] = ka.authToken
kb = LINE(pin['token3'],appName='CHANNELCP\t2.9.1\tAndroid OS\t5.1.1')
pin['token3'] = kb.authToken
kc = LINE(pin['token4'],appName='CHANNELCP\t2.9.1\tAndroid OS\t5.1.1')
pin['token4'] = kc.authToken
kd = LINE(pin['token5'],appName='CHANNELCP\t2.9.1\tAndroid OS\t5.1.1')
pin['token5'] = kd.authToken
ke = LINE(pin['token6'],appName='CHANNELCP\t2.9.1\tAndroid OS\t5.1.1')
pin['token6'] = ke.authToken
kf = LINE(pin['token7'],appName='CHANNELCP\t2.9.1\tAndroid OS\t5.1.1')
pin['token7'] = kf.authToken
k1 = LINE(pin['token8'],appName='CHANNELCP\t2.9.1\tAndroid OS\t5.1.1')
pin['token8'] = k1.authToken

print ("\nじєαᴘʀᴏ ᴠ.3.ᴀ Succes Run ")

linePoll = OEPoll(cl)

Amin = [ka,kb,kc,kd,ke,kf]
mid = cl.getProfile().mid
Amid = ka.getProfile().mid
Bmid = kb.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Fmid = kf.getProfile().mid
Smid = k1.getProfile().mid

Zie=["u449da14db2551208d9a80ef00a91c2df"]

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid]
Ajs=[Smid]
Lea = Bots+Zie+Ajs
botlist=[ka,kb,kc,kd,ke,kf]

mulai   = time.time()

LeaZie = livejson.File('settSB.json')
wait = {"blacklist":{},"Member":[]}
cctv = {"cyduk":{},"point":{},"sidermem":{}}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def Rchat(self,to):
    self.removeAllMessages(op.param2)
    self.sendMessage(to,"ˢᵉᵐᵘᵃ ᵖᵉˢᵃⁿ ᵗᵉˡᵃʰ ᵈⁱʰᵃᵖᵘˢ•✓")

def Res(self,to):
    self.sendMessage(to,"ˢⁱᵃᵖ ᵐᵉⁿᵉʳⁱᵐᵃ ᵖᵉʳⁱⁿᵗᵃʰ ᵇᵒˢˢᵠᵘʰ")

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d D %02d H %02d M %02d S' % (days, hours, mins, secs)

def restartProgram():
	print ('##----- RUNNING BOT RESTARTED -----##')
	python = sys.executable
	os.execl(python, python, *sys.argv)

def command(text):
    pesan = text.lower()
    if pesan.startswith(LeaZie["keyCmd"]):
        cmd = pesan.replace(LeaZie["keyCmd"],"")
    else:
        cmd = "command"
    return cmd

def bot(op):
      try:
          global time
          global ast
          global groupParam
          global multiprocessing
          global subprocess
          global threading
          if op.type == 11:
            if op.param1 in LeaZie["proqr"]:
                if op.param2 in Lea or op.param2 in LeaZie["Bots"] or op.param2 in LeaZie["admin"]:pass
                else:
                    Z = cl.getCompactGroup(op.param1)
                    if Z.preventedJoinByTicket == False:
                        Z.preventedJoinByTicket = True
                        random.choice(Amin).updateGroup(Z)
                        random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                    else:
                        random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
  
            if op.param2 in wait["blacklist"]:
                G = cl.getCompactGroup(op.param1)
                if G.preventedJoinByTicket == False:
                    G.preventedJoinByTicket = True
                    random.choice(Amin).updateGroup(G)
                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                else:
                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])

          if op.type == 15:
            if op.param2 in Ajs:
                try:
                    random.choice(Amin).inviteIntoGroup(op.param1,Ajs)
                except:
                    try:
                        cl.inviteIntoGroup(op.param1,Ajs)
                    except:
                        pass
          if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                else:pass

          if op.type == 32:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                else:pass

          if op.type == 32:
            if op.param3 in Lea or op.param3 in LeaZie["admin"] or op.param3 in LeaZie["Bots"]:
                if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            pass
                else:pass

          if op.type == 19:
            if Amid in op.param3:
                if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        ka.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            ka.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kd.inviteIntoGroup(op.param1,[op.param3])
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                ka.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ke.nviteIntoGroup(op.param1,[op.param3])
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                        ka.acceptGroupInvitation(op.param1)
                                    except:pass
                else:pass
                return

            if Bmid in op.param3:
                if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kb.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kb.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                kb.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ka.inviteIntoGroup(op.param1,[op.param3])
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    kb.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)
                                    except:pass
                else:pass
                return

            if Cmid in op.param3:
                if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ka.kickoutFromGroup(op.param1,[op.param2])
                                ka.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:pass
                else:pass
                return

            if Dmid in op.param3:
                if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kd.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                            kd.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                kd.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kd.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                        kd.acceptGroupInvitation(op.param1)
                                    except:pass
                else:pass
                return

            if Emid in op.param3:
                if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                    ke.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)
                                    except:pass
                else:pass
                return

            if Fmid in op.param3:
                if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                        kf.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            kf.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kf.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                    kf.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        kf.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.acceptGroupInvitation(op.param1)
                                        except:pass
                else:pass
                return

            if mid in op.param3:
                if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:pass
                    try:
                        k1.acceptGroupInvitation(op.param1)
                        k1.findAndAddContactsByMid(op.param3)
                        k1.inviteIntoGroup(op.param1,[mid])
                        cl.acceptGroupInvitation(op.param1)
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = False
                        cl.updateGroup(X)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.leaveGroup(op.param1)
                    except:
                        pass
                else:pass
                return
            if Smid in op.param3:
                if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                        except:pass
                else:pass
                return
            if op.type == 19:
                if op.param3 in Zie:
                    if op.param2 not in Lea:
                        wait["blacklist"][op.param2] = True
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.findAndAddContactsByMid(op.param3)
                            ka.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.findAndAddContactsByMid(op.param3)
                                kb.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.findAndAddContactsByMid(op.param3)
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.findAndAddContactsByMid(op.param3)
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                                kf.findAndAddContactsByMid(op.param3)
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                pass
                        try:
                            k1.acceptGroupInvitation(op.param1)
                            k1.findAndAddContactsByMid(op.param3)
                            k1.inviteIntoGroup(op.param1,[op.param3])
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = False
                            cl.updateGroup(X)
                            Ticket = cl.reissueGroupTicket(op.param1)
                            ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k1.leaveGroup(op.param1)
                        except:
                            pass
                    else:pass
                    return

                if op.param3 in LeaZie["Bots"]:
                    if op.param2 not in Lea or op.param2 not in LeaZie["Bots"] or op.param2 not in LeaZie["admin"]:
                        wait["blacklist"][op.param2] = True
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                pass
                    else:pass
                    return

                if op.param3 in LeaZie["admin"]:
                    if op.param2 not in Lea or op.param2 not in LeaZie["Bots"] or op.param2 not in LeaZie["admin"]:
                        wait["blacklist"][op.param2] = True
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.findAndAddContactsByMid(op.param3)
                            ka.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.findAndAddContactsByMid(op.param3)
                                kb.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.findAndAddContactsByMid(op.param3)
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.findAndAddContactsByMid(op.param3)
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                                kf.findAndAddContactsByMid(op.param3)
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                pass
                    else:pass
                    return

          if op.type == 0:
              return

          if op.type == 5:
            if LeaZie["autoAdd"] == True:
                if op.param2 not in Lea:
                    cl.findAndAddContactsByMid(op.param1)
                    if (LeaZie["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, LeaZie["message"])

          if op.type == 11:
            if op.param1 in LeaZie["intaPoint"]:
                if op.param2 in Lea and op.param2 in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                    pass
                else:
                    X = cl.getGroup(op.param1)
                    if X.preventedJoinByTicket == True:
                        pass
                    else:
                        cl.updateGroup(X)
                        invsend = 0
                        Ti = cl.reissueGroupTicket(op.param1)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)
                        kb.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
                        kf.acceptGroupInvitationByTicket(op.param1,Ti)

          if op.type == 13:
            if mid in op.param3:
                if LeaZie["autoJoin"] == True:
                    if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                        cl.acceptGroupInvitation(op.param1)
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        if LeaZie["bypas"] == True:
                            cl.inviteIntoGroup(op.param1,Bots)
                            ka.acceptGroupInvitation(op.param1)
                            kb.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            kd.acceptGroupInvitation(op.param1)
                            ke.acceptGroupInvitation(op.param1)
                            kf.acceptGroupInvitation(op.param1)
                            ran=[ka,kb,kc,kd,ke,kf,cl]
                            dex=random.choice(ran)
                            x = cl.getGroup(op.param1)
                            if x.invitee == None:nama = []
                            else:nama = [contact.mid for contact in x.invitee]
                            target = []
                            for a in nama:
                              if a not in Lea:
                                  target.append(a)
                            cmd = 'bypass.js gid={} token={}'.format(op.param1, dek.authToken)
                            nami = [contact.mid for contact in x.members]
                            tarsih = []
                            for s in nami:
                              if s not in Lea:
                                  tarsih.append(s)
                            for y in target:
                                cmd += ' uid={}'.format(y)
                            for k in tarsih:
                                cmd += ' uid={}'.format(k)
                            success = execute_js(cmd)
                            
            if Amid in op.param3:
                if LeaZie["autoJoin"] == True:
                    if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                        ka.acceptGroupInvitation(op.param1)
                        ka.leaveGroup(op.param1)
                    else:
                        ka.acceptGroupInvitation(op.param1)
            if Bmid in op.param3:
                if LeaZie["autoJoin"] == True:
                    if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                        kb.acceptGroupInvitation(op.param1)
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
            if Cmid in op.param3:
                if LeaZie["autoJoin"] == True:
                    if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                        kc.acceptGroupInvitation(op.param1)
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
            if Dmid in op.param3:
                if LeaZie["autoJoin"] == True:
                    if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                        kd.acceptGroupInvitation(op.param1)
                        kd.leaveGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
            if Emid in op.param3:
                if LeaZie["autoJoin"] == True:
                    if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                        ke.acceptGroupInvitation(op.param1)
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
            if Fmid in op.param3:
                if LeaZie["autoJoin"] == True:
                    if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                        kf.acceptGroupInvitation(op.param1)
                        kf.leaveGroup(op.param1)
                    else:
                        kf.acceptGroupInvitation(op.param1)
            if Smid in op.param3:
                if LeaZie["bypas"] == True:
                    if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                        k1.acceptGroupInvitation(op.param1)
                        k1.leaveGroup(op.param1)
                    else:
                        k1.acceptGroupInvitation(op.param1)
                        x = k1.getGroup(op.param1)
                        if x.invitee == None:nama = []
                        else:nama = [contact.mid for contact in x.invitee]
                        target = []
                        for a in nama:
                          if a not in Lea:
                              target.append(a)
                        cmd = 'bypass.js gid={} token={}'.format(op.param1, k1.authToken)
                        nami = [contact.mid for contact in x.members]
                        tarsih = []
                        for s in nami:
                          if s not in Lea:
                              tarsih.append(s)
                        for y in target:
                            cmd += ' uid={}'.format(y)
                        for k in tarsih:
                            cmd += ' uid={}'.format(k)
                        success = execute_js(cmd)
                        k1.leaveGroup(op.param1)
          if op.type == 13:
            if op.param1 in LeaZie["proInvite"]:
                if op.param2 in Lea or op.param2 in LeaZie["Bots"] or op.param2 in LeaZie["admin"]:
                    pass
                else:
                    try:
                        if op.param3 in Lea or op.param3 in LeaZie["Bots"] or op.param3 in LeaZie["admin"]:
                            pass
                        else:
                            if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                                wait["blacklist"][op.param2] = True
                                anu = cl.getCompactGroup(op.param1)
                                if anu.invitee is not None:
                                    pipo = [a.mid for a in anu.invitee]
                                    for target in pipo:
                                      if target in op.param3 and target not in Lea and target not in LeaZie["Bots"] and target not in LeaZie["admin"]:
                                        wait["blacklist"][target] = True
                                        random.choice(botlist).cancelGroupInvitation(op.param1,[target])
                                        random.choice(botlist).kickoutFromGroup(op.param1,[target])
                                    random.choice(botlist).kickoutFromGroup(op.param1,[op.param2])
                            else:pass
                    except:
                        pass
            else:
                if op.param3 in Lea or op.param3 in LeaZie["Bots"] or op.param3 in LeaZie["admin"]:pass
                else:
                    Kacang = op.param3.split('\x1e')
                    for i in Kacang:
                      if i in wait["blacklist"]:
                        try:
                            kb.cancelGroupInvitation(op.param1,[i])
                        except:
                            try:
                                kc.cancelGroupInvitation(op.param1,[i])
                            except:
                                try:
                                    kd.cancelGroupInvitation(op.param1,[i])
                                except:
                                    try:
                                        ke.cancelGroupInvitation(op.param1,[i])
                                    except:
                                        try:
                                            kf.cancelGroupInvitation(op.param1,[i])
                                        except:
                                            try:
                                                ka.cancelGroupInvitation(op.param1,[i])
                                            except:pass
                        try:
                            if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                                wait["blacklist"][op.param2] = True
                                for i in botlist:
                                    i.kickoutFromGroup(op.param1,[op.param2])
                        except:pass
                if op.param2 not in wait["blacklist"]:pass
                else:
                    Kacang = op.param3.split('\x1e')
                    for i in Kacang:
                        wait["blacklist"][i] = True
                        try:
                            kb.cancelGroupInvitation(op.param1,[i])
                        except:
                            try:
                                kc.cancelGroupInvitation(op.param1,[i])
                            except:
                                try:
                                    kd.cancelGroupInvitation(op.param1,[i])
                                except:
                                    try:
                                        ke.cancelGroupInvitation(op.param1,[i])
                                    except:
                                        try:
                                            kf.cancelGroupInvitation(op.param1,[i])
                                        except:
                                            try:
                                                ka.cancelGroupInvitation(op.param1,[i])
                                            except:pass
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ka.kickoutFromGroup(op.param1,[op.param2])
                                            except:pass

          if op.type == 15:
            if op.param1 in LeaZie["leaveMsg"]:
                if op.param2 not in Lea and op.param2 not in LeaZie["admin"] and op.param2 not in LeaZie["Bots"]:
                    return
                else:
                    cl.sendMessage(op.param1, LeaZie["leftmsg"])

          if op.type == 17:
            if op.param1 in LeaZie["welcome"]:
                if op.param2 in Lea or op.param2 in LeaZie["Bots"] or op.param2 in LeaZie["admin"]:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

          if op.type == 19:
            if op.param1 in LeaZie["proKick"]:
                if op.param2 in Lea or op.param2 in LeaZie["Bots"] or op.param2 in LeaZie["admin"]:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                        except:pass
                    try:
                        if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                            wait["blacklist"][op.param2] = True
                            if op.param3 not in wait["blacklist"]:
                                try:
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    ka.findAndAddContactsByMid(op.param3)
                                    ka.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param3)
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.findAndAddContactsByMid(op.param3)
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                kd.findAndAddContactsByMid(op.param3)
                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                    ke.findAndAddContactsByMid(op.param3)
                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    try:
                                                        kf.findAndAddContactsByMid(op.param3)
                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                                    except:pass
                            else:pass
                        else:pass
                    except:pass

          if op.type == 32:
            if op.param1 in LeaZie["proCancel"]:
                if op.param2 in Lea or op.param2 in LeaZie["Bots"] or op.param2 in LeaZie["admin"]:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                        except:pass
                    try:
                        if op.param2 not in Lea and op.param2 not in LeaZie["Bots"] and op.param2 not in LeaZie["admin"]:
                            wait["blacklist"][op.param2] = True
                            if op.param3 not in wait["blacklist"]:
                                try:
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    ka.findAndAddContactsByMid(op.param3)
                                    ka.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param3)
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.findAndAddContactsByMid(op.param3)
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                kd.findAndAddContactsByMid(op.param3)
                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                    ke.findAndAddContactsByMid(op.param3)
                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    try:
                                                        kf.findAndAddContactsByMid(op.param3)
                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                                    except:pass
                            else:pass
                        else:pass
                    except:pass

          if op.type == 55:
            try:
                if op.param1 in LeaZie["readPoint"]:
                   if op.param2 in LeaZie["readMember"][op.param1]:pass
                   else:LeaZie["readMember"][op.param1][op.param2] = True
                else:pass
            except:pass


          if op.type in [25,26]:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            keyt = LeaZie["keyCmd"]
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if LeaZie["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"╔══════════════\n╠•❲ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ❳\n╠• sᴛᴋɪᴅ : " + msg.contentMetadata["STKID"] +"\n╠• sᴛᴋᴘᴋɢɪᴅ : " + msg.contentMetadata["STKPKGID"] + "\n╠• sᴛᴋᴠᴇʀ : " + msg.contentMetadata["STKVER"] + "\n╠• " + "line://shop/detail/" + msg.contentMetadata["STKPKGID"] +"\n╚══════════════")
               if msg.contentType == 13:
                 if LeaZie["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"╔══════════════\n╠• ɴᴀᴍᴀ : " + msg.contentMetadata["displayName"] + "\n╠• ᴍɪᴅ : " + msg.contentMetadata["mid"] + "\n╠• sᴛᴀᴛᴜs : " + contact.statusMessage + "\n╠• ᴘɪᴄᴛᴜʀᴇ ᴜʀʟ : http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n╚══════════════")
                        cl.sendImageWithURL(msg.to, image)

               if msg.contentType == 13:
                 if msg._from in Zie:
                  if LeaZie["abots"] == True:
                    if msg.contentMetadata["mid"] in LeaZie["Bots"]:
                        cl.sendMessage(msg.to,"ᴡᴀs ʙᴏᴛ ғʀɪᴇɴᴅ")
                    else:
                        LeaZie["Bots"][msg.contentMetadata["mid"]] = True
                        cl.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴀᴅᴅ ʙᴏᴛs")
                 if LeaZie["dbots"] == True:
                    if msg.contentMetadata["mid"] in LeaZie["Bots"]:
                        del LeaZie["Bots"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇᴍᴏᴠᴇ ʙᴏᴛs")
                    else:
                        cl.sendMessage(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ɴᴏᴛ ɪɴ ʟɪsᴛ ʙᴏᴛs")
                 if msg._from in Zie:
                  if LeaZie["addadmin"] == True:
                    if msg.contentMetadata["mid"] in LeaZie["admin"]:
                        cl.sendMessage(msg.to,"ᴡᴀs ᴀᴅᴍɪɴ")
                    else:
                        LeaZie["admin"][msg.contentMetadata["mid"]] = True
                        cl.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴀᴅᴅ ᴀᴅᴍɪɴ")
                 if LeaZie["deladmin"] == True:
                    if msg.contentMetadata["mid"] in LeaZie["admin"]:
                        del LeaZie["admin"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇᴍᴏᴠᴇ ᴀᴅᴍɪɴ")
                    else:
                        cl.sendMessage(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ɴᴏᴛ ɪɴ ʟɪsᴛ ᴀᴅᴍɪɴ")
                 if msg._from in Zie:
                  if LeaZie["ablacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"ᴡᴀs ʙʟᴀᴄᴋʟɪsᴛ")
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        cl.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴀᴅᴅ ɪɴ ʙʟᴀᴄᴋʟɪsᴛ")
                 if LeaZie["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇᴍᴏᴠᴇ ʙʟᴀᴄᴋʟɪsᴛ")
                    else:
                        cl.sendMessage(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ɴᴏᴛ ɪɴ ʙʟᴀᴄᴋʟɪsᴛ")

               if msg.toType == 2:
                 if msg._from in Zie:
                   if LeaZie["gPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     LeaZie["gPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "sᴜᴄᴄᴇs ᴜᴘᴅᴀᴛᴇ ɢʀᴏᴜᴘ ᴘɪᴄᴛᴜᴛᴇ")

               if msg.contentType == 1:
                       if msg._from in Zie:
                           if LeaZie["DPicture"] == True:
                               for cc in [ka,kb,kc,kd,ke,kf]:
                                   path = cc.downloadObjectMsg(msg_id)
                                   LeaZie["DPicture"] = False
                                   cc.updateProfilePicture(path)
                                   cc.sendMessage(msg.to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴅɪsᴘʟᴀʏ ᴘɪᴄᴛᴜʀᴇ")

               if msg.contentType == 1:
                 if msg._from in Zie:
                   if mid in LeaZie["cPicture"]:
                     path = cl.downloadObjectMsg(msg_id)
                     del LeaZie["cPicture"][mid]
                     cl.updateProfilePicture(path)
                     cl.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴜᴘᴅᴀᴛᴇ ᴅɪsᴘʟᴀʏ ᴘɪᴄᴛᴜʀᴇ")
                   if Amid in LeaZie["cPicture"]:
                     path1 = ka.downloadObjectMsg(msg_id)
                     del LeaZie["cPicture"][Amid]
                     ka.updateProfilePicture(path1)
                     ka.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴜᴘᴅᴀᴛᴇ ᴅɪsᴘʟᴀʏ ᴘɪᴄᴛᴜʀᴇ")
                   if Bmid in LeaZie["cPicture"]:
                     path2 = kb.downloadObjectMsg(msg_id)
                     del LeaZie["cPicture"][Bmid]
                     kb.updateProfilePicture(path2)
                     kb.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴜᴘᴅᴀᴛᴇ ᴅɪsᴘʟᴀʏ ᴘɪᴄᴛᴜʀᴇ")
                   if Cmid in LeaZie["cPicture"]:
                     path3 = kc.downloadObjectMsg(msg_id)
                     del LeaZie["cPicture"][Cmid]
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴜᴘᴅᴀᴛᴇ ᴅɪsᴘʟᴀʏ ᴘɪᴄᴛᴜʀᴇ")
                   if Dmid in LeaZie["cPicture"]:
                     path4 = kd.downloadObjectMsg(msg_id)
                     del LeaZie["cPicture"][Dmid]
                     kd.updateProfilePicture(path4)
                     kd.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴜᴘᴅᴀᴛᴇ ᴅɪsᴘʟᴀʏ ᴘɪᴄᴛᴜʀᴇ")
                   if Emid in LeaZie["cPicture"]:
                     path5 = ke.downloadObjectMsg(msg_id)
                     del LeaZie["cPicture"][Emid]
                     ke.updateProfilePicture(path5)
                     ke.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴜᴘᴅᴀᴛᴇ ᴅɪsᴘʟᴀʏ ᴘɪᴄᴛᴜʀᴇ")
                   if Fmid in LeaZie["cPicture"]:
                     path6 = kf.downloadObjectMsg(msg_id)
                     del LeaZie["cPicture"][Fmid]
                     kf.updateProfilePicture(path6)
                     kf.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴜᴘᴅᴀᴛᴇ ᴅɪsᴘʟᴀʏ ᴘɪᴄᴛᴜʀᴇ")
                   if Smid in LeaZie["cPicture"]:
                     path7 = k1.downloadObjectMsg(msg_id)
                     del LeaZie["cPicture"][Smid]
                     k1.updateProfilePicture(path7)
                     k1.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴜᴘᴅᴀᴛᴇ ᴅɪsᴘʟᴀʏ ᴘɪᴄᴛᴜʀᴇ")

               if msg.contentType == 0:
                    if LeaZie["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        commandM = command(text)
                        commandM = commandM.strip()

                    for cmd in commandM.split('.'):
                        if msg._from in Zie:
                            if cmd.startswith("1run "):
                                cust = cmd.split("1run ")[1]
                                os.system('nohup python3 %s.py jp &'%cust)
                                cl.sendMessage(msg.to, "ʀᴜɴɴɪɴɢ ᴘʀᴏᴊᴇᴄᴛ {} sᴜᴄᴄᴇss".format(cust))
                            elif cmd.startswith("1kill "):
                               cust = cmd.split("1kill ")[1]
                               try:
                                   p = subprocess.Popen(['ps', 'ax'], stdout=subprocess.PIPE)
                                   out, err = p.communicate()
                                   for line in out.splitlines():
                                       if '%s.py'%cust in line.decode("utf-8"):
                                           pid = int(line.split(None, 1)[0])
                                           os.kill(pid, signal.SIGKILL)
                               except:
                                   pass
                               cl.sendMessage(msg.to,' succes kill %s'%cust)
                            elif cmd == '1run':
                                try:
                                    n = 0
                                    r = ''
                                    p = subprocess.Popen(['ps', 'ax'], stdout=subprocess.PIPE)
                                    out, err = p.communicate()
                                    for line in out.splitlines():
                                        if 'python3' in line.decode('utf-8'):
                                            name = line.decode('utf-8').split('python3')[1]
                                            if '.py' in name and '4ang' not in name:
                                                r += '%s: %s\n'%(n,name.replace('.py',''))
                                                n += 1
                                    if len(r) > 0:
                                        cl.sendMessage(msg.to,r.rstrip())
                                    else:
                                        cl.sendMessage(msg.to,'empy project run')
                                except:
                                    cl.sendMessage(msg.to,'error')

                            elif cmd == "friend":
                               Flist(cl,to)
                            elif cmd == "allfriend":
                               for d in Amin:
                                   Flist(d,to)

                            elif cmd == 'bot:room':
                                a = []
                                b = cl.getGroup(to)
                                lss = cl.refreshContacts()
                                for i in b.members:
                                  if i.mid not in mid:
                                     a.append(i.mid)
                                     if i.mid not in lss:
                                        cl.findAndAddContactsByMid(i.mid)
                                     time.sleep(0.2)
                                if a == []:
                                   cl.sendMessage(to,"Nothing to added.")
                                else:cl.sendMessage(to,'Add whitelist')

                            elif cmd == 'bot1:room':
                                a = []
                                b = ka.getGroup(to)
                                lss = ka.refreshContacts()
                                for i in b.members:
                                  if i.mid not in Amid:
                                     a.append(i.mid)
                                     if i.mid not in lss:
                                        ka.findAndAddContactsByMid(i.mid)
                                     time.sleep(0.2)
                                if a == []:
                                   ka.sendMessage(to,"Nothing to added.")
                                else:ka.sendMessage(to,'Add whitelist')
                            elif cmd == 'bot2:room':
                                a = []
                                b = kb.getGroup(to)
                                lss = kb.refreshContacts()
                                for i in b.members:
                                  if i.mid not in Bmid:
                                     a.append(i.mid)
                                     if i.mid not in lss:
                                        kb.findAndAddContactsByMid(i.mid)
                                     time.sleep(0.2)
                                if a == []:
                                   kb.sendMessage(to,"Nothing to added.")
                                else:kb.sendMessage(to,'Add whitelist')
                            elif cmd == 'bot3:room':
                                a = []
                                b = kc.getGroup(to)
                                lss = kc.refreshContacts()
                                for i in b.members:
                                  if i.mid not in Cmid:
                                     a.append(i.mid)
                                     if i.mid not in lss:
                                        kc.findAndAddContactsByMid(i.mid)
                                     time.sleep(0.2)
                                if a == []:
                                   kc.sendMessage(to,"Nothing to added.")
                                else:kc.sendMessage(to,'Add whitelist')
                            elif cmd == 'bot4:room':
                                a = []
                                b = kd.getGroup(to)
                                lss = kd.refreshContacts()
                                for i in b.members:
                                  if i.mid not in Dmid:
                                     a.append(i.mid)
                                     if i.mid not in lss:
                                        kd.findAndAddContactsByMid(i.mid)
                                     time.sleep(0.2)
                                if a == []:
                                   kd.sendMessage(to,"Nothing to added.")
                                else:kd.sendMessage(to,'Add whitelist')
                            elif cmd == 'bot5:room':
                                a = []
                                b = ke.getGroup(to)
                                lss = ke.refreshContacts()
                                for i in b.members:
                                  if i.mid not in Emid:
                                     a.append(i.mid)
                                     if i.mid not in lss:
                                        ke.findAndAddContactsByMid(i.mid)
                                     time.sleep(0.2)
                                if a == []:
                                   ke.sendMessage(to,"Nothing to added.")
                                else:ke.sendMessage(to,'Add whitelist')
                            elif cmd == 'bot6:room':
                                a = []
                                b = kf.getGroup(to)
                                lss = kf.refreshContacts()
                                for i in b.members:
                                  if i.mid not in Fmid:
                                     a.append(i.mid)
                                     if i.mid not in lss:
                                        kf.findAndAddContactsByMid(i.mid)
                                     time.sleep(0.2)
                                if a == []:
                                   kf.sendMessage(to,"Nothing to added.")
                                else:kf.sendMessage(to,'Add whitelist')
                            elif cmd == 'kicker:room':
                                a = []
                                b = k1.getGroup(to)
                                lss = k1.refreshContacts()
                                for i in b.members:
                                  if i.mid not in Smid:
                                     a.append(i.mid)
                                     if i.mid not in lss:
                                        k1.findAndAddContactsByMid(i.mid)
                                     time.sleep(0.2)
                                if a == []:
                                   k1.sendMessage(to,"Nothing to added.")
                                else:k1.sendMessage(to,'Add whitelist')

                            elif cmd.startswith("tkn "):
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               if pesan == "":
                                   setKey = "" if not LeaZie['keyCmd'] else LeaZie['keyCmd']
                               else:
                                   setKey = pesan
                               cl.sendMessage(to, str(setKey))
                        if msg._from in Zie or msg._from in LeaZie["admin"]:
                          if cmd == "menu":cl.sendMessage(to, Menu.help(keyt))
                          if cmd == "menu1":cl.sendMessage(to, Menu.helpset(keyt))
                          if cmd == "menu2":cl.sendMessage(to, Menu.helpbot(keyt))

                          if cmd == "settbot":
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                eltime = time.time() - mulai
                                md = "╭━━━━━━━━━━━─\n╰─⟦ 𝕯'𝖕𝖗𝖔 𝕶𝖎𝖑𝖑𝖊𝖗 𝕻𝖗𝖔𝖙𝖊𝖈𝖙𝖎𝖔𝖓 ⟧\n\n"
                                md+="  「on ==📳  <|>  📴 == off」\n\n"
                                if msg.to in LeaZie["proqr"]:md+="  「📳」 ᴘʀᴏᴛᴇᴄᴛ ʟɪɴᴋ \n"
                                else:md+="  「📴」 ᴘʀᴏᴛᴇᴄᴛ ʟɪɴᴋ \n"
                                if msg.to in LeaZie["proKick"]:md+="  「📳」 ᴘʀᴏᴛᴇᴄᴛ ᴋɪᴄᴋ \n"
                                else:md+="  「📴」 ᴘʀᴏᴛᴇᴄᴛ ᴋɪᴄᴋ \n"
                                if msg.to in LeaZie["proCancel"]:md+="  「📳」 ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ \n"
                                else:md+="  「📴」 ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ \n"
                                if msg.to in LeaZie["proInvite"]:md+="  「📳」 ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ \n"
                                else:md+="  「📴」 ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ \n"
                                if msg.to in LeaZie["intaPoint"]:md+="  「📳」 sᴇᴛᴛ ᴀᴜᴛᴏ ᴘᴏɪɴᴛ \n"
                                else:md+="  「📴」 sᴇᴛᴛ ᴀᴜᴛᴏ ᴘᴏɪɴᴛ \n"
                                if LeaZie["bypas"] == True:md+="  「📳」 ʙʏᴘᴀss ᴇɴᴀʙʟᴇ \n"
                                else:md+="  「📴」 ʙʏᴘᴀss ᴅɪsᴀʙʟᴇ \n"
                                if LeaZie["autoJoin"] == True:md+="  「📳」 ᴀ'ᴊᴏɪɴ ɢʀᴏᴜᴘ \n"
                                else:md+="  「📴」 ᴀ'ᴊᴏɪɴ ɢʀᴏᴜᴘ \n"
                                if LeaZie["autoJoinTicket"] == True:md+="  「📳」 ᴀ'ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ \n"
                                else:md+="  「📴」 ᴀ'ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ \n"
                                if LeaZie["contact"] == True:md+="  「📳」 ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ \n"
                                else:md+="  「📴」 ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ \n"
                                if LeaZie["sticker"] == True:md+="  「📳」 ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ \n"
                                else:md+="  「📴」 ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ \n"
                                if LeaZie["detectMention"] == True:md+="  「📳」 ʀᴇsᴘᴏɴ ᴍᴇɴᴛɪᴏɴ \n"
                                else:md+="  「📴」 ʀᴇsᴘᴏɴ ᴍᴇɴᴛɪᴏɴ \n"
                                if LeaZie["autoAdd"] == True:md+="  「📳」 ᴀᴅᴅ ᴄᴏɴᴛᴀᴄᴛ \n"
                                else:md+="  「📴」 ᴀᴅᴅ ᴄᴏɴᴛᴀᴄᴛ \n"
                                if LeaZie["LikeOn"] == True:md+="  「📳」 ʟɪᴋᴇ & ᴄᴏᴍᴍᴇɴᴛ \n"
                                else:md+="  「📴」 ʟɪᴋᴇ & ᴄᴏᴍᴍᴇɴᴛ \n"
                                if LeaZie["checkPost"] == True:md+="  「📳」 ᴄʜᴇᴄᴋ ᴘᴏsᴛ \n"
                                else:md+="  「📴」 ᴄʜᴇᴄᴋ ᴘᴏsᴛ \n"
                                if LeaZie["Unsend"] == True:md+="  「📳」 ᴅ'ᴜɴsᴇɴᴅ ᴍsɢ \n"
                                else:md+="  「📴」 ᴅ'ᴜɴsᴇɴᴅ ᴍsɢ \n"
                                if msg.to in LeaZie["welcome"]:md+="  「📳」 ᴍsɢ ᴡᴇʟʟᴄᴏᴍᴇ \n"
                                else:md+="  「📴」 ᴍsɢ ᴡᴇʟʟᴄᴏᴍᴇ \n"
                                if msg.to in LeaZie["leaveMsg"]:md+="  「📳」 ᴍsɢ ʟᴇᴀᴠᴇ \n"
                                else:
                                    md+="  「📴」 ᴍsɢ ʟᴇᴀᴠᴇ \n\n"
                                    md+="  ⌚"+ datetime.strftime(timeNow,'%H:%M:%S')+"  📆 "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n"
                                    md+="   ʀᴜɴ "+waktu(eltime)+"\n"
                                    md+="╭━━━━━━━━━━━─\n「 http://line.me/ti/p/~dprokiller88 」\n╰━━━━━━━━━━━─"
                                cl.sendReplyMessage(msg_id, to, str(md))

                          if cmd == "me" or text.lower() == 'me':
                                ca = cl.getContact(msg._from)
                                lip = ("「ᴍʏ ɴᴀᴍᴇ」\n ") + ca.displayName
                                cl.sendMessage(to, lip),cl.sendContact(msg.to,sender)

                          if cmd == 'bypas on':
                              if LeaZie["bypas"] == True:
                                  cl.sendMessage(to,"𝐁𝐲𝐩𝐚𝐬𝐬 𝐬𝐮𝐝𝐚𝐡 𝐝𝐢𝐚𝐤𝐭𝐢𝐟𝐤𝐚𝐧")
                              else:
                                  LeaZie["bypas"] = True
                                  cl.sendMessage(to,"𝐌𝐨𝐝𝐞 𝐛𝐲𝐩𝐚𝐬𝐬 𝐭𝐞𝐥𝐚𝐡 𝐝𝐢𝐚𝐤𝐭𝐢𝐟𝐤𝐚𝐧")

                          if cmd == 'bypas off':
                              if LeaZie["bypas"] == False:
                                  cl.sendMessage(to,"𝐁𝐲𝐩𝐚𝐬𝐬 𝐬𝐮𝐝𝐚𝐡 𝐝??𝐦𝐚𝐭𝐢𝐤𝐚𝐧")
                              else:
                                  LeaZie["bypas"] = False
                                  cl.sendMessage(to,"𝐌𝐨𝐝𝐞 𝐛𝐲𝐩𝐚𝐬𝐬 𝐭𝐞𝐥𝐚𝐡 𝐝𝐢𝐦𝐚𝐭𝐢𝐤𝐚𝐧")

                          if "gname " in cmd:
                                X = cl.getGroup(msg.to)
                                X.name = msg.text.replace("gname ","")
                                cl.updateGroup(X)

                          if "mid " in cmd:
                               if 'MENTION' in msg.contentMetadata.keys()!= None:
                                   names = re.findall(r'@(\w+)', text)
                                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                   mentionees = mention['MENTIONEES']
                                   lists = []
                                   for mention in mentionees:
                                       if mention["M"] not in lists:
                                           lists.append(mention["M"])
                                   ret_ = ""
                                   for ls in lists:
                                       ret_ += "{}".format(str(ls))
                                   cl.sendMessage(to, str(ret_),{'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+'M', 'AGENT_NAME': 'Mention', 'AGENT_LINK': 'http://line.me/ti/p/~{}'.format(cl.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + cl.getProfile().picturePath})

                          if "info " in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "• Nama : "+str(mi.displayName)+"\n• Mid : " +key1+"\n• Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                          if cmd == "mybot":
                               ka.sendContact(msg.to, Amid)
                               time.sleep(0.15)
                               kb.sendContact(msg.to, Bmid)
                               time.sleep(0.15)
                               kc.sendContact(msg.to, Cmid)
                               time.sleep(0.15)
                               kd.sendContact(msg.to, Dmid)
                               time.sleep(0.15)
                               ke.sendContact(msg.to, Emid)
                               time.sleep(0.15)
                               kf.sendContact(msg.to, Fmid)

                          if cmd == "myrechat":
                               try:cl.removeAllMessages(op.param2)
                               except:pass

                          if cmd == "reject":
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  cl.sendReplyMessage(msg_id, to, "ʙᴇʀʜᴀsɪʟ ᴛᴏʟᴀᴋ sᴇʙᴀɴʏᴀᴋ {} ᴜɴᴅᴀɴɢᴀɴ ɢʀᴜᴘ".format(str(len(ginvited))))
                              else:
                                  cl.sendReplyMessage(msg_id, to, "ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴜɴᴅᴀɴɢᴀɴ ʏᴀɴɢ ᴛᴇʀᴛᴜɴᴅᴀ")

                          if cmd == "leave allgrup":
                            group = cl.getGroupIdsJoined()
                            for i in group:
                                cl.sendMessage(i,"ʙᴏᴛ ʟᴇᴀᴠᴇ ᴀʟʟ ɢʀᴏᴜᴘ ")
                                cl.leaveGroup(i)
                                ka.leaveGroup(i)
                                kb.leaveGroup(i)
                                kc.leaveGroup(i)
                                kd.leaveGroup(i)
                                ke.leaveGroup(i)
                                kf.leaveGroup(i)
                                cl.sendMessage(msg.to,"sᴜᴄᴄᴇs ʟᴇᴀᴠᴇ ᴀʟʟ ɢʀᴜᴘ")
                          if cmd.startswith("openqr no "):
                                if msg.toType == 2:
                                    text = cmd.split(" ")
                                    number = text[2]
                                    if number.isdigit():
                                        groups = cl.getGroupIdsJoined()
                                        if int(number) < len(groups) and int(number) >= 0:
                                            groupid = groups[int(number)]
                                            try:
                                                X = cl.getGroup(groupid)
                                                X.preventedJoinByTicket = False
                                                cl.updateGroup(X)
                                                gurl = cl.reissueGroupTicket(groupid)
                                                cl.sendMessage(msg.to,"This link Group For u can it Bro... \nline://ti/g/" + gurl)
                                            except:
                                                cl.sendMessage(msg.to," Gagal Bro ")
                          if cmd.startswith("leave to "):
                                text = cmd.split(" ")
                                number = text[2]
                                if number.isdigit():
                                    groups = cl.getGroupIdsJoined()
                                    if int(number) < len(groups) and int(number) >= 0:
                                        groupid = groups[int(number)]
                                        try:
                                            groupname = cl.getGroup(groupid).name
                                            cl.leaveGroup(groupid)
                                            ka.leaveGroup(groupid)
                                            kb.leaveGroup(groupid)
                                            kc.leaveGroup(groupid)
                                            kd.leaveGroup(groupid)
                                            ke.leaveGroup(groupid)
                                            kf.leaveGroup(groupid)
                                            cl.sendMessage(msg.to,"Successfully  Leave from %s"%groupname)
                                        except:
                                            cl.sendMessage(msg.to," Leave Gagal Bro ")
                          if cmd == "rechat":
                              for i in botlist:
                                  Rchat(i,to)
                          if cmd.startswith("bcg: "):
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ ʙʀᴏᴀᴅᴄᴀsᴛ ]\n" + str(pesan))
                          if cmd == "mykey":
                               cl.sendMessage(msg.to, "ᴋᴇʏ ɴᴏᴡ「 " + str(LeaZie["keyCmd"]) + " 」")
                          if cmd.startswith("setkey "):
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "ᴄʜᴀɴɢᴇ ᴋᴇʏ ғᴀɪʟᴇᴅ")
                               else:
                                   LeaZie["keyCmd"] = str(key).lower()
                                   cl.sendMessage(msg.to, "sᴜᴄᴄᴇs ᴀᴅᴅ ᴋᴇʏ ᴛᴏ「{}」".format(str(key).lower()))
                          if cmd == "resetkey":
                               LeaZie["keyCmd"]=""
                               cl.sendMessage(msg.to, "sᴜᴄᴄᴇs ʀᴇssᴇᴛ ᴋᴇʏ ᴄᴏᴍᴍᴀɴᴅ")
                          if cmd == "/reboot":
                               cl.sendMessage(msg.to, "ᴡᴀɪᴛɪɴɢ ᴀ sᴇᴄᴏɴᴅ")
                               restartProgram()
                          if cmd == "ginfo":
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "тєятυтυρ"
                                    gTicket = "тı∂αk α∂α"
                                else:
                                    gQr = "тєявυkα"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "  •⌻「gяυρ ıηƒσ」⌻•\n\n ηαмα gяσυρ : {}".format(G.name)+ "\nı∂ gяσυρ : {}".format(G.id)+ "\ncяєαтσя gяσυρ : {}".format(G.creator.displayName)+ "\ncяєαтє тıмє gяσυρ : {}".format(str(timeCreated))+ "\nłısтмємвєя : {}".format(str(len(G.members)))+ "\nłısт ıηѵıтє : {}".format(gPending)+ "\ngяσυρ qя : {}".format(gQr)+ "\nтıckєт gяσυρ : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))
                          if cmd.startswith("infogrup"):
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "No file"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "  •⌻ List Grup Info ⌻•\n"
                                ret_ += "\n⌬ Nama Group : {}".format(G.name)
                                ret_ += "\n⌬ ID Group : {}".format(G.id)
                                ret_ += "\n⌬ Pembuat : {}".format(gCreator)
                                ret_ += "\n⌬ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n⌬ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n⌬ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n⌬ Group Qr : {}".format(gQr)
                                ret_ += "\n⌬ Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass
                          if cmd.startswith("infomem"):
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "● "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"● Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except:
                                pass
                          if cmd.startswith("leave: "):
                            text = cmd.replace("leave: ","")
                            gid = cl.getGroupIdsJoined()
                            for i in gid:
                                x = cl.getGroup(i).name
                                if x == text:
                                    try:
                                        ka.leaveGroup(i)
                                        kb.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        kd.leaveGroup(i)
                                        ke.leaveGroup(i)
                                        kf.leaveGroup(i)
                                        cl.leaveGroup(i)
                                        cl.sendMessage(msg.to,"ѕυкѕєѕ кєℓυαя ∂αяι gяυρ %s"%text)
                                    except:
                                        cl.sendMessage(msg.to,"gαgαℓ кєℓυαя ∂αяι gяυρ %s"%text)
                          if cmd == "friendlist":
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")
                          if cmd == "gruplist":
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
                          if cmd == "ourl":
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                gurl = cl.reissueGroupTicket(msg.to)
                                cl.sendMessage(msg.to,"line://ti/g/" + gurl)
                          if cmd == "curl":
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "ᴅᴏɴᴇ ᴄʟᴏsᴇ ǫʀ°")
#===========================================#
                          if cmd == "runtime":
                                eltime = time.time() - mulai
                                cl.sendMessage(to, "Bot Run : "+eltime)
                          if cmd == "pictgrup":
                              if msg.toType == 2:
                                LeaZie["gPicture"] = True
                                cl.sendMessage(msg.to,"ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴘɪᴄᴛ")
                          if cmd == "updatefoto":
                                LeaZie["DPicture"] = True
                                cl.sendMessage(msg.to,"ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴘɪᴄᴛ")
                          if 'dpbot ' in cmd:
                              spl = cmd.replace('dpbot ','')
                              if spl == 'me':
                                  LeaZie["cPicture"][mid] = True
                                  cl.sendMessage(msg.to,"ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴘɪᴄᴛ")
                              if spl == '1':
                                  LeaZie["cPicture"][Amid] = True
                                  ka.sendMessage(msg.to, "ᴘᴇʟᴀsᴇ sᴇɴᴅ ᴘɪᴄᴛ ʙᴏss")
                              if spl == '2':
                                  LeaZie["cPicture"][Bmid] = True
                                  kb.sendMessage(msg.to, "ᴘᴇʟᴀsᴇ sᴇɴᴅ ᴘɪᴄᴛ ʙᴏss")
                              if spl == '3':
                                  LeaZie["cPicture"][Cmid] = True
                                  kc.sendMessage(msg.to, "ᴘᴇʟᴀsᴇ sᴇɴᴅ ᴘɪᴄᴛ ʙᴏss")
                              if spl == '4':
                                  LeaZie["cPicture"][Dmid] = True
                                  kd.sendMessage(msg.to, "ᴘᴇʟᴀsᴇ sᴇɴᴅ ᴘɪᴄᴛ ʙᴏss")
                              if spl == '5':
                                  LeaZie["cPicture"][Emid] = True
                                  ke.sendMessage(msg.to, "ᴘᴇʟᴀsᴇ sᴇɴᴅ ᴘɪᴄᴛ ʙᴏss")
                              if spl == '6':
                                  LeaZie["cPicture"][Fmid] = True
                                  kf.sendMessage(msg.to, "ᴘᴇʟᴀsᴇ sᴇɴᴅ ᴘɪᴄᴛ ʙᴏss")
                              if spl == 'ghost':
                                  LeaZie["cPicture"][Smid] = True
                                  k1.sendMessage(msg.to, "ᴘᴇʟᴀsᴇ sᴇɴᴅ ᴘɪᴄᴛ ʙᴏss")
                          if cmd.startswith("dname: "):
                            separate = text.split(" ")
                            string = text.replace(separate[0] + " ","")
                            if string == "":
                               setKey = "" if not LeaZie['keyCmd'] else LeaZie['keyCmd']
                            else:
                               setKey = string
                            profile = cl.getProfile()
                            profile.displayName = string
                            cl.updateProfile(profile)
                            cl.sendMessage(msg.to,"Succes " + str(string) + "")
                          if cmd.startswith("d1name: "):
                            separate = text.split(" ")
                            string = text.replace(separate[0] + " ","")
                            if string == "":
                               setKey = "" if not LeaZie['keyCmd'] else LeaZie['keyCmd']
                            else:
                               setKey = string
                            profile = ka.getProfile()
                            profile.displayName = string
                            ka.updateProfile(profile)
                            ka.sendMessage(msg.to,"Succes " + str(string) + "")
                          if cmd.startswith("d2name: "):
                            separate = text.split(" ")
                            string = text.replace(separate[0] + " ","")
                            if string == "":
                               setKey = "" if not LeaZie['keyCmd'] else LeaZie['keyCmd']
                            else:
                               setKey = string
                            profile = kb.getProfile()
                            profile.displayName = string
                            kb.updateProfile(profile)
                            kb.sendMessage(msg.to,"Succes " + str(string) + "")
                          if cmd.startswith("d3name: "):
                            separate = text.split(" ")
                            string = text.replace(separate[0] + " ","")
                            if string == "":
                               setKey = "" if not LeaZie['keyCmd'] else LeaZie['keyCmd']
                            else:
                               setKey = string
                            profile = kc.getProfile()
                            profile.displayName = string
                            kc.updateProfile(profile)
                            kc.sendMessage(msg.to,"Succes " + str(string) + "")
                          if cmd.startswith("d4name: "):
                            separate = text.split(" ")
                            string = text.replace(separate[0] + " ","")
                            if string == "":
                               setKey = "" if not LeaZie['keyCmd'] else LeaZie['keyCmd']
                            else:
                               setKey = string
                            profile = kd.getProfile()
                            profile.displayName = string
                            kd.updateProfile(profile)
                            kd.sendMessage(msg.to,"Succes " + str(string) + "")
                          if cmd.startswith("d5name: "):
                            separate = text.split(" ")
                            string = text.replace(separate[0] + " ","")
                            if string == "":
                               setKey = "" if not LeaZie['keyCmd'] else LeaZie['keyCmd']
                            else:
                               setKey = string
                            profile = ke.getProfile()
                            profile.displayName = string
                            ke.updateProfile(profile)
                            ke.sendMessage(msg.to,"Succes " + str(string) + "")
                          if cmd.startswith("d6name: "):
                            separate = text.split(" ")
                            string = text.replace(separate[0] + " ","")
                            if string == "":
                               setKey = "" if not LeaZie['keyCmd'] else LeaZie['keyCmd']
                            else:
                               setKey = string
                            profile = kf.getProfile()
                            profile.displayName = string
                            kf.updateProfile(profile)
                            kf.sendMessage(msg.to,"Succes " + str(string) + "")
                          if cmd.startswith("ghostname: "):
                            separate = text.split(" ")
                            string = text.replace(separate[0] + " ","")
                            if string == "":
                               setKey = "" if not LeaZie['keyCmd'] else LeaZie['keyCmd']
                            else:
                               setKey = string
                            profile = k1.getProfile()
                            profile.displayName = string
                            k1.updateProfile(profile)
                            k1.sendMessage(msg.to,"Succes " + str(string) + "")
                          if cmd.startswith("allcn: "):
                            separate = text.split(" ")
                            string = text.replace(separate[0] + " ","")
                            for x in Amin:
                              if string == "":
                                 setKey = "" if not LeaZie['keyCmd'] else LeaZie['keyCmd']
                              else:
                                 setKey = string
                              profile = x.getProfile()
                              profile.displayName = string
                              x.updateProfile(profile)
                              x.sendMessage(msg.to,"Succes " + str(string) + "")
                          if cmd == "desah" or text.lower() == 'mention':
                                group = cl.getGroup(msg.to)
                                k = len(group.members)//20
                                for j in range(k+1):
                                    aa = []
                                    for x in group.members[j*20 : (j+1)*20]:
                                        aa.append(x.mid)
                                    try:
                                        arrData = ""
                                        textx = "╔══════════════════\n╠• . "
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += "╠• . ".format(str(b))
                                            else:
                                                textx += "╚══════════════════\n╔══════════════════\n  「 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀ : {} 」\n╚══════════════════".format(str(len(aa)))
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))

                                                except:
                                                    no = " "
                                        msg.to = msg.to
                                        msg.text = textx
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage(to, textx,{'AGENT_NAME':'[ Mentions ]', 'AGENT_LINK': 'line://ti/p/~{}'.format(cl.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + cl.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                    except Exception as e:
                                        cl.sendText(msg.to,str(e))
                          if cmd == "bots":
                                ma = ""
                                a = 0
                                for m_id in LeaZie["Bots"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"| じisτ B̶ѳτઽ •\n\n"+ma+"τσταℓ : 「%s」 B̶ѳτઽ" %(str(len(LeaZie["Bots"]))))
                          if cmd == "adminlist":
                                mb = ""
                                b = 0
                                for m_id in LeaZie["admin"]:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"| α∂мiท вστs •\n\n"+mb+"\nτσταℓ :「%s」 α∂мiท" %(str(len(LeaZie["admin"]))))
                          if cmd == "respon":
                              for i in [ka,kb,kc,kd,ke,kf]:
                                  Res(i,to)
                          if cmd == "rs":
                              a = cl.getContact(msg._from).displayName
                              for i in botlist:
                                  i.sendMessage(to, "𝐊𝐚𝐦𝐢 𝐬𝐢𝐚𝐩 𝐦𝐞𝐧𝐞𝐫𝐢𝐦𝐚 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡 "+ a)
                          if cmd == 'midku':
                              cl.sendMessage(msg.to,mid+'","'+Amid+'","'+Bmid+'","'+Cmid+'","'+Dmid+'","'+Emid+'","'+Fmid+'","'+Smid)
                          if 'lp ' in cmd:
                              spl = cmd.replace('lp ','')
                              for i in botlist:
                                  i.sendMessage(msg.to,spl)
                          if cmd == "inv":
                                try:
                                    cl.inviteIntoGroup(msg.to,Bots)
                                    for i in botlist:
                                        i.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                          if cmd == "masuk" or text.lower() == "come":
                                G = cl.getCompactGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                for i in botlist:
                                    i.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                random.choice(botlist).inviteIntoGroup(msg.to,Ajs)
                          if cmd == "drespon":
                              a = cl.getContact(msg._from).displayName
                              k1.sendMessage(to, "𝐊𝐚𝐦𝐢 𝐬𝐢𝐚𝐩 𝐦𝐞𝐧𝐞𝐫𝐢𝐦𝐚 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡 "+ a)
                          if cmd == "djoin":
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                          if cmd.startswith("bypass"):
                                try:
                                    jser = threading.Thread(target=ProsesJs, args=(to, wait["Member"])).start()
                                except:
                                    cl.sendMessage(to,"Gagal BroW")
                          if cmd.startswith("qr no "):
                                if msg.toType == 2:
                                    text = cmd.split(" ")
                                    number = text[2]
                                    if number.isdigit():
                                        groups = cl.getGroupIdsJoined()
                                        if int(number) < len(groups) and int(number) >= 0:
                                            groupid = groups[int(number)]
                                            try:
                                                X = cl.getGroup(groupid)
                                                X.preventedJoinByTicket = False
                                                cl.updateGroup(X)
                                                gurl = cl.reissueGroupTicket(groupid)
                                                cl.sendMessage(msg.to,"This link Group For u can it Bro... \nline://ti/g/" + gurl)
                                            except:
                                                cl.sendMessage(msg.to," Gagal Bro ")

                          if cmd.startswith("sikat "):
                              txtt = cmd.split(" ")
                              number = txtt[2]
                              if number.isdigit():
                                  groups = cl.getGroupIdsJoined()
                                  if int(number) < len(groups) and int(number) >= 0:
                                      groupid = groups[int(number)]
                                      for dhe in [ka,kb,kc,kd,ke,kf,cl]:
                                        try:
                                            x = cl.getGroup(groupid)
                                            anu = x.id
                                            if x.invitee == None:nama = []
                                            else:nama = [contact.mid for contact in x.invitee]
                                            targets = []
                                            for a in nama:
                                              if a not in Lea:
                                                targets.append(a)
                                            nami = [contact.mid for contact in x.members]
                                            targetk = []
                                            cms = 'dual.js gid={} token={}'.format(anu,dhe.authToken)
                                            for a in nami:
                                              if a not in Lea:
                                                targetk.append(a)
                                            for y in targets:
                                                cms += ' uid={}'.format(y)
                                            for y in targetk:
                                                cms += ' uik={}'.format(y)
                                            success = execute_js(cms)
                                            cl.sendMessage(to,'𝐑𝐚𝐭𝐚 𝐠𝐚𝐤 𝐫𝐚𝐭𝐚 𝐲𝐚𝐧𝐠 𝐩𝐞𝐧𝐭𝐢𝐧𝐠 𝐠𝐰 𝐬𝐞𝐧𝐚𝐧𝐠')
                                            if x.preventedJoinByTicket == True:
                                                x.preventedJoinByTicket = False
                                                cl.updateGroup(x)
                                            gurl = cl.reissueGroupTicket(group)
                                            cl.sendMessage(to, 'join boss.. \n\nhttp://line.me/R/ti/g/'+gurl+'')
                                        except:
                                            cl.sendMessage(to, "gagal execusi")

                          if cmd == 'khilaf':
                            for dhe in [ka,kb,kc,kd,ke,kf,cl]:
                              try:
                                  x = cl.getGroup(to)
                                  if x.invitee == None:nama = []
                                  else:nama = [contact.mid for contact in x.invitee]
                                  targets = []
                                  for a in nama:
                                      if a not in Lea:
                                          targets.append(a)
                                  nami = [contact.mid for contact in x.members]
                                  targetk = []
                                  cms = 'dual.js gid={} token={}'.format(to,dhe.authToken)
                                  for a in nami:
                                      if a not in Lea:
                                          targetk.append(a)
                                  for y in targets:
                                      cms += ' uid={}'.format(y)
                                  for y in targetk:
                                      cms += ' uik={}'.format(y)
                                  success = execute_js(cms)
                                  cl.sendMessage(to,'𝐑𝐚𝐭𝐚 𝐠𝐚𝐤 𝐫𝐚𝐭𝐚 𝐲𝐚𝐧𝐠 𝐩𝐞𝐧𝐭𝐢𝐧𝐠 𝐠𝐰 𝐬𝐞𝐧𝐚𝐧𝐠')
                              except:
                                  print("gagal")
                          if cmd.startswith("nuke no "):
                                if msg.toType == 2:
                                    text = cmd.split(" ")
                                    number = text[2]
                                    if number.isdigit():
                                        groups = cl.getGroupIdsJoined()
                                        if int(number) < len(groups) and int(number) >= 0:
                                            groupid = groups[int(number)]
                                            try:
                                                for hk in [ka,kb,kc,kd,ke,kf,cl]:
                                                    X = cl.getGroup(groupid)
                                                    desi = X.id
                                                    if X.invitee == None:nama = []
                                                    else:nama = [contact.mid for contact in X.invitee]
                                                    target = []
                                                    for a in nama:
                                                        if a not in Lea:
                                                            target.append(a)
                                                    cmd = 'bypass.js gid={} token={}'.format(desi, hk.authToken)
                                                    d = [o.mid for o in X.members]
                                                    tarsem = []
                                                    for s in d:
                                                        if s not in Lea:
                                                            tarsem.append(s)
                                                    for y in target:
                                                        cmd += ' uid={}'.format(y)
                                                    for k in tarsem:
                                                        cmd += ' uid={}'.format(k)
                                                    success = execute_js(cmd)
                                                    X.preventedJoinByTicket = False
                                                    cl.updateGroup(X)
                                                    gurl = cl.reissueGroupTicket(groupid)
                                                    cl.sendMessage(to,"This link Group For u can it Bro... \nline://ti/g/" + gurl)
                                            except:cl.sendMessage(to,"Sorry i'cant nuker this numb room")
                          if cmd == "dstay":
                                try:
                                    for k in Amin:
                                        k.inviteIntoGroup(msg.to,Ajs)
                                except:
                                    cl.inviteIntoGroup(msg.to,Ajs)
                          if cmd == "ajscancel":
                                try:
                                    for k in Amin:
                                        k.cancelGroupInvitation(msg.to,[Ajs])
                                except:
                                    cl.cancelGroupInvitation(msg.to,[Ajs])
                          if cmd == "dbye":
                                G = k1.getGroup(msg.to)
                                k1.sendMessage(msg.to, "sєє υ мємвєя "+str(G.name))
                                k1.leaveGroup(msg.to)
                          if cmd == "pulang":
                              try:
                                  G = cl.getGroup(msg.to)
                                  ka.sendMessage(msg.to, "❂➤ kami pulang dulu ya,,,gerah banget di "+str(G.name))
                                  for i in botlist:
                                      i.leaveGroup(msg.to)
                              except:
                                  pass
                          if cmd == "/pamit":
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "❂➤ pamit pulang ah,,,gerah di  "+str(G.name))
                                try:
                                    k1.acceptGroupInvitation(msg.to)
                                    cl.leaveGroup(msg.to)
                                    k1.leaveGroup(msg.to)
                                except:
                                    cl.leaveGroup(msg.to)
                          if cmd == "speed" or cmd == "sp":
                                jb=[cl]
                                for i in jb:
                                    Speed(i,to)
                          if cmd == "!sp":
                                jb=botlist
                                for i in jb:
                                    Sp(i,to)
                          if cmd == "lurk on":
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 LeaZie['readPoint'][msg.to] = msg_id
                                 LeaZie['readMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "Lurking berhasil diaktifkan\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                          if cmd == "lurk off":
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del LeaZie['readPoint'][msg.to]
                                 del LeaZie['readMember'][msg.to]
                                 cl.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                          if cmd == "lurkers":
                            if msg.to in LeaZie['readPoint']:
                                if LeaZie['readMember'][msg.to] != {}:
                                    aa = []
                                    for x in LeaZie['readMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\n⌬ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del LeaZie['readPoint'][msg.to]
                                        del LeaZie['readMember'][msg.to]
                                    except:
                                        pass
                                    LeaZie['readPoint'][msg.to] = msg.id
                                    LeaZie['readMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "User kosong...")
                            else:
                                cl.sendMessage(msg.to, "Ketik lurking on ")
                          if cmd == "sider on":
                              try:
                                  cl.sendMessage(msg.to, "ᴄʜᴇᴄᴋ sɪᴅᴇʀ ᴍᴇᴍʙᴇʀ ᴀʟʟʀᴇᴀᴅʏ ᴏɴ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True
                          if cmd == "sider off":
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "ᴄʜᴇᴄᴋ sɪᴅᴇʀ ᴍᴇᴍʙᴇʀ ᴀʟʟʀᴇᴀᴅʏ ᴏғғ")
                              else:
                                  cl.sendMessage(msg.to, "ᴄʜᴇᴄᴋ sɪᴅᴇʀ ᴍᴇᴍʙᴇʀ ᴡᴀs ᴏғғ")
                          if cmd.startswith("max: "):
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                LeaZie["Maxlimit"] = num
                                cl.sendMessage(msg.to,"ᴀʟʟʀᴇᴀᴅʏ sᴘᴀᴍ ᴍᴇɴᴛɪᴏɴ ɪɴ :" +strnum)
                          if cmd.startswith("scall: "):
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                LeaZie["limit"] = num
                                cl.sendMessage(msg.to,"ᴀʟʟʀᴇᴀᴅʏ sᴘᴀᴍ ᴄᴀʟʟ ɪɴ :" +strnum)
                          if cmd.startswith("stag "):
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = ast.literal_eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(LeaZie["Maxlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"Jumlah melebihi 1000")
                          if cmd == "scall":
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(LeaZie["limit"])
                                cl.sendMessage(to, "sᴜᴄᴄᴇs sᴇɴᴅ {} sᴘᴀᴍ ᴄᴀʟʟ".format(str(LiproSett["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                         cl.acquireGroupCallRoute(to)
                                         cl.inviteIntoGroupCall(to, contactIds=members)
                                     except:
                                         pass
                                else:
                                    cl.sendMessage(to,"Jumlah melebihi batas")
                          if 'Spam: ' in cmd:
                              korban = cmd.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      ka.sendMessage(midd, str(LeaZie["spamMsg"]))
                                      kb.sendMessage(midd, str(LeaZie["spamMsg"]))
                                      kc.sendMessage(midd, str(LeaZie["spamMsg"]))
                                      kd.sendMessage(midd, str(LeaZie["spamMsg"]))
                                      ke.sendMessage(midd, str(LeaZie["spamMsg"]))
                                      kf.sendMessage(midd, str(LeaZie["spamMsg"]))
                          if 'id line: ' in cmd:
                              msgs = cmd.replace('id line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)
                          if 'welcome ' in cmd:
                              spl = cmd.replace('welcome ','')
                              if spl == 'on':
                                  if msg.to in LeaZie["welcome"]:
                                       msgs = "ᴡᴀs ᴏɴ"
                                  else:
                                       LeaZie["welcome"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏɴ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴡᴇʟᴄᴏᴍᴇ」" + msgs)
                              elif spl == 'off':
                                    if msg.to in LeaZie["welcome"]:
                                         del LeaZie["welcome"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏғғ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴡᴀs ᴏғғ"
                                    cl.sendMessage(msg.to, "「sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴡᴇʟᴄᴏᴍᴇ 」" + msgs)
                          if 'left ' in cmd:
                              spl = cmd.replace('left ','')
                              if spl == 'on':
                                  if msg.to in LeaZie["leaveMsg"]:
                                       msgs = "ᴡᴀs ᴏɴ"
                                  else:
                                       LeaZie["leaveMsg"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏɴ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「sᴇɴᴅ ᴍᴇssᴀɢᴇ ʟᴇᴀᴠᴇ」" + msgs)
                              elif spl == 'off':
                                    if msg.to in LeaZie["leaveMsg"]:
                                         del LeaZie["leaveMsg"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏғғ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴡᴀs ᴏғғ"
                                    cl.sendMessage(msg.to, "「sᴇɴᴅ ᴍᴇssᴀɢᴇ ʟᴇᴀᴠᴇ」" + msgs)
                          if 'proqr ' in cmd:
                              spl = cmd.replace('proqr ','')
                              if spl == 'on':
                                  if msg.to in LeaZie["proqr"]:
                                       msgs = "ᴡᴀs ᴏɴ"
                                  else:
                                       LeaZie["proqr"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏɴ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ʟɪɴᴋ」" + msgs)
                              elif spl == 'off':
                                    if msg.to in LeaZie["proqr"]:
                                         del LeaZie["proqr"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏғғ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴡᴀs ᴏғғ"
                                    cl.sendMessage(msg.to, "「ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ʟɪɴᴋ」" + msgs)
                          if 'prokick ' in cmd:
                              spl = cmd.replace('prokick ','')
                              if spl == 'on':
                                  if msg.to in LeaZie["proKick"]:
                                       msgs = "ᴡᴀs ᴏɴ"
                                  else:
                                       LeaZie["proKick"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏɴ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「ᴘʀᴏᴛᴇᴄᴛ ᴋɪᴄᴋ」" + msgs)
                              elif spl == 'off':
                                    if msg.to in LeaZie["proKick"]:
                                         del LeaZie["proKick"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏғғ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴡᴀs ᴏғғ"
                                    cl.sendMessage(msg.to, "「ᴘʀᴏᴛᴇᴄᴛ ᴋɪᴄᴋ」" + msgs)
                          if 'proinvite ' in cmd:
                              spl = cmd.replace('proinvite ','')
                              if spl == 'on':
                                  if msg.to in LeaZie["proInvite"]:
                                       msgs = "ᴡᴀs ᴏɴ"
                                  else:
                                       LeaZie["proInvite"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏɴ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ」" + msgs)
                              elif spl == 'off':
                                    if msg.to in LeaZie["proInvite"]:
                                         del LeaZie["proInvite"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏғғ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴡᴀs ᴏғғ"
                                    cl.sendMessage(msg.to, "「ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ」" + msgs)
                          if 'procancel ' in cmd:
                              spl = cmd.replace('procancel ','')
                              if spl == 'on':
                                  if msg.to in LeaZie["proCancel"]:
                                       msgs = "ᴡᴀs ᴏɴ"
                                  else:
                                       LeaZie["proCancel"] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏɴ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ」" + msgs)
                              elif spl == 'off':
                                    if msg.to in LeaZie["proCancel"]:
                                         LeaZie["proCancel"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏғғ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴡᴀs ᴏғғ"
                                    cl.sendMessage(msg.to, "「ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ」" + msgs)
                          if 'protect ' in cmd:
                              spl = cmd.replace('protect ','')
                              if spl == 'on':
                                  if msg.to in LeaZie["proqr"]:
                                       msgs = ""
                                  else:
                                       LeaZie["proqr"][msg.to] = True
                                  if msg.to in LeaZie["proKick"]:
                                      msgs = ""
                                  else:
                                       LeaZie["proKick"][msg.to] = True
                                  if msg.to in LeaZie["proInvite"]:
                                      msgs = ""
                                  else:
                                       LeaZie["proInvite"][msg.to] = True
                                  if msg.to in LeaZie["proCancel"]:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "ᴡᴀs ᴏɴ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  else:
                                       LeaZie["proCancel"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏɴ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「ᴀʟʟ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ」" + msgs)
                              elif spl == 'off':
                                    if msg.to in LeaZie["proqr"]:
                                         del LeaZie["proqr"][msg.to]
                                    else:
                                         msgs = ""
                                    if msg.to in LeaZie["proKick"]:
                                         del LeaZie["proKick"][msg.to]
                                    else:
                                         msgs = ""
                                    if msg.to in LeaZie["proInvite"]:
                                         del LeaZie["proInvite"][msg.to]
                                    else:
                                         msgs = ""
                                    if msg.to in LeaZie["proCancel"]:
                                         del LeaZie["proCancel"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏғғ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴡᴀs ᴏғғ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "「ᴀʟʟ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ」" + msgs)
                          if 'inta ' in cmd:
                              spl = cmd.replace('inta ','')
                              if spl == 'on':
                                  if msg.to in LeaZie["intaPoint"]:
                                       msgs = "ᴡᴀs ᴏɴ"
                                  else:
                                       LeaZie["intaPoint"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏɴ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「ɪɴᴛᴀ ᴘᴏɪɴᴛ」" + msgs)
                              elif spl == 'off':
                                    if msg.to in LeaZie["intaPoint"]:
                                         del LeaZie["intaPoint"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴀʟʟʀᴇᴀᴅʏ ᴏғғ ɪɴ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴡᴀs ᴏғғ"
                                    cl.sendMessage(msg.to, "「ɪɴᴛᴀ ᴘᴏɪɴᴛ」" + msgs)
                          if "bot kick " in cmd:
                              if 'MENTION' in msg.contentMetadata.keys():
                                  mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  for mention in mentions['MENTIONEES']:
                                      uid = mention['M']
                                      if uid in Zie or uid in Bots or uid in LeaZie["Bots"]:
                                          continue
                                      try:
                                          random.choice(botlist).kickoutFromGroup(msg.to, [uid])
                                          wait["blacklist"][uid] = True
                                      except:
                                          cl.sendMessage(msg.to,"ʟɪᴍɪᴛʙᴏsᴋᴜʜ")
                          if "invite" in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target in wait["blacklist"]:
                                       cl.sendMessage(msg.to, "sᴏʀʀʏ ᴄᴏɴᴛᴀᴄᴛ ɪɴ ʙʟᴀᴄᴋʟɪsᴛ")
                                   else:
                                       try:
                                           ka.findAndAddContactsByMid(target)
                                           ka.inviteIntoGroup(msg.to, [target])
                                       except:
                                           ka.sendMessage(msg.to, "sᴏʀʀʏ!! ᴛᴀʀɢᴇᴛ ɪɴᴠɪᴛᴇ ɴᴏᴛ ғᴏᴜɴᴅ ᴏʀ ʙᴏᴛs ʟɪᴍɪᴛ ɪɴᴠɪᴛᴇ")
                                           try:
                                               kb.findAndAddContactsByMid(target)
                                               kb.inviteIntoGroup(msg.to, [target])
                                           except:
                                               kb.sendMessage(msg.to, "sᴏʀʀʏ!! ᴛᴀʀɢᴇᴛ ɪɴᴠɪᴛᴇ ɴᴏᴛ ғᴏᴜɴᴅ ᴏʀ ʙᴏᴛs ʟɪᴍɪᴛ ɪɴᴠɪᴛᴇ")
                                               try:
                                                   kc.findAndAddContactsByMid(target)
                                                   kc.inviteIntoGroup(msg.to, [target])
                                               except:
                                                   kc.sendMessage(msg.to, "sᴏʀʀʏ!! ᴛᴀʀɢᴇᴛ ɪɴᴠɪᴛᴇ ɴᴏᴛ ғᴏᴜɴᴅ ᴏʀ ʙᴏᴛs ʟɪᴍɪᴛ ɪɴᴠɪᴛᴇ")
                          if "invite1" in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target in wait["blacklist"]:
                                       cl.sendMessage(msg.to, "sᴏʀʀʏ ᴄᴏɴᴛᴀᴄᴛ ɪɴ ʙʟᴀᴄᴋʟɪsᴛ")
                                   else:
                                       try:
                                           kd.findAndAddContactsByMid(target)
                                           kd.inviteIntoGroup(msg.to, [target])
                                       except:
                                           kd.sendMessage(msg.to, "sᴏʀʀʏ!! ᴛᴀʀɢᴇᴛ ɪɴᴠɪᴛᴇ ɴᴏᴛ ғᴏᴜɴᴅ ᴏʀ ʙᴏᴛs ʟɪᴍɪᴛ ɪɴᴠɪᴛᴇ")
                                           try:
                                               ke.findAndAddContactsByMid(target)
                                               ke.inviteIntoGroup(msg.to, [target])
                                           except:
                                               try:
                                                   kf.findAndAddContactsByMid(target)
                                                   kf.inviteIntoGroup(msg.to, [target])
                                               except:
                                                   kf.sendMessage(msg.to, "sᴏʀʀʏ!! ᴛᴀʀɢᴇᴛ ɪɴᴠɪᴛᴇ ɴᴏᴛ ғᴏᴜɴᴅ ᴏʀ ʙᴏᴛs ʟɪᴍɪᴛ ɪɴᴠɪᴛᴇ")
                          if "kiss " in cmd:
                              if 'MENTION' in msg.contentMetadata.keys():
                                  mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  for mention in mentions['MENTIONEES']:
                                      uid = mention['M']
                                      if uid in Zie or uid in Bots or uid in LeaZie["Bots"]:
                                          continue
                                      try:
                                          cl.kickoutFromGroup(msg.to, [uid])
                                      except:
                                          cl.sendMessage(msg.to,"ʟɪᴍɪᴛʙᴏsᴋᴜʜ")
                          if "@cancelin" in cmd:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "kσsσηg вσss ")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     if x not in Zie and x not in Bots and x not in LeaZie["Bots"] and x not in LeaZie["admin"]:
                                       cl.cancelGroupInvitation(msg.to, [x])
                                       time.sleep(0.3)
                                   cl.sendMessage(to, "∂σηє.")
                          if "bot cancel" in cmd:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "kσsσηg вσss ")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     for j in [ka,kb,kc,kd,ke,kf]:
                                       if x not in Zie and x not in Bots and x not in LeaZie["Bots"] and x not in LeaZie["admin"]:
                                         j.cancelGroupInvitation(msg.to, [x])
                                         time.sleep(0.3)
                                   cl.sendMessage(to, "∂σηє.")
                          if "addadmin " in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target in LeaZie["admin"]:
                                       cl.sendMessage(msg.to,"ωαs ıη α∂мıη")
                                   else:
                                       try:
                                           LeaZie["admin"][target] = True
                                           cl.sendMessage(msg.to,"sυccєs α∂∂ α∂мıη")
                                       except:
                                           pass
                          if "addbot " in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target in LeaZie["Bots"]:
                                       cl.sendMessage(msg.to,"ωαs ıη вσтs")
                                   else:
                                       try:
                                           LeaZie["Bots"][target] = True
                                           cl.sendMessage(msg.to,"sυccєs α∂∂ вσтs")
                                       except:
                                           pass
                          if "deladmin " in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in LeaZie["admin"]:
                                       cl.sendMessage(msg.to,"ησт ıη α∂мıη")
                                   else:
                                       try:
                                           del LeaZie["admin"][target]
                                           cl.sendMessage(msg.to,"sυccєs ∂єłєтє α∂мıη")
                                       except:
                                           pass
                          if "delbot " in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in LeaZie["Bots"]:
                                       cl.sendMessage(msg.to,"ησт ıη ʙᴏᴛs")
                                   else:
                                       try:
                                           del LeaZie["Bots"][target]
                                           cl.sendMessage(msg.to,"sυccєs ∂єłєтє вσтs")
                                       except:
                                           pass
                          if "addcontact" in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                 for c in [cl,ka,kb,kc,kd,ke,kf]:
                                   gid = c.getAllContactIds()
                                   if target in gid:
                                       c.sendMessage(msg.to,"ᴛᴀʀɢᴇᴛ ᴡᴀs ɪɴ ᴄᴏɴᴛᴀᴄᴛ ʟɪsᴛ")
                                   else:
                                       try:
                                           bit = c.getContact(target)
                                           c.findAndAddContactsByMid(bit.mid)
                                           c.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴀᴅᴅᴇᴅ ᴄᴏɴᴛᴀᴄᴛ " + c.getContact(target).displayName)
                                       except:
                                           cl.sendMessage(msg.to,"ʙᴏᴛs ʟɪᴍɪᴛ ᴀᴅᴅ ᴄᴏɴᴛᴀᴄᴛ")
                          if cmd.startswith("join to "):
                                text = cmd.split(" ")
                                number = text[2]
                                if number.isdigit():
                                    groups = cl.getGroupIdsJoined()
                                    if int(number) < len(groups) and int(number) >= 0:
                                        groupid = groups[int(number)]
                                        try:
                                            cl.findAndAddContactsByMid(sender)
                                            cl.inviteIntoGroup(groupid,[sender])
                                            groupname = cl.getGroup(groupid).name
                                            cl.sendMessage(msg.to,"Successfully invite %s"%groupname)
                                        except:
                                            cl.sendMessage(msg.to," Invite banned Bro " + cl.getContact(sender).displayName)

                          if cmd == "groups":
                                gid = cl.getGroupIdsJoined()
                                num = 0
                                g = ""
                                for i in gid:
                                    g += "%i - " % num + "%s" % (cl.getGroup(i).name + "(%s)\n" % (str (len (cl.getGroup(i).members))))
                                    num = (num+1)
                                cl.sendMessage(msg.to,"Group List:\n\n"+ g + "Total Groups : " + str(len(gid)))

                          if cmd == "cbot" or text.lower() == 'clear bot':
                              ang = cl.getContacts(LeaZie["Bots"])
                              mc = "%i вστs " % len(ang)
                              cl.sendMessage(msg.to,"ᴅᴏɴᴇ ᴄʟᴇᴀʀ " +mc)
                              LeaZie["Bots"] = {}
                          if cmd == "cadmin" or text.lower() == 'clear admin':
                              ang = cl.getContacts(LeaZie["admin"])
                              mc = "%i ᴀᴅᴍɪɴ " % len(ang)
                              cl.sendMessage(msg.to,"ᴅᴏɴᴇ ᴄʟᴇᴀʀ " +mc)
                              LeaZie["admin"] = {}
                          if cmd == "admin:on" or text.lower() == 'admin:on':
                                LeaZie["addadmin"] = True
                                cl.sendMessage(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ...")
                          if cmd == "admin:del" or text.lower() == 'admin:del':
                                LeaZie["deladmin"] = True
                                cl.sendMessage(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ...")
                          if cmd == "admin:off" or text.lower() == 'admin off':
                                LeaZie["addadmin"] = False
                                cl.sendMessage(msg.to,"ᴀʟʟʀᴇᴀᴅʏ ᴏғғ")
                          if cmd == "deladmin:off" or text.lower() == 'deladmin off':
                                LeaZie["deladmin"] = False
                                cl.sendMessage(msg.to,"ᴀʟʟʀᴇᴀᴅʏ ᴏғғ")
                          if cmd == "bot:on" or text.lower() == 'bot on':
                                LeaZie["abots"] = True
                                cl.sendMessage(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ...")
                          if cmd == "bot:off" or text.lower() == 'bot off':
                                LeaZie["abots"] = False
                                cl.sendMessage(msg.to,"ᴀʟʟʀᴇᴀᴅʏ ᴏғғ")
                          if cmd == "bot:del" or text.lower() == 'bot del':
                                LeaZie["dbots"] = True
                                cl.sendMessage(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ...")
                          if cmd == "delbot:off" or text.lower() == 'delbot off':
                                LeaZie["dbots"] = False
                                cl.sendMessage(msg.to,"ᴀʟʟʀᴇᴀᴅʏ ᴏғғ")
                          if cmd == "allrefresh" or text.lower() == 'refresh':
                                LeaZie["addadmin"] = False
                                LeaZie["deladmin"] = False
                                LeaZie["abots"] = False
                                LeaZie["dbots"] = False
                                LeaZie["ablacklist"] = False
                                LeaZie["dblacklist"] = False
                                LeaZie["LikeOn"] = False
                                cl.sendMessage(msg.to," ❂𝐁𝐨𝐭 𝐭𝐞𝐥𝐚𝐡 𝐝𝐢𝐫𝐞𝐟𝐫𝐞𝐬𝐡❂")
                          if cmd == "killban":
                                if msg.toType == 2:
                                    group = cl.getGroup(msg.to)
                                    gMembMids = [contact.mid for contact in group.members]
                                    matched_list = []
                                    for tag in wait["blacklist"]:
                                        matched_list+=filter(lambda str: str == tag, gMembMids)
                                    if matched_list == []:
                                        pass
                                    for jj in matched_list:
                                        try:
                                            klist=[ka,kb,kc,kd,ke,kf]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[jj])
                                            print (msg.to,[jj])
                                        except:
                                            pass
                          if cmd == "ctbot" or text.lower() == 'ctbot':
                                ma = ""
                                for i in LeaZie["Bots"]:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                          if cmd == "ctban" or text.lower() == 'ctbanlist':
                                ma = ""
                                for i in wait["blacklist"]:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                          if cmd == "contact:on" or text.lower() == 'contact on':
                                LeaZie["contact"] = True
                                cl.sendMessage(msg.to,"ᴄʜᴇᴄᴋ ᴅᴇᴛᴀɪʟ ᴄᴏɴᴛᴀᴄᴛ ᴀʟʟʀᴇᴀᴅʏ ᴏɴ")
                          if cmd == "contact:off" or text.lower() == 'contact off':
                                LeaZie["contact"] = False
                                cl.sendMessage(msg.to,"ᴄʜᴇᴄᴋ ᴅᴇᴛᴀɪʟ ᴄᴏɴᴛᴀᴄᴛ ᴀʟʟʀᴇᴀᴅʏ ᴏғғ")
                          if cmd == "respon:on" or text.lower() == 'respon on':
                                LeaZie["detectMention"] = True
                                cl.sendMessage(msg.to,"ʀᴇsᴘᴏɴ ᴍᴇɴᴛɪᴏɴ ᴀʟʟʀᴇᴀᴅʏ ᴏɴ")
                          if cmd == "respon:off" or text.lower() == 'respon off':
                                LeaZie["detectMention"] = False
                                cl.sendMessage(msg.to,"ʀᴇsᴘᴏɴ ᴍᴇɴᴛɪᴏɴ ᴀʟʟʀᴇᴀᴅʏ ᴏғғ")
                          if cmd == "autojoin:on" or text.lower() == 'autojoin on':
                                LeaZie["autoJoin"] = True
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏᴊᴏɪɴ ᴀʟʟʀᴇᴀᴅʏ ᴏɴ")
                          if cmd == "autojoin:off" or text.lower() == 'autojoin off':
                                LeaZie["autoJoin"] = False
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏᴊᴏɪɴ ᴀʟʟʀᴇᴀᴅʏ ᴏғғ")
                          if cmd == "like:on" or text.lower() == 'like on':
                              LeaZie["LikeOn"] = True
                              cl.sendMessage(msg.to,"ᴀᴜᴛᴏʟɪᴋᴇ ᴀʟʟʀᴇᴀᴅʏ ᴏɴ")
                          if cmd == "like:off" or text.lower() == 'like off':
                              LeaZie["LikeOn"] = False
                              cl.sendMessage(msg.to,"ᴀᴜᴛᴏʟɪᴋᴇ ᴀʟʟʀᴇᴀᴅʏ ᴏғғ")
                          if cmd == "scan:on" or text.lower() == 'scan on':
                                LeaZie["checkmid"] = True
                                cl.sendMessage(msg.to,"ᴄʜᴇᴄᴋ ᴍɪᴅ ᴄᴏɴᴛᴀᴄᴛ ᴀʟʟʀᴇᴀᴅʏ ᴏɴ")
                          if cmd == "scan:off" or text.lower() == 'scan off':
                                LeaZie["checkmid"] = False
                                cl.sendMessage(msg.to,"ᴄʜᴇᴄᴋ ᴍɪᴅ ᴄᴏɴᴛᴀᴄᴛ ᴀʟʟʀᴇᴀᴅʏ ᴏғғ")
                          if cmd == "post:on" or text.lower() == 'post on':
                                LeaZie["checkPost"] = True
                                cl.sendMessage(msg.to,"ᴅᴇᴛᴇᴄᴛ ᴘᴏsᴛ ᴀʟʟʀᴇᴀᴅʏ ᴏɴ")
                          if cmd == "post:off" or text.lower() == 'post off':
                                LeaZie["checkPost"] = False
                                cl.sendMessage(msg.to,"ᴅᴇᴛᴇᴄᴛ ᴘᴏsᴛ ᴀʟʟʀᴇᴀᴅʏ ᴏғғ")
                          if cmd == "unsend:on" or text.lower() == 'unsend on':
                                LeaZie["Unsend"] = True
                                cl.sendMessage(msg.to,"ᴅᴇᴛᴇᴄᴛ ᴜɴsᴇɴᴅ ᴍᴇssᴀɢᴇ ᴀʟʟʀᴇᴅʏ ᴏɴ")
                          if cmd == "unsend:off" or text.lower() == 'unsend off':
                                LeaZie["Unsend"] = False
                                cl.sendMessage(msg.to,"ᴅᴇᴛᴇᴄᴛ ᴜɴsᴇɴᴅ ᴍᴇssᴀɢᴇ ᴀʟʟʀᴇᴅʏ ᴏғғ")
                          if cmd == "autoadd:on" or text.lower() == 'autoadd on':
                                LeaZie["autoAdd"] = True
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ ᴀʟʟʀᴇᴅʏ ᴏɴ")
                          if cmd == "autoadd:off" or text.lower() == 'autoadd off':
                                LeaZie["autoAdd"] = False
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ ᴀʟʟʀᴇᴅʏ ᴏғғ")
                          if cmd == "sticker:on" or text.lower() == 'sticker on':
                                LeaZie["sticker"] = True
                                cl.sendMessage(msg.to,"ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ ᴀʟʟʀᴇᴅʏ ᴏɴ")
                          if cmd == "sticker:off" or text.lower() == 'sticker off':
                                LeaZie["sticker"] = False
                                cl.sendMessage(msg.to,"ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ ᴀʟʟʀᴇᴅʏ ᴏғғ")
                          if cmd == "jticket:on" or text.lower() == 'jticket on':
                                LeaZie["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ ᴀʟʟʀᴇᴅʏ ᴏɴ")
                          if cmd == "jticket:off" or text.lower() == 'jticket off':
                                LeaZie["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ ᴀʟʟʀᴇᴅʏ ᴏғғ")
                          if "ban " in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target in wait["blacklist"]:
                                       cl.sendMessage(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ᴡᴀs ɪɴ ʙʟᴀᴄᴋʟɪsᴛ")
                                   else:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"sᴜᴄᴄᴇs ᴀᴅᴅ ᴛᴏ ʙʟᴀᴄᴋʟɪsᴛ")
                                       except:
                                           pass
                          if "delbl " in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in wait["blacklist"]:
                                       cl.sendMessage(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ɴᴏᴛ ɪɴ ʙʟᴀᴄᴋʟɪsᴛ")
                                   else:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"sᴜᴄᴄᴇs ʀᴇᴍᴏᴠᴇ ɪɴ ʙʟᴀᴄᴋʟɪsᴛ")
                                       except:
                                           pass
                          if cmd == "ban:on" or text.lower() == 'ban on':
                                LeaZie["ablacklist"] = True
                                cl.sendMessage(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ...")
                          if cmd == "ban:off" or text.lower() == 'ban off':
                                LeaZie["ablacklist"] = False
                                cl.sendMessage(msg.to,"ᴀʟʟʀᴇᴀᴅʏ ᴏғғ")
                          if cmd == "unban:on" or text.lower() == 'unban on':
                                LeaZie["dblacklist"] = True
                                cl.sendMessage(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ...")
                          if cmd == "unban:off" or text.lower() == 'unban off':
                                LeaZie["dblacklist"] = False
                                cl.sendMessage(msg.to,"ᴀʟʟʀᴇᴀᴅʏ ᴏғғ")
                          if cmd == "banlist" or text.lower() == 'blacklist':
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"| Terciduk ●\n\n"+ma+"\nTotal : 「%s」 Terciduk " %(str(len(wait["blacklist"]))))
                          if cmd == "cban" or text.lower() == 'cban':
                              ang = cl.getContacts(wait["blacklist"])
                              mc = "%i Tersangka " % len(ang)
                              cl.sendMessage(msg.to,"Di Ampuni " +mc)
                              wait["blacklist"] = {}
                          if 'add: ' in cmd:
                              ang = cmd.replace('add: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  LeaZie["message"] = ang
                                  cl.sendMessage(msg.to, "「ᴍᴇssᴀɢᴇ ᴀᴅᴅ」 :\n\n「{}」".format(str(ang)))
                          if 'left: ' in cmd:
                              ang = cmd.replace('left: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  LeaZie["leftmsg"] = ang
                                  cl.sendMessage(msg.to, "「ᴍᴇssᴀɢᴇ ʟᴇᴀᴠᴇ」 :\n\n「{}」".format(str(ang)))
                          if 'welcome: ' in cmd:
                              ang = cmd.replace('welcome: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  LeaZie["sambutan"] = ang
                                  cl.sendMessage(msg.to, "「ᴍᴇssᴀɢᴇ ᴡᴇʟʟᴄᴏᴍᴇ」 :\n\n「{}」".format(str(ang)))
                          if 'tag: ' in cmd:
                              ang = cmd.replace('tag: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  LeaZie["msgTag"] = ang
                                  cl.sendMessage(msg.to, "「ᴍᴇssᴀɢᴇ ᴍᴇɴᴛɪᴏɴ」:\n\n「{}」".format(str(ang)))
                          if 'spam: ' in cmd:
                              ang = cmd.replace('spam: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  LeaZie["spamMsg"] = ang
                                  cl.sendMessage(msg.to, "「ᴍᴇssᴀɢᴇ sᴘᴀᴍ」 :\n\n「{}」".format(str(ang)))
                          if 'sider: ' in cmd:
                              znf = cmd.replace('sider: ','')
                              if znf in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  LeaZie["siderMsg"] = znf
                                  cl.sendMessage(msg.to, "「ᴍᴇssᴀɢᴇ sɪᴅᴇʀ」:\n\n「{}」".format(str(znf)))
                          if 'invmid ' in cmd:
                              znf = cmd.replace('invmid ','')
                              try:
                                  cl.findAndAddContactsByMid(znf)
                                  cl.sendContact(to,znf)
                              except Exception as e:
                                  traceback.print_exc()
                                  
                          if cmd == "cekmsg":
                               cl.sendMessage(msg.to, "「ᴍᴇssᴀɢᴇ ᴀᴅᴅ」 :\n「 " + str(LeaZie["message"]) + " 」")
                               cl.sendMessage(msg.to, "「ᴍᴇssᴀɢᴇ sɪᴅᴇʀ」:\n「 " + str(LeaZie["siderMsg"]) + " 」")
                               cl.sendMessage(msg.to, "「ᴍᴇssᴀɢᴇ ᴍᴇɴᴛɪᴏɴ」:\n「 " + str(LeaZie["msgTag"]) + " 」")
                               cl.sendMessage(msg.to, "「ᴍᴇssᴀɢᴇ sᴘᴀᴍ」:\n「 " + str(LeaZie["spamMsg"]) + " 」")
                               cl.sendMessage(msg.to, "「ᴍᴇssᴀɢᴇ ᴡᴇʟʟᴄᴏᴍᴇ」:\n「 " + str(LeaZie["sambutan"]) + " 」")
                               cl.sendMessage(msg.to, "「ᴍᴇssᴀɢᴇ ʟᴇᴀᴠᴇ」:\n「 " + str(LeaZie["leftmsg"]) + " 」")
#===========JOIN TICKET============#
                          if "/ti/g/" in msg.text.lower():
                              if LeaZie["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "sᴜᴄᴄᴇs ᴊᴏɪɴ : %s" % str(group.name))
                          if cmd == "cleanse":
                               if msg.toType == 2:
                                  group = cl.getGroup(msg.to)
                                  nama = [contact.mid for contact in group.members]
                                  for x in nama:
                                      if x not in Lea:
                                          if x not in LeaZie["Bots"]:
                                              if x not in LeaZie["admin"]:
                                                  try:
                                                      klist=[ka,kb,kc,kd,ke,kf]
                                                      ang=random.choice(klist)
                                                      ang.kickoutFromGroup(msg.to,[x])
                                                  except:
                                                      print ("limit")
                          if msg.text.lower() in ["check"]:
                                anu = cl.getGroup(msg.to)
                                oncom = ["ub52696beffd79277a44e6c6133a5723d"] #MID PUSKUN
                                for _mid in oncom:
                                    message="╭━❁𝕯'𝖕𝖗𝖔 𝕶𝖎𝖑𝖑𝖊𝖗❁━─\n"
                                    try:
                                        cl.kickoutFromGroup(msg.to,[_mid])
                                        message+="│「☇ғʀᴇsʜ」ᴋɪᴄᴋ\n"
                                    except:
                                        message+="│「🤒 ʟɪᴍɪᴛ」ᴋɪᴄᴋ\n"
                                    try:
                                        ka.inviteIntoGroup(msg.to,[_mid])
                                        message+="│「☇ғʀᴇsʜ」ɪɴᴠɪᴛᴇ\n"
                                    except:
                                        message+="│「🤒 ʟɪᴍɪᴛ」ɪɴᴠɪᴛᴇ\n"
                                    try:
                                        kb.kickoutFromGroup(msg.to,[_mid])
                                        message+="│「☇ғʀᴇsʜ」ᴋɪᴄᴋ\n"
                                    except:
                                        message+="│「🤒 ʟɪᴍɪᴛ」ᴋɪᴄᴋ\n"
                                    try:
                                        kc.inviteIntoGroup(msg.to,[_mid])
                                        message+="│「☇ғʀᴇsʜ」ɪɴᴠɪᴛᴇ\n"
                                    except:
                                        message+="│「🤒 ʟɪᴍɪᴛ」ɪɴᴠɪᴛᴇ\n"
                                    try:
                                        kd.kickoutFromGroup(msg.to,[_mid])
                                        message+="│「☇ғʀᴇsʜ」ᴋɪᴄᴋ\n"
                                    except:
                                        message+="│「🤒 ʟɪᴍɪᴛ」ᴋɪᴄᴋ\n"
                                    try:
                                        ke.inviteIntoGroup(msg.to,[_mid])
                                        message+="│「☇ғʀᴇsʜ」ɪɴᴠɪᴛᴇ\n"
                                    except:
                                        message+="│「🤒 ʟɪᴍɪᴛ」ɪɴᴠɪᴛᴇ\n"
                                    try:
                                        kf.kickoutFromGroup(msg.to,[_mid])
                                        message+="│「☇ғʀᴇsʜ」ᴋɪᴄᴋ\n"
                                    except:
                                        message+="│「🤒 ʟɪᴍɪᴛ」ᴋɪᴄᴋ\n"
                                    message+="╰━━━━━━━━─"
                                    cl.sendMessage(msg.to,message)
                          if msg.text.lower() in ["kicker check"]:
                                anu = cl.getGroup(msg.to)
                                oncom = ["ub52696beffd79277a44e6c6133a5723d"] #MID PUSKUN
                                for _mid in oncom:
                                    message="╭━❁𝕯'𝖕𝖗𝖔 𝕶𝖎𝖑𝖑𝖊𝖗❁━─\n"
                                    try:
                                        k1.kickoutFromGroup(msg.to,[_mid])
                                        message+="│「☇ғʀᴇsʜ」ᴋɪᴄᴋ\n"
                                    except:
                                        message+="│「🤒 ʟɪᴍɪᴛ」ᴋɪᴄᴋ\n"
                                    message+="╰━━━━━━━━─"
                                    cl.sendMessage(msg.to,message)

      except Exception as e:
          print(e)

def Flist(self,to):
    ma = "╭━━━━━━━━━━━─\n╰─⟦ Friend List ⟧\n\n"
    a = 0
    gid = self.getAllContactIds()
    for i in gid:
        G = self.getContact(i)
        a = a + 1
        end = "\n"
        ma += "∘· " + str(a) + ". " +G.displayName+ "\n"
    self.sendMessage(to,ma+"\n╭──「 "+str(len(gid))+"  Friends  」\n╰━━━━━━━━━━━─")
def Sp(self,to):
      get_group_time_start = time.time()
      get_group = self.getGroupIdsJoined()
      get_group_time = time.time() - get_group_time_start
      self.sendMessage(to, "[ ~G : %.4f ⚡]" % (get_group_time/2))

def Speed(self,to):
      get_group_time_start = time.time()
      get_group = self.getGroupIdsJoined()
      get_group_time = time.time() - get_group_time_start
      get_contact_time_start = time.time()
      get_contact = self.getContact(mid)
      get_contact_time = time.time() - get_contact_time_start
      get_profile_time_start = time.time()
      get_profile = self.getProfile()
      get_profile_time = time.time() - get_profile_time_start
      self.sendMessage(to, "[ ~P : %.4f ⚡]\n[ ~C : %.4f ⚡]\n[ ~G : %.4f ⚡]" % (get_profile_time/2,get_contact_time/2,get_group_time/2))

def likePost(self, mid, postId, likeType=1001):
    if mid is None:
        mid = cl.profile.mid
    if likeType not in [1001,1002,1003,1004,1005,1006]:
        raise Exception('Invalid parameter likeType')
    params = {'homeId': mid, 'sourceType': 'TIMELINE'}
    url = cl.server.urlEncode(cl.server.LINE_TIMELINE_API, '/v23/like/create', params)
    data = {'likeType': likeType, 'postId': postId, 'actorId': mid}
    r = cl.server.postContent(url, data=data, headers=cl.server.channelHeaders)
    return r.json()

def createComment(self, mid, postId, text):
    if mid is None:
        mid = self.profile.mid
    params = {'homeId': mid, 'sourceType': 'TIMELINE'}
    url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v39/comment/create.json', params)
    data = {'commentText': text, 'activityExternalId': postId, 'actorId': mid}
    data = json.dumps(data)
    r = self.server.postContent(url, data=data, headers=self.server.timelineHeaders)
    return r.json()

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "「reader {} member」\nhai ka.. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+LeaZie["siderMsg"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "「Member Join {}」\Wellcome ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+LeaZie["sambutan"]+"\ndi group : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def indukjs(grup,blaklist):
    try:
        cmd = 'bypass.js gid={} token={}'.format(grup, cl.authToken)
        for t in blaklist:
            if t not in Lea:
                cmd += ' uid={}'.format(t)
        success = execute_js(cmd)
        squad = [Amid,Bmid,Cmid,Dmid,Emid,Fmid]
        cl.inviteIntoGroup(grup, squad)
        try:ka.acceptGroupInvitation(grup);kb.acceptGroupInvitation(grup);kc.acceptGroupInvitation(grup);kd.acceptGroupInvitation(grup);ke.acceptGroupInvitation(grup);kf.acceptGroupInvitation(grup)
        except:ka.acceptGroupInvitation(grup);kb.acceptGroupInvitation(grup);kc.acceptGroupInvitation(grup);kd.acceptGroupInvitation(grup);ke.acceptGroupInvitation(grup);kf.acceptGroupInvitation(grup)
    except:pass
    print ('success')
def kajs(grup,blaklist):
    try:
        cmd = 'bypass.js gid={} token={}'.format(grup, ka.authToken)
        for t in blaklist:
            if t not in Lea:
                cmd += ' uid={}'.format(t)
        success = execute_js(cmd)
        squad = [mid,Bmid,Cmid,Dmid,Emid,Fmid]
        ka.inviteIntoGroup(grup, squad)
        try:cl.acceptGroupInvitation(grup);kb.acceptGroupInvitation(grup);kc.acceptGroupInvitation(grup);kd.acceptGroupInvitation(grup);ke.acceptGroupInvitation(grup);kf.acceptGroupInvitation(grup)
        except:cl.acceptGroupInvitation(grup);kb.acceptGroupInvitation(grup);kc.acceptGroupInvitation(grup);kd.acceptGroupInvitation(grup);ke.acceptGroupInvitation(grup);kf.acceptGroupInvitation(grup)
    except:pass
    print ('success')
def kbjs(grup,blaklist):
    try:
        cmd = 'bypass.js gid={} token={}'.format(grup, kb.authToken)
        for t in blaklist:
            if t not in Lea:
                cmd += ' uid={}'.format(t)
        success = execute_js(cmd)
        squad = [mid,Amid,Cmid,Dmid,Emid,Fmid]
        kb.inviteIntoGroup(grup, squad)
        try:cl.acceptGroupInvitation(grup);ka.acceptGroupInvitation(grup);kc.acceptGroupInvitation(grup);kd.acceptGroupInvitation(grup);ke.acceptGroupInvitation(grup);kf.acceptGroupInvitation(grup)
        except:cl.acceptGroupInvitation(grup);ka.acceptGroupInvitation(grup);kc.acceptGroupInvitation(grup);kd.acceptGroupInvitation(grup);ke.acceptGroupInvitation(grup);kf.acceptGroupInvitation(grup)
    except:pass
    print ('success')
def kcjs(grup,blaklist):
    try:
        cmd = 'bypass.js gid={} token={}'.format(grup, kc.authToken)
        for t in blaklist:
            if t not in Lea:
                cmd += ' uid={}'.format(t)
        success = execute_js(cmd)
        squad = [mid,Amid,Bmid,Dmid,Emid,Fmid]
        kc.inviteIntoGroup(grup, squad)
        try:cl.acceptGroupInvitation(grup);ka.acceptGroupInvitation(grup);kb.acceptGroupInvitation(grup);kd.acceptGroupInvitation(grup);ke.acceptGroupInvitation(grup);kf.acceptGroupInvitation(grup)
        except:cl.acceptGroupInvitation(grup);ka.acceptGroupInvitation(grup);kb.acceptGroupInvitation(grup);kd.acceptGroupInvitation(grup);ke.acceptGroupInvitation(grup);kf.acceptGroupInvitation(grup)
    except:pass
    print ('success')
def kdjs(grup,blaklist):
    try:
        cmd = 'bypass.js gid={} token={}'.format(grup, kd.authToken)
        for t in blaklist:
            if t not in Lea:
                cmd += ' uid={}'.format(t)
        success = execute_js(cmd)
        squad = [mid,Amid,Bmid,Cmid,Emid,Fmid]
        kd.inviteIntoGroup(grup, squad)
        try:cl.acceptGroupInvitation(grup);ka.acceptGroupInvitation(grup);kb.acceptGroupInvitation(grup);kc.acceptGroupInvitation(grup);ke.acceptGroupInvitation(grup);kf.acceptGroupInvitation(grup)
        except:cl.acceptGroupInvitation(grup);ka.acceptGroupInvitation(grup);kb.acceptGroupInvitation(grup);kc.acceptGroupInvitation(grup);ke.acceptGroupInvitation(grup);kf.acceptGroupInvitation(grup)
    except:pass
    print ('success')
def kejs(grup,blaklist):
    try:
        cmd = 'bypass.js gid={} token={}'.format(grup, ke.authToken)
        for t in blaklist:
            if t not in Lea:
                cmd += ' uid={}'.format(t)
        success = execute_js(cmd)
        squad = [mid,Amid,Bmid,Cmid,Dmid,Fmid]
        ke.inviteIntoGroup(grup, squad)
        try:cl.acceptGroupInvitation(grup);ka.acceptGroupInvitation(grup);kb.acceptGroupInvitation(grup);kc.acceptGroupInvitation(grup);kd.acceptGroupInvitation(grup);kf.acceptGroupInvitation(grup)
        except:cl.acceptGroupInvitation(grup);ka.acceptGroupInvitation(grup);kb.acceptGroupInvitation(grup);kc.acceptGroupInvitation(grup);kd.acceptGroupInvitation(grup);kf.acceptGroupInvitation(grup)
    except:pass
    print ('success')
def kfjs(grup,blaklist):
    try:
        cmd = 'bypass.js gid={} token={}'.format(grup, kf.authToken)
        for t in blaklist:
            if t not in Lea:
                cmd += ' uid={}'.format(t)
        success = execute_js(cmd)
        squad = [mid,Amid,Bmid,Cmid,Dmid,Emid]
        kf.inviteIntoGroup(grup, squad)
        try:cl.acceptGroupInvitation(grup);ka.acceptGroupInvitation(grup);kb.acceptGroupInvitation(grup);kc.acceptGroupInvitation(grup);kd.acceptGroupInvitation(grup);ke.acceptGroupInvitation(grup)
        except:cl.acceptGroupInvitation(grup);ka.acceptGroupInvitation(grup);kb.acceptGroupInvitation(grup);kc.acceptGroupInvitation(grup);kd.acceptGroupInvitation(grup);ke.acceptGroupInvitation(grup)
    except:pass
    print ('success')

def ProsesJs(grup, targets):
    x = cl.getGroup(grup)
    adb = [o.mid for o in x.members]
    matched_list = []
    for tag in wait["Member"]:
        matched_list+=filter(lambda str: str == tag, adb)
    if matched_list == []:
        pass
    for g in matched_list:
        try:
            ka.inviteIntoGroup(grup, [Smid])
            time.sleep(0.3)
            gaspol1 = threading.Thread(target=kajs, args=(grup,g)).start()
        except:
            try:
                kb.inviteIntoGroup(grup, [Smid])
                time.sleep(0.4)
                gaspol2 = threading.Thread(target=kbjs, args=(grup,g)).start()
            except:
                try:
                    kc.inviteIntoGroup(grup, [Smid])
                    time.sleep(0.5)
                    gaspol3 = threading.Thread(target=kcjs, args=(grup,g)).start()
                except:
                    try:
                        kd.inviteIntoGroup(grup, [Smid])
                        time.sleep(0.6)
                        gaspol4 = threading.Thread(target=kdjs, args=(grup,g)).start()
                    except:
                        try:
                            ke.inviteIntoGroup(grup, [Smid])
                            time.sleep(0.7)
                            gaspol5 = threading.Thread(target=kejs, args=(grup,g)).start()
                        except:
                            try:
                                kf.inviteIntoGroup(grup, [Smid])
                                time.sleep(0.8)
                                gaspol6 = threading.Thread(target=kfjs, args=(grup,g)).start()
                            except:
                                try:
                                    cl.inviteIntoGroup(grup, [Smid])
                                    time.sleep(0.9)
                                    gaspol7 = threading.Thread(target=indukjs, args=(grup,g)).start()
                                except:pass
    print("Bypass done")

def Save(grup):
    x = cl.getGroup(grup)
    if x.invitee == None:nama = []
    else:nama = [contact.mid for contact in x.invitee]
    for a in nama:
        if a not in Lea:
            nama.append(a)
    db = [contact.mid for contact in x.members]
    nami = []
    for c in db:
        if c not in Lea:
            nami.append(c)
    for y in nama:
        wait["Member"].append(y)
    for sd in nami:
        wait["Member"].append(sd)

while True:
    try:
        ops = linePoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                    linePoll.setRevision(op.revision)
                    thread = threading.Thread(target=bot, args=(op,))
                    thread.start()
    except Exception as e:
        print(e)

