from jinja2 import Environment, FileSystemLoader
import yaml
from yaml.loader import SafeLoader

#with open('input.yaml') as f:
#    data_yaml = yaml.load(f, Loader=SafeLoader)
#    print(data_yaml)

file_load = FileSystemLoader('j2-templates/')
env = Environment(loader=file_load)
template = env.get_template('deployment.yaml.j2')
print(template)
output = template.render()
print(output)

