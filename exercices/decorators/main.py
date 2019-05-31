def my_decorator(function):
  def decoreted_original_function():
    print("Some code in decoreted function.")
    function()
    print("More code in decoreted function.")

  return decoreted_original_function

# If the @my_decorator is commented, the original_function() will be executed
# with just its own functionalities. If not, the original_function will be
# executed within the my_decorator() functionalities.
@my_decorator
def original_function():
  print("Original function.")

original_function()
