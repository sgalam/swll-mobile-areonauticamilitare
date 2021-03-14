

from jinja2 import Template, Environment,FileSystemLoader,select_autoescape

class SWLL_Output:

    def generate_output(self, data):
        env = Environment(
            loader=FileSystemLoader('html_template/'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template('index.j2')
        output = template.render(swll_data=data)
        with open('/dist/index.html', 'w') as f:
            f.write(output)

    def general_error(self, ):
        env = Environment(
            loader=FileSystemLoader('html_template/'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template('general_error.j2')
        output = template.render()
        with open('/dist/index.html', 'w') as f:
            f.write(output)
\