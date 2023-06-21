# Week 8: Lists

[Python lists](https://www.w3schools.com/python/python_lists.asp) <br>
[Python lists-access](https://www.w3schools.com/python/python_lists_access.asp) <br>
[Python change elements in list](https://www.w3schools.com/python/python_lists_change.asp) <br>
[Python add list items](https://www.w3schools.com/python/python_lists_add.asp) <br>
[Python loop lists](https://www.w3schools.com/python/python_lists_loop.asp) <br>

---

**List** --> a mutable, iterable, sequential collection (object)

**Properties of Python Lists:** <br>
_can have nested lists_

![Python Lists](./images/week8/list.png)

**Python Literals:** `[1, 2, 3], ["abc", 2.5, [1,2], [],...` <br>
**Operators:** `+, *, - ...` <br>
_Cannot multiply a list by a float, another list or a string_ <br>

![list_literals](./images/week8/list_literals.png)

**Boolean Operators:** `==, !=, <, >, <=, >=, in, not in`

![list_boolean_operators](./images/week8/list_bools.png)

Interpreter compares the lists lexicographically (similar to strings comparison). <br>
Compares each list component and determines the difference. <br>
Second example (comparing 3 with 5) will mean a "True" result as 3 < 5.

![list_boolean_operators](./images/week8/list_bools2.png)

Sequential Properties: <br>
**Indexing:** `lst[i]`

![list_indexing](./images/week8/list_indexing.png)

**Slicing:** `lst[start:end]`

![list_slicing](./images/week8/list_slicing.png)

---

**Functions:**

```python
len(lst)
min(lst)
max(lst)
sum(lst)
```

![list_functions](./images/week8/functions.png)

Lists as Iterable Collections

![list_iterable](./images/week8/iterable_collections.png)

![for_in](./images/week8/for..in.png)

**List Methods:**

`Append(value)` --> adds a value to the end of the list <br>
![list_append](./images/week8/list_append.png)

`Insert(index, value)` --> inserts a value at a given index <br>
![list_insert](./images/week8/list_insert.png)

`Extend(iterable)` --> adds all the elements of an iterable to the end of the list <br>
![list_extend](./images/week8/list_extend.png)

`pop(index), pop()` --> removes the element at the given index and returns it <br>
![list_pop](./images/week8/list_pop.png)'

`Index(value)` --> returns the index of the first occurrence of the value <br>
`Count(value)` --> returns the number of occurrences of the value <br>
![list_index_count](./images/week8/list_index_count.png)

`Reverse()` --> reverses the list in place <br>
`Sort()` --> sorts the list in place <br>

**Comparing lists and strings:** <br>
![list_vs_string](./images/week8/list_vs_string.png)
![list_vs_string2](./images/week8/list_vs_string2.png)

- `Upper` method was not a mutating operation - did not change the change/update the calling object. Unlike the `append` method.
  - Ex: `s` still refers to lower-case string.
  - We could assign a new variable for the upper-case string

List Mutability: <br>
![list_mutability](./images/week8/list_mutability.png)
![list_mutability2](./images/week8/list_mutability2.png)
![list_mutabilit3](./images/week8/list_mutability3.png)

Mutation vs. Construction: <br>
![mutation_vs_construction](./images/week8/mutation_vs_construction.png)
![constructing_list](./images/week8/constructing_list.png)
![mutating_list](./images/week8/mutating_list.png)
