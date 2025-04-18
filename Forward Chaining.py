# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i5Q-CL0xQ9B4K2BSfwlmjXoKcQvWtwHR
"""

!pip install experta

!pip install --upgrade frozendict

def forward_chaining(facts, rules):
  inferred = set(facts)
  changed = True
  while changed:
    changed = False
    for rule in rules:
      if rule["if"].issubset(inferred) and rule["then"] not in inferred:
        inferred.add(rule["then"])
        changed = True
  return inferred

facts = {"has_feather", "has_beak", "carnivore"}
rules = [
    {"if": {"has_feather", "has_beak"}, "then": "is_bird"},
    {"if": {"lays_eggs", "is_bird"}, "then": "is_chicken"},
    {"if": {"cannot_fly", "is_bird"}, "then": "is_pinguin"},
    {"if": {"carnivore", "is_bird"}, "then": "is_eagle"}

]

result = forward_chaining(facts, rules)
print("inferred facts:", result)