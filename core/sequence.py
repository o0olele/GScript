from .node import Node

class Sequence:
    def __init__(self, config: dict):
        self.id = config['id']

        self.nodes = []

        if len(config['nodes']) > 0:
            self.init_nodes(config['nodes'])

    def init_nodes(self, nodes_conf):
        for item in nodes_conf:
            self.nodes.append(Node(item))

    def detect(self, aim_mat):
        for node in self.nodes:
            ok = node.detect(aim_mat)

            if not ok:
                continue

            return node.events()
        
        return None

