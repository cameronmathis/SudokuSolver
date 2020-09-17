# AkariSolver
This is a Python Application that solves Sudoku Puzzles.

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Language details](#Language-details)
* [Contact](#contact)

## General info
This is a project I decided I wanted to do in order to familiarize myself with Python.

## Setup
In order to run, clone this repo onto your local machine. <br/><br/>
Edit the SudokuSolver.txt file to contain your puzzle. The accepted format is: 
>(1,9), (2,9), (3,9), ..., (9,9) <br/>
>(1,8), (2,8), (3,8), ..., (9,8) <br/>
>(1,7), (2,7), (3,7), ..., (9,7) <br/>
>... <br/>
>(1,1), (2,1), (3,1), ..., (9,1) <br/>

Where each coordinate represents a cell on the board. Empty cells should have 0s and numbered cells should have the
appropriate number. All coordinates should be comma separated.
The bottom left of the puzzle should be indexed at (1,1).
Do not add blank lines at the start or end of file. <br/>
An example of the top left grid of a puzzle can be found here: <br/>
>5, 3, 0 <br/>
>6, 0, 0 <br/>
>0, 9, 8 <br/>

<br/>Run the run.sh script. The accepted format is:
>./run.sh [problem file path+name]

## Features
Implemented:
* Puzzle file can be read and stored
* Puzzle can be printed

To-do list:
* Can solve sudoku puzzles using backtracking
* Write script

## Status
Project is: _in progress_

## Language details
Language used: Python </br>
Version used: 3.8

## Contact
Created by [@cameronmathis](https://github.com/cameronmathis/) - feel free to contact me!