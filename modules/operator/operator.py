import os
import sys
import yaml

class Operator:
    
    def __init__(self):
        self.operators = []
        self.load_operators()
        self.current_path = os.path.dirname(os.path.abspath(__file__)) + "\\operators.yaml"

    def load_operators(self):
        print(self.current_path)
        with open(self.current_path, "r") as f:
            self.operators = yaml.load(f, Loader=yaml.FullLoader)

    def save_operators(self):
        with open(self.current_path, "w") as f:
            yaml.dump(self.operators, f)

    def is_operator(self, user_id):
        return user_id in self.operators

    def add_operator(self, user_id):
        if not self.is_operator(user_id):
            self.operators.append(user_id)
            self.save_operators()

    def remove_operator(self, user_id):
        if self.is_operator(user_id):
            self.operators.remove(user_id)
            self.save_operators()

    def get_operator_list(self):
        return self.operators