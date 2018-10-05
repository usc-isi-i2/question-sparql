import unittest
import sys
import os
sys.path.append('../')
from src.GraphQuery import GraphQuery
from src.QueryTool import QueryTool, Mode

base_path = os.path.dirname(__file__)
gq = GraphQuery(base_path + '/sample_queries/graph_queries.xml')
ttl_path = base_path + '/sample_ttls/doc1.ttl'


class TestGraphQuery(unittest.TestCase):
    def test_graph_singleton(self):
        qt = QueryTool(ttl_path, Mode.SINGLETON)
        responses, errors = gq.ask_all(qt)
        self.assertFalse(errors.get('errors'))
        self.assertEqual(len(responses), 6)

    def test_graph_cluster(self):
        qt = QueryTool(ttl_path, Mode.CLUSTER, relax_num_ep=1)
        responses, errors = gq.ask_all(qt)
        self.assertFalse(errors.get('errors'))
        self.assertEqual(len(responses), 8)

    def test_graph_prototype(self):
        qt = QueryTool(ttl_path, Mode.PROTOTYPE)
        responses, errors = gq.ask_all(qt)
        self.assertFalse(errors.get('errors'))
        self.assertEqual(len(responses), 6)
