import os
import csv
import datetime


timectrl = {}
phones = {}
timectrl_copy = {}
phones_copy = {}
print('Welcome to contact list app!')
print()
print()
print()

def event_handler(op):

	for key in phones:
		phones_copy.setdefault(key, phones[key])

	if op == 'n':
		print('#To move to the menu, u can enter "exit" in any line')
		name = input('Name contact:')
		if exit_option(name):main()

		while True:
			phnumb = input('Phone number:')
			if exit_option(phnumb):break

			try:
				phones.setdefault(name, int(phnumb));		phones_copy.setdefault(name, int(phnumb))
				d = datetime.datetime.today()

			except ValueError:
				print('Phone number must have only numbers not letters))')
				continue

			
			timectrl.setdefault(d, name);					timectrl_copy.setdefault(d, name)

			print('Sucsess!')
			print()
			break

	########

	elif op == 's':
		print('\t Name{0:>27}'.format('Phone number'))
		n = 1
		for key in phones:
			print('{0:>3}  {1:<20}  {2:>9}'.format(n, key, phones[key]))
			n+=1
		print()

	########

	elif op == 'd':
		while True:
			print('#To move to the menu, u can enter "exit" in any line')
			contact = input('Enter the name of contact you want to deliete wich: ')
			if exit_option(contact):break

			try:
				phones.pop(contact);		phones_copy.pop(contact)

			except KeyError:
				print('Invalid contact name\nTry again\n')
				continue
			print('Sucsess!')
			print()
			break

	########

	elif op == 'e':
		while True:
			print('#To move to the menu, u can enter "exit" in any line')
			contact = input('Enter the name of contact wich name u want change: ')
			if exit_option(contact):break

			try:
				phnumb = phones[contact]

			except IndexError:
				print('Invalid contact name\nTry again\n')
				continue
			n_name = input('Enter new contact name: ')
			if exit_option(n_name):break		

			k = phones.keys()
			x = 0
			for name in k:
				if name == contact:
					break
				else:
					x+=1

			phones.clear()
			a = 0
			for key in phones_copy:
				if a != x:
					phones.setdefault(key, phones_copy[key])
				elif a == x:
					phones.setdefault(n_name, phones_copy[key])
				a+=1

			phones_copy.clear()
			for key in phones:
				phones_copy.setdefault(key, phones[key])

			print(timectrl_copy)

			timectrl.clear()
			a = 0
			for key in timectrl_copy:
				if a != x:
					timectrl.setdefault(key, timectrl_copy[key])
				elif a == x:
					timectrl.setdefault(key, n_name)
				a+=1

			timectrl_copy.clear()
			for key in timectrl:
				timectrl_copy.setdefault(key, timectrl[key])

			print(timectrl)
			print('Sucsess!')
			print()
			break

	########

	elif op == 'l':
		while True:
			print('#To move to the menu, u can enter "exit" in any line')
			path = input('Enter the path of your csv file: ')
			if exit_option(path):break

			try:
				with open (path) as f:
					pass
			except FileNotFoundError:
				print('Invalid file name\nTry again\n')
				continue
			b = input('Do you want to save previos contacts with new list? (yes/no):  ')
			if exit_option(b):break

			with open (path) as f:
				if b.lower() == 'no':
					phones.clear();			phones_copy.clear()
				if b.lower() == 'yes' or 'no':
					reader = csv.DictReader(f, fieldnames=['name', 'phone number'])
					for line in reader:
						phones.setdefault(line['name'], line['phone number']);			phones_copy.setdefault(line['name'], line['phone number'])
				else:
					print('Invalid answer\nTry again\n')

			break
		print('Sucsess!')
		print()

	########

	elif op == 'g':
		while True:
			print('#To move to the menu, u can enter "exit" in any line')
			direct = input('Enter a directory where you want to save csv file: ')
			if exit_option(direct): break

			try:
				os.chdir(direct)
			except (NotADirectoryError, OSError):
				print('Invalid directory!\nTry again')
				continue 

			name = input('Enter a name of your future file(without .csv): ')
			if exit_option(name):break

			with open ('{}\\{}.csv'.format(direct, name), 'w+') as f1:
				f1.write('name,phone number')
				for key in phones:
					f1.write('\n{},{}'.format(key, phones[key]))
			print('Sucsess!')
			print()
			break

	########

	elif op == 'r':
		while True:
			print('#To move to the menu, u can enter "exit" in any line')
			sorter = input('Sort 1)alphabetically\n\t 2)by creation time\n')
			if exit_option(sorter):break

			if sorter == '2' or '2)':
				o_n = input('Wich contacts will be at the top of the list? (old/new): ')
				if exit_option(o_n):break


				print(timectrl)


				if o_n == 'new':
					dates = sorted(timectrl, reverse=True)
				elif o_n == 'old':
					dates = sorted(timectrl, reverse=False)
				t_order = []
				for item in dates:	
					t_order.append(timectrl[item])	

				for name in t_order:
					numb = phones.pop(str(name));			phones_copy.pop(str(name))
					phones.setdefault(name, numb);			phones_copy.setdefault(name, numb)

				print('Sucsess!')
				break

			elif sorter == '1' or '1)':
				d = {}
				for key in sorted(phones):
					d.setdefault(key, phones[key])
				phones.clear();			phones_copy.clear()
				for i in d:
					phones.setdefault(i, d[i])

				print('Sucsess!')
				print()
				break

			else:
				print('Invalid option!\nTry again\n')
				continue


	main()


def rw_menu_option():

	print('Choose one of the following options:')
	print('   s) Show')
	print('   n) New')
	print('   d) Delete')
	print('   e) Edit')
	print('   r) Reorder')
	print('   g) Get csv file of your contact list')
	print('   l) Load csv file of another contact list')
	option = input('your chose: ').lower()
	if option in ['s', 'n', 'd', 'e', 'r', 'g', 'l']:
		print()
		return True, option
	print('invalid option!\nTry again\n')
	return False, None


def main():
	while True:
		bool, op = rw_menu_option()
		if bool:
			event_handler(op)
			break


def exit_option(s):
	if s.lower() == 'exit':
		print()
		return True
		



main()


