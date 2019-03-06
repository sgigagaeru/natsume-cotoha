from graphviz import Digraph

def graphviz_parse(jsonfile):
    dependencies,chunks = extract_dependency_info(jsonfile)

    # グラフの初期化
    G = Digraph(format='png')
    G.attr('node', shape="circle")
    G.attr(rankdir='LR')

    for k in chunks:
#      print(chunks[k])
      G.node(chunks[k])

    # 係り受け情報よりノードとエッジを追加
    for dependency in dependencies:
        G.edge(chunks[dependency[0]],chunks[dependency[1]],label=dependency[2])

    # グラフ描写
    return G.source.replace("\n", "").replace("\t", " ")
#    G.render("graphs")


def extract_dependency_info(jsonfile):
    chunkid_text_dict = dict()
    dependency_info = list()

    # 解析結果(json)から係り受け情報を抽出
    for chunk in jsonfile["result"]:
        chunk_id = chunk["chunk_info"]["id"]
        tokens = [token["form"] for token in chunk["tokens"]]
        chunkid_text_dict[chunk_id] = " ".join(tokens)
        for link in chunk["chunk_info"]["links"]:
            dependency_info.append([chunk_id,link["link"],link["label"]])

#    print(chunkid_text_dict)
#    print(dependency_info)

    return dependency_info,chunkid_text_dict
