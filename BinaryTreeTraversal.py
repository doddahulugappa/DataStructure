class Solution:
    def __init__(self, api):
        self.api = api
        # You can initiate and calculate things here

    def level_1_depth_first_pre_order(self, root_node_id):
        """
        Carry out depth first pre-order traversal

        :type root_node_id: string
        """
        # Write your code here

        if root_node_id:
            self.api.activate_node(root_node_id)
            self.level_1_depth_first_pre_order(self.api.get_children(root_node_id)[0])
            self.level_1_depth_first_pre_order(self.api.get_children(root_node_id)[1])

    def level_2_depth_first_in_order(self, root_node_id):
        """
        Carry out depth first in-order traversal (blue circles in the tree)

        :type root_node_id: string
        """
        # Write your code here
        if root_node_id:
            self.level_2_depth_first_in_order(self.api.get_children(root_node_id)[0])
            self.api.activate_node(root_node_id)
            self.level_2_depth_first_in_order(self.api.get_children(root_node_id)[1])

    def level_3_depth_first_post_order(self, root_node_id):
        """
        Carry out depth first post-order traversal (red circles in the tree)

        :type root_node_id: string
        """
        # Write your code here
        if root_node_id:
            self.level_3_depth_first_post_order(self.api.get_children(root_node_id)[0])
            self.level_3_depth_first_post_order(self.api.get_children(root_node_id)[1])
            self.api.activate_node(root_node_id)

    def level_4_breadth_first(self, root_node_id):
        """
        Carry out breadth first traversal

        :type root_node_id: string
        """
        # Write your code here
        self.api.activate_node(root_node_id)
        childrens = self.api.get_children(root_node_id)
        while childrens:
            childrens1 = []
            for child in childrens:
                self.api.activate_node(child)
                childrens1.extend(self.api.get_children(child))
            for i in range(childrens1.count('')):
                childrens1.remove('')
            childrens = childrens1
