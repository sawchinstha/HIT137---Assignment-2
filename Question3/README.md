Question 3

Create a program that uses a recursive function to generate a geometric pattern using Python's turtle graphics. The pattern starts with a regular polygon and recursively modifies each edge to create intricate designs.
Pattern Generation Rules:

For each edge of the shape:
1. Divide the edge into three equal segments
2. Replace the middle segment with two sides of an equilateral triangle pointing
inward (creating an indentation)
3. This transforms one straight edge into four smaller edges, each 1/3 the length of
the original edge
4. Apply this same process recursively to each of the four new edges based on the
specified depth

Depth 0: Draw a straight line (no modification)
Depth 1: Line becomes: ——\⁄—— (indentation pointing inward)

User Input Parameters:
The program should prompt the user for:
Number of sides: Determines the starting shape
Side length: The length of each edge of the initial polygon in pixels
Recursion depth: How many times to apply the pattern rules

-------------------------------------------------------------------------------------------------------------------------
question3.py file inside the Question3 folder contains the code satisfying all the requirement provided by the professor.
THANK YOU