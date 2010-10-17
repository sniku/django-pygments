from django.template import Library, Node, resolve_variable
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

register = Library()

# usage: {% pygmentize "language" %}...language text...{% endpygmentize %}
class PygmentizeNode(Node):
    def __init__(self, nodelist, *varlist):
        self.nodelist, self.vlist = (nodelist, varlist)

    def render(self, context):
        lang = 'python'
        if len(self.vlist) > 0:
            lang = resolve_variable(self.vlist[0], context)
        try:
            lexer = get_lexer_by_name(lang, encoding='UTF-8')
        except:
            lexer = HtmlLexer()

        return highlight(self.nodelist.render(context), lexer, HtmlFormatter())

def pygmentize(parser, token):
    nodelist = parser.parse(('endpygmentize',))
    parser.delete_first_token()
    return PygmentizeNode(nodelist, *token.contents.split()[1:])

pygmentize = register.tag(pygmentize)
