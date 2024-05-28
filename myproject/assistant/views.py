import json
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from .assistant_files.index import Assistant 
from django.views.decorators.csrf import csrf_exempt
import json

assistant = Assistant()

def assistant_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('user_input')
            print(user_input)
            response = assistant.assist(user_input)
            return JsonResponse({'response': response})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data in request'}, status=400)
        
    elif request.method == 'GET':
        return render(request, 'assistant.html')
    
    else: 
        return JsonResponse({'error': 'Only POST and GET requests are allowed'}, status=405)


