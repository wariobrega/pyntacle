import unittest
import os, sys, glob

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

from config import *
from cmds.metrics import Metrics as metrics_command
from tools.misc.graph_load import GraphLoad
from algorithms.global_topology import GlobalTopology
from algorithms.shortest_path import ShortestPath
from tools.enums import *

from tests import getmd5


class DummyObj:
    pass


class WidgetTestMetrics(unittest.TestCase):
    def setUp(self):
        self.cleanup()
        self.Args = DummyObj()
        self.Args.directory = os.path.join(current_dir, 'tests/test_sets/tmp')
        self.Args.format = None
        self.Args.input_file = os.path.join(current_dir, 'tests/test_sets/input/figure_8.txt')
        self.Args.largest_component = False
        self.Args.no_header = False
        self.Args.no_nodes = None
        self.Args.no_plot = True
        self.Args.plot_dim = None
        self.Args.plot_format = 'pdf'
        self.Args.report_format = 'txt'
        self.Args.save_binary = False
        self.Args.v = None

    def test_global(self):
        sys.stdout.write("Testing global metrics\n")
        self.Args.which = 'global'
        mt = metrics_command(self.Args)
        with self.assertRaises(SystemExit) as cm:
            mt.run()
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 0)
        fileout = glob.glob(os.path.join(current_dir, "tests/test_sets/tmp/pyntacle_report_*_Global_*"))[0]
        with open(fileout, 'r') as fin:
            data = fin.read().splitlines(True)
        with open(fileout, 'w') as fout:
            fout.writelines(data[1:])
        expected = os.path.join(current_dir, 'tests/test_sets/output/metrics/figure8_global.txt')
        self.assertEqual(getmd5(fileout), getmd5(expected),
                         'Wrong checksum for Metrics, global case')
        
        # CPU, GPU, igraph coherence check
        graph = GraphLoad(self.Args.input_file, "adjm", header=True).graph_load()
        
        implementation = CmodeEnum.igraph
        igraph_result = round(ShortestPath.average_global_shortest_path_length(graph, implementation), 5)
        
        implementation = CmodeEnum.cpu
        cpu_result = ShortestPath.average_global_shortest_path_length(graph, implementation)
        
        self.assertEqual(igraph_result, cpu_result)
        
        if cuda_avail:
            implementation = CmodeEnum.gpu
            gpu_result = ShortestPath.average_global_shortest_path_length(graph, implementation)
            self.assertEqual(igraph_result, gpu_result)
        
    def test_local(self):
        sys.stdout.write("Testing local metrics\n")
        self.Args.damping_factor = 0.85
        self.Args.which = 'local'
        self.Args.nodes = 'HS,BR,WD,PS,WS'
        self.Args.weights = None

        mt = metrics_command(self.Args)
        with self.assertRaises(SystemExit) as cm:
            mt.run()
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 0)
        fileout = glob.glob(os.path.join(current_dir, "tests/test_sets/tmp/pyntacle_report_*_Local_*"))[0]
        with open(fileout, 'r') as fin:
            data = fin.read().splitlines(True)
        with open(fileout, 'w') as fout:
            fout.writelines(data[1:])
        expected = os.path.join(current_dir, 'tests/test_sets/output/metrics/figure8_local.txt')
        self.assertEqual(getmd5(fileout), getmd5(expected),
                         'Wrong checksum for Metrics, local case')
        
    def tearDown(self):
        self.cleanup()

    def cleanup(self):
        files = glob.glob(os.path.join(current_dir, 'tests/test_sets/tmp/*'))
        for f in files:
            os.remove(f)
            
if __name__ == '__main__':
    unittest.main()