from pathlib import Path
from docx_renderer import DOCXRenderer

p = DOCXRenderer("testdoc.docx")

variable = "world!"

def somemethod(abc):
    return f"{abc} " * 5

table_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

p.render(
    "output.docx",
    {
        "variable": variable,
        "mymethod": somemethod,
        "table_data": table_data,
        "myimage": r".\docs\_src\_static\is_it_worth_the_time.png",
    },
)
