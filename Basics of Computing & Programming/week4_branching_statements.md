# Week 4: Branching Statements

[Python Operators](https://www.w3schools.com/python/python_operators.asp) <br>
[Python Conditions](https://www.w3schools.com/python/python_conditions.asp)

---

## Part 1:

Data Types:

- Int
- Float
- Bool

Expressions:

- I/O expressions
- Assignment
- Arithmetic expressions
- Boolean expressions

Control Flow:

- Sequential
- Branching

![control flow](./images/week4/control_flow.png)

**The Bool Data Type**

Kind of Data:

- Truth value (true/false)

Inner Representation:

- False is represented by a sequence of 0s
- True is any non-zero value

Python Literals (upper-case first letters):

- True
- False

Boolean Operators:

- Not
- And
- Or --> most programming languages use inclusive `or` operator

![exclusive_inclusive_or](./images/week4/exclusive_inclusive.png)

**Boolean Expressions** <br>
Atomic Boolean Expressions:

- The bool literals - `True, False`
- Arithmetic expressions compared with relational operators: `<, >, ≤, ≥, ==, !=`
  - `==` --> check equivalency; is equal to?
  - `!=` --> check equivalency; is not equal to?

Compound Boolean Expressions:

- Simple Boolean expressions combined with Boolean operators (not, and, or)

Syntax and Semantics <br>
`if` statement --> `if` keyword followed by a space (or parentheses) containing Boolean expression ending with a colon `:` and indented block statements afterwards; these statements are conditioned by the `if`

![if_statement](./images/week4/if_statement.png)

_Computing Absolute Value_ <br>

![absolute_value](./images/week4/abs_value.png)
![absolute_value](./images/week4/abs_value1.png)
![absolute_value](./images/week4/abs_value2.png)

---

## Part 2:

Syntax and Semantics <br>
`If-else` statement (two-way if)

![if_else_statement](./images/week4/ifElse_statement.png)

_Determining Parity (even or odd)_ <br>

![parity](./images/week4/parity.png)

Two-way if (`if-else`) statement:

- Guarantees that one out of two blocks of code will be executed
- No way for zero or both blocks of code to be executed

Sequential If statements:

- Can lead to zero, one, or two blocks of code being executed (though not in this specific case)

---

## Part 3:

The Letter Grade Problem
Implementation with excess nesting that requires more computation

- Two-way if leads to another two-way if etc.

![letter_grade](./images/week4/letter_grade.png)
![letter_grade1](./images/week4/branching.png)

Syntax and Semantics <br>
`If-elif-else` statement: <br>
![if-elif-else](./images/week4/if_elif_else.png)

Solving the Letter Grade Problem: <br>
Using direct multi-way (`if-elif-else`) implementation

![letter_grade](./images/week4/letter_grade1.png)

Convert 24-hour to 12-hour time format:
![Convert Time](./images/week4/time_conversion.png)

![Convert Time Example](./images/week4/time_conversion_example.png)

Add the `sep=""` parameter in the print statement to eliminate the (default) spacing in the output
