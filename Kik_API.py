import requests
import json
from requests.auth import HTTPBasicAuth
#from Tkinter import *
#from tkFileDialog   import askopenfilename


"""  ----------------------

# Send Image Type Message

def sendRelatedImages( str ) :
    r = requests.post(
                      'https://api.kik.com/v1/message',
                      auth=('krupen33', 'b9e8a410-39b7-400d-b05f-7f019f0dd9d2'),
                      headers={
                      'Content-Type': 'application/json'
                      },
                      data=json.dumps({
                                      'messages': [
                                                   {
                                                   'chatId': '538a7a849efbc7f0acb2fe5ec66305c10541bf5ce4c3369bb0c33c579f2b2ebb' ,
                                                   'type': 'picture',
                                                   'to': 'krupen32',
                                                   'picUrl': str
                                                   }
                                                   ]
                                      })
                      )
    return;




def callback():

    name= askopenfilename()
    print("image name" + name)
    print("\n")


    # CALL Fitroom API
    r = requests.get('https://fitroom-api.herokuapp.com/api/images?type=emoda&key=unity&imageURL=http://contents.multilingualcart.com/ori/50114/goods_img/goods_8153_thum.jpg')


    responseFromAPI = r.json()

    #
    result = responseFromAPI['result']
    imagesArray = []
    
    for value in result:
        im_url = value['value_map']['im_url']
        imagesArray.append(im_url)
        sendRelatedImages(im_url)

errmsg = 'Error!'
Button(text='Select Image', command = callback).pack(fill=X)

mainloop()









# GET Setting Configuration of BOT

r = requests.get('https://api.kik.com/v1/config', auth=HTTPBasicAuth('krupen33', 'b9e8a410-39b7-400d-b05f-7f019f0dd9d2'))




    
# Set BOT Configuration

r = requests.post(
                  'https://api.kik.com/v1/config',
                  auth=('krupen33', 'b9e8a410-39b7-400d-b05f-7f019f0dd9d2'),
                  headers={
                  'Content-Type': 'application/json'
                  },
                  data=json.dumps({
                                  "webhook": "http://salemount.com/cgi-bin/Kik_API.py",
                                  "features": {
                                  "manuallySendReadReceipts": False,
                                  "receiveReadReceipts": False,
                                  "receiveDeliveryReceipts": True,
                                  "receiveIsTyping": False
                                  }
                                  })
                  )


"""



# Send Text Message

r = requests.post(
                  'https://api.kik.com/v1/message',
                  auth=('krupen33', 'b9e8a410-39b7-400d-b05f-7f019f0dd9d2'),
                  headers={
                  'Content-Type': 'application/json'
                  },
                  data=json.dumps({
                                  'messages': [
                                               {
                                               'body': 'Hey , there what can i do for you ?',
                                               'to': 'krupen32',
                                               'type': 'text', 
                                               'chatId': '538a7a849efbc7f0acb2fe5ec66305c10541bf5ce4c3369bb0c33c579f2b2ebb'
                                               }
                                               ]
                                  })
                  )







print("Done")
