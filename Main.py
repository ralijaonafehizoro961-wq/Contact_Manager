contacts = []
FILENAME = "Donnee.txt"

# 1. Add a new contact
def Add():
	name = input("Name : ").strip()
	phone_number = input("Phone Number : ").strip()
	contacts.append([name,phone_number])
	print("New contact successfully added")

#2. List the contacts
def Lister():
	for i,(name,phone_number) in enumerate(contacts, 1):
		print(f"{i}. {name} - {phone_number}")


#3. Save contacts
def Save():
	with open(FILENAME, "a") as fic:
		for i,(name,phone_number) in enumerate(contacts, 1):
			fic.write(f"\n - CONTACT {i}")
			fic.write(f"\n   NAME       : {name}")
			fic.write(f"\n   NUMBER : {phone_number}\n ")



# menu 
def menu():
	while True:
		try :
			print("\n" + "="*10 +  " CONTACT MANAGER " + "="*10)
			print("1 . Add a new contact")
			print("2 . List the contacts")
			print("3 . Save contacts")
			print("4 . Exit")
			choice = int(input("Entrer votre choix : "))
			if choice == "1":
				Add()
			elif choice == "2":
				Lister()
			elif choice == "3":
				Save()
			elif choice == "4":
				print("Goodbye ! ")
				break
			else :
				print("Please, enter a valid choice !")
		except ValueError :
			print("Error, please enter valid numbers")


if __name__ == "__main__":
	menu()