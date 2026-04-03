# Day 10 - Pandas Basics

## Topics Covered

* Introduction to Pandas
* Series
* DataFrame
* Creating DataFrames
* Basic DataFrame operations

---

## What I Learned

### 1. Introduction to Pandas

Pandas is a Python library used for data analysis and manipulation.
It provides powerful data structures like Series and DataFrame.

Pandas is widely used in data science and machine learning for handling datasets.

---

### 2. Series

A Series is a one-dimensional labeled array.

Example:
import pandas as pd

data = [10, 20, 30]
s = pd.Series(data)
print(s)

Explanation:

* Stores data in a single column
* Has index and values

---

### 3. DataFrame

A DataFrame is a two-dimensional table with rows and columns.

Example:
data = {
"name": ["Atharva", "Rahul"],
"marks": [85, 90]
}

df = pd.DataFrame(data)
print(df)

Explanation:

* Similar to a table or spreadsheet
* Columns can have different data types

---

### 4. Creating DataFrames

Example:
import pandas as pd

data = {
"Name": ["A", "B", "C"],
"Age": [20, 21, 22]
}

df = pd.DataFrame(data)

---

### 5. Basic Operations

#### View data

print(df.head())

#### Get column

print(df["Name"])

#### Get multiple columns

print(df[["Name", "Age"]])

#### Shape of data

print(df.shape)

#### Info about data

print(df.info())

Explanation:

* head() shows first few rows
* shape gives rows and columns
* info() gives summary of dataset

---

## Code Example

import pandas as pd

data = {
"Name": ["Atharva", "Rahul"],
"Marks": [85, 90]
}

df = pd.DataFrame(data)
print(df)

---

## My Understanding

Pandas makes it easy to work with structured data.
DataFrames are very powerful and are used in almost every data science task.
It is similar to working with Excel but using Python.

---

## Challenges Faced

* Understanding difference between Series and DataFrame
* Learning syntax of Pandas

---

## Key Takeaways

* Pandas is used for data analysis
* Series is 1D, DataFrame is 2D
* DataFrame is the most important structure

---

## Next Step

Learn data selection, filtering, and handling missing data
