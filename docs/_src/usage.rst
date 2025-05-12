Using DOCXRenderer
==================

DOCXRenderer allows you to write Python code inside a Word document and execute
it like a script. The output is rendered as a new document. You can use the
following types of Python code inside the input template.

Simple Python expressions
-------------------------

You can write simple Python expressions inside any paragraph which gets evaluated
at render time.

For example, you can write `{{{5.566*3.456}}}` or `{{{sum([1123, 123, 123, 4])}}}`

Substituting variable values and function results
-------------------------------------------------

You can write expressions like `{{{variable_name}}}` or function calls like
`{{{my_function("arg")}}}` in the document. These variables and functions
should be passed in as arguments to the render function.

For example:

If there is a template document which contains `{{{my_variable}}}` in a paragraph,
and there is a function call `{{{calculate_square(my_variable)}}}` in another
(or the same) paragraph, you can pass in the input like below.

.. code-block:: python

   from docx_renderer import DOCXRenderer
   p = DOCXRenderer("template.docx")

   def sqr(input):
       return input*input

   p.render(
      "output.docx", 
      {
         "my_variable": 100,
         "calculate_square": sqr
      }
   )

Inserting images
----------------

You can replace placeholders with images using `DOCXRenderer`.
To insert an image, add a placeholder text in the format `{{{path_to_image:image()}}}`
where `path_to_image` is a variable whose value is the path to the image to be inserted.

Inserting tables
----------------

Similar to images, you can replace placeholders with tables.
To create a table, add a placeholder text in the format 
`{{{table_data:table()}}}` where `table_data` is a variable whose value is a
list of lists.

For example:

.. code-block:: python

   table_data = [["Header1", "Header2"], ["Row1Col1", "Row1Col2"]]
   p.render("output.docx", {"table_data": table_data})

Writing code in comments
-------------------------

Apart from using Python expressions inside paragraphs, you can write more
elaborate code inside the comments of the document surrounded by triple backticks
followed by the `python` keyword as shown below.

.. code-block::

   ```python
   # Python code
   ```

The code inside this block will get executed before the document is evaluated.
So, for example, you can define a function inside the comments like below.

.. code-block::

   ```python
   def doubler(input):
      return input*2
   ```

Then you can write `{{{doubler(100)}}}` inside one of the paragraphs in the same
document.