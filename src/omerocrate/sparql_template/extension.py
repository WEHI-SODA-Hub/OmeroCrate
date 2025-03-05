from dataclasses import dataclass
from jinja2 import nodes
from jinja2.parser import Parser
from jinja2.ext import Extension
from rdflib import Graph

class SparqlExtension(Extension):
    # a set of names that trigger the extension.
    tags = {"sparql"}

    # def __init__(self, graph: Graph, **kwargs):
    #     self.graph = graph
    #     super().__init__(**kwargs)

    #     # add the defaults to the environment
    #     environment.extend(fragment_cache_prefix="", fragment_cache=None)

    def parse(self, parser: Parser) -> nodes.Node:
        # the first token is the token that started the tag.  In our case
        # we only listen to ``'cache'`` so this will be a name token with
        # `cache` as value.  We get the line number so that we can give
        # that line number to the nodes we create by hand.
        lineno = next(parser.stream).lineno
        query = parser.parse_expression()
        ret = self.graph.query(query)
        query_vars = ret.vars

        # now we parse the body of the cache block up to `endcache` and
        # drop the needle (which would always be `endcache` in that case)
        body = parser.parse_statements(["name:endsparql"], drop_needle=True)

        # now return a `CallBlock` node that calls our _cache_support
        # helper method on this extension.
        # return nodes.CallBlock(
        #     self.call_method("_cache_support", args), [], [], body
        # ).set_lineno(lineno)
        return nodes.For(target=nodes.Tuple(*query_vars), iter=nodes.List(ret), body=body).set_lineno(lineno)
