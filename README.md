# redis-query
A query language for redis rejson.
## CREATE
Creates a documentof a choosen name and schema at a choosen path.
```
CREATE DOCUMENT 'obj' ('{"obj":"value"}') AT PATH('ROOT')
```
## SELECT
Gets value from redis database by name. 
```
SELECT 'name' FROM PATH('ROOT')
```
## INSERT
CREATE but only for alredy existion values.
```
INSERT 'obj' ('{"obj":"value"}') INTO PATH('ROOT')
```
## PATH
A Path in [JSONPath](https://goessner.net/articles/JsonPath/) syntax. Type ROOT for root path.
``` 
PATH('ROOT')
```
