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
            user_input = data.get('user_input', '')  # Assuming the key is 'user_input'
            # Call the assist method with user_input
            response = assistant.assist(user_input)
            return JsonResponse({'response': response})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data in request'}, status=400)
    elif request.method == 'GET':
        # myproject\assistant\templates\assistant\assistant.html
        return render(request, 'assistant.html')
    else: 
        return JsonResponse({'error': 'Only POST and GET requests are allowed'}, status=405)





# def assistant_view(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         user_input = data.get('user_input')
#         response = assistant.assist(user_input)  # Assume assist method takes input and returns a response
#         return JsonResponse({'response': response})
#     return render(request, 'assistant/assistant.html')
