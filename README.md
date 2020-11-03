# SudokuSolver
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
Do not add blank lines at the start or end of file. <br/>
An example of the top left grid of a puzzle can be found here: <br/>
>5, 3, 0 <br/>
>6, 0, 0 <br/>
>0, 9, 8 <br/>

<br/>Run the run.sh script. The accepted format is:
>./run.sh [puzzle txt file path+name]

or
>./run.sh

where SudokuPuzzle.txt is used as the puzzle txt file

## Features
Implemented:
* Script
* Puzzle file can be read and stored
* Can solve sudoku puzzles using backtracking
* Puzzle can be printed

## Status
Project is: _finished_

## Language details
Language used: Python </br>
Version used: 3.8

## Contact
Created by [@cameronmathis](https://github.com/cameronmathis/) - feel free to contact me!
