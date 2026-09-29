
Big O answers one question: if the input gets bigger, how much more work does the function do? n is the size of the input, such as the length of the list.

O(n): the work grows in step with the input. Double the list, double the work. This is usually a single loop that visits each item once.
O(n^2): a loop inside a loop, both running over the input. Double the list, and the work goes up four times.
O(log n): each step throws away half of what's left. Double the list, and the work goes up by only one step.

Why O(n²) breaks at scale

At 10 items, an O(n²) algorithm does about 100 operations, which a computer finishes almost instantly. That makes it look perfectly fine, and it is fine at that size. The problem is that quadratic work grows much faster than the input. At 1,000 items it's 1,000,000 operations. At 1,000,000 items it's 1,000,000,000,000 operations. An O(n log n) algorithm on that same million items needs only about 20 million.

In practice, this is the difference between "runs in a second" and "runs for hours." A buggy-slow O(n²) loop often passes every test on small sample data and then fails in production when real data arrives. Faster hardware doesn't save you either: a computer twice as fast only lets you handle about 1.4× more data in the same time.

