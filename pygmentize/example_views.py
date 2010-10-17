
from django.shortcuts import render_to_response
from django.template import RequestContext
from pygmentize import pygmentizer

def pygmentize_example(request):

    some_text = """
    {% pygmentize 'python' %}
    '''this text comes from database or from other source'''
    def add_pygment(matchobj):
        #string = matchobj.group(0)
        lang = matchobj.group(2)
        text = matchobj.group(4)
        #print text, lang
        try:
            lexer = get_lexer_by_name(lang, encoding='UTF-8')
        except:
            lexer = HtmlLexer()
        return highlight(text, lexer, HtmlFormatter())

        {% endpygmentize %}
    """

    vars = {
        "some_text": pygmentizer.pygmentize(some_text)
    }
    return render_to_response('pygmentize_example.html', vars, context_instance=RequestContext(request))
