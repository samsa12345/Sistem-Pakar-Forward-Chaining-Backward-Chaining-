# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i5Q-CL0xQ9B4K2BSfwlmjXoKcQvWtwHR
"""

!pip install experta

!pip install --upgrade frozendict

def backward_chaining(goal, facts, rules):
  if goal in facts:
    return True
  for rule in rules:
    if rule["then"] == goal:
      if all(backward_chaining(cond, facts, rules) for cond in rule["if"]):
        return True
  return False

facts = {"has_feather", "has_small_wings"}
rules = [
    {"if": {"has_feather"}, "then": "is_bird"},
    {"if": {"has_small_wings"}, "then": "cannot_fly"},
    {"if": {"is_bird", "cannot_fly"}, "then": "is_penguin"}
]

goal = "is_penguin"
result = backward_chaining(goal, facts, rules)
print(f"is '{goal} probable? ->", result)