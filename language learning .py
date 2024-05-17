#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

class LanguageLearningTool:
    def __init__(self, vocabulary, grammar_rules, pronunciation):
        self.vocabulary = vocabulary
        self.grammar_rules = gr
        +mmar_rules
        self.pronunciation = pronunciation
        self.progress = {"vocabulary": 0, "grammar": 0, "pronunciation": 0}
    
    def practice_vocabulary(self):
        word, meaning = random.choice(list(self.vocabulary.items()))
        print(f"What does '{word}' mean?")
        user_input = input("Enter the meaning: ")
        if user_input.lower() == meaning.lower():
            print("Correct!")
            self.progress["vocabulary"] += 1
        else:
            print(f"Wrong! The correct meaning is '{meaning}'.")
    
    def practice_grammar(self):
        rule, example = random.choice(list(self.grammar_rules.items()))
        print(f"What's an example sentence for '{rule}'?")
        print(f"Example: {example}")
        input("Press enter to continue...")
        self.progress["grammar"] += 1
    
    def practice_pronunciation(self):
        word = random.choice(list(self.pronunciation.keys()))
        print(f"How do you pronounce '{word}'?")
        input("Press enter to reveal the pronunciation...")
        print(f"Pronunciation: {self.pronunciation[word]}")
        self.progress["pronunciation"] += 1
    
    def track_progress(self):
        print("Your progress:")
        for category, value in self.progress.items():
            print(f"{category.capitalize()}: {value} exercises completed.")

# Example usage:
vocabulary = {"apple": "a fruit", "house": "a place to live", "book": "a written or printed work"}
grammar_rules = {"present tense": "I eat pizza every Friday."}
pronunciation = {"hello": "həˈloʊ", "world": "wɜːrld"}

tool = LanguageLearningTool(vocabulary, grammar_rules, pronunciation)
tool.practice_vocabulary()
tool.practice_grammar()
tool.practice_pronunciation()
tool.track_progress()

