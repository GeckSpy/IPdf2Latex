# my own tokenizer, which just tokenizes on whitespace--equivalent to .split() method in python

import abc
from nltk.stem import porter



class Tokenizer(abc.ABC):
  """Abstract base class for a tokenizer.

  Subclasses of Tokenizer must implement the tokenize() method.
  """

  @abc.abstractmethod
  def tokenize(self, text):
    raise NotImplementedError("Tokenizer must override tokenize() method")


class DefaultTokenizer(Tokenizer):
  """Default tokenizer which tokenizes on whitespace."""

  def __init__(self):
    """Constructor for DefaultTokenizer.


    """
    

  def tokenize(self, text):
    text1 = text.split()
    return text1
