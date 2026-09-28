
Big O answers one question: if the input gets bigger, how much more work does the function do? n is the size of the input, such as the length of the list.

O(n): the work grows in step with the input. Double the list, double the work. This is usually a single loop that visits each item once.
O(n^2): a loop inside a loop, both running over the input. Double the list, and the work goes up four times.
O(log n): each step throws away half of what's left. Double the list, and the work goes up by only one step.

