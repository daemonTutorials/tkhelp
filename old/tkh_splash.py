#/usr/bin/python3

import tkinter as tk # GUI Interface
import sys # Exit Programm
import os

def splash(title , imageUrl, execute):
	# Initieren
	splash = tk.Tk()
	splash.overrideredirect(True) # Keine Balken
	
	# Starte Programm
	def startApp():
	    splash.withdraw()
	    os.system(execute)
	    sys.exit(0)
	
	#Fensterdaten
	screen_width  = int(splash.winfo_screenwidth())
	screen_height = int(splash.winfo_screenheight())
	
	width = 500
	height = 350
	
	xpos = (screen_width - width) / 2
	ypos = (screen_height - height) / 2
	
	splash.wm_geometry("%dx%d+%d+%d" % (width, ypos, xpos,ypos))
	
	# Canvas initialisieren
	splashScreen = tk.Canvas(splash, width=500, height=350, bg="white") # Canvas
	
	# Foto
	photo = tk.PhotoImage(file=imageUrl) # Das Foto
	splashScreen.create_image(0,0, image=photo, anchor=tk.NW) # Bild
	
	# If title under 20 Chars?
	if len(title) <= 20:
		splashScreen.create_text(250,50, text=title, font="30") # Titel
	else:
		print("ERROR: Your Title must be under 21 Chars! Your length: "+str(len(title)))
		sys.exit(0)
		
	splashScreen.pack(expand=tk.YES, fill=tk.BOTH) 
	# If pressed Strg+C
	try:
	    splash.after(2*1000, startApp)
	    splash.mainloop()
	    
	except KeyboardInterrupt:
		print("\nProgramm wird beendet!")
		splash.destroy()

