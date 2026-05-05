# Introduction to Data Cleansing

During writing, reading, storage, transmission, or processing, errors can occur which introduce unintended changes to the original data.

## Learning Objectives

By the end of this lesson, learners should be able to:

- Define what Data Cleansing is
- Explore areas to consider when assessing data quality
- Gain insight into the ways data is inspected
- Identify some approaches to cleansing data
- Apply basic cleaning techniques in Jupyter notebooks
  - Use Pandas to identify and fix simple data quality problems

## What is Data Cleansing?

Data cleansing is the process of detecting and correcting data quality.

Real-world data may be:

- Inaccurate
- Missing values
- Inconsistent
- Duplicated
- Poorly formatted
- Corrupt
- Irrelevant

There can also be Personally Identifiable Information (PII) in data that needs to be removed

Before analysing data, building dashboards, or training machine learning models, we usually need to clean the data first.

**Can you spot the dirty data?**

![](img/dirty-data-table.svg)

<details><summary>Reveal</summary>Examples of dirty data in the image:

- Duplicate values in id column
- "FF" in age column
- Typo of "Computer Science" in branch column
- "Computing" vs "Computer Science" in branch column
- "Mrs X" vs "Mrs. X" in teacher column
- DD/MM/YYYY vs MM/DD/YYYY in start_date column
- Missing number in tel column
- Duplicate person "Mary Ahmed"
</details>

### Why Data Cleansing Matters

Poor quality data can lead to:

- Incorrect business decisions
- Misleading reports
- Failed automation
- Software bugs
- Unreliable machine learning predictions

A common phrase in data science is:

>“Garbage in, garbage out.”

If the input data is poor, the results will also be poor.

### Data Quality

When assessing data quality, consider the following:

- Validity
- Accuracy
- Consistency
- Completeness
- Uniformity

#### Validity

The degree to which the data conforms to defined business rules or constraints.

Examples could include:

- Ages should not be negative
- Email addresses should contain '@'
- Dates should use valid formats
- Product quantities should not be below zero
- Certain columns can't be empty
- Certain columns must be a particular data type.

#### Accuracy

The degree to which the data is 'true'.

For example, validating that a postcode actually exists, however, data can be valid, but inaccurate. If someone moves house but their data isn't updated, all of the address details are valid, but now inaccurate.

#### Consistency

The degree to which the data is consistent, within the same data set or across multiple data sets.

Examples include:

- A customer has two different addresses in two different tables.
  - This might indicate a need to normalise
- Different data being entered to represent the same thing; "uk", "UK", and "United Kingdom" all mean the same thing to a human, but not a computer.

Inconsistent data can cause:

- Incorrect grouping
- Duplicate categories
- Broken reports
- Poor visualisations

#### Completeness

The degree to which all the data required is known.

E.g. missing fields from a form that was filled in.

#### Uniformity

Ensuring that data is using the same format, unit, and structure.

Examples of non-uniform data:

|Price|
|---|
|£100|
|100 GBP|
|100|

or:

|Date|
|---|
|01/05/2026|
|2026-05-01|
|May 1st 2026|

Data that lacks uniformity may result in:

- Incorrect Sorting
- Calculations may break
- Data analysis becomes unreliable


# 5. Uniformity

## What is Uniformity?

Uniformity means:

> Data uses the same format, units, and structure.

Examples of non-uniform data:

| Example |
| ------- |
| £100    |
| 100 GBP |
| 100     |

or:

| Example      |
| ------------ |
| 01/05/2026   |
| 2026-05-01   |
| May 1st 2026 |

---

# Why Uniformity Matters

Without uniform formatting:

* Sorting may fail
* Calculations may break
* Data analysis becomes unreliable

---

# Example — Date Formatting

```python
orders = pd.DataFrame({
    'date': ['01/05/2026', '2026-05-02', 'May 3 2026']
})

orders
```

---

# Converting to Uniform Dates

```python
orders['date'] = pd.to_datetime(orders['date'])

orders
```

---

# Example — Uniform Text Case

```python
sales_data['country'] = sales_data['country'].str.upper()
```

---

# Example — Uniform Whitespace

```python
sales_data['country'] = sales_data['country'].str.strip()
```

---

# Summary Table

| Concept      | Meaning                               | Example Problem       |
| ------------ | ------------------------------------- | --------------------- |
| Validity     | Follows rules                         | Negative age          |
| Accuracy     | Reflects reality                      | Wrong salary          |
| Consistency  | Same meaning represented consistently | UK vs uk              |
| Completeness | Missing data exists                   | Empty email           |
| Uniformity   | Same formatting/style                 | Multiple date formats |

---

# Suggested Classroom Activities

# Activity 1 — Spot the Problems

Give learners a messy dataset and ask them to identify:

* Invalid values
* Missing values
* Inconsistent formatting
* Suspicious data

---

# Activity 2 — Clean the Dataset

Learners should:

1. Standardise country names
2. Remove invalid ages
3. Fill missing purchase amounts
4. Convert dates to uniform format

---

# Activity 3 — Create Validation Rules

Ask learners to define rules such as:

* Age must be between 0 and 120
* Emails must contain '@'
* Purchase amounts must be positive

---

# Extension Activities

## Duplicate Detection

```python
sales_data.duplicated()
```

---

## Remove Duplicates

```python
sales_data.drop_duplicates()
```

---

## Data Type Inspection

```python
sales_data.dtypes
```

---

## Convert Data Types

```python
sales_data['age'] = sales_data['age'].astype('float')
```

---

# Suggested Discussion Topics

* Is automated cleaning always safe?
* Can cleaning introduce bias?
* Should original raw data always be preserved?
* Why is data governance important?

---

# Mini Project Suggestion

Provide learners with a CSV file containing:

* Missing values
* Invalid ages
* Inconsistent country names
* Duplicate rows
* Mixed date formats

Task:

> Clean the dataset and prepare it for analysis.

Learners should document:

* What problems they found
* How they fixed them
* Which assumptions they made

---

# Final Takeaways

Good quality data should be:

* Valid
* Accurate
* Consistent
* Complete
* Uniform

Data cleansing is a critical step in:

* Data analysis
* Business intelligence
* Machine learning
* Software systems
* Reporting and dashboards

In real-world projects, cleaning data often takes far more time than analysing it.
