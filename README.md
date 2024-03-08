# ImprovMX Python

ImprovMX Python is a wrapper around ImprovMX's public API built in Python3.11.

## Features

- Create domain alias
- Bulk create domain alias
- Edit domain alias
- Delete domain alias
- Session alias
## Usage/Examples

### Create domain alias
```python
from ... import ImprovMX # ... being the file with the ImprovMX class in it.

improvMX = ImprovMX(api_user="<api_user>", api_key="<api_key>") # <api_user> being the api user (default: api) # <api_key> being the api key (get one: https://app.improvmx.com/api)

improvMX.create_alias(
    domain="example.com", # The domain for which to create the alias. (must be added at https://app.improvmx.com/)
    alias="test", # The alias or list of aliases to be created. (in this example we're added a single alias)
    forward="test@gmail.com", # The email address the alias forwards to.
    bulk=False # Indicates whether to create aliases in bulk. Defaults to False.
)
```

### Bulk create domain aliases
```python
from ... import ImprovMX # ... being the file with the ImprovMX class in it.

improvMX = ImprovMX(api_user="<api_user>", api_key="<api_key>") # <api_user> being the api user (default: api) # <api_key> being the api key (get one: https://app.improvmx.com/api)

improvMX.create_alias(
    domain="example.com", # The domain for which to create the alias. (must be added at https://app.improvmx.com/)
    alias=[ # The alias or list of aliases to be created. (in this example we're added a single alias)
        {"alias": "testalias1", "forward": "test1@gmail.com"}, 
        {"alias": "testalias2", "forward": "test2@gmail.com"},
        {"alias": "testalias3", "forward": "test3@gmail.com"},
    ],
    bulk=True, # Indicates whether to create aliases in bulk. Defaults to False.
    bulkBehavior="update" # The behavior when creating aliases in bulk. Can be "add" or "update". Defaults to None.
)
```

### Edit domain alias
```python
from ... import ImprovMX # ... being the file with the ImprovMX class in it.

improvMX = ImprovMX(api_user="<api_user>", api_key="<api_key>") # <api_user> being the api user (default: api) # <api_key> being the api key (get one: https://app.improvmx.com/api)

improvMX.edit_alias(
    domain="example.com", # The domain for which the alias belongs.
    alias="test", # The existing alias to be edited.
    forward="newexample@test.com" # The new email address the edited alias forwards to.
)
```

### Delete domain alias
```python
from ... import ImprovMX # ... being the file with the ImprovMX class in it.

improvMX = ImprovMX(api_user="<api_user>", api_key="<api_key>") # <api_user> being the api user (default: api) # <api_key> being the api key (get one: https://app.improvmx.com/api)

improvMX.delete_alias(
    domain="example.com", # The domain from which to delete the alias.
    alias="test", # The existing alias to be deleted.
)
```
## Showcase

![Create & Delete aliases](https://raw.githubusercontent.com/ImInTheICU/ImprovMX-Python/main/demo/test_create_and_delete_alias.mp4)


## Example Code

```python
import time
from ... import ImprovMX

improvMX = ImprovMX(api_user="<api_user>", api_key="<api_key>")

print("list_aliases() ALIASES -> ", improvMX.list_aliases(domain="nootnoot.dev"))

time.sleep(1.5)

print("create_alias() CREATE -> ", improvMX.create_alias(domain="nootnoot.dev", alias="test", forward="new_api_user@proton.me", bulk=False))

time.sleep(1.5)

print("create_alias() CREATE BULK -> ", improvMX.create_alias(domain="nootnoot.dev", alias=[{"alias": "bulktest1", "forward": "new_api_user@proton.me"}, {"alias": "bulktest2", "forward": "new_api_user@proton.me"}], forward="new_api_user@proton.me", bulk=True, bulkBehavior="update"))

time.sleep(1.5)

print("create_alias() EDIT -> ", improvMX.edit_alias(domain="nootnoot.dev", alias="test", forward="newer_api_user@proton.me"))

time.sleep(1.5)

print("create_alias() DELETE -> ", improvMX.delete_alias(domain="nootnoot.dev", alias="test"))

time.sleep(1.5)

print("create_alias() DELETE -> ", improvMX.delete_alias(domain="nootnoot.dev", alias="bulktest1"))

time.sleep(1.5)

print("create_alias() DELETE -> ", improvMX.delete_alias(domain="nootnoot.dev", alias="bulktest2"))
```


## Authors

- [Christopher](https://www.github.com/ImInTheICU)


## License

[MIT](https://choosealicense.com/licenses/mit/)

