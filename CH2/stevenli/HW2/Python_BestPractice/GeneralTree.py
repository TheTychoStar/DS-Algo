class Tree :
    """Abstract base class representing a tree structure"""

    # ----------------nested Position class------------------------------------
    class Position :
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other) :
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other) :
            return not (self == other)
        #-----------------abstract methods that concrete subclass must support------------
        def root(self) :
            raise NotImplementedError('must be implemented by subclass')

        def parent(self, p):
            """Return Position representing p's parent(or None if p is root)"""
            raise NotImplementedError('must be implemented by subclass')

        def num_children(self,p):
            raise NotImplementedError('must be implemented by subclass')

        def children(self,p):
            raise NotImplementedError('must be implemented by subclass')

        def __len__(self):
            raise NotImplementedError('must be implemented by subclass')

        def depth(self,p):
            """Return the number of levels separating Positions p from the root"""
            if self.is_root(p):
                return 0
            else:
                return 1+self.depth(self.parent(p))

        def _height_(self,p):
            """Return the height of the subtree rooted at Position p."""
            if self.is_leaf(p):
                return 0
            else:
                return 1+max(self._height_(c) for c in self.children(p))
