# Question 1
#  Given two strings s and t, determine whether some anagram of t is a substring of s.
#  For example: if s = "udacity" and t = "ad", then the function returns True.
#  Your function definition should look like: question1(s, t) and return a boolean True or False.

def question1(s, t):
  # check for bad inputs
  if s == None or t == None: return False
  # convert inputs to lower case
  s = s.lower()
  t = t.lower()
  t_length = len(t)
  # keep track of how many consecutive characters of potential anagram are found
  consecutive_characters = 0
  # keep track of remaining letters in anagram of t
  remaining = t_length
  # create lookup table for characters in t
  t_table = {}
  original_t_table = {}
  # populate table with initial lowercase letters and numbers
  for c in "abcdefghijklmnopqrstuvwxyz0123456789":
    t_table[c] = 0
    original_t_table[c] = 0
  # populate t_table with t characters
  for c in t:
    t_table[c] += 1
    original_t_table[c] += 1
  # go through each character c in s
  for c in s:
    # check if c is in t
    if t_table[c] > 0:
      # set t_table[c] to False since it has been used
      t_table[c] -= 1
      # member of anagram is found
      consecutive_characters += 1
      # subtract from remaining characters total
      remaining -= 1
    elif consecutive_characters == t_length and remaining == 0:
      # anagram found
      return True
    else: # otherwise reset variables
      consecutive_characters = 0
      remaining = t_length
      for c in original_t_table:
        t_table[c] = original_t_table[c]
  # in case loop does not find anagram earlier, return whether or not one was found
  return remaining == 0 and consecutive_characters == t_length


## Outputs
print "Question 1\n------------------"

print question1("kabab", "baba")
# True
print question1("udacity", "ad")
# True
print question1("udacity", "da")
# True
print question1("UdAcIty", "da")
# True
print question1("udacity123", "213")
# True
print question1("udacity", "tciy")
# True
print question1("bczazycba", "abc")
# True
print question1("udacity", "day")
# False
print question1("udacity", "daz")
# False

## Edge cases
print question1("udacity", None)
# False
print question1(None, "test")
# False


# Question 2
#  Given a string a, find the longest palindromic substring contained in a.
#  Your function definition should look like question2(a), and return a string.

class Palindrome(object):
  # create a palindrome object
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def __repr__(self):
    return str((self.left, self.right))

def findBiggestPalindrome(palindromes, a):
  # initialize variables
  maximum = 0
  biggest = None
  # go through midpoints of palindromes
  for midpoint in palindromes:
    # get palindrome from palindromes dictionary
    palindrome = palindromes[midpoint]
    # get distance from right to left indices
    distance = palindrome.right - palindrome.left
    # update maximums if bigger
    if distance > maximum:
      biggest = palindrome
      maximum = distance
  # if biggest palindrome found, return substr of a at left and right indices
  if biggest:
    return a[biggest.left:biggest.right+1]
  return False

def expandPalindromes(palindromes, a):
  length = len(a)
  # store offset for odd length palindromes
  offset = 0
  # update offset if odd
  if length % 2 == 1:
    offset = 1
  # go through each palindrome
  for midpoint in palindromes:
    # get palindrome from palindromes dictionary
    palindrome = palindromes[midpoint]
    # bound left and right by 0 and length of a
    while palindrome.left > 0 and palindrome.right < length - 1:
      # check if one step out from current left and right bounds is palindrome
      if a[palindrome.left - 1] == a[palindrome.right + 1]:
        palindrome.left -= 1
        palindrome.right += 1
      elif a[palindrome.left - offset - 1] == a[palindrome.right]:
        # for odd length palindrome
        palindrome.left -= 1 + offset * 2
        palindrome.right += 1
      elif a[palindrome.left - 1] == a[palindrome.right + offset]:
        palindrome.left -= 1
        palindrome.right += 1
      else:
        break
  return palindromes

def findPalindromes(a):
  palindromes = {}
  i = 1
  length = len(a)
  while i < length - 1:
    # check for midpoint of palindrome
    if a[i - 1] == a[i + 1]:
      # add palindrome to palindromes object
      palindromes[i] = Palindrome(i - 1, i + 1)
    if i < length - 2 and a[i - 1] == a[i + 2] and a[i] == a[i + 1]: # odd length palindrome
      # add palindrome to palindromes object
      palindromes[i] = Palindrome(i - 1, i + 2)
    i += 1
  return palindromes

def question2(a=None):
  # handle edge cases
  if a == None or len(a) == 0: return None
  if len(a) == 0: return None
  # find biggest palindrome
  return findBiggestPalindrome( expandPalindromes( findPalindromes(a), a), a)


## Outputs
print "\nQuestion2\n----------------"

print question2("a")
# a
print question2("ab")
# False
print question2("aba")
# aba
print question2("abaabbba")
# abbba
print question2("abba")
# abbba
print question2("abbba")
# abbba
print question2("abbbba")
# abbbba
print question2("abcba")
# abcba
print question2("cabaz")
# aba
print question2("zzaba")
# aba
print question2("abazz")
# aba
print question2("abcba")
# False
print question2("abccba")
# abccba
print question2("cabccba")
# abccba

## Edge Cases
print question2("")
# None
print question2()
# None


# Question 3
#  Given an undirected graph G, find the minimum spanning tree within G.
#  A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges.
#  Your function should take in and return an adjacency list structured like this:
#  {'A': [('B', 2)],
#   'B': [('A', 2), ('C', 5)],
#   'C': [('B', 5)]}
#  Vertices are represented as unique strings. The function definition should be question3(G)

class Node(object):
  def __init__(self, value):
    self.value = value
    self.edges = []

  def __repr__(self):
    return "%s" % (self.value)

  def inspect(self):
    print "\n<%s>" % self.value
    for edge in self.edges:
      print " ", edge
    print "</%s>\n" % self.value

class Edge(object):
  def __init__(self, value, node_from, node_to):
    self.value = value
    self.node_from = node_from
    self.node_to = node_to

  def __repr__(self):
    return "%s --> %s" % (self.node_from, self.node_to)

class Graph(object):
  def __init__(self, nodes=[], edges=[]):
    self.nodes = nodes
    self.nodes_by_value = {}
    self.edges = set(edges)

  def insert_node(self, node_value):
    node = Node(node_value)
    self.nodes.append(node)
    self.nodes_by_value[node_value] = node

  def find_node(self, value):
    if value in self.nodes_by_value:
      return self.nodes_by_value[value]
    else:
      return None

  def add_edge(self, weight, from_value, to_value):
    # get node from values
    from_node = self.find_node(from_value)
    to_node = self.find_node(to_value)
    # if to node or from node doesn't exist, exit
    if None in [to_node, from_node]:
      return None
    # create new edge
    edge = Edge(weight, from_node, to_node)
    # add it to from_node edges
    if edge not in from_node.edges:
      from_node.edges.append(edge)
    # add it to to_node edges
    if edge not in to_node.edges:
      to_node.edges.append(edge)
    # add to all edges list
    self.edges.add(edge)

  def get_adjacency_list(self, edges=[]):
    adjacencies = {}
    # get edges if none provided
    if not len(edges):
      edges = self.edges
    for edge in edges:
      # check for existing adjacency
      if adjacencies.get(edge.node_from.value, None):
        adjacencies[edge.node_from.value].append((edge.node_to.value, edge.value))
      else:
        adjacencies[edge.node_from.value] = [(edge.node_to.value, edge.value)]
    return adjacencies

  def get_minimum_spanning_tree(self):
    # path stores edges to traverse tree
    path = set()
    # visited stores edges that have been visited
    visited = {}
    # sort edges and iterate through
    for edge in sorted(self.edges, key=lambda x: x.value):
      # add edge to path if edge has not been visited
      if edge.node_to not in visited:
        path.add(edge)
        visited[edge.node_to] = True
      if edge.node_from not in visited:
        path.add(edge)
        visited[edge.node_from] = True
    # return an adjacency list for the path
    return self.get_adjacency_list(sorted(path))

def question3(G=None):
  # handle edge cases
  if G == None: return None
  graph = Graph()
  # insert nodes into graph
  for node_value in G:
    graph.insert_node(node_value)
  # insert edges into graph
  for node_value in G:
    for edge in G[node_value]:
      graph.add_edge(edge[1], node_value, edge[0])
  return graph.get_minimum_spanning_tree()

## Inputs
q3_test = {
  'A': [('B', 2)],
  'B': [('A', 2), ('C', 5)],
  'C': [('B', 5)]
}

q3_test_2 = {
  'A': [('B', 2)],
  'B': [('A', 2), ('C', 5), ('D', 1)],
  'C': [('B', 5), ('D', 6)],
  'D': [('B', 1), ('C', 6)]
}

q3_test_3 = {
  'A': [('B', 2)],
}

q3_test_4 = None


## Outputs
print "\nQuestion 3:\n---------------"

print question3(q3_test)
# {'A': [('B', 2)], 'B': [('C', 5)]}

print question3(q3_test_2)
# {'A': [('B', 2)], 'C': [('B', 5)], 'D': [('B', 1)]}


## Edge cases
print question3(q3_test_3) # incomplete graph
# {}

print question3(q3_test_4) # bad input
# None


# Question 4
#  Find the least common ancestor between two nodes on a binary search tree.
#  The least common ancestor is the farthest node from the root that is an ancestor of both nodes.
#  For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents
#  of the root's left child, then that left child might be the lowest common ancestor.
#  You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties.
#  The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix,
#  where the index of the list is equal to the integer stored in that node and a 1 represents a child node,
#  r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing
#  the two nodes in no particular order. For example, one test case might be
#  question4([[0, 1, 0, 0, 0],
#             [0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0],
#             [1, 0, 0, 0, 1],
#             [0, 0, 0, 0, 0]],
#             3,
#             1,
#             4)
#  and the answer would be 3.

print "\nQuestion 4\n------------------"

class Node:
  # initialize node
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
  # for printing node
  def __repr__(self):
    return str((self.value, self.left, self.right))

def least_common_ancestor(nodes, root_index, n1, n2):
  # get root element from node list
  root = nodes[root_index]
  # check that root exists
  if root is None:
    return None
  # compare root value to n1 and n2 values
  if(root.value > n1 and root.value > n2):
    # root is bigger than both n1 and n2, so search root's left subtree
    return least_common_ancestor(nodes, root.left, n1, n2)
  if(root.value < n1 and root.value < n2):
    # root is smaller than both n1 and n2, so search root's right substree
    return least_common_ancestor(nodes, root.right, n1, n2)
  # return root value
  return root.value

def question4(T, r, n1, n2):
  # make sure inputs are valid
  if None in [T, r, n1, n2]:
    return None
  try:
    n1 = int(n1)
    n2 = int(n2)
  except ValueError:
    return None
  # create a node array to store nodes
  nodes = [None] * len(T)
  # iterate through the tree matrix
  for row_i in range(len(T)):
    row = T[row_i]
    # iterate through the columns of this row
    for col_i in range(len(row)):
      col = row[col_i]
      # if column value is > 0 there is a node relationship here
      if col > 0:
        # child node doesn't exist, so create it
        if nodes[col_i] == None:
          nodes[col_i] = Node(col_i)
        # parent node doesn't exist, so create it
        if nodes[row_i] == None:
          nodes[row_i] = Node(row_i)
        # if child value is smaller then parent, add to left of parent
        if row_i > col_i:
          nodes[row_i].left = col_i
        else: # child value is larger than parent, add to right of parent
          nodes[row_i].right = col_i
  # perform a least common ancestor search
  return least_common_ancestor(nodes, r, n1, n2)

test_a = [[0, 1, 0, 0, 0], #      3
          [0, 0, 0, 0, 0], #     / \
          [0, 0, 0, 0, 0], #    0   4
          [1, 0, 0, 0, 1], #   /
          [0, 0, 0, 0, 0]] #  1

test_b = [[0, 0, 0, 0, 0], #     3
          [1, 0, 1, 0, 0], #    / \
          [0, 0, 0, 0, 0], #   1   4
          [0, 1, 0, 0, 1], #  / \
          [0, 0, 0, 0, 0]] # 0   2

print question4(test_a, 3, 1, 4)
# 3

print question4(test_b, 3, 0, 2)
# 1

print question4(test_b, 3, 0, 4)
# 3

## Edge Cases
print question4(None, 3, 0, 4) # bad bst value
# None

print question4(test_b, 3, 0, "a") # bad n2 value
# None


# Question 5
#  Find the element in a singly linked list that's m elements from the end.
#  For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element.
#  The function definition should look like question5(ll, m), where ll is the first node of a
#  linked list and m is the "mth number from the end". You should copy/paste the Node class below
#  to use as a representation of a node in the linked list. Return the value of the node at that position.

class Node(object):
 def __init__(self, data):
   self.data = data
   self.next = None

class LinkedList(object):
  def __init__(self, head=None):
    self.head = head
    # keep track of the number of elements in the list
    self.count = 0

  def append(self, element):
    # start at head
    current = self.head
    # check for existing head
    if self.head:
      # go through all elements
      while current.next:
        current = current.next
      current.next = element
    else: # otherwise add it
      self.head = element
    # add to count
    self.count += 1

  def from_last(self, m):
    # check if m is within length of list
    if m > self.count - 1:
      return None
    # initialize count
    i = 0
    # start at head
    current = self.head
    if current:
      # go through elements through count - m
      while i < self.count - m - 1 and current.next:
        current = current.next
        i += 1
      # return current element's value
      return current.data

def question5(ll, m=None):
  if m is None: return m
  return ll.from_last(m)

print "\nQuestion 5\n---------------"

# set up linked list
ll = LinkedList()
for i in range(5):
  ll.append( Node(i) )

# < 0, 1, 2, 3, 4, 5 >

## outputs
print question5(ll, 0)
# 4

print question5(ll, 1)
# 3

print question5(ll, 2)
# 2

print question5(ll, 3)
# 1

print question5(ll, 4)
# 0

## Edge Cases
print question5(ll, 5) # m outside of linked list
# None

print question5(ll) # bad input
# None