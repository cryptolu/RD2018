# RD2018

This repository contains the code used to generate the boards and transactions for the Blockchain game.

## Dependencies

python3, pdflatex and various latex packages (mainly 'labels').

## Usage

1. For example, generate 10 sets of boards. Each board contains 6 identical 6 sheets. The generated .tex file is automatically compiled using pdflatex.

```bash
> cd build
> ../src/gen_boards.py -p 10 -n 6 -c
> evince boards.pdf & # for visualization/print
```

2. For example, generate 3 sheets with 48 transactions on each sheet. Each transaction has 10% probability to be invalid. The generated .tex file is automatically compiled using pdflatex.

```bash
> cd build
> ../src/gen_transactions.py -p 3 -n 48 -e 0.1 -c
> evince transactions.pdf & # for visualization/print
```
