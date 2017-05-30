import urllib.request
import tarfile

response = urllib.request.urlopen('http://konect.uni-koblenz.de/downloads/tsv/munmun_twitterex_ut.tar.bz2')
zipped = response.read()
f = open('munmun_twitterex_ut.tar.bz2', 'wb')
f.write(zipped)
f.close()

tar = tarfile.open("munmun_twitterex_ut.tar.bz2")
tar.extractall()
tar.close()

twi_G = nx.Graph()

fg = open('munmun_twitterex_ut/out.munmun_twitterex_ut')
for indx, line in enumerate(fg):
    if indx:
        line = line.strip()
        node_1, node2 = line.split()
        twi_G.add_edge(node_1, node2)
fg.close()

print(nx.transitivity(twi_G))
deg_twi = nx.degree_centrality(twi_G)
i = 0
for nodeid in sorted(deg_twi, key=deg_twi.get, reverse=True):
    i += 1
    print(nodeid, round(deg_twi[nodeid], 3))
    if i == 10:
        break

pos = nx.spectral_layout(twi_G)
#pos = nx.shell_layout(dolphin_G)
nx.draw_networkx_nodes(twi_G, pos, node_color='blue', node_size=1) 
nx.draw_networkx_edges(twi_G, pos, edge_color='green')
nx.draw_networkx_labels(twi_G, pos, font_size=10, font_family='Arial')
plt.axis('off') 
plt.show()
