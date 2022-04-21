class MyHashSet(object):

    def __init__(self):
        self.arr=[]
        

    def add(self, key):
        if key not in self.arr:
            self.arr.append(key)
        """
        :type key: int
        :rtype: None
        """
        

    def remove(self, key):
        if key in self.arr:
            self.arr.remove(key)
        """
        :type key: int
        :rtype: None
        """
        

    def contains(self, key):
        if key in self.arr:
            return True
        return False