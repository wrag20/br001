from tkinter import *
import sys, time

box = Tk()
box.geometry("800x600")

class Window(Frame):

	# Main Frane
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		master.title("Testing")
		lbl = Label(box, text="PIZZA TIME", relief='solid', height=5, width=50, justify='center')
		lbl.place(x=170,y=20)
		#lbl2 = Label(box, text="Order 1", relief='solid', height=5, width=20, justify='left')
		#lbl2.place(x=20, y=150)
		# Choice 1 Options
		ch1opt = ["--Choose Your Main Option--","Pizza","Sandwiches","Pasta"]
		psize = ["--Pick Your Size--","Small","Medium","Large"]
		#ptype = ["--Pick Your Flavor--","Hand Tossed Wisconsin","Hand Tossed Pizza","Thin Wisconsin 6 Cheese Pizza"]
		ptype = ["--Pick Your Flavor--","Hand Tossed Wisconsin"]
		sdwtype = ["--Pick Your Sandwhiches--","Chicken Bacon Ranch Sandwich","Chicken Parm Sandwich","Italian Sandwich"]
		pastype = ["--Choose Your Pasta--","Chicken Alfredo Pasta","Chicken Carbonara Pasta","Italian Sausage Marinara Pasta"]
		ch2opt = ["--Choose Your Extras--","Breads", "Deserts", "Drinks"]
		brtype = ["--Type Bread Type--","Parmesan Bread Twists","Garlic Bread Twists","Stuffed Cheesy Bread"]
		cktype = ["--Choose Your Desert--","Chocolate Lava Crunch"]
		drtype = ["--Choose Your Drink--","20oz Bottle Coke","20oz Bottle Fanta Orange","20oz Bottle  Barqs Root Beer","20oz Bottle Sprite"]


		# The Start of the Drop Down menu
		# Main Choice
		mevar = StringVar(box)
		mevar.set(ch1opt[0])
		# Extras
		exvar2 = StringVar(box)
		exvar2.set(ch2opt[0])
		# Pizza Size
		pszvar = StringVar(box)
		pszvar.set(psize[0])
		# Pizza Type
		pzt = StringVar(box)
		pzt.set(ptype[0])
		# Sandwiches Type
		sdvar = StringVar(box)
		sdvar.set(sdwtype[0])
		# Pasta Type
		pasty = StringVar(box)
		pasty.set(pastype[0])
		# Breads
		brvar = StringVar(box)
		brvar.set(brtype[0])
		# Desert
		cakvar = StringVar(box)
		cakvar.set(cktype[0])
		# Drinks
		drvar = StringVar(box)
		drvar.set(drtype[0])
		# Dropdown menu for Orders

		# Main Request
		Com1 = OptionMenu(box, mevar, *ch1opt)
		Com1.config(width=20, font=('Helvetica', 12))
		Com1.place(x=20,y=150)

		# Extras
		Com2 = OptionMenu(box, exvar2, *ch2opt)
		Com2.config(width=20, font=('Helvetica', 12), state='disabled')
		Com2.place(x=230,y=150)

		# Function for Main Request

		orderlist=[]

		def callback1(*args):
			if mevar.get() == 'Pizza':
				#Pizza Size
				Com3 = OptionMenu(box, pszvar, *psize)
				Com3.config(width=20, font=('Helvetica', 12))
				Com3.place(x=20,y=190)
			elif mevar.get() == 'Sandwiches':
				Com4 = OptionMenu(box, sdvar, *sdwtype)
				Com4.config(width=20, font=('Helvetica', 12))
				Com4.place(x=20,y=190)
			elif mevar.get() == 'Pasta':
				Com5 = OptionMenu(box, pasty, *pasty)
				Com5.config(width=20, font=('Helvetica', 12))
				Com5.place(x=20,y=190)
			global sel1
			sel1 = mevar.get()
			#print(sel1)
			
			#return sel1
		# Function for Size
		def callback2(*args):
			if pszvar.get() == 'Small':
				Com5 = OptionMenu(box, pzt, *ptype)
				Com5.config(width=20, font=('Helvetica', 12))
				Com5.place(x=20,y=230)
				code = 'P10IRECZ'
				price = '$11.99'
				#sel2 = 'Small'
				#return sel2
			elif pszvar.get() == 'Medium':
				Com5 = OptionMenu(box, pzt, *ptype)
				Com5.config(width=20, font=('Helvetica', 12))
				Com5.place(x=20,y=230)
				#sel2 = 'Medium'
				#return sel2
			elif pszvar.get() == 'Large':
				Com5 = OptionMenu(box, pzt, *ptype)
				Com5.config(width=20, font=('Helvetica', 12))
				Com5.place(x=20,y=230)
				#sel2 = 'Large'
				#return sel2
			global sel2
			sel2 = pszvar.get()
			print('Customer Order = ',str(code),str(price))
			#orderlist.append(sel2)
			

		def callback3(*args):
			if pzt.get() == 'Hand Tossed Wisconsin':
				sel3 = 'Hand Tossed Wisconsin'
			elif pzt.get() == 'Hand Tossed Pizza':
				sel3 = 'Hand Tossed Pizza'
			elif pzt.get() == 'Thin Wisconsin 6 Cheese Pizza':
				sel3 = 'Thin Wisconsin 6 Cheese Pizza'
			print(sel3)
			

		def exitfun():
			sys.exit()

		# Buttons
		probtn = Button(box, text='PROCEED', activebackground='#00FF00', fg='black', width=25, height=2, justify='center')
		probtn.place(x=20, y=500)
		exitbtn = Button(box, text='Exit', activebackground='#00FF00', fg='black', width=25, height=2, justify='right', command=exitfun)
		exitbtn.place(x=550, y=500)
		mevar.trace('w', callback1)
		pszvar.trace('w', callback2)
		pzt.trace('w',callback3)



		'''
		if mevar.get() == 'Pizza':
			mevar.trace('w', callback1)
			pszvar.trace('w', callback2)
		elif mevar.get() == 'Sandwhiches':
			mevar.trace('w', sandfunc)
		elif mevar.get() == 'Pasta':
			mevar.trace('w', pastafunc)
		'''
		

		
		#btn = Button(box, text="Exit NOW", bg='cyan', font='white', relief='raised', command=sys.exit)
		#btn.place(x=100, y=100)

		# Title Box
		#headline = Text(box, width=50)
		#headline.insert(INSERT,"WALEED")
		#headline.place(x=200, y=50)

#class Window2(Frame2)


app = Window(box)
box.mainloop()