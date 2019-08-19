import pytest
import logging
from app.models.customer import Customer
from app.managers.customerManager import CustomerManager

def test_create_customer_ok():
    customer_manager = CustomerManager()
    customer = customer_manager.create_customer('35025191', 'Julian', 'Massolo', 'Mitre 182', 'massolo.j@gmail.com',
                                                '222225', [])
    assert isinstance(customer, Customer) == True

def test_create_customer_notok():
    customer_manager = CustomerManager()
    customer = customer_manager.create_customer('35025191', 1, 'Massolo', 'Mitre 182', 'massolo.j@gmail.com',
                                                '222225', [])
    assert isinstance(customer, Customer) == False

def test_add_customer():
    customer_manager = CustomerManager()
    customer = customer_manager.create_customer('35025191', 'Julian', 'Massolo', 'Mitre 182', 'massolo.j@gmail.com',
                                                '222225', [])
    size = len(customer_manager.customers)
    customer_manager.add_customer(customer)
    newsize = len(customer_manager.customers)

    assert (newsize < size) == False


def test_add_rent():
    pass
    #customer_manager = CustomerManager()
    #customer = customer_manager.create_customer('35025191', 'Julian', 'Massolo', 'Mitre 182', 'massolo.j@gmail.com',
    #                                            '222225', [])
