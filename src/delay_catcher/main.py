import sys
import time

from g_python.gextension import Extension
from g_python.hmessage import Direction, HMessage
from g_python.hpacket import HPacket

extension_info = {
    "title": "Delay Catcher",
    "description": "This bot analyzes room enter delay",
    "version": "1.0",
    "author": "Shib"
}

ext = Extension(extension_info, sys.argv)
ext.start()

last_delay = 0
delays = []
count = 1

# Delay catcher
def on_user_enter_room(message):
  try:
    (_, _, username, _, _, _, _, _, _, _, _, _, _, _, _, _, _) = message.packet.read('iisssiiisiisiiiib')

    if username.lower() == current_user.lower():
      global last_delay
      timestamp = int(round(time.time() * 1000))
      delays.append(timestamp)
          
      if len(delays) == 2:
        last_delay = delays[1] - delays[0]
      elif len(delays) > 2:
        global count
        current_delay = delays[2] - delays[1]
        ext.write_to_console(current_delay)
        
        if last_delay -10 <= current_delay <= last_delay + 10:
          count += 1
          ext.write_to_console(f"[AVVISO:] L'utente {current_user} è entrato con {current_delay} ms di ritardo per {count} volte consecutive")
        else:
          count = 1
              
        last_delay = current_delay
        delays.pop(0)
          
  except IndexError:
    pass
  except:
    print("[ERRORE:] Si è verificato un errore!")

                                              
if __name__ == "__main__":
  ext.write_to_console("[ESTENZIONE:] Estenzione avviata")
  global current_user
  current_user = input("[INPUT:] Inserisci nome utente: ")
  ext.write_to_console(f"[AVVISO:] L'utente selezionato è {current_user}")

ext.intercept(Direction.TO_CLIENT, on_user_enter_room, 'Users')
