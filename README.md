# Addok usage_name_BAN_FR

[Addok](https://github.com/etalab/addok) plugin to support short city name as equal as full city name.

## Addressed problem

Some cities have composed names, some times long one, e.g. Adelans-et-le-Val-de-Bithaine.
But long names are not in use in daily life.

Assuming autoclomplete as false.
When you use the name of "Brive" in France you probably mean the city of "Brive-la-Gaillarde", but not the locality of "Brive" about the village of "Guenrouet".

## Configuration

Add `addok_usage_name_BAN_FR.make_labels` after `addok_france.make_labels`.

```
SEARCH_RESULT_PROCESSORS_PYPATHS = [
    ...
    'addok_france.make_labels',
    'addok_usage_name_BAN_FR.make_labels',
    ...
```

## How it works

On query this plugin rewrite the result from Addok search by replacing each result label by possible subpart of the name splited on "-".

Example:
```
input: Adelans-et-le-Val-de-Bithaine
matchable output: Adelans-et-le-Val-de-Bithaine, Adelans-et-le-Val, Adelans
```
