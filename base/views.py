from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random
import time

# Create your views here.

def getToken(request):
    appId = '0678c07fac6b4864a104474994f6fae2'
    appCertificate = 'adb1afde714649ca8ee66927871d8a87'
    channelName = request.GET.get('channel')
    uid = random.randint(1,230)
    expirationRimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationRimeInSeconds
    role = 1
    
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token, 'uid':uid}, safe=False)



def lobby(request):
    return render(request, 'base/lobby.html')

def room(request):
    return render(request, 'base/room.html')