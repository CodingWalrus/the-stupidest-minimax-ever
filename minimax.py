import functions as f
import networkx as nx
    
def FindBestMove(G,V,t,M,dist=0):
    if M:
        bestDist = 0
        bestValue = 0
        for i in range(nx.eccentricity(G,t)):
            for g in G.nodes():
                if nx.shortest_path_length(G,g,t) == (i+1):
                    V_new = V.copy()
                    V_new.append(g)
                    value = minimax(G, V_new, g, 0, False)
                    if value >= bestValue:
                        bestValue = value
                        bestDist = i
        return bestDist, bestValue
    else:
        bestVert = None
        bestValue = 1
        for g in G.nodes():
            if nx.shortest_path_length(G,g,t) == dist:
                V_new = V.copy()
                V_new.append(g)
                value = minimax(G, V_new, g, 0, True)
                if value >= bestValue:
                        bestValue = value
                        bestVert = g
        return bestVert, bestValue
        
def minimax(G,V,t,d,isMax):
    if f.Done(G,V,t):
        return len(V)/len(G)
    else:
        if isMax:
            bestValue = 0
            value = 0
            for i in range(nx.eccentricity(G,t)):
                for g in G.nodes():
                    if nx.shortest_path_length(G,g,t) == (i+1):
                        V_new = V.copy()
                        V_new.append(g)
                        value = minimax(G,V_new,g,d+1,False)
                        if value >= bestValue:
                            bestValue = value
        else:
            bestValue = 1
            value = 1
            for i in range(nx.eccentricity(G,t)):
                for g in G.nodes():
                    if nx.shortest_path_length(G,g,t) == (i+1):
                        V_new = V.copy()
                        V_new.append(g)
                        value = minimax(G,V_new,g,d+1,False)
                        if value <= bestValue:
                            bestValue = value
        return bestValue
        
def fdmin(G,v):
    token_vertex = v
    V = set(v)
    
    while f.Done(G,V,token_vertex) is False:
        dist_move = FindBestMove(G,V,token_vertex,True)
        vert_select = FindBestMove(G,V,token_vertex,False,dist_move)
        V.append(vert_select)
        token_vertex = vert_select
        
    return len(V)
        
G = nx.path_graph(3)
print(fdmin(G,0))
f.draw_graph(G)