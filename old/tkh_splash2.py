#/usr/bin/python3
import tkinter
from sys import exit
# Error Class

class SplashTitleError(Exception):
	def __init__(self, title):
		self.title = title
		self.value = repr("ERROR: Your Title must be under 21 Chars! Your length: "+str(len(self.title)))
        
	def __str__(self):
		return self.value

def splash(parent, title , image_url, splash_width=500, splash_height=350):
	# Initieren
	parent.withdraw()
	splash = tkinter.Toplevel(parent)
	splash.overrideredirect(True) # Keine Balken
	
	# Starte Programm
	def startApp():
	    splash.withdraw()
	    parent.deiconify()
	
	#Fensterdaten
	screen_width  = int(splash.winfo_screenwidth())
	screen_height = int(splash.winfo_screenheight())
	
	xpos = (screen_width - splash_width) / 2
	ypos = (screen_height - splash_height) / 2
	
	splash.wm_geometry("%dx%d+%d+%d" % (splash_width, ypos, xpos,ypos))
	
	# Canvas initialisieren
	splashScreen = tkinter.Canvas(splash, width=splash_width, height=splash_height, bg="white") # Canvas
	
	# Foto
	photo = tkinter.PhotoImage(file=image_url) # Das Foto
	splashScreen.create_image(0,0, image=photo, anchor=tkinter.NW) # Bild
	
	# If title under 20 Chars?
	if len(title) <= 20:
		splashScreen.create_text(250,50, text=title, font="30") # Titel
	else:
		raise SplashTitleError(title)
			
		
		
	splashScreen.pack(expand=tkinter.YES, fill=tkinter.BOTH) 
	# If pressed Strg+C
	try:
	    splash.after(2*1000, startApp)
	    
	except KeyboardInterrupt:
		print("\nYou must exit the Main Window!")
		

