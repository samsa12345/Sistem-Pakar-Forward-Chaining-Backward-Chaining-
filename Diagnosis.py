# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i5Q-CL0xQ9B4K2BSfwlmjXoKcQvWtwHR
"""

!pip install experta

!pip install --upgrade frozendict

from experta import *
class diagnosis(KnowledgeEngine):
  @Rule(Fact(cough=True) & Fact(fever=True) & Fact(fatigue=True))
  def flu(self):
    print("Diagnosis : you may have the flu.")

  @Rule(Fact(cough=True) & Fact(fever=True) & Fact(breathing_difficulty=True))
  def pneumonia(self):
    print("Diagnosis : you may have  pneumonia.")

  @Rule(Fact(sneezing=True) & Fact(runny_nose=True) & Fact(cough=False))
  def cold(self):
    print("Diagnosis : you may have common cold.")

  @Rule(Fact(sore_throat=True) & Fact(fever=True))
  def throat_infection(self):
    print("Diagnosis : you may have a throat infection.")

  @Rule(Fact(cough=False) & Fact(fever=False) & Fact(fatigue=False) & Fact(sakit_kepala=False) & Fact(demam=False) & Fact(mual=False) & Fact(mata_gatal=False) & Fact(bersin=False) & Fact(hidung_berair=False) & Fact(nyeri_perut=False) & Fact(diare=False) & Fact(nyeri_dada=False) & Fact(sesak_napas=False))
  def healthy(self):
    print("Diagnosis : you seem to be the healthy.")

  @Rule(Fact(sakit_kepala=True) & Fact(demam=True) & Fact(mual=True))
  def demam_berdarah(self):
    print("Diagnosis: Anda mungkin terkena demam berdarah.")

  @Rule(Fact(mata_gatal=True) & Fact(bersin=True) & Fact(hidung_berair=True))
  def alergi(self):
    print("Diagnosis: Anda mungkin mengalami alergi.")

  @Rule(Fact(nyeri_perut=True) & Fact(mual=True) & Fact(diare=True))
  def keracunan_makanan(self):
    print("Diagnosis: Anda mungkin mengalami keracunan makanan.")

  @Rule(Fact(nyeri_dada=True) & Fact(sesak_napas=True))
  def masalah_jantung(self):
    print("Diagnosis: Anda mungkin mengalami masalah jantung. Segera periksa ke dokter.")


def get_input():
  def ask_question(question):
    return input(question + " (yes/no): ").strip().lower() == "yes"

  return {
      "cough": ask_question("Do you have a cough?"),
      "fever": ask_question("Do you have a fever?"),
      "fatigue": ask_question("Do you feel fatigued?"),
      "breathing_difficulty": ask_question("Do you have breathing difficulties?"),
      "sneezing": ask_question("Do you have a sneezing?"),
      "runny_nose": ask_question("Do you have a runny nose?"),
      "sore_throat": ask_question("Do you have a sore throat?"),
      "sakit_kepala": ask_question("Apakah Anda mengalami sakit kepala?"),
      "mual": ask_question("Apakah Anda merasa mual?"),
      "mata_gatal": ask_question("Apakah mata Anda terasa gatal?"),
      "bersin": ask_question("Apakah Anda merasa bersin?"),
      "hidung_berair": ask_question("Apakah hidung Anda terasa berair?"),
      "nyeri_perut": ask_question("Apakah Anda merasa nyeri di perut?"),
      "diare": ask_question("Apakah Anda mengalami diare?"),
      "nyeri_dada": ask_question("Apakah Anda merasakan nyeri di dada?"),
      "sesak_napas": ask_question("Apakah Anda mengalami sesak napas?")

  }

if __name__ == "__main__":
  symptoms = get_input()
  engine = diagnosis()
  engine.reset()

  for symptom, present in symptoms.items():
    engine.declare(Fact(**{symptom: present}))

  engine.run()