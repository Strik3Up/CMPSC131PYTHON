# Author: Carter Monroe cam7002@psu.edu
# Collaborator: Nasser Zaher nzz5096@psu.edu
# Collaborator: Angela Bao ymb5072@psu.edu
# Collaborator: Anna Gillard amg7307@psu.edu
# Section: 2
# Breakout: 5

def remove_duplicate_sorted(t):
  """
  this function returns a new list generated from t that has t's
  elements without duplicates and is sorted from smallest to largest.
  
  make a set then sort the set
  """
  nt = set(t)
  lnt = list(nt)
  snt = sorted(lnt)
  
  return snt

def list_to_dictionary(t):
  """
  t is a list of values (values could be str, list, tuple, set, dictionary),
  create and return a dictionary such that the key is len(v) for some v in t,
  and the value is a list of values [v1, v2, ...] from t (in the order they
  appeared in t) whose len(vi) is the key.
  for example: if t = [(1,2,3), "abc", [1, 2], (), ""]
  then return value of this function should be:
  {3: [(1, 2, 3), 'abc'], 2: [[1, 2]], 0: [(), '']}
  """
  dicf = dict()
  for x in t:
    if len(x) not in t:
      dicf[len(x)] = [x]
    else:
      dicf[len(x)].append(x)
  return dicf

def run():
  """
  This function repeatedly asks the user to enter a string and store them in a
  list and print it out.
  It also passes this list to remove_duplicate_sorted() function and
  list_to_dictionary() function and print out the results of the function
  calls.
  """
  il = list()
  c = 0
  while c < 1: 
    i = input("Enter a string: \n")
    il.append(i)
    ils = remove_duplicate_sorted(il)
    ild = list_to_dictionary(il)
    print(f"List: [{il}]\n")
    print(f"Sorted List: [{ils}]\n")
    print(f"Dict: {ild}\n")
    if i == "done":
      ils = remove_duplicate_sorted(il)
      ild = list_to_dictionary(il)
      #print(f"List: [{il}]\n")
      print(f"Sorted List: [{ils}]\n")
      print(f"Dict: {ild}\n")
      c + 1
      

if __name__ == "__main__":
  run()
