# csvcut

> Select, drop and reorder CSV columns by name instead of by index.

## Why

`cut -f 2,5` breaks the moment someone reorders a column. `csvcut` addresses
columns by name, so your pipeline survives a schema change.

## Usage

```
python csvcut.py data.csv --list                 # print the column names
python csvcut.py data.csv -f name,email          # keep these, in this order
python csvcut.py data.csv -x password,token      # keep everything else
python csvcut.py data.csv -f id --ignore-missing # tolerate absent columns
cat data.csv | python csvcut.py - -f id
```

Output goes to stdout as CSV, so it chains:

```
python csvcut.py users.csv -f id,email | python csv2json.py - --lines
```

## Notes

- `-f` and `-x` are mutually exclusive in practice; `-f` wins if both are given.
- Rows missing a requested column emit an empty cell rather than failing.
- The delimiter is used for both reading and writing, so `-d ';'` round-trips.
