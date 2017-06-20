import urllib.request
import json
import networkx as nx
import matplotlib.pyplot as plt

# given_id = str(118932635)
friends = ''

def get_friends(given_id): #вот это наш список друзей, внутри которого мы работаем
    req = urllib.request.Request('https://api.vk.com/method/friends.get?user_id='+str(given_id))
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    main_list = json.loads(result)
    friends = main_list['response']
    # print(friends)
    return friends

def draw_nods():
    # given_id = str(118932635)
    # get_friends(str(118932635))
    # main_friends = friends
    G = nx.Graph() # пустой граф
    for ids in friends:
        for id in ids:
            print(id)
            G.add_node(id)
    return G
    # return main_friends


def draw_connections():
    for friend in friends:
        # given_id = friend
        get_friends(friend)
        for i in main_friends:
            if i in friends:
                G.add_edge(given_id,i)
    return G


# given_id=str(118932635)
get_friends(str(118932635))
print(friends)
main_friends = friends
draw_nods()
draw_connections()






#G.add_nodes_from([(main_list['response'])]) # добавляем два узла сразу

# То, как мы обозначаем узлы (1, 2, 3 ...) -- это их id. Но вообще-то мы можем приклеить к ним и человекопонятные ярлыки:
#G.add_node(1, label="node_1")

#G.add_edge(1,3) # ребро между узлами 1 и 3
#G.add_edges_from([(1, 4), (1, 5), (3, 5), (4, 5), (1, 6), (1, 7)])

nx.write_gexf(G, 'graph_file.gexf')

pos=nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='red', node_size=50) # рисуем узлы красным цветом, задаём размер узла
nx.draw_networkx_edges(G, pos, edge_color='yellow') # рисуем рёбра жёлтым
plt.axis('off') # по умолчанию график будет снабжён осями с координатами, здесь они бессмысленны, так что отключаем
plt.show() 



