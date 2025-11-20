import json
from pprint import pp
import time
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import dotenv
import smtplib
import smtplib


with open('lekcja46/menu.json', 'r', encoding='utf-8') as file:
	menu = json.load(file)

list_of_pizzas = menu['menu']

list_of_pizzas_names = []
for pizza in list_of_pizzas:
	list_of_pizzas_names.append(pizza["pizza"])

order = []

def main_page():
	print("Witaj na stronie pizzeri u Vita")
	print("Wybierz co chcesz zrobić")
	print("1. Wyświetl menu")
	print("2. Dodaj pizze do zamówienia")
	print("3. Wyczyść zamówienie")
	print("4. Wyślij zamówienie")
	print("5. Zakończ")
	option = input("")
	if option == '1':
		display_menu()
		main_page()
	elif option == '2':
		pass  
		main_page()
	elif option == '3':
		order.clear()
		print("Zamówienie wyczyszczone.")
		time.sleep(2)
		main_page()
	elif option == '4':
		pass  
		main_page()
	elif option == '5':
		print("Dowidzenia! Życzymy miłego dnia.")
		time.sleep(3)
		quit()
	else:
		print("Podano złą opcję")
		time.sleep(2)
		main_page()



def display_menu():
	for pizza in list_of_pizzas:
		print(f"Pizza {pizza['pizza']}")
		print(f"Składniki: {', '.join(pizza['dodatki'])}")
		print(f"Ceny:")
		print(f"  Mała: {pizza['ceny']['S']} zł")
		print(f"  Średnia: {pizza['ceny']['M']} zł")
		print(f"  Duża: {pizza['ceny']['L']} zł")
		print()
#        x = input("Jeśli chcesz wrócić kliknij 'Enter'")
#        if x == "":
			 
	   
def add_to_order():
	print("Którą pizzę chcesz zamówić: ")
	for pizza_name in list_of_pizzas_names:
		print(f"{list_of_pizzas_names.index(pizza_name)+1}.{pizza_name}")
	pizza_name_number = int(input("Podaj numer pizzy: "))
	pizza_amount = int(input("Ile pizz chcesz zamówić: "))
	size = input("Jakie rozmiary mają być pizze (S/M/L): ")
	order.append({'size':size, 'pizza_amount': pizza_amount, 'pizza_name': list_of_pizzas_names[pizza_name_number-1]})

	print(f"Dodano {pizza_amount} x {list_of_pizzas_names[pizza_name_number -1]} [{size}] do zamówienia")
	time.sleep(3)

def calculate_cost(ordered_pizza):
	for pizza in list_of_pizzas:
		if pizza['pizza'] == ordered_pizza['pizza_name']:
			cost = int(ordered_pizza['pizza_amount']) * int(pizza["ceny"][ordered_pizza['size']])
	return cost

def send_email(message_txt):
	dotenv.load_dotenv()
	subject = "Pizzeria u Vita - potwierdzenie zamówienia"
	send_email = os.getenv('sender_email')
	send_client = os.getenv('sender_client')
	sender_password = os.getenv('sender_password')
	smtp_server = "smtp.wp.pl"
	smtp_port = 465

	message = MIMEMultipart()
	message['subject'] = subject
	message['From'] = send_email
	message['To'] = send_client
	body_part = MIMEText(message_txt)
	message.attach(body_part)

	with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
		server.login(send_email, sender_password)
		server.sendmail(send_email, send_client)

def send_order():
	tekst = "Dziękujemy za wybranie pizzeri u Vita, oto podsumowanie Twojego zamówinia:\n"
	total_cost = 0
	for pizza in order:
		cost = calculate_cost(pizza)
		tekst+=f"{pizza['pizza_amount']} x {pizza['pizza_name']}[{pizza['size']}] : {cost}zł\n"
		total_cost += cost
	tekst += f"Łączny koszt: {total_cost}zł"
	print(tekst)
	print("Zamówienie zostało złożone")
	input("Wciśnij enter aby kontynuować")

main_page()

# pp(menu)  # Jeśli takiego można powiedzieć "debug mode"'a menu
