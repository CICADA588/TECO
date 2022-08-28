##----------[ IMPORT MODULE AND INGREDIENT ]---------- ###
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json, threading,platform,string
import urllib3
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Cannot Install Rich Module, Try Manual Install (pip install rich)')
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from time import sleep
ses = requests.Session()
device = platform.platform()

###----------[ IMPORT RICH AND INGREDIENT ]---------- ###
from rich.table import Table as me
from rich.console import Console as sol
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
exec(base64.b64decode(b'ZnJvbSByaWNoIGltcG9ydCBwcmludCBhcyBjZXRhaw=='))
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
console = Console()
##----------[ IMPORT MODULEl ]---------- ###
from data import login_key as xx
from data import lainya as xjs
from src import cok
from data import logo as asy
from data import cokz as sx
from data import cek as cpp
#M1amSmyH
##----------[ license ]---------- #
def menu_apikey():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  asy.Logo().log()
  server = requests.get('https://pastebin.com/raw/bs6RnXNs').text  
  try:
    httpCaht = requests.get("https://pastebin.com/raw/bs6RnXNs").text
    if id in httpCaht:
      prints(Panel("""[green]YOUR LICENSE ACTIVATED...![/]
[blue]Thanks for Using Our Script . Please Use Wisely[/]
Support :[green]Team Medusa[/] & [cyan]Team Xnxx[/]""",style=f"bold green"));time.sleep (4)
      msg = str(os.geteuid())
      cok.Brute().moch_yayan()
      pass
    else:
      prints(Panel(f"""
[bold cyan]Premium Membership  Required [/] [bold red]You Are Not Premium User ❌[/]

[bold cyan]Your License Key 🔐[/]  Here > -> [bold green] {id} [/]

[bold cyan]Copy Your License and Press Enter to Send to the Admin

[bold red]FOR ACTIVATION (FB) INBOX  mafiavau[/]""",style=f"red"));time.sleep (0.9)

      os.system('xdg-open https://wa.me/+8801923554174')
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	#print(logo)
    	menu_apikey()
menu_apikey()
