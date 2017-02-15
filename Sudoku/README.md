# Sudoku Solver
Eventually, I want to build a Sudoku solver. The Excel file here is more of a helper than a solver. I built it several years ago as a first step.

After a big of research, it may actually be easier to build a solution matcher than an actual solver. By "solver", I think of a program that takes a Sudoku puzzle and works through it deductively. Alternatively, a "solution matcher" would take the given puzzle and search a dataset of all possible Sudoku solutions for a solution that fits.

There are 6,670,903,752,021,072,936,960 (6.67 sextillion) possible Sudoku solutions. However, that reduces to 5,472,730,538 (5.47 billion) solutions, when you eliminate symmetries such as rotation, reflection, permutation, and relabelling. Now THAT might be a workable number, assuming I can find or analytically create a database of these. 














### Links of interest:
* [Wikipedia: Mathematics of Sudoku](https://en.wikipedia.org/wiki/Mathematics_of_Sudoku "Mathematics of Sudoku")
* [Sequence A107739 in the OEIS](https://oeis.org/A107739 "Number of (completed) sudokus (or Sudokus) of size n^2 X n^2.")
* [Sequence A109741 in the OEIS](https://oeis.org/A109741 "Number of inequivalent (completed) n^2 X n^2 sudokus (or Sudokus).")