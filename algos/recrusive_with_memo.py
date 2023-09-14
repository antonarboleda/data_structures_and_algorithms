# A template for recursive problems with memoization
def recursive_memo(args):
  if args in memoized:
    return memoized_vals
  
  base case with early return

  modification / calculation before recursive calls
    - try to limit modifications / calculations to this node only with context
      from previous calls
  
  recrusive iteration / expansion / call

  modification / calculation before recursive calls
    - try to limit modifications / calculations to this node only with context
      from previous calls
  
  if memoized, cache return vals
    e.g. map[args] = ret_vals
  return ret_vals
