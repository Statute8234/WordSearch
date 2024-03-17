# WordSearch

This Python script creates a word search puzzle grid by asking the user to input a name and number of words. The grid is then generated and filled with random letters from the input words, creating a visually appealing word search puzzle.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Imports](#Imports)
- [Rating: 3/10](#Rating)

# About

This Python script creates a word search puzzle grid by asking the user to provide a name and number of words to include. The user inputs the words individually, and the script then constructs a grid filled with random letters from the input words. The grid is displayed as a word search puzzle, indicating the user's input and the number of words to be included. The process ensures a visually appealing and engaging experience for the user.

# Features

The Python script creates a word search puzzle grid by prompting the user to input a name and the number of words they want to include. The grid is constructed with random letters from the user's input words, which form the basis of the puzzle. The grid is displayed as a word search puzzle, allowing users to visually search for the input words. The process ensures a visually appealing and engaging experience for the user, with personalized names and word inclusions enhancing interaction. Overall, this script provides a fun and interactive way for users to create and explore word search puzzles.

# Imports

random

# Rating

For its user interaction and randomness. It uses the `random.choice()` function to randomly select letters and words, adding variability to the word search. However, there are areas for improvement, such as variable naming, formatting, logic errors, and unused variables. Variable names like `colloms`, `word_name`, and `letters` have misspellings and are not descriptive. The output grid is not well-structured, with letters printed in an irregular manner, making it difficult to read. The loop generating the word search grid is not functioning correctly, and the variable `list` is defined but never used. The word search grid is not consistent in its layout, with inconsistent spacing between letters and words. The code lacks error handling mechanisms for user inputs of unexpected values or invalid words. Modularization could improve the code's readability, functionality, and overall quality. Addressing these areas can enhance the overall quality of the word search generator.
