from peekingduck.runner import Runner
from peekingduck.pipeline.nodes.input import live
from peekingduck.pipeline.nodes.model import yolo
from peekingduck.pipeline.nodes.draw import bbox
# from peekingduck.pipeline.nodes.output import media_writer
from peekingduck.pipeline.nodes.output import screen
input_dir = None # Change this as desired
ouput_dir = None # Change this as desired
# Initialise the nodes
input_node = live.Node(input_dir = input_dir)
yolo_node = yolo.Node()
draw_node = bbox.Node()
output_node = screen.Node()
# Run it in the runner
runner = Runner(nodes=[input_node, yolo_node, draw_node, output_node])
runner.run()
#Inspect the data
runner.pipeline.data
