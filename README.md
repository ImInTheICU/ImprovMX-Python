<h1 align="center" id="title">🐍 ImprovMX-Python</h1>
<p align="center"><img src="https://socialify.git.ci/ImInTheICU/ImprovMX-Python/image?description=1&font=Source%20Code%20Pro&language=1&name=1&owner=1&pattern=Solid&pulls=1&stargazers=1&theme=Dark" alt="ImprovMX-Python" width="640" height="320" /></p>

<h2 align="center">🚀 Showcase</h2>
<p align="center">https://github.com/ImInTheICU/ImprovMX-Python/assets/111275373/3755e2d0-6c3d-4e60-ba15-f4032060d3e8</p>

<h2 align="center">🧐 Features</h2>

*   Create domain alias
*   Bulk create domain alias
*   Edit domain alias
*   Delete domain alias
*   Requests sessions

<h2 align="center">✂🔨 Usage</h2>
<h3 align="left">
  -> Create domain alias

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
</h3>

<h2 align="center">🛡️ License</h2>
<p>This project is licensed under the [MIT License](https://github.com/ImInTheICU/ImprovMX-Python/blob/main/LICENSE).</p>
