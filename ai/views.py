# views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .ai_helper import get_ai_response

SYSTEM_PROMPT = """
You are an AI assistant. 
Always respond in the most concise way possible, ideally 3 short sentence or less, regardless of topic.
Do not add extra explanations, greetings, or filler unless explicitly asked.
Treat every user message as a new, separate turn — never merge with previous responses.
Answer clearly and directly.
"""



@csrf_exempt
def ai_chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('query', '').strip()

        if 'chat_history' not in request.session:
            request.session['chat_history'] = [
                {"role": "system", "content": SYSTEM_PROMPT}
            ]

        request.session['chat_history'].append({"role": "user", "content": query})

        answer = get_ai_response(request.session['chat_history'])

        request.session['chat_history'].append({"role": "assistant", "content": answer})
        request.session.modified = True

        return JsonResponse({"answer": answer})




@csrf_exempt
def reset_ai_chat(request):
    request.session['chat_history'] = []
    return JsonResponse({"status": "ok"})
