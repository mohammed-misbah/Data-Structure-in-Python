class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        space = ' ' * self.get_level() * 2
        print(space + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def product_tree():
    root = Tree("Cars")

    MERCEDES = Tree("MERCEDES")
    MERCEDES.child(Tree("GLC"))
    MERCEDES.child(Tree("S class"))
    MERCEDES.child(Tree("A class"))

    BMW = Tree("BMW")
    BMW.child(Tree("Q6"))
    BMW.child(Tree("Q7"))
    BMW.child(Tree("X3"))

    AUDI = Tree("AUDI")
    AUDI.child(Tree("rs3"))
    AUDI.child(Tree("r8"))
    AUDI.child(Tree("a5"))

    root.child(MERCEDES)
    root.child(BMW)
    root.child(AUDI)

    return root


if __name__ == '__main__':
    roots = product_tree()
    print(roots.get_level())
    roots.print_tree()

# Tree Example 2


# class TreeNode:
#     def __init__(self, name, designation):
#         self.name = name
#         self.designation = designation
#         self.subnode = []
#         self.rootnode = None
#
#     def sub(self, sub):
#         sub.rootnode = self
#         self.subnode.append(sub)
#
#     def get_level(self):
#         level = 0
#         rn = self.rootnode
#         while rn:
#             level += 1
#             rn = rn.rootnode
#         return level
#
#     def print_tree(self, property_name):
#         if property_name == 'both':
#             value = self.name + "(" + self.designation + ")"
#         elif property_name == 'name':
#             value = self.name
#         else:
#             value = self.designation
#
#         space = '  ' * self.get_level() * 2
#         print(space + value)
#         if self.subnode:
#             for sub in self.subnode:
#                 sub.print_tree(property_name)
#
#
# def export_manager():
#     # CTO Hierarchy
#
#     infra_head = TreeNode("Vishwa", "Infrastructure head")
#     infra_head.sub(TreeNode("Dhaval", "Cloud manager"))
#     infra_head.sub(TreeNode("Abijith", "App manager"))
#
#     CTO = TreeNode("chinmay", "CTO")
#     CTO.sub(infra_head)
#     CTO.sub(TreeNode("Aamir", "Application head"))
#     # HR Hierarchy
#
#     HR_head = TreeNode("Gels", "HR Head")
#     HR_head.sub(TreeNode("peter", "Requirement manager"))
#     HR_head.sub(TreeNode("waqas", "Policy manager"))
#
#     CEO = TreeNode("BANDRA", "CEO")
#     CEO.sub(CTO)
#     CEO.sub(HR_head)
#
#     return CEO
#
#
# if __name__ == '__main__':
#     root_node = export_manager()
#     root_node.print_tree("name")
#     root_node.print_tree("designation")
#     root_node.print_tree("both")


