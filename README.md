# Discord-Bot
Ich zeige dir, wie du deinen eigenen Discord Bot ganz einfach erstellen kannst. 
Als erstees musst du dir eine App unter : https://discord.com/developers/applications erstellen.
Danach gehst du auf den Punkt Bot und erstellst einen.
Dort wird etwas von einem Token stehen, den musst du unbedingt aufbeahren, erstelle dir dafür am besten eine Textdatei und sichere sie, du kannst den Token zwar zurrücksetzen, aber dann musst du den Token austauschen. 

Jetzt musst du dir Discord-py installieren: 

# Discord py:
MAC OS:
python3 -m pip install -U discord.py
Windows:
py -3 -m pip install -U discord.py

# Discord-Bot #2
Jetzt installierst du dir VS-Code: https://code.visualstudio.com/download mit dem Python Addon, welches du im VS-Code Addon Store findest.
Jetzt installierst du dir das Programm Python : https://code.visualstudio.com/download
Du kannst die Datei Bot als Ansatz nutzen.

# Einrichten vom Skript
Wenn du dir das Skript dann heruntergeladen und in VS-Code geöffnet hast, wirst in "Zeile 10" sehen "activity = discord.Game(name="KI", type=1)" 
Das KI kannst z.B durch den Namen des Bots, oder ein beliebiges Wort ersetzen.
In "Zeile 11" wirstdu das sehen "await client.change_presence(status=discord.Status.online, activity=activity)" , das online kannst du durch online,idle,do_not_disturb oder invisble ersetzen.

In "Zeile 23,24" kannst du sehen "if message.content.startswith('hello'): await message.channel.send('Hello!')" das erste Hello ist ein Befehl, den könnt ihr beliebig verändern, der Teil wo das zweite Hello ist das, was passiert wenn z.B hello geschrieben wird.

Auf dem Skript könnt ihr eueren Bot aufbauen.

# Hosten vom Bot
Ihr könnt euern Bot z.B be replit hosten, wer den Bot aber bei sich Zuhause hosten möchte, kann ein Raspberry Pi mit dem Rapberry Pi Os nehmen, dann könnt ihr per VNC Connect einen Remote-Zugriff darauf einrichten , wo ihr auch den vollständigen Desktop vom Pi sehen könnt.
Alle Libarys die das Bot-Skript braucht, müsst ihr auch auf dem Pi installieren.
Discord-py müsst ihr auf dem Pi installieren, sonst geht gar nichts, die restlichen Liabrys die ihr euch nachinstalliert habt, welche auch vom Skript genutzt werden, müssen dann halt auch auf dem Pi installiert werden.



# Sonstiges
Discord Python bei GitHub: https://github.com/Rapptz/discord.py
                                  

