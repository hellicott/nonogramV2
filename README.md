# nonogramV2

A second attempt at a nonogram solver. This one takes a similar approach to the first. It fills in all definite squares then 
randomly fills in others, based on the ratio of filled to not filled squares expected.
This one, however, actually works! This is because it checks through rows and columns, not just rows


The solver works on small puzzles (5x5) quite quickly. But when testing it on larger puzzles (10x10) it could not find a 
solution in under 1 million iterations.
