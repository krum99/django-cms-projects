import re

def split_words(obj: object | str) -> str:
    """
    Split a CamelCase string or class name into separate words.

    This function accepts either a string or a class/type object and
    returns a human-readable string where words in CamelCase notation
    are separated by spaces.

    Parameters
    ----------
    obj : str or type
        A CamelCase string (e.g. "MyClassName") or a class/type object
        whose name will be processed.

    Returns
    -------
    str
        A string with words separated by spaces.
        Example: "MyClassName" -> "My Class Name"

    Raises
    ------
    TypeError
        If `obj` is neither a string nor a class/type object.

    Examples
    --------
    >>> split_words("MyClass")
    'My Class'

    >>> class MyClass:
    ...     pass
    >>> split_words(MyClass)
    'My Class'

    >>> split_words("HTTPServer")
    'HTTP Server'
    """

    if not isinstance(obj, str):
        if hasattr(obj, "__name__"):
            obj = obj.__name__
        else:
            raise TypeError("Object must be a string or a class")

    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', obj)

