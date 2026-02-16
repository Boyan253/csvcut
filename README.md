# csvcut

> Select, drop and reorder CSV columns by name instead of by index.

## Why

`cut -f 2,5` breaks the moment someone reorders a column. `csvcut` addresses
columns by name, so your pipeline survives a schema change.
