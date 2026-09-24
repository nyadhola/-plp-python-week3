# Week 3 Assignment: Conditions and Loops

## File Descriptions
- `grade_reporter.py`: Iterates through a list of scores to assign letter grades, counts passing and failing students, and prints the rounded average.
- `bug_hunt.py`: Uses a `while` loop to sum numbers from 1 to 5 after correcting three syntax and logic bugs.

## Reflection Question
The hardest bug to find in Part B was the off-by-one logic error in the `while` loop condition (`count < 5`). Because standard comparison operators run without raising any syntax or execution errors, Python didn't crash. I knew something was wrong because the printed sum was `10` instead of the expected `15`, showing that the loop stopped early before adding `5`.
