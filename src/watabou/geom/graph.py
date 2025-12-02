"""Graph data structure with A* pathfinding."""
from typing import Dict, List, Optional
import math


class Node:
    """Graph node with weighted links to other nodes."""
    
    def __init__(self):
        """Initialize a node."""
        self.links: Dict['Node', float] = {}
    
    def link(self, node: 'Node', price: float = 1.0, symmetrical: bool = True) -> None:
        """Link this node to another with a cost."""
        self.links[node] = price
        if symmetrical:
            node.links[self] = price
    
    def unlink(self, node: 'Node', symmetrical: bool = True) -> None:
        """Remove link to another node."""
        if node in self.links:
            del self.links[node]
        if symmetrical and self in node.links:
            del node.links[self]
    
    def unlink_all(self) -> None:
        """Remove all links."""
        for node in list(self.links.keys()):
            self.unlink(node)


class Graph:
    """Graph data structure with pathfinding capabilities."""
    
    def __init__(self):
        """Initialize an empty graph."""
        self.nodes: List[Node] = []
    
    def add(self, node: Optional[Node] = None) -> Node:
        """Add a node to the graph."""
        if node is None:
            node = Node()
        self.nodes.append(node)
        return node
    
    def remove(self, node: Node) -> None:
        """Remove a node from the graph."""
        node.unlink_all()
        if node in self.nodes:
            self.nodes.remove(node)
    
    def a_star(self, start: Node, goal: Node, exclude: Optional[List[Node]] = None) -> Optional[List[Node]]:
        """Find shortest path using A* algorithm."""
        closed_set: List[Node] = exclude.copy() if exclude is not None else []
        open_set: List[Node] = [start]
        came_from: Dict[Node, Node] = {}
        
        g_score: Dict[Node, float] = {start: 0}
        
        while len(open_set) > 0:
            current = open_set.pop(0)
            if current == goal:
                return self._build_path(came_from, current)
            
            if current in open_set:
                open_set.remove(current)
            closed_set.append(current)
            
            cur_score = g_score.get(current, math.inf)
            for neighbour, cost in current.links.items():
                if neighbour in closed_set:
                    continue
                
                score = cur_score + cost
                if neighbour not in open_set:
                    open_set.append(neighbour)
                elif score >= g_score.get(neighbour, math.inf):
                    continue
                
                came_from[neighbour] = current
                g_score[neighbour] = score
        
        return None
    
    def _build_path(self, came_from: Dict[Node, Node], current: Node) -> List[Node]:
        """Build path from came_from map."""
        path = [current]
        
        while current in came_from:
            current = came_from[current]
            path.append(current)
        
        return path
    
    def calculate_price(self, path: List[Node]) -> float:
        """Calculate total cost of a path."""
        if len(path) < 2:
            return 0.0
        
        price = 0.0
        current = path[0]
        
        for i in range(len(path) - 1):
            next_node = path[i + 1]
            if next_node in current.links:
                price += current.links[next_node]
            else:
                return math.nan
            current = next_node
        
        return price
