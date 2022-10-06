# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler, *args):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)
        self.root_handler = root_handler
        if args:
            self.not_found_handler = args[0]
        else:
            self.not_found_handler = None

    def getRootHandler(self):
        return self.root_handler

    def getNotFoundHandler(self):
        return self.not_found_handler

    def insert(self, pathArr, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for key in pathArr:
            if not current_node.children.get(key):
                current_node.children[key] = RouteTrieNode()
            current_node = current_node.children[key]

        current_node.handler = handler

    def find(self, pathArr):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        # A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
        if len(pathArr) == 1 and pathArr[0] == "":
            return self.getRootHandler()

        current_node = self.root
        for key in pathArr:
            if key not in current_node.children:
                return self.getNotFoundHandler()
            else:
                current_node = current_node.children.get(key)
        return current_node.handler


class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler


class Router:
    def __init__(self, root_handler, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.trie.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler = self.trie.find(self.split_path(path))
        if handler is None:
            return self.trie.getNotFoundHandler()
        else:
            return handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        # Here are some test cases and expected outputs you can use to test your implementation

        # create the router and add a route
        # remove the 'not found handler' if you did not implement this
        return path.strip("/").split("/")


router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
assert router.lookup("/") == "root handler"  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
assert router.lookup("/home") == "not found handler"
# should print 'about handler'
assert router.lookup("/home/about") == "about handler"
# should print 'about handler' or None if you did not handle trailing slashes
assert router.lookup("/home/about/") == "about handler"
# should print 'not found handler' or None if you did not implement one
assert router.lookup("/home/about/me") == "not found handler"


# Test Case 2: edge case, not found handler is None
router2 = Router("root handler")
router2.add_handler("/home/about", "about handler")
router2.add_handler("/home/about/detail", "about detail handler")
assert router2.lookup("/home/not_added") is None
router2.add_handler("/codebase", "codebase handler")
assert router2.lookup("/codebase/") == "codebase handler"

# Test Case 3: edge case
router3 = Router("root handler")
current_path = "/"
for i in range(1000):
    word = "sub" + str(i)
    current_path = current_path + word + "/"
    router3.add_handler(current_path, "handler " + str(i))

assert router3.lookup(current_path) == "handler 999"
assert router3.lookup("/sub1/sub2/sub3") is None
