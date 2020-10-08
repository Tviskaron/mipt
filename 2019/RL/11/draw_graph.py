import pygraphviz as pgv


def draw_graph(file_name, graph):
    """
    drawing png graph from the list of edges
    :param file_name: file_name
    :param graph: graph file with format: (left_edge, right_edge) or (left_edge, right_edge, label)
    :return: None
    """
    g_out = pgv.AGraph(strict=False, directed=True)
    for i in graph:
        g_out.add_edge(i[0], i[1], color='black')
        edge = g_out.get_edge(i[0], i[1])

        if len(i) > 2:
            edge.attr['label'] = i[2]

    g_out.layout(prog='dot')
    g_out.draw(path="{file_name}.png".format(**locals()))


def main():
    draw_graph(file_name="test", graph=[("A", "B", 'test'), (2, 3)])


if __name__ == "__main__":
    main()
