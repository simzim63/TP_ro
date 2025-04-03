from unittest import TestCase

from src.evaluation import fonction_evaluation
from src.optimizers.random_descent import random_descent

from src.problem import load_problem

class TestRandomDescent(TestCase):
    def test_draw_realistic_example(self):
        problem = load_problem("fapp05_0050.coo")
        value, solution = random_descent(problem, fonction_evaluation)