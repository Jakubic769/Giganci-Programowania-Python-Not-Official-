
from queue import Queue

class Customer:
    def __init__(self, name, order):
        self.name = name
        self.order = order

    def __str__(self):
        return f"{self.name} zamówił(a): {self.order}"

class CinemaQueue:
    def __init__(self):
        self.queue = Queue()

    def add_customer(self, customer):
        self.queue.put(customer)
        print(f"Dodano do kolejki: {customer}")

    def serve_customer(self):
        if not self.queue.empty():
            customer = self.queue.get()
            print(f"Obsłużono klienta: {customer}")
        else:
            print("Kolejka jest pusta!")

    def is_empty(self):
        return self.queue.empty()

    def queue_size(self):
        return self.queue.qsize()

if __name__ == "__main__":
    kino = CinemaQueue()

    kino.add_customer(Customer("Alicja", "Popcorn i Cola"))
    kino.add_customer(Customer("Bartek", "Bilet 3D"))
    kino.add_customer(Customer("Celina", "Bilet VIP i Nachosy"))

    print("\nObsługa klientów:")
    while not kino.is_empty():
        kino.serve_customer()
