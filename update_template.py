import yaml
from yaml.loader import SafeLoader
import go_template
import re

def format_helm_template_for_python():
    with open('helm-templates-generate/output-templates/deployment.yaml') as f:
        lines  = list(f)
        new_file = ''
        for number, line in enumerate(lines):
            if 'labels' in line:
                new_file += line
                new_file += '    type-project: dag\n'
            else:
                new_file += line
            #if '{{' in line and ':' not in line:
            #    new_format_line = line.replace('{{','#{{')
            #    new_file += new_format_line
            #elif ':' in line:
            #    temp_dict = line.split(':')
            #    key = temp_dict[0]
            #    value = temp_dict[-1]
            #    if '{{' in value:
            #        value = value.replace('{{', '"{{').replace('}}','}}"')
            #    new_format_line = f'{key}: {value}'
            #    new_file += new_format_line
        #data_yaml = yaml.load(new_file, Loader=SafeLoader)
        print(new_file)
    #return data_yaml

template = format_helm_template_for_python()



 







#deployment_tmpl_file = 'helm-templates-generate/output-templates/deployment.yaml'
#txt = '{{- if .Values.objects.deployment.enabled }}'
#
#pattern = '\{\{'
#a = re.findall(txt, pattern)
#print(re.findall(txt, pattern))


#with open(deployment_tmpl_file) as tmpl_file:
#    temp_file = tmpl_file.readlines()
#    temp_file_list = []
#    for line in temp_file:
#        if line.startswith('{{'):
#            print('Inicia com {{')
#            add_comment = line.replace('{{', '#{{')
#            temp_file_list.append(add_comment)
#        else:
#            temp_file_list.append(line)
#
#    print(temp_file_list)
#    with open('temp_file.yaml','w') as temp_file:
#        for line in temp_file_list:
#            temp_file.write(line)

    




    
