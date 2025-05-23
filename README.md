# DOCX Renderer

This package lets you run your Microsoft Word documents like a script.
You can insert placeholders in the document and use either a Python function
or an equivalent command-line tool to convert it into an output rendered document.

[Documentation](https://docx-renderer.readthedocs.io/en)

## Installation
```console
pip install docx-renderer
```

## Usage
Below is a simple example.

```python
from docx_renderer import DOCXRenderer
p = DOCXRenderer("template.docx")

someval = "world!"
def mymethod(abc):
    return f"{abc} " * 5

p.render(
    "output.docx", 
    {
        "variable": someval, "mymethod": mymethod, "myimage": "is_it_worth.png"
    }
)
```

This will replace placeholders in the template document with the provided values.

## Before

![Before](./docs/_src/_static/before.png)

## After

![After](./docs/_src/_static/after.png)

If the template document is a self-contained Python script (i.e., it does not require
variable values and function definitions to be passed from outside), you can
generate the output document directly from the command line using the following
command.

```console
docx-renderer input_template.docx output_file.docx
```

## Placeholders
You can have placeholders for text, images, or tables. Placeholders can be added
as regular text. All placeholders should be enclosed within a pair
of triple braces (`{{{` and `}}}`).

### Text
Any placeholder which can be evaluated into a string can act as a text placeholder.

For example: `{{{"hello " * 10/2}}}` or `{{{abs(-2)}}}`

### Image
If you have added `:image()` as a suffix to the Python statement, the renderer will
try to convert the value of the Python statement to a file location and insert an
image from that file location.

For example: `{{{"c:\\temp\\myimage.png":image()}}}`

### Table
Tables are similar to images, but instead of a string, the Python
statement should evaluate to a list of lists. Then you can add `:table()` as a
suffix, and it will be converted to a table inside the document.

For example: `{{{[["col1", "col2", "col3"],[1, 2, 3]]:table()}}}` will render to

|col1 | col2 | col3|
|-----|------|-----|
|1    |2     |3    |

You can create nested tables as well (if you put a variable placeholder inside
an existing table which evaluates to a list of lists with `:table()` plugin)

### Hyperlinks
You can use placeholders with hyperlinks. These hyperlinks inturn can contain other
placeholders which should evaluate to an external link. Please note that target
placeholders dont support any plugins.