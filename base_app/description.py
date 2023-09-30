TAGS = [
    {
        'name': 'extends',
        'description': """
         Used to create a template inheritance hierarchy in Django.
         """,
        'syntax': """{% extends template %}"""
    },
    {
        'name': 'debug',
        'description': """
         Outputs a whole load of debugging information, including the current context and 
         imported modules. {% debug %} outputs nothing when the DEBUG setting is False.
         """,
        'syntax': """{% debug %}""",
    },
    {
        'name': 'cycle',
        'description': """
         Produces one of its arguments each time this tag is encountered. The first argument is 
         produced on the first encounter, the second argument on the second encounter, and so forth
         """,
        'example': """<p>
                <b>{% cycle 'first' 'second' as tmp %}</b>
            </p>
            <p>
                <b>{% cycle tmp %}</b>
            </p>
        """,
    },
    {
        'name': 'regroup',
        'description': """
         The regroup tag returns a new object grouped by a specified value.
         """,
        'syntax': """{% regroup list_of_dicts %}""",
    },
    {
        'name': 'csrf_token',
        'description': """
         This tag is used for CSRF protection.
         """,
        'syntax': """{% csrf_token %}""",
    },
    {
        'name': 'lorem',
        'description': """Displays random “lorem ipsum” Latin text. 
         This is useful for providing sample data in templates.
         """,
        'syntax': """{% lorem [count] [method] [random] %}""",
        'example': """{% lorem %}""",
    },
    {
        'name': 'block',
        'description': """Defines a block that can be overridden by child templates""",
        'syntax': """{% block name %}""",
    },
    {
        'name': 'include',
        'description': """Loads a template and renders it with the current context. 
         This is a way of “including” other templates within a template.
         """,
        'syntax': """{% include path %}""",
    },
]

FILTERS = [
    {
        'name': 'linebreaks',
        'description': """Replaces line breaks in plain text with appropriate HTML""",
        'text': 'Hello \n world',
        'syntax': """{{ 'Hello World'|linebreaks }}""",
        'example': """{{ tag.text|linebreaks }}"""
    },
    {
        'name': 'length_is',
        'description': """Returns True if the value’s length is the argument, or False otherwise.""",
        'example': """{{ 'HEllo'|length_is:'5' }}"""
    },
    {
        'name': 'random',
        'description': """Returns a random item from the given iterable.""",
        'example': """{{ 'abcdefg'|random }}"""
    },
    {
        'name': 'escape',
        'description': """Escapes a string’s HTML. Specifically, it makes these replacements:
        < is converted to &lt;
        > is converted to &gt;
        ' (single quote) is converted to &#x27;
        " (double quote) is converted to &quot;
        & is converted to &amp;""",
        'text': '<b>HAllo!</b>',
        'syntax': """{{ '<b>HAllo!</b>'|escape }}""",
        'example': """{{ tag.text|escape }}""",
    },
    {
        'name': 'pluralize',
        'description': """Returns a plural suffix if the value is not 1, '1', or an object of length 1.
        By default, this suffix is 's'.""",
        'example': """You have 10 message{{ 10|pluralize }}""",
    },
    {
        'name': 'linenumbers',
        'description': """Displays text with line numbers.""",
        'text': "one\ntwo\nthree",
        'syntax': "{{ 'one \\n two \\n three'|linenumbers }}",
        'example': """{{ tag.text|linenumbers }}""",
    },
    {
        'name': 'make_list',
        'description': """Returns the value turned into a list.
        For a string, it’s a list of characters. For an integer, the argument is cast to a string before creating a list.""",
        'example': """{{ 'Joel'|make_list }}""",
    },
    {
        'name': 'first',
        'description': """Returns the first item in a sequence.""",
        'example': """{{ 'Joel'|first }}""",
    },
    {
        'name': 'divisibleby',
        'description': """Returns True if the value is divisible by the argument.""",
        'example': """{{ '15'|divisibleby:'5' }}""",
    },
    {
        'name': 'center',
        'description': """Centers the value in a field of a given width.""",
        'example': """{{ 'Hallo'|center:'15' }}""",
    },
    {
        'name': 'filesizeformat',
        'description': """Formats the value like a ‘human-readable’ file size (i.e. '13 KB', '4.1 MB', '102 bytes', etc.).""",
        'example': """{{ '123456789'|filesizeformat }}""",
    },
    {
        'name': 'urlize',
        'description': """Converts URLs and email addresses in text into clickable links.""",
        'example': """{{ "Check out www.djangoproject.com"|urlize }}""",
    },
    {
        'name': 'linebreaksbr',
        'description': """Converts all newlines in a piece of plain text to HTML line breaks""",
        'text': "Joel\nis a slug",
        'syntax': """{{ "Joel\\nis a slug"|urlize }}""",
        'example': """{{ tag.text|linebreaksbr }}""",
    },
    {
        'name': 'dictsort',
        'description': """Takes a list of dictionaries and returns that list sorted by the key given in the argument.""",
        'val': [{"name": "zed"}, {"name": "amy"}, {"name": "joe"},],
        'syntax': """{{ [{"name": "zed"},
        {"name": "amy"}, 
        {"name": "joe"}
        ]|dictsort:'name' }}""",
        'example': """{{ tag.val|dictsort:'name' }}""",
    },
    {
        'name': 'stringformat',
        'description': """Formats the variable according to the argument, a string formatting specifier.""",
        'example': """{{ 15213|stringformat:'X' }}""",
    },
]
