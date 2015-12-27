# Addok postcode_usage_name_BAN_FR

[Addok](https://github.com/etalab/addok) add-on to support postcode and short city name as equal as full city name.

This add-on makes two things:
* Support city name, only postcode, or both to produce same result.
* Support first part of composed city name as equal of full city name.

## Addressed problem

### Postcode

|   | Just Addok | This add-on |
|---|---|---|
|q=Bordeaux | city | city |
|q=33000 | a street | city |
|q=33000 Bordeaux | a street | city |

### First part of city name

Some cities have composed names, some times long one, e.g. Adelans-et-le-Val-de-Bithaine.
But long names are not in use in daily life.

Assuming autoclomplete as false.
When you use the name of "Brive" in France you probably mean the city of "Brive-la-Gaillarde", but not the locality of "Brive" about the village of "Guenrouet".

## Configuration

Load the add-on in Addok config file and use it:
```python
sys.path.append('/srv/addok/addok') # abs path to config file directory
from postcode_usage_name_BAN_FR import get_labels

MAKE_LABELS = get_labels
```

## How it works

### Postcode

On query this add-on rewrite the result from Addok search by replacing each result label by three:
- with, city name only, the original
- with postcode only
- with both postcode and city name

### First part of city name

Same principle here, this add-on replaces labels by multiple versions after split the name on "-".

Example:
```
input: Adelans-et-le-Val-de-Bithaine
matchable output: Adelans-et-le-Val-de-Bithaine, Adelans-et-le-Val, Adelans
```
