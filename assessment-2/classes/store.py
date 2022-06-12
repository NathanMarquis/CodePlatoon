import os
import csv
# Will be main class before runner
# Stores customers objects and inventory object
class Store:
    def __init__(self, name):
        self.name = name
        self.customers = Customer.customers()
        self.inventory = Inventory.movies()
    
    def view_inventory(self):
        print('\n')
        for movie in self.inventory:
            print(f"Movie ID: {movie['id']} == {movie['title']} is {movie['rating']} rated and released in {movie['release_year']}. Available copies: {movie['copies_available']}.")

    def add_customer(self, new_customer_data):
        new_customer = Customer(**new_customer_data)
        self.customers.append(new_customer)
        print (f"Thank you {new_customer_data['first_name']}, you have created a new user account! Your user ID is {new_customer_data['id']}.")

    def valid_id_check(self, id):
        for customer in self.customers:
            if id == customer.id:
                return True
        return False

    def valid_movie_check(self, movie_title):
        for movie in self.inventory:
            if movie_title == movie.title:
                return False
        return True

    def view_customer_rentals(self, id):
        for customer in self.customers:
            if id == customer.id:
                if customer.current_video_rentals == '':
                    return print('You do not have any video rentals.')
                print('\nYour rentals:')
                for rental in customer.current_video_rentals.split('/'):
                    print(f"-{rental}")
                return

class Customer:
    def __init__(self, id, account_type, first_name, last_name, current_video_rentals):
        self.id = id
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals
    def __repr__(self):
        return f'{self.id} {self.account_type} {self.first_name} {self.last_name} {self.current_video_rentals}.'

    @classmethod
    def customers(cls):
        customers = []
        path = ("data/customers.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customers.append(cls(**row))

        return customers

class Inventory:
    def __init__(self, id, title, rating, release_year, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = copies_available

    def __str__(self):
        return f"Movie ID: {self.id}. Title: {self.title}."

    @classmethod
    def movies(cls):
        movies = []
        path = ("data/inventory.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                movies.append(row)

        return movies
    
