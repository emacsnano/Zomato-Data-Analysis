# Zomato Restaurant EDA

This project is a small exploratory data analysis (EDA) of a Zomato restaurant dataset. The goal is to look at how restaurant attributes relate to customer engagement and ratings, using a Python-based data analysis workflow rather than a production web app or dashboard.

The analysis focuses on questions such as:
- Which restaurant categories are most common?
- Which restaurants receive the most votes?
- Does offering online ordering correlate with different rating patterns?
- How are restaurant ratings distributed?
- What is the typical approximate cost for two people?
- Are certain restaurant types more likely to support online ordering?

## Dataset
The project uses the file `Zomato-data-.csv`, which contains fields such as:
- `name`
- `online_order`
- `book_table`
- `rate`
- `votes`
- `approx_cost(for two people)`
- `listed_in(type)`

This dataset is primarily about restaurant metadata, customer feedback, and ordering availability rather than a full transactional or customer-order history.

## What the script does
The Python script `zomato.py` performs a straightforward EDA workflow:
1. Loads the CSV data.
2. Cleans the `rate` column by converting values like `4.1/5` into numeric floats.
3. Explores restaurant categories and popular types.
4. Identifies the most-voted restaurants.
5. Visualizes online-order availability and rating distributions.
6. Compares ratings for online vs offline ordering.
7. Builds a heatmap showing ordering preferences by restaurant category.

## Libraries used
- pandas
- numpy
- matplotlib
- seaborn

## Run it locally
From the project folder:

```bash
pip install pandas numpy matplotlib seaborn
python zomato.py
```

## Key learnings from this EDA
This project demonstrates a few useful data-analysis patterns that are common in exploratory work:

- Data cleaning is essential: restaurant ratings in the CSV are stored as strings like `4.1/5`, so they need to be converted to numeric values before analysis.
- Visual exploration helps uncover patterns quickly: countplots and heatmaps make it easier to spot restaurant type trends and ordering behaviors.
- Aggregation can highlight business insights: grouping by `listed_in(type)` and analyzing `votes` reveals which kinds of restaurants attract more customer attention.
- Categorical comparisons are useful for decision-making: examining `online_order` against `rate` and restaurant type helps understand customer preferences and operational trends.
- EDA is not only about charts; it’s about asking the right questions and turning raw values into business understanding.

This project is best understood as a quick, practical EDA script for learning data cleaning, grouping, and visualization with real restaurant data.
