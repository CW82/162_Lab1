class Car:
#creates class
	def __init__(
		#attributes
		self,
		new_car_engine = "V8",
		new_car_cylinder_head = "Loop-Flow",
		new_car_spark_plugs = 8,
		new_car_comb_chamb = "Pentroof",
		
		new_cus_style = "Coup",
		new_cus_color = "Lavender",
		new_cus_door_style = "Butterfly",
		new_cus_fuel_type = "Eletric"
		):

		self.car_engine = new_car_engine
		self.car_cylinder_head = new_car_cylinder_head
		self.car_spark_plugs = new_car_spark_plugs
		self.car_comb_chamb = new_car_comb_chamb

		self.cus_style = new_cus_style
		self.cus_color = new_cus_color
		self.cus_door_style = new_cus_door_style
		self.cus_fuel_type = new_cus_fuel_type

	def __str__(self): #another method
		result = f"The cars engine is a: {self.car_engine}\n" \
		f"The cars cylinder head type is: {self.car_cylinder_head}\n" \
		f"The amount of spark plugs in the car is: {self.car_spark_plugs}\n" \
		f"The cars comb chamber type is: {self.car_comb_chamb}\n" \
		f"The cars style is: {self.cus_style}\n" \
		f"The cars color is: {self.cus_color}\n" \
		f"The cars door style is: {self.cus_door_style}\n" \
		f"The cars fuel type is: {self.cus_fuel_type}"

		return result

your_car = Car()
my_car = Car()

bad = True
while bad == True:
	user = (input(     #displays the menu to the user
		f"0: Quit\n" \
     	"1: Enter your cars specs\n" \
    	 "2: Display current car specs\n" \
		"What would you like to do?\n"\
	))

	if user not in ["0", "1", "2"]:
		print(f"That's not valid")    #If the user inputs smt not in the list, it'll print 'thats not valid'
	else:
		bad = False

if user == "1": 
	your_car_engine = input(f"What type of engine does your car have?: ")
	your_car_color = input(f"What color is your car?: ")
	your_car = Car(your_car_engine, your_car_color)
	print(my_car)
elif user == "2":
	print(my_car)
elif user == "0":
	pass

