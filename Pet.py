#!/usr/bin/venv python
# -*- coding: utf-8 -*-
'''
pet attributes and statistic methods
one pet
Lily: 
{
    age: 10,
    name: Lily,
    color: yellow,
    height: 0.5m,
    weight: 20kg,
    class: dog,
    gender: male,
    price: 10
}

'''

class PET():

    def __init__(self):
        self.all_pet_dict = {}
        chosen_pet_dict = {}

    def get_all_pets(self):
        pass

    def get_total_val(self, key):
        pet_dict = self.all_pet_dict
        sum = 0
        # num = 0
        # ave = 0
        for pet in pet_dict:
            sum = sum + pet[key]
            # num = num + 1
        return sum
    
    def get_ave_val(self, key):
        pet_dict = self.all_pet_dict
        sum = 0
        num = 0
        ave = 0
        for pet in pet_dict:
            sum = sum + pet[key]
            num = num + 1
        ave = sum * 1.0 / num
        return ave

    def get_all_val(self, key):
        pet_dict = self.all_pet_dict
        key_list = []
        # sum = 0
        # num = 0
        # ave = 0
        for pet in pet_dict:
            key_list.append(pet[key])
            # sum = sum + pet[key]
            # num = num + 1
        # ave = sum * 1.0 / num
        return key_list
