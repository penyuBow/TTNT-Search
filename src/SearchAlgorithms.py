from Space import *
from Constants import *
import time

def check_Node(node:Node,arr: list[Node]):
    for i in range(0,len(arr)):
        if arr[i].value == node.value:
            return True;
        return False;

def set_Color_pattern(g: Graph,path, sc: pygame.surface):
    print("Has found solution: ")
    g.goal.set_color(purple);
    g.draw(sc);
    child = g.goal.value
    while child != g.start.value:
        pygame.draw.line(sc,green,(g.grid_cells[child].x,g.grid_cells[child].y),(g.grid_cells[path[child]].x, g.grid_cells[path[child]].y), 2)
        pygame.display.flip()
        child = path[child]
        g.grid_cells[child].set_color(grey)
        g.draw(sc)
    g.start.set_color(orange)
    g.draw(sc)

def Cost_Two_Nodes(self, a: Node, b: Node):
        return sqrt((a.x - b.x)**2+(a.y - b.y)**2)

def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start]
    closed_set = []
    father = [-1]*g.get_len()

    #TODO: Implement DFS algorithm using open_set, closed_set, and father
    while(open_set):
        #lấy node đầu của đỉnh stack (danh sách mở)
        currNode = open_set.pop()
        #khi node đang xét là node đích
        if g.is_goal(currNode):
            while True:
                time.sleep(0.05)
                fatherNode = father[currNode.value]

                fatherNode.set_color(grey)
                g.start.set_color(orange)
                g.draw(sc)

                pygame.draw.line(sc, white, currNode.return_xy(), fatherNode.return_xy())
                time.sleep(0.025)

                if(g.is_start(fatherNode)):
                    g.draw(sc)
                    pygame.draw.line(sc, white, currNode.return_xy(), fatherNode.return_xy())
                    time.sleep(0.025)
                    break   
                currNode = fatherNode
            return

        #nếu node đang xét đang năm trong danh sách mở thì bỏ qua
        if currNode in closed_set:
            continue

        currNode.set_color(yellow)
        g.draw(sc)
        #thêm node curr vào danh sách mở
        closed_set.append(currNode)
        #get các neighbor code curr
        for neighbor in g.get_neighbors(currNode):
            if neighbor not in closed_set and not neighbor in open_set:
                father[neighbor.value] = currNode
                neighbor.set_color(red)
            #thmee các neighbor vào stack
            open_set.append(neighbor)

        g.goal.set_color(purple)
        g.start.set_color(orange)
        currNode.set_color(blue)
        g.draw(sc)
    raise NotImplementedError('Not implemented')

def BFS(g:Graph, sc:pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start]
    closed_set = []
    father = [-1]*g.get_len()
    
    #TODO: Implement BFS algorithm using open_set, closed_set, and father
    closed_set.append(g.start)
    while(open_set):
        currNode = open_set.pop(0)
        if g.is_goal(currNode):
            g.start.set_color(orange)
            while True:
                time.sleep(0.05)
                fatherNode = father[currNode.value]
                fatherNode.set_color(grey)
                g.start.set_color(orange)
                g.draw(sc)
                pygame.draw.line(sc, white, currNode.return_xy(), fatherNode.return_xy())
                time.sleep(0.025)

                if(g.is_start(fatherNode)):
                    g.draw(sc)
                    pygame.draw.line(sc, white, currNode.return_xy(), fatherNode.return_xy())
                    time.sleep(0.025)
                    break   
                currNode = fatherNode
            return

        currNode.set_color(yellow)
        g.draw(sc)

        for neighbor in g.get_neighbors(currNode):
            if neighbor not in closed_set and not neighbor in open_set:
                closed_set.append(neighbor)
                open_set.append(neighbor)
                father[neighbor.value] = currNode
                neighbor.set_color(red)

        currNode.set_color(blue)
        g.goal.set_color(purple)
        g.start.set_color(orange)
        g.draw(sc)
    raise NotImplementedError('Not implemented')
def UCS(g:Graph, sc:pygame.Surface):
    print('Implement UCS algorithm')

    open_set = {}
    open_set[g.start] = 0
    closed_set:list[Node] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    #TODO: Implement UCS algorithm using open_set, closed_set, and father
    while open_set:
        open_set = {k: v for k,v in sorted(open_set.items(),key=lambda item: item[1])}

        currNode = next(iter(open_set))

        if g.is_goal(currNode):
            g.start.set_color(orange)
            while True:
                time.sleep(0.05)
                fatherNode = father[currNode.value]

                fatherNode.set_color(grey)
                g.start.set_color(orange)
                g.draw(sc)

                pygame.draw.line(sc,green,currNode.return_xy(),fatherNode.return_xy())
                time.sleep(0.025)

                if(g.is_start(fatherNode)):
                    g.draw(sc)
                    pygame.draw.line(sc,green,currNode.return_xy(),fatherNode.return_xy())
                    time.sleep(0.025)
                    break
                currNode = fatherNode
            return

        currNode.set_color(yellow)
        g.draw(sc)

        cost[currNode.value] = open_set[currNode]
        for neighbor in g.get_neighbors(currNode):
            cost[neighbor.value] = cost[currNode.value] + 1
            if neighbor not in closed_set:
                closed_set.append(neighbor)
                open_set[neighbor] = cost[neighbor.value]
                father[neighbor.value] = currNode
                neighbor.set_color(red)
        open_set.pop(currNode)

        currNode.set_color(blue)
        g.goal.set_color(purple)
        g.start.set_color(orange)
        g.draw(sc)
    

    raise NotImplementedError('Not implemented')

def AStar(g:Graph, sc:pygame.Surface):
    print('Implement A* algorithm')

    open_set = {}
    open_set[g.start] = 0
    closed_set:list[Node] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    #TODO: Implement A* algorithm using open_set, closed_set, and father
    while open_set:
        currNode = None

        for node in open_set.keys():
            if currNode == None or open_set.get(node) + g.get_heuristic(node) < open_set.get(currNode) + g.get_heuristic(currNode):
                currNode = node
        if currNode == None:
            return
        currNode.set_color(yellow)
        g.goal.set_color(purple)
        g.start.set_color(orange)
        g.draw(sc)

        if g.is_goal(currNode):
            g.start.set_color(orange)
            while True:
                time.sleep(0.05)
                fatherNode = father[currNode.value]

                fatherNode.set_color(grey)
                g.start.set_color(orange)
                g.draw(sc)

                pygame.draw.line(sc, green, currNode.return_xy(), fatherNode.return_xy())
                time.sleep(0.025)
                if(g.is_start(fatherNode)):
                    g.draw(sc)
                    pygame.draw.line(sc, green, currNode.return_xy(), fatherNode.return_xy())
                    time.sleep(0.025)
                    break
                
                currNode = fatherNode
            return
        for neighbor in g.get_neighbors(currNode):
            if neighbor not in open_set.keys() and neighbor not in closed_set:
                open_set[neighbor] = open_set[currNode] + 1
                cost[neighbor.value] = cost[currNode.value] + 1
                father[neighbor.value] = currNode
                neighbor.set_color(red)
            else:
                if cost[neighbor.value] > cost[currNode.value] + 1:
                    cost[neighbor.value] = cost[currNode.value] + 1
                    father[neighbor.value] = currNode
                    if neighbor in closed_set:
                        closed_set.remove(neighbor)
                        open_set[neighbor] = cost[neighbor.value]

        
        currNode.set_color(blue)
        g.draw(sc)

        open_set.pop(currNode,None)
        closed_set.append(currNode)

    
    raise NotImplementedError('Not implemented')

def Greedy(g:Graph, sc:pygame.Surface):
    print('Implement Greedy algorithm')

    open_set = {}
    open_set[g.start] = 0
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    while open_set:
        currNode = None

        for node in open_set.keys():
            if currNode == None or g.get_heuristic(node) < g.get_heuristic(currNode):
                currNode = node
        if currNode == None:
            return
        currNode.set_color(yellow)
        g.goal.set_color(purple)

        g.draw(sc)

        if g.is_goal(currNode):
            g.start.set_color(orange)
            while True:
                time.sleep(0.05)
                fatherNode = father[currNode.value]

                fatherNode.set_color(grey)
                g.start.set_color(orange)
                g.draw(sc)
                pygame.draw.line(sc, green, currNode.return_xy(), fatherNode.return_xy())
                time.sleep(0.025)
                if(g.is_start(fatherNode)):
                    g.draw(sc)
                    pygame.draw.line(sc, green, currNode.return_xy(), fatherNode.return_xy())
                    time.sleep(0.025)
                    break
                
                currNode = fatherNode
            return
        for neighbor in g.get_neighbors(currNode):
            if neighbor not in open_set.keys() and neighbor not in closed_set:
                open_set[neighbor] = open_set[currNode] + 1
                cost[neighbor.value] = cost[currNode.value] + 1
                father[neighbor.value] = currNode
                neighbor.set_color(red)
            else:
                if cost[neighbor.value] > cost[currNode.value] + 1:
                    cost[neighbor.value] = cost[currNode.value] + 1
                    father[neighbor.value] = currNode
                    if neighbor in closed_set:
                        closed_set.remove(neighbor)
                        open_set[neighbor] = cost[neighbor.value]

        
        currNode.set_color(blue)
        g.draw(sc)

        open_set.pop(currNode,None)
        closed_set.append(currNode)

    raise NotImplementedError('Not implemented')