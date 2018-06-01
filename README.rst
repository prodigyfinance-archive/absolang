Absolang
========

A sentiment analysis library for detecting absolutist language.

Quickstart
----------

Installation::

    $ pip install absolang
    $ python -m spacy download en_core_web_sm

Determining absolutist index for text::

    >>> from absolang import absolutist, absolutist_index
    >>> absolutist_index("The bigger dog is running.")
    0.0
    >>> absolutist("The bigger dog is running.")
    False
    >>> absolutist_index("He was completely bowled over.")
    0.2
    >>> absolutist("He was completely bowled over.")
    True

Algorithm
---------

* Parse text into tokens using Spacy's en_core_web_sm language model.
* Count the number of word tokens (a token is considered a word if it
  consists solely of characters from the alphabet).
* Count the number of absolutist word tokens (a token is considered
  absolutist if its stem word is in the dictionary of absolutist words
  and it is not preceded by a negation, modifier or interjection).
* The absolutist index is the number of absolutist words divided by the
  total number of words.
* Text is considered absolutist if the index is greater than 1.1 percent.

Caveats
-------

* The frequency of absolutist words in control texts (ones written by
  people presumed not to suffer from anxiety or depression more than
  the average person) is about 1%, so one needs a few hundred words of
  texts before results start becoming meaningful.

References
----------

* `In an Absolute State: Elevated Use of Absolutist Words Is a Marker Specific to Anxiety, Depression, and Suicidal Ideation <http://journals.sagepub.com/doi/pdf/10.1177/2167702617747074>`_

* `FCA Occasional Paper No. 8: Consumer Vulnerability <https://www.fca.org.uk/publications/occasional-papers/occasional-paper-no-8-consumer-vulnerability>`_
