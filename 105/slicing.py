from string import ascii_lowercase

text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""


def slice_and_dice(text=text):
    """Strip the whitespace (newlines) off text at both ends,
       split the text string on newline (\n).
       Next check if the first char of each (stripped) line is lowercase,
       if so split the line into words and append the last word to
       the results list. Make sure that you strip off any trailing
       exclamation marks (!) and dots (.), Return the results list."""

    results = []

    strip_text = text.strip("\n")

    final_text = strip_text.split("\n")

    for x in final_text:

        x = x.strip(" ")

        if x[0].islower():

            y = x.strip("!.")

            final_split = y.split(" ")

            results.append(final_split[-1])

    return results


slice_and_dice()
