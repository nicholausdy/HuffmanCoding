class HuffmanNode():
    def __init__(self, left = None, right = None, char = '', prob = 0):
        self.left = left
        self.right = right
        self.char = char
        self.prob = prob
        

class HuffmanCompressor():
    def __init__(self, text_model):
       self.text_model = text_model 
       self.code_word_table = {}

    def create_huffman_tree(self):
        # Instantiate list of huffman nodes
        list_of_nodes = []
        for char, prob in self.text_model.items():
            node = HuffmanNode(char=char, prob=prob)
            list_of_nodes.append(node)

        # Create tree by initially sorting, then merging two nodes with two smallest probability
        # as a single tree
        while (len(list_of_nodes) != 1):
            list_of_nodes = sorted(list_of_nodes, key = lambda node: node.prob)
            a = list_of_nodes.pop(0)
            b = list_of_nodes.pop(0)
            c = HuffmanNode(left=a, right=b, char = a.char + b.char, prob=a.prob + b.prob)
            list_of_nodes.append(c)

        return list_of_nodes[0]

    def obtain_code_word(self, node, prefix = ""):
        # Obtain code words by depth-first traversal
        if (node.left is None) and (node.right is None):
            self.code_word_table[node.char] = prefix

        else:
            self.obtain_code_word(node.left, prefix = prefix + "0")
            self.obtain_code_word(node.right, prefix = prefix + "1")

    def generate_code_word_table(self):
        huffman_tree = self.create_huffman_tree()
        self.obtain_code_word(huffman_tree)

    def compress_text(self, text):
        compressed_text = ''
        for char in text:
            compressed_text = compressed_text + self.code_word_table[char]
        return compressed_text
